#!/usr/bin/env python3
"""
Tests for issue_match.py: python3 diamond-demand/test_issue_match.py

The first group is a regression. identities() once emitted the bare design family
(`SN-RG-SL-EM` out of `SN-RG-SL-EM-20`), so SN-RG-SL-EM-33 matched the add-on issued
for EM-20 and 21 rows were reported issued instead of 5. Nineteen stones that had
never been issued would have been dropped from the demand. Every identity must carry
the sub-design discriminator.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import issue_match as im

FAILED = []


def check(name, cond, detail=""):
    print(("PASS  " if cond else "FAIL  ") + name
          + (f"\n      {detail}" if not cond and detail else ""))
    if not cond:
        FAILED.append(name)


def overlap(a, b):
    return bool(im.identities(*a) & im.identities(*b))


# --- the regression: siblings in one design family must never match -----------------
check("a sibling sub-design does not match an issued add-on",
      not overlap(("SN-RG-SL-EM-20", "ADD ON  20"), ("SN-RG-SL-EM-33", "33")),
      sorted(im.identities("SN-RG-SL-EM-20", "ADD ON  20")))
check("no identity is the bare design family",
      "SN-RG-SL-EM" not in im.identities("SN-RG-SL-EM-20", "ADD ON  20"),
      sorted(im.identities("SN-RG-SL-EM-20", "ADD ON  20")))
check("a different CUH sub-design does not match",
      not overlap(("SN-RG-SL-CUH-WG-020", "ADD ON  020"), ("SN-RG-SL-CUH-WG-34", "34")))

# --- the matches that must be found ------------------------------------------------
check("same design and sub match",
      overlap(("SN-RG-SL-EM-19", "ADD ON  19"), ("SN-RG-SL-EM-19", "19")))
check("zero padding does not block a match",
      overlap(("SN-BR-AMF-CL-003", "ADD ON  003"), ("SN-BR-AMF-CL-3", "3")))
check("a repair matches on its bracketed stock code",
      overlap(("SN-RG-RAD-SL-WG-012  (ST NO S1205C)", "ADD ON  012"),
              ("S1205C", "REPAIRE")))
check("a sub kept in its own column matches a sub folded into the design",
      overlap(("SN-BR-PE-WG-50PT - 022", "ADD ON"), ("SN-BR-PE-WG-50PT-022", "022")))

# --- size: numeric, never textual --------------------------------------------------
check("1.3 MM and 1.30 MM are the same stone",
      im.size_key("1.3 MM") == im.size_key("1.30 MM") is not None)
check("8.25*4 MM and 8.25*4.00 MM are the same stone",
      im.size_key("8.25*4 MM") == im.size_key("8.25*4.00 MM"))
check("different sizes stay different",
      im.size_key("1.30 MM") != im.size_key("1.20 MM"))
check("a sieve range is never matchable", im.size_key("+2.5-3") is None)
check("a blank size is never matchable", im.size_key("") is None)

# --- shape folding for matching only -----------------------------------------------
check("MQ matches the office's MARQUISE", im.shape_key("MQ") == im.shape_key("MARQUISE"))
check("mfg's EMARLD matches EMERALD", im.shape_key("EMARLD") == im.shape_key("EMERALD"))
check("different shapes stay different", im.shape_key("PEAR") != im.shape_key("ROUND"))

# --- classify ----------------------------------------------------------------------
fake = {}
rec = {"sheet": "S", "row": 1, "design": "SN-RG-SL-EM-19", "sub": "ADD ON  19",
       "shape": im.shape_key("ROUND"), "size": im.size_key("1.3 MM"),
       "raw_size": "1.3 MM", "pcs": "6.0"}
for ident in im.identities("SN-RG-SL-EM-19", "ADD ON  19"):
    fake.setdefault(ident, []).append(rec)

same = {"design_no": "SN-RG-SL-EM-19", "sub": "19", "shape": "ROUND", "size": "1.30 MM"}
check("an issued stone classifies ISSUED", im.classify(same, fake)[0] == "ISSUED")

other_size = dict(same, size="1.60 MM")
check("a different size on an issued design classifies DIFFERS, never ISSUED",
      im.classify(other_size, fake)[0] == "DIFFERS")

other_design = dict(same, design_no="SN-RG-SL-EM-33", sub="33")
check("an unrelated design classifies NEW", im.classify(other_design, fake)[0] == "NEW")

sieve = dict(same, size="+2.5-3")
check("a sieve-range request is never dropped as issued",
      im.classify(sieve, fake)[0] != "ISSUED")

# --- metal codes and sub ranges ----------------------------------------------------
# The Jangad inserts WG/YG mid-design and records runs of sub-designs as one row.
# Treating those as non-matches reported 87 of 88 rows "no fresh issue found".
check("a metal code inserted mid-design does not block a match",
      overlap(("SN-BR-TN-MQ-0.40PT-YG-006", "006"), ("SN-BR-TN-MQ-0.40PT-006", "006")))
check("a karat and country suffix does not block a match",
      overlap(("SN-BR-SL-4CT-WG-002", "002"), ("SN-BR-SL-4CT-002-WG-14KT-USA", "002")))
check("a sub-design range covers a sub inside it",
      overlap(("SN-BR-SL-4CT-WG-002-011", None), ("SN-BR-SL-4CT-005-WG-14KT-USA", "005")))
check("a sub-design range does not cover a sub outside it",
      not overlap(("SN-BR-SL-4CT-WG-002-011", None), ("SN-BR-SL-4CT-030-YG", "030")))
check("a bracketed range is read as a range",
      overlap(("SN-BR-RD-3CT-YG-(001-006)", None), ("SN-BR-RD-3CT-004", "004")))
check("a bracketed range does not reach an unrelated sub",
      not overlap(("SN-BR-RD-3CT-YG-(001-006)", None), ("SN-BR-RD-3CT-030", "030")))
check("two far-apart numbers are not a range",
      not overlap(("SN-X-1938-2007", None), ("SN-X-1970", "1970")))
check("a bare stock code still matches itself",
      overlap(("S1667C", "0"), ("S1667C", "REPAIRE")))
check("the EM-33 regression still holds after the rewrite",
      not overlap(("SN-RG-SL-EM-20", "ADD ON  20"), ("SN-RG-SL-EM-33", "33")))
check("a metal code does not collapse two different subs",
      not overlap(("SN-RG-SL-CUH-WG-020", "ADD ON  020"), ("SN-RG-SL-CUH-YG-37", "37")))

# --- the type line is per row: an issued add-on is re-raised as FRESH -------------
item = {"design_no": "D-1", "shape": "ROUND", "size": "1.30 MM", "pcs": "4"}
blocks = im.build_demand([(item, "CVD", "ADD ON")])
check("the type line carries the demand type",
      blocks[0].splitlines()[2] == "ADD ON" and blocks[0].splitlines()[3] == "CVD",
      blocks[0])

blocks = im.build_demand([(item, "CVD", "FRESH")])
check("FRESH replaces ADD ON on the type line",
      blocks[0].splitlines()[2] == "FRESH" and "ADD ON" not in blocks[0], blocks[0])

other = dict(item, size="1.50 MM")
blocks = im.build_demand([(item, "CVD", "ADD ON"), (other, "CVD", "FRESH")])
check("an add-on and a fresh demand on one design do not merge",
      len(blocks) == 2
      and {b.splitlines()[2] for b in blocks} == {"ADD ON", "FRESH"}, blocks)

blocks = im.build_demand([(item, "CVD", "ADD ON"), (other, "HPHT", "ADD ON")])
check("two qualities on one design do not merge", len(blocks) == 2, blocks)

# --- the CVD fallback is a labelled default, never a silent one --------------------
blocks = im.build_demand([({"design_no": "D-9", "shape": "ROUND",
                            "size": "1.00 MM", "pcs": "3"}, "CVD", "ADD ON")])
check("a fallback row still renders a complete demand",
      blocks[0].splitlines()[3] == "CVD" and blocks[0].rstrip().endswith("D-9"),
      blocks[0])

print()
if FAILED:
    print(f"{len(FAILED)} FAILED: {', '.join(FAILED)}")
    sys.exit(1)
print("all passed")
