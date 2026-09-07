#!/usr/bin/env python3
"""
Turn a diamond request .xlsx from manufacturing into the fixed demand format we send
to the diamond department.

    python3 diamond-demand/convert.py <file.xlsx> [more.xlsx ...]
                                      [--type "ADD ON"] [--quality CVD]
                                      [--out diamond-demand/demands/<name>.txt]

Several files at once produce ONE run of demands, in the order given, divided by a rule.
Deval copies the whole thing in one go and sends it to the group.

Reads values only, with the standard library. openpyxl is not used on purpose: this
workbook carries no formulas, and pip is not reliably reachable from a session container.

The format is locked in team/checklists/diamond-demand.md. Change it there first.
"""
import argparse
import datetime
import re
import sys
import zipfile
from xml.etree import ElementTree as ET

NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"

# Spellings seen on incoming files -> the spelling the diamond department reads.
# Only add a row here once you have actually seen it on a file. Never guess a shape.
SHAPE_SPELLINGS = {
    "EMARLD": "EMERALD",
    "EMRALD": "EMERALD",
    "EMERALD": "EMERALD",
    "ROUND": "ROUND",
    "RND": "ROUND",
    "PEAR": "PEAR",
    "OVAL": "OVAL",
    "MARQUISE": "MARQUISE",
    "MARQUES": "MARQUISE",
    "PRINCESS": "PRINCESS",
    "BAGUETTE": "BAGUETTE",
    "BAGUATE": "BAGUETTE",
    "CUSHION": "CUSHION",
    "HEART": "HEART",
    "RADIANT": "RADIANT",
    "ASSCHER": "ASSCHER",
    "TRILLION": "TRILLION",
    "TAPER": "TAPER",
}

# Header label (normalised) -> field name. The header row is found by these, never by
# a hardcoded row number.
HEADERS = {
    "S DARSHAN DESIGN NO": "design_no",
    "BAG": "bag",
    "SUB DESIGN NO": "sub_design_no",
    "DESIGN NO": "alt_design_no",
    "DIA SHAPE": "shape",
    "DIA SIZE": "size",
    "DIA PCS": "pcs",
    "DIA WT": "wt",
    "REMARK": "remark",
    "REQ.DATE": "req_date",
    "REQ DATE": "req_date",
}
REQUIRED = ("design_no", "shape", "size", "pcs")


def norm(text):
    return re.sub(r"\s+", " ", str(text)).strip().upper()


def read_sheet(path):
    """Return the first worksheet as {row_number: {column_letter: value}}."""
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        strings = []
        if "xl/sharedStrings.xml" in names:
            for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall(f"{NS}si"):
                strings.append("".join(t.text or "" for t in si.iter(f"{NS}t")))
        sheets = sorted(n for n in names if re.fullmatch(r"xl/worksheets/sheet\d+\.xml", n))
        if not sheets:
            sys.exit(f"{path}: no worksheet inside the workbook.")
        sheet = ET.fromstring(z.read(sheets[0]))

    rows = {}
    for cell in sheet.iter(f"{NS}c"):
        ref, ctype = cell.get("r"), cell.get("t")
        v, inline = cell.find(f"{NS}v"), cell.find(f"{NS}is")
        if ctype == "s" and v is not None:
            value = strings[int(v.text)]
        elif ctype == "inlineStr" and inline is not None:
            value = "".join(t.text or "" for t in inline.iter(f"{NS}t"))
        elif v is not None:
            value = v.text
        else:
            continue
        if value is None or str(value).strip() == "":
            continue
        col, rn = re.match(r"([A-Z]+)(\d+)", ref).groups()
        rows.setdefault(int(rn), {})[col] = str(value).strip()
    return rows


def find_header(rows):
    """Locate the header row by its labels. Returns (row_number, {col: field})."""
    best = (0, None, None)
    for rn in sorted(rows):
        mapping = {c: HEADERS[norm(v)] for c, v in rows[rn].items() if norm(v) in HEADERS}
        hits = len(set(mapping.values()))
        if hits > best[0]:
            best = (hits, rn, mapping)
    hits, rn, mapping = best
    if not mapping or not all(f in mapping.values() for f in REQUIRED):
        found = sorted(set((mapping or {}).values()))
        sys.exit(
            "Could not find the header row. Expected labels including "
            f"{', '.join(REQUIRED)}; matched {found or 'nothing'}.\n"
            "The file layout has changed — stop and check it by hand rather than "
            "sending a demand built on a guess."
        )
    return rn, mapping


def as_pcs(raw):
    try:
        n = float(raw)
    except (TypeError, ValueError):
        return norm(raw)
    return str(int(n)) if n == int(n) else str(n)


def as_size(raw):
    size = re.sub(r"\s+", " ", str(raw)).strip().upper()
    size = size.replace("X", "*").replace("×", "*")
    size = re.sub(r"\s*\*\s*", "*", size)
    if not size.endswith("MM"):
        size = f"{size} MM"
    return re.sub(r"\s*MM$", " MM", size)


def as_date(raw):
    try:
        serial = float(raw)
    except (TypeError, ValueError):
        return str(raw)
    return (datetime.date(1899, 12, 30) + datetime.timedelta(days=int(serial))).isoformat()


def collect(rows, header_rn, colmap):
    """Read the request rows below the header.

    Manufacturing writes the design number **once** and leaves it blank on the further
    sizes for that same design — see rows 11-14 and 16-20 of the 2026-09-02 file. Those
    continuation rows carry only a size and a pcs count. Dropping them silently
    under-orders the demand, so they are attributed to the design above them.
    """
    items, warnings, carried, carried_rows = [], [], None, {}
    for rn in sorted(rows):
        if rn <= header_rn:
            continue
        rec = {field: rows[rn].get(col) for col, field in colmap.items()}
        if not any(rec.get(f) for f in REQUIRED):
            continue

        if not rec.get("design_no") and rec.get("size") and rec.get("pcs"):
            if carried is None:
                sys.exit(
                    f"Row {rn} carries a size and pcs but no design number, and no row "
                    "above it carries one either, so it cannot be attributed.\n"
                    "Stop and ask mfg. A size sent against the wrong design number is "
                    "worse than a late demand."
                )
            for field in ("design_no", "shape", "bag", "remark", "req_date"):
                if not rec.get(field):
                    rec[field] = carried[field]
            carried_rows.setdefault(carried["design_no"], []).append(rn)
        else:
            carried = None

        missing = [f for f in REQUIRED if not rec.get(f)]
        if missing:
            warnings.append(f"row {rn}: blank {', '.join(missing)} — row skipped, ask mfg")
            continue

        raw_shape = norm(rec["shape"])
        shape = SHAPE_SPELLINGS.get(raw_shape)
        if shape is None:
            shape = raw_shape
            warnings.append(
                f"row {rn}: shape '{rec['shape']}' is not in SHAPE_SPELLINGS — sent through "
                "unchanged. Confirm the spelling before the demand goes out."
            )
        rec = {
            "row": rn,
            "design_no": str(rec["design_no"]).strip(),
            "shape": shape,
            "size": as_size(rec["size"]),
            "pcs": as_pcs(rec["pcs"]),
            "bag": rec.get("bag"),
            "remark": rec.get("remark"),
            "req_date": as_date(rec["req_date"]) if rec.get("req_date") else None,
        }
        items.append(rec)
        carried = rec if carried is None else carried

    return items, warnings, carried_rows


SEPARATOR = "-" * 40


def render(items, demand_type, quality):
    """One self-contained message per design number per shape.

    Deval sends these to the diamond department one at a time, so each message repeats
    the `DIAMOND DEMAND` header and stands on its own. Never merge two designs into one
    message: he cannot copy half a block, and a size read against the wrong design
    number is the mistake this whole file exists to prevent.
    """
    blocks, order = {}, []
    for it in items:
        key = (it["design_no"], it["shape"])
        if key not in blocks:
            blocks[key] = []
            order.append(key)
        line = f"{it['size']} - {it['pcs']} PCS"
        if line not in blocks[key]:
            blocks[key].append(line)

    messages = []
    for design_no, shape in order:
        lines = ["DIAMOND DEMAND", "", demand_type, quality, shape, ""]
        lines += blocks[(design_no, shape)]
        lines += ["", design_no]
        messages.append("\n".join(lines) + "\n")
    return messages


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("xlsx", nargs="+", help="one or more request workbooks")
    ap.add_argument("--type", default="ADD ON", help='demand type line, default "ADD ON"')
    ap.add_argument("--quality", default="CVD", help="diamond type line, default CVD")
    ap.add_argument("--out", help="also write the demand text to this path")
    args = ap.parse_args()

    all_messages, notes = [], []
    for path in args.xlsx:
        rows = read_sheet(path)
        header_rn, colmap = find_header(rows)
        items, warnings, carried_rows = collect(rows, header_rn, colmap)
        if not items:
            sys.exit(f"{path}: no usable request rows below the header. Nothing demanded.")

        messages = render(items, norm(args.type), norm(args.quality))
        all_messages += messages

        dates = sorted({i["req_date"] for i in items if i["req_date"]})
        notes.append(f"-- {len(messages)} demand(s) from {len(items)} row(s), {path}"
                     + (f" (REQ.DATE {', '.join(dates)})" if dates else ""))
        for design_no, rns in carried_rows.items():
            notes.append(f"-- CARRIED: row(s) {', '.join(str(r) for r in rns)} had no design "
                         f"number and were read as further sizes for {design_no}.")
        notes += [f"-- WARNING: {w}" for w in warnings]

    # SEPARATOR divides one demand from the next. It is part of the message Deval sends —
    # it is what lets the diamond department see where one demand ends and the next begins.
    text = f"\n{SEPARATOR}\n\n".join(all_messages)
    sys.stdout.write(text)
    if args.out:
        with open(args.out, "w") as fh:
            fh.write(text)

    print(f"\n-- {len(all_messages)} demand(s) across {len(args.xlsx)} file(s)", file=sys.stderr)
    print(
        f'-- NOT IN FILE: demand type "{norm(args.type)}" and quality "{norm(args.quality)}" '
        "are supplied by the operator, not read from the workbook. Confirm both.",
        file=sys.stderr,
    )
    for n in notes:
        print(n, file=sys.stderr)


if __name__ == "__main__":
    main()
