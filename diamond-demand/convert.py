#!/usr/bin/env python3
"""
Turn a diamond request .xlsx from manufacturing into the fixed demand format we send
to the diamond department.

    python3 diamond-demand/convert.py <file.xlsx> [--type "ADD ON"] [--quality CVD]
                                      [--out diamond-demand/demands/<name>.txt]

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
    items, warnings = [], []
    for rn in sorted(rows):
        if rn <= header_rn:
            continue
        rec = {field: rows[rn].get(col) for col, field in colmap.items()}
        if not any(rec.get(f) for f in REQUIRED):
            continue
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
        items.append(
            {
                "row": rn,
                "design_no": str(rec["design_no"]).strip(),
                "shape": shape,
                "size": as_size(rec["size"]),
                "pcs": as_pcs(rec["pcs"]),
                "bag": rec.get("bag"),
                "remark": rec.get("remark"),
                "req_date": as_date(rec["req_date"]) if rec.get("req_date") else None,
            }
        )
    return items, warnings


def render(items, demand_type, quality):
    """One block per design number per shape, so no size can land on the wrong design."""
    blocks, order = {}, []
    for it in items:
        key = (it["design_no"], it["shape"])
        if key not in blocks:
            blocks[key] = []
            order.append(key)
        line = f"{it['size']} - {it['pcs']} PCS"
        if line not in blocks[key]:
            blocks[key].append(line)

    out = ["DIAMOND DEMAND", ""]
    for i, (design_no, shape) in enumerate(order):
        if i:
            out.append("")
        out += [demand_type, quality, shape, ""]
        out += blocks[(design_no, shape)]
        out += ["", design_no]
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("xlsx")
    ap.add_argument("--type", default="ADD ON", help='demand type line, default "ADD ON"')
    ap.add_argument("--quality", default="CVD", help="diamond type line, default CVD")
    ap.add_argument("--out", help="also write the demand text to this path")
    args = ap.parse_args()

    rows = read_sheet(args.xlsx)
    header_rn, colmap = find_header(rows)
    items, warnings = collect(rows, header_rn, colmap)
    if not items:
        sys.exit("No usable request rows below the header. Nothing demanded.")

    text = render(items, norm(args.type), norm(args.quality))
    sys.stdout.write(text)
    if args.out:
        with open(args.out, "w") as fh:
            fh.write(text)

    dates = sorted({i["req_date"] for i in items if i["req_date"]})
    print(f"\n-- {len(items)} request row(s), {args.xlsx}", file=sys.stderr)
    if dates:
        print(f"-- REQ.DATE on file: {', '.join(dates)}", file=sys.stderr)
    print(
        f'-- NOT IN FILE: demand type "{norm(args.type)}" and quality "{norm(args.quality)}" '
        "are supplied by the operator, not read from the workbook. Confirm both.",
        file=sys.stderr,
    )
    for w in warnings:
        print(f"-- WARNING: {w}", file=sys.stderr)


if __name__ == "__main__":
    main()
