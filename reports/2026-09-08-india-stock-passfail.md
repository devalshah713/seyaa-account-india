# India stock sheet — pass/fail, new and changed entries

Sheet: NEW. Read-only audit against `team/checklists/india-stock-sheet.md`.
Export taken 2026-09-08. Scope: 18 rows new or changed since the 2026-09-07 12:06 IST watermark.

**15 PASS · 3 FAIL**

## Fail

| Stock # | Cell | Problem | Should be |
|---|---|---|---|
| S1060C | U1061 | Product Code blank while TDW = 5.16 | a fancy code matching the shape |
| S1060C | V1061 | Diamond $ hardcoded `=M1061*250` | VLOOKUP on the product code |
| S1060C | Z1061 | Diamond ₹ hardcoded `=M1061*27000` | VLOOKUP on the product code |
| S1688C | U1689 | Product Code blank while TDW = 3.11 | a fancy code matching the shape |
| S0204 | U205 | Product Code blank while TDW = 4.97 | see the MELT question below |

## Root cause — letter pendants

S1060C and S1688C are not two unrelated slips. Column R (SHAPE) holds the pendant's
letter or `NA` instead of a diamond shape, so no product code can be chosen, and on
S1060C the price was hardcoded to work around it.

| Stock # | Design | Shape (R) | Code (U) |
|---|---|---|---|
| S1708C | A LETTER PENDANT 1 CTS EACH | `A` | MIX — already open |
| S1710C | A LETTER PENDANT 1 CTS EACH | `A` | MIX — already open |
| S1060C | S LETTER PENDANT | `NA` | blank — new |
| S1688C | A LETTER PENDANT | `A` | blank — new |

Every fancy stone that passed today carries a real shape and therefore a real code:
S1739C `MQ`→`MQ : 01`, S1742C `EM`→`EM : 02`, S1826C `OV`→`OV : 01`. The fancy
price list has OV, PE, MQ, EM, CU, AS and PR families, so the codes exist — they are
not reachable while the shape column holds a letter.

Fixing the shape column on letter pendants closes all four rows, including the two
that have been open since 7 September.

## Question — MELT rows

S0204 is at Location `MELT`, party `SEYAA FACTORY MELTED`, and is unpriced. The rule
as written says a product code is compulsory when TDW > 0, so it is reported as a
fail — but a melted piece arguably no longer needs one. **Should MELT be carved out
of the product-code rule?** Not assumed either way.

## What the other 15 rows were

Mostly a movement sweep, not new manufacturing: 9 rows moved to REPAIR (ANTHEM
JEWELS and SEYAA FACTORY), 1 to MELT. Two genuinely new pieces, S1825 and S1826C,
both clean. Four RAJKUMAR MIX rows unchanged in substance.
