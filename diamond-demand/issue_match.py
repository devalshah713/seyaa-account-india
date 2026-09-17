#!/usr/bin/env python3
"""
Cross-check mfg diamond requests against the office Diamond Issue Jangad workbook.

    python3 diamond-demand/issue_match.py <issue.xlsx> <request.xlsx> [more.xlsx ...]

An add-on already ISSUED must not be demanded again. The issue workbook records that
in the **Sub Design No** column, where the sub number carries an `ADD ON` tag
(`ADD ON`, `ADD ON  17`, `002 ADD ON`). Matching is on design number + sub design
number + that tag, exactly as Deval specified.

Three things make a plain string compare useless here, and each is handled:

- **Size.** The issue sheet writes `1.3 MM` where mfg writes `1.30 MM`. Sizes are
  compared as numbers, never as text.
- **Shape.** Mfg writes `MQ`; the office's own sheet writes `MARQUISE` for the same
  design (SN-BR-TN-MQ-0.50PT-004). Shapes are folded to one spelling for matching
  only — the demand text itself is never altered here.
- **Design identity.** The sub number sits in the design string on some rows
  (`SN-BR-PE-WG-50PT - 022`) and in its own column on others, and a repair carries
  its stock code in brackets (`SN-RG-RAD-SL-WG-012  (ST NO S1205C)`). Every row is
  reduced to a set of candidate identities and a match on any one counts.

Output: `ISSUED` rows are already covered, `STONE DIFFERS` rows share a design and
sub with an issued add-on but name a different stone — those are reported, never
dropped silently, because a different stone on a known design is still needed.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import convert
import issue_scan

# For matching only. Mfg's abbreviation vs the office's full word.
MATCH_SHAPES = dict(convert.SHAPE_SPELLINGS)
MATCH_SHAPES.update({"MQ": "MARQUISE", "MARQ": "MARQUISE", "RD": "ROUND",
                     "EM": "EMERALD", "PE": "PEAR", "OV": "OVAL"})

ADDON = re.compile(r"add\s*[-_ ]?\s*on", re.I)


def shape_key(shape):
    s = convert.norm(shape or "")
    return MATCH_SHAPES.get(s, s)


def size_key(size):
    """Sizes as numbers, so 1.3 MM and 1.30 MM are the same stone.

    Returns None for a sieve range (+2.5-3) or anything without a clean number —
    those are never matched, so they can only ever be reported, not dropped.
    """
    s = str(size or "").upper()
    if "+" in s or re.search(r"\d\s*-\s*\d", s):
        return None                      # sieve range, not a millimetre size
    nums = re.findall(r"\d+(?:\.\d+)?", s)
    if not nums:
        return None
    return tuple(round(float(n), 3) for n in nums)


def clean(text):
    t = convert.norm(text)
    t = re.sub(r"\s*-\s*", "-", t)       # "SN-BR-PE-WG-50PT - 022" -> "...-022"
    return re.sub(r"\s+", " ", t).strip()


# Metal and market codes the Jangad inserts mid-design and mfg leaves out:
# ours "SN-BR-TN-MQ-0.40PT-006" is their "SN-BR-TN-MQ-0.40PT-YG-006".
# RG is NOT here — it is the ring prefix in SN-RG-..., not rose gold.
NOISE = {"WG", "YG", "PG", "9KT", "10KT", "14KT", "18KT", "22KT", "USA", "UK"}
MAX_RANGE = 60          # "002-011" is a sub range; "1938-2007" is not


def parse_design(design):
    """-> (base, [trailing numeric tokens]). Strips metal codes and brackets."""
    d = clean(design).replace("(", "-").replace(")", "-")
    toks = [t for t in re.split(r"[-\s]+", d) if t]
    toks = [t for t in toks if t not in NOISE]
    nums = []
    while len(toks) > 1 and re.fullmatch(r"\d+", toks[-1]):
        nums.insert(0, toks.pop())
    return "-".join(toks), nums


def subs_of(nums):
    """Sub-design numbers a design string covers.

    The Jangad records one row for a run of sub-designs: `SN-BR-SL-4CT-WG-002-011`
    is subs 002 through 011, and `SN-BR-RD-3CT-YG-(001-006)` is 001 through 006.
    Two ascending numbers a reasonable distance apart are read as that range.
    """
    vals = [int(n) for n in nums]
    if len(vals) == 2 and vals[0] < vals[1] <= vals[0] + MAX_RANGE:
        return set(range(vals[0], vals[1] + 1))
    return set(vals)


def identities(design, sub):
    """Candidate identities for one row. A match on any one counts.

    Every identity MUST carry the sub-design discriminator. An earlier version also
    emitted the bare design family (`SN-RG-SL-EM` out of `SN-RG-SL-EM-20`), which
    made SN-RG-SL-EM-33 match the add-on issued for EM-20 and would have dropped 19
    stones that were never issued. Never emit a family-only key when a sub is known.
    """
    out = set()
    raw = clean(design)
    if not raw:
        return out

    # A repair row carries its stock code in brackets: "... (ST NO S1205C)"
    for code in re.findall(r"\(([^)]*)\)", raw):
        for tok in re.findall(r"[A-Z]*\d+[A-Z]*", code):
            if len(tok) >= 4 and not re.fullmatch(r"\d{1,3}", tok):
                out.add(tok)
    base, nums = parse_design(re.sub(r"\(ST\s*NO[^)]*\)", "", raw))

    subs = subs_of(nums)
    s = clean(ADDON.sub("", sub or ""))
    if re.fullmatch(r"\d+", s):
        subs.add(int(s))

    out |= {f"{base}#{n}" for n in subs}
    if not subs:
        out.add(base)                      # no sub known anywhere
    if "-" not in base and base:
        out.add(base)                      # a bare stock code: S1667C, S0020C, 1990
    return {i for i in out if i}


QUALITIES = {"CVD", "HPHT"}


def fresh_index(issue_xlsx):
    """{identity: [fresh row, ...]} for every NON add-on row in the issue workbook.

    Used to answer "was this design issued CVD or HPHT?". The Jangad's Cvd/Hpht
    column is genuinely mixed — HPHT outnumbers CVD across the workbook — so the
    quality line on an add-on demand must be read from the fresh issue of that
    design, never assumed.
    """
    index = {}
    for r in issue_scan.flat(issue_xlsx):
        if r["sub"] and ADDON.search(str(r["sub"])):
            continue
        q = convert.norm(r["quality"] or "")
        rec = {
            "sheet": r["sheet"], "row": r["row"],
            "design": r["design"], "sub": r["sub"], "quality": q,
            "shape": shape_key(r["shape"]), "size": size_key(r["size"]),
            "raw_size": r["size"], "pcs": r["pcs"],
        }
        for ident in identities(r["design"], r["sub"]):
            index.setdefault(ident, []).append(rec)
    return index


def quality_for(item, fresh):
    """-> (quality, basis). Reads CVD/HPHT off the fresh issue of the same design.

    A precision ladder, best evidence first. Never guesses: if the fresh rows
    disagree, or there are none, the caller is told so and must ask rather than
    send a demand that names the wrong kind of stone.
    """
    cands = [rec for ident in identities(item["design_no"], item["sub"])
             for rec in fresh.get(ident, [])]
    cands = [c for c in cands if c["quality"] in QUALITIES]
    if not cands:
        return None, "no fresh issue found for this design"

    want_shape, want_size = shape_key(item["shape"]), size_key(item["size"])

    exact = [c for c in cands if c["shape"] == want_shape
             and c["size"] is not None and c["size"] == want_size]
    same_shape = [c for c in cands if c["shape"] == want_shape]
    for rung, rows in (("same stone", exact),
                       ("same shape on this design", same_shape),
                       ("this design", cands)):
        if not rows:
            continue
        qs = {c["quality"] for c in rows}
        if len(qs) == 1:
            return qs.pop(), f"{rung} ({rows[0]['sheet']} r{rows[0]['row']})"
        return None, f"fresh issue disagrees on {rung}: {'/'.join(sorted(qs))}"
    return None, "no fresh issue found for this design"


def issued_addons(issue_xlsx):
    """{identity: [row, ...]} for every ADD ON tagged row in the issue workbook."""
    index = {}
    for r in issue_scan.flat(issue_xlsx):
        if not (r["sub"] and ADDON.search(str(r["sub"]))):
            continue
        rec = {
            "sheet": r["sheet"], "row": r["row"],
            "design": r["design"], "sub": r["sub"],
            "shape": shape_key(r["shape"]), "size": size_key(r["size"]),
            "raw_size": r["size"], "pcs": r["pcs"],
        }
        for ident in identities(r["design"], r["sub"]):
            index.setdefault(ident, []).append(rec)
    return index


def request_rows(paths):
    for path in paths:
        rows = convert.read_sheet(path)
        hdr, colmap = convert.find_header(rows)
        sub_col = next((c for c, f in colmap.items() if f == "sub_design_no"), None)
        items, _, _ = convert.collect(rows, hdr, colmap)
        for it in items:
            it["file"] = os.path.basename(path)
            it["sub"] = rows.get(it["row"], {}).get(sub_col) if sub_col else None
            yield it


def classify(item, index):
    """-> (verdict, matching issue row or None). Verdict: ISSUED / DIFFERS / NEW."""
    cands = [rec for ident in identities(item["design_no"], item["sub"])
             for rec in index.get(ident, [])]
    if not cands:
        return "NEW", None
    want_shape, want_size = shape_key(item["shape"]), size_key(item["size"])
    for rec in cands:
        if rec["shape"] == want_shape and rec["size"] is not None \
                and rec["size"] == want_size:
            return "ISSUED", rec
    return "DIFFERS", cands[0]


def build_demand(rows):
    """Demand blocks with the quality line read per design, not assumed.

    Grouped by design + shape + quality. A design whose stones were issued partly
    CVD and partly HPHT therefore yields two blocks, which is correct — they are
    two different demands to the diamond department.
    """
    blocks, order = {}, []
    for item, quality in rows:
        key = (item["design_no"], item["shape"], quality)
        if key not in blocks:
            blocks[key] = []
            order.append(key)
        line = f"{item['size']} - {item['pcs']} PCS"
        if line not in blocks[key]:
            blocks[key].append(line)
    out = []
    for design_no, shape, quality in order:
        out.append("\n".join(["DIAMOND DEMAND", "", "ADD ON", quality, shape, ""]
                              + blocks[(design_no, shape, quality)]
                              + ["", design_no]) + "\n")
    return out


def emit_ledger(issued, path):
    """Write the issued rows as demand blocks, so convert.py --ledger excludes them.

    The blocks carry the REQUEST side's design, shape and size, not the issue
    sheet's, so the text matches what convert.py would itself produce and the
    string-keyed ledger lands exactly. The numeric matching has already happened.
    """
    blocks = []
    for item, rec in issued:
        blocks.append("\n".join([
            "DIAMOND DEMAND", "", "ADD ON", "CVD", item["shape"], "",
            f"{item['size']} - {item['pcs']} PCS", "", item["design_no"],
        ]) + "\n")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w") as fh:
        fh.write(f"\n{convert.SEPARATOR}\n\n".join(blocks))
    return len(blocks)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    emit = next((a.split("=", 1)[1] for a in sys.argv[1:]
                 if a.startswith("--emit-ledger=")), None)
    demand_out = next((a.split("=", 1)[1] for a in sys.argv[1:]
                       if a.startswith("--emit-demand=")), None)
    if len(args) < 2:
        sys.exit(__doc__)
    sys.argv = [sys.argv[0]] + args
    index = issued_addons(sys.argv[1])
    print(f"-- {len({id(r) for recs in index.values() for r in recs})} add-on rows "
          f"in the issue workbook, {len(index)} identities", file=sys.stderr)

    verdicts = {"ISSUED": [], "DIFFERS": [], "NEW": []}
    for item in request_rows(sys.argv[2:]):
        v, rec = classify(item, index)
        verdicts[v].append((item, rec))

    if emit:
        n = emit_ledger(verdicts["ISSUED"], emit)
        print(f"-- wrote {n} issued add-on(s) to {emit}", file=sys.stderr)

    if demand_out:
        fresh = fresh_index(sys.argv[1])
        seen, known, unknown = set(), [], []
        for item, _ in verdicts["NEW"] + verdicts["DIFFERS"]:
            key = (item["design_no"], item["shape"], item["size"])
            if key in seen:                      # duplicate file in the drop
                continue
            seen.add(key)
            q, basis = quality_for(item, fresh)
            (known if q else unknown).append((item, q or basis))
        blocks = build_demand(known)
        with open(demand_out, "w") as fh:
            fh.write(f"\n{convert.SEPARATOR}\n\n".join(blocks))
        print(f"-- wrote {len(blocks)} demand(s) from {len(known)} row(s) to "
              f"{demand_out}", file=sys.stderr)
        print(f"-- {len(unknown)} row(s) have no readable CVD/HPHT and were LEFT OUT:",
              file=sys.stderr)
        for item, why in unknown:
            print(f"   {item['design_no']} | {item['shape']} {item['size']} "
                  f"x{item['pcs']} | {why}", file=sys.stderr)

    for v in ("ISSUED", "DIFFERS", "NEW"):
        print(f"\n### {v} ({len(verdicts[v])})")
        for item, rec in verdicts[v]:
            line = (f"{item['design_no']} | sub {item['sub']} | {item['shape']} "
                    f"{item['size']} x{item['pcs']}")
            if rec:
                line += (f"   <- issue {rec['sheet']} r{rec['row']}: "
                         f"{rec['design']!r} sub {rec['sub']!r} "
                         f"{rec['shape']} {rec['raw_size']} x{rec['pcs']}")
            print("  " + line)


if __name__ == "__main__":
    main()
