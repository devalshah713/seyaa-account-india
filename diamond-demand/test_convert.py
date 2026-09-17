#!/usr/bin/env python3
"""
Tests for convert.py. Standard library only: python3 diamond-demand/test_convert.py

The first test is the one that matters. On 2026-09-07 the converter silently dropped
every row where mfg had left the design number blank — the further sizes for the design
above — and would have under-ordered a real demand by 122 pieces. Nothing about the
output looked wrong; it was just short. Keep that test passing.
"""
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile

CONVERT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "convert.py")

HEADER = ["S DARSHAN DESIGN NO", "BAG", "SUB DESIGN NO", "DESIGN NO",
          "DIA SHAPE", "DIA SIZE", "DIA PCS", "DIA WT", "CIN-0000", "REMARK", "REQ.DATE"]


def write_xlsx(path, rows):
    """Minimal .xlsx with inline strings — enough for the reader under test."""
    def cell(col_i, rn, value):
        if value in (None, ""):
            return ""
        ref = f"{chr(ord('A') + col_i)}{rn}"
        text = str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        return f'<c r="{ref}" t="inlineStr"><is><t>{text}</t></is></c>'

    body = "".join(
        f'<row r="{rn}">' + "".join(cell(i, rn, v) for i, v in enumerate(row)) + "</row>"
        for rn, row in enumerate(rows, start=1)
    )
    with zipfile.ZipFile(path, "w") as z:
        z.writestr("[Content_Types].xml",
                   '<?xml version="1.0"?><Types xmlns="http://schemas.openxmlformats.org/'
                   'package/2006/content-types"><Default Extension="xml" ContentType="application/xml"/>'
                   '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-'
                   'officedocument.spreadsheetml.sheet.main+xml"/><Override PartName="/xl/worksheets/'
                   'sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.'
                   'spreadsheetml.worksheet+xml"/></Types>')
        z.writestr("_rels/.rels",
                   '<?xml version="1.0"?><Relationships xmlns="http://schemas.openxmlformats.org/'
                   'package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.'
                   'openxmlformats.org/officeDocument/2006/relationships/officeDocument" '
                   'Target="xl/workbook.xml"/></Relationships>')
        z.writestr("xl/workbook.xml",
                   '<?xml version="1.0"?><workbook xmlns="http://schemas.openxmlformats.org/'
                   'spreadsheetml/2006/main"><sheets><sheet name="REQ.DIAMOND" sheetId="1" '
                   'r:id="rId1" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/'
                   'relationships"/></sheets></workbook>')
        z.writestr("xl/_rels/workbook.xml.rels",
                   '<?xml version="1.0"?><Relationships xmlns="http://schemas.openxmlformats.org/'
                   'package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.'
                   'openxmlformats.org/officeDocument/2006/relationships/worksheet" '
                   'Target="worksheets/sheet1.xml"/></Relationships>')
        z.writestr("xl/worksheets/sheet1.xml",
                   '<?xml version="1.0"?><worksheet xmlns="http://schemas.openxmlformats.org/'
                   f'spreadsheetml/2006/main"><sheetData>{body}</sheetData></worksheet>')


def run(rows, *args):
    """Run the converter on a throwaway workbook.

    --no-ledger by default: without it these fixtures would be checked against the
    real diamond-demand/demands/ folder, and a fixture design that happens to match
    a demand actually sent would be dropped as a repeat. Tests that want the ledger
    pass --ledger explicitly.
    """
    if "--ledger" not in args:
        args = ("--no-ledger",) + args
    with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as fh:
        path = fh.name
    try:
        write_xlsx(path, rows)
        p = subprocess.run([sys.executable, CONVERT, path, *args],
                           capture_output=True, text=True)
        return p.returncode, p.stdout, p.stderr
    finally:
        os.unlink(path)


def run_files(rowsets, *args):
    """Run the converter over several workbooks in one command, as a zip drop does."""
    paths = []
    try:
        for rows in rowsets:
            fh = tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False)
            fh.close()
            write_xlsx(fh.name, rows)
            paths.append(fh.name)
        args = args if "--ledger" in args else ("--no-ledger",) + args
        p = subprocess.run([sys.executable, CONVERT, *paths, *args],
                           capture_output=True, text=True)
        return p.returncode, p.stdout, p.stderr
    finally:
        for path in paths:
            os.unlink(path)


def with_ledger(rows, ledger_text, *args):
    """Run the converter against a ledger folder holding one past demand file."""
    d = tempfile.mkdtemp()
    with open(os.path.join(d, "2026-01-01-past.txt"), "w") as fh:
        fh.write(ledger_text)
    try:
        return run(rows, "--ledger", d, *args)
    finally:
        shutil.rmtree(d)


def req(design, shape, size, pcs):
    return [design, "", "", "", shape, size, pcs, "", "", "", ""]


FAILED = []


def check(name, condition, detail=""):
    print(("PASS  " if condition else "FAIL  ") + name + (f"\n      {detail}" if not condition and detail else ""))
    if not condition:
        FAILED.append(name)


# --- the regression -----------------------------------------------------------------
# mfg writes the design number once, then leaves it blank on the further sizes for that
# same design. Every one of those rows must reach the demand.
code, out, err = run([
    ["ANIL EXPORTS DIAMOND CHANGING"],
    HEADER,
    req("SN-RG-SL-CHU-021", "ROUND", "0.90 MM", "48"),
    ["", "", "", "", "", "1.00 MM", "20", "", "", "", ""],
    ["", "", "", "", "", "1.20 MM", "22", "", "", "", ""],
    req("SN-RG-SL-CHU-020", "ROUND", "1.00 MM", "16"),
    ["", "", "", "", "", "1.30 MM", "4", "", "", "", ""],
])
check("continuation rows are attributed to the design above", code == 0 and out == """DIAMOND DEMAND

ADD ON
CVD
ROUND

0.90 MM - 48 PCS
1.00 MM - 20 PCS
1.20 MM - 22 PCS

SN-RG-SL-CHU-021

----------------------------------------

DIAMOND DEMAND

ADD ON
CVD
ROUND

1.00 MM - 16 PCS
1.30 MM - 4 PCS

SN-RG-SL-CHU-020
""", f"got:\n{out}")
check("carried rows are reported, not silent", "CARRIED" in err and "SN-RG-SL-CHU-021" in err, err)

# A continuation row with nothing above it cannot be attributed. Stop, never guess.
code, out, err = run([HEADER, ["", "", "", "", "", "1.00 MM", "20", "", "", "", ""]])
check("orphan continuation row stops the run", code != 0 and "cannot be attributed" in err, err)

# --- normalisation ------------------------------------------------------------------
code, out, err = run([HEADER, req("D-1", "EMARLD", "6.05*4.10 MM", "1")])
check("EMARLD is corrected to EMERALD", "EMERALD" in out and "EMARLD" not in out, out)

code, out, err = run([HEADER, req("D-1", "RND", "2.50x1.80 mm", "4")])
check("size separator and unit are normalised", "2.50*1.80 MM - 4 PCS" in out, out)

code, out, err = run([HEADER, req("D-1", "WEIRDSHAPE", "3.00 MM", "1")])
check("unknown shape passes through with a warning, never guessed",
      code == 0 and "WEIRDSHAPE" in out and "WARNING" in err, err)

# --- layout -------------------------------------------------------------------------
code, out, err = run([["note"], ["another note"], HEADER, req("D-1", "ROUND", "1.00 MM", "2")])
check("header is found by label, not by row number", code == 0 and "D-1" in out, out)

bad = ["DESIGN", "BAG", "X", "Y", "STONE SHAPE", "STONE SIZE", "QTY", "", "", "", ""]
code, out, err = run([bad, ["D-1", "", "", "", "ROUND", "1.00 MM", "2", "", "", "", ""]])
check("a relabelled file stops instead of guessing",
      code != 0 and "layout has changed" in err, err)

# --- two shapes on one design -------------------------------------------------------
code, out, err = run([HEADER,
                      req("D-1", "ROUND", "1.00 MM", "2"),
                      req("D-1", "PEAR", "5.00*3.00 MM", "1")])
check("two shapes on one design give two messages",
      out.count("DIAMOND DEMAND") == 2 and out.count("D-1") == 2 and out.count("ROUND") == 1, out)

# Each message must stand alone — Deval sends them to the group one at a time.
code, out, err = run([HEADER,
                      req("D-1", "ROUND", "1.00 MM", "2"),
                      req("D-2", "PEAR", "5.00*3.00 MM", "1"),
                      req("D-3", "OVAL", "6.00*4.00 MM", "3")])
parts = [p.strip() for p in out.split("-" * 40)]
check("one self-contained message per design", len(parts) == 3
      and all(p.startswith("DIAMOND DEMAND") for p in parts)
      and [p.splitlines()[-1] for p in parts] == ["D-1", "D-2", "D-3"], out)
check("the separator is never inside a message",
      all("-" * 40 not in p for p in parts), out)

# --- the ledger: never demand the same stone twice ----------------------------------
PAST = """DIAMOND DEMAND

ADD ON
CVD
ROUND

1.00 MM - 20 PCS
1.20 MM - 22 PCS

D-OLD

----------------------------------------

DIAMOND DEMAND

ADD ON
CVD
PEAR

5.00*3.00 MM - 2 PCS

D-PEAR
"""

code, out, err = with_ledger([HEADER,
                              req("D-OLD", "ROUND", "1.00 MM", "20"),
                              req("D-NEW", "ROUND", "1.00 MM", "20")], PAST)
check("a stone already demanded is dropped",
      code == 0 and "D-OLD" not in out and "D-NEW" in out, out)
check("the drop is reported as a REPEAT", "REPEAT" in err and "D-OLD" in err, err)

# A different count on the same stone is the same demand raised again, not a new one.
code, out, err = with_ledger([HEADER, req("D-OLD", "ROUND", "1.00 MM", "19"),
                              req("D-NEW", "ROUND", "3.00 MM", "1")], PAST)
check("a differing piece count is still a repeat", "D-OLD" not in out, out)
check("both counts are reported so a top-up can be spotted",
      "19 pcs now, 20 pcs already demanded" in err, err)

# Same design, size the ledger has never seen -> genuinely new, must go out.
code, out, err = with_ledger([HEADER, req("D-OLD", "ROUND", "1.60 MM", "4")], PAST)
check("an unseen size on a known design still goes out",
      code == 0 and "1.60 MM - 4 PCS" in out and "D-OLD" in out, out)

# Same design and size but a different shape -> different stone, must go out.
code, out, err = with_ledger([HEADER, req("D-OLD", "PEAR", "1.00 MM", "2")], PAST)
check("a different shape on a known design and size still goes out",
      code == 0 and "D-OLD" in out, out)

code, out, err = with_ledger([HEADER, req("D-OLD", "ROUND", "1.00 MM", "20")], PAST,
                             "--no-ledger")
check("--no-ledger demands it anyway", code == 0 and "D-OLD" in out, out)

code, out, err = with_ledger([HEADER, req("D-OLD", "ROUND", "1.00 MM", "20")], PAST)
check("all rows repeated stops with a clear message, no empty demand",
      code != 0 and "already demanded" in err and "DIAMOND DEMAND" not in out, err)

# --- one run must never demand the same stone twice --------------------------------
# Zips of request files routinely carry byte-identical copies ("... (1).xlsx") and
# rows that overlap between files. Neither may reach the message twice.
same = [HEADER, req("D-1", "ROUND", "1.00 MM", "4"), req("D-2", "PEAR", "5.00*3.00 MM", "1")]
code, out, err = run_files([same, same])
check("an identical duplicate file adds nothing",
      code == 0 and out.count("DIAMOND DEMAND") == 2
      and out.count("D-1") == 1 and out.count("D-2") == 1, out)
check("the intra-run drop says it came from this run", "already in this run" in err, err)

code, out, err = run_files([[HEADER, req("D-1", "ROUND", "1.00 MM", "4")],
                            [HEADER, req("D-1", "ROUND", "1.00 MM", "9"),
                             req("D-3", "OVAL", "6.00*4.00 MM", "2")]])
check("a row repeated across two files in one run is demanded once",
      code == 0 and out.count("D-1") == 1 and "D-3" in out
      and "1.00 MM - 4 PCS" in out and "9 PCS" not in out, out)

# --no-ledger switches off history, never intra-run de-duplication.
code, out, err = run_files([same, same], "--no-ledger")
check("--no-ledger still does not duplicate inside one run",
      out.count("D-1") == 1, out)

# --- the operator lines -------------------------------------------------------------
code, out, err = run([HEADER, req("D-1", "ROUND", "1.00 MM", "2")], "--quality", "natural")
check("--quality overrides the CVD line", "NATURAL" in out and "CVD" not in out, out)
check("operator-supplied lines are always flagged", "NOT IN FILE" in err, err)

print()
if FAILED:
    print(f"{len(FAILED)} FAILED: {', '.join(FAILED)}")
    sys.exit(1)
print("all passed")
