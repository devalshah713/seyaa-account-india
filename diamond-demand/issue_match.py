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


def identities(design, sub):
    """Candidate identities for one row. A match on any one counts.

    Every identity MUST carry the sub-design discriminator. An earlier version also
    emitted the bare family (`SN-RG-SL-EM` from `SN-RG-SL-EM-20`), which made
    SN-RG-SL-EM-33 match the add-on issued for EM-20 and would have dropped 19
    stones that were never issued. Never emit a family-only key.
    """
    out = set()
    d = clean(design)
    if not d:
        return out

    # A repair row carries its stock code in brackets: "... (ST NO S1205C)"
    for code in re.findall(r"\(([^)]*)\)", d):
        for tok in re.findall(r"[A-Z]*\d+[A-Z]*", code):
            if len(tok) >= 4:
                out.add(tok)
    d = clean(re.sub(r"\([^)]*\)", "", d))
    out.add(d)

    # Zero-padding differs between the two sheets: SN-BR-AMF-CL-003 vs -CL-3.
    m = re.match(r"(.*)-0*(\d+)$", d)
    if m and m.group(1):
        out.add(f"{m.group(1)}-{m.group(2)}")

    s = clean(ADDON.sub("", sub or ""))
    if s:
        bare = s.lstrip("0") or "0"
        # Only when the design does not already end with that sub number, so the
        # sub is never dropped from the identity.
        if not re.search(r"-0*" + re.escape(bare) + r"$", d):
            out.add(f"{d}-{s}")
            out.add(f"{d}-{bare}")
    return {i for i in out if i}


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
