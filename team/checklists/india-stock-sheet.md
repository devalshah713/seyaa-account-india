# India Stock Sheet — Locked Audit Rules

Audited by `stock-auditor`. Implemented mechanically in `stock-audit/audit.py`.

**These sheets are production-critical** — they set the sell price and the labour pay to
manufacturers. A wrong value *or* a wrong formula means wrong pay and wrong sell.

**Audit only. Never edit either sheet unless Deval explicitly asks.**

---

## Assigned files (locked)

| Label | File | ID |
|---|---|---|
| NEW (live, primary watch) | Stock Sheet of Seyaa Factory for India | `1sWcfksBvp42a91q4LIkbx6qYZpi3AHv4DESshysvM-Y` |
| OLD (history / study) | Stock Sheet New For India | `1hXt65tYxq39Mh-LVHkKIc89FRWTAq5xG5fDIT8J7KzU` |

Tabs that matter: `Price List` · `STOCK` · Multi (NEW: `Multiple Dia Entry` / OLD: `MULTIPLE DIA JEW`).

Nothing else is in scope. No USA, no Purchase Cost, no PL. Those belong to sibling agents.

## Cadence

**12:00 and 17:00 IST, weekdays only.** Each run covers **only rows new or changed since
the last run** — never a full-sheet re-audit. Nothing new and no errors → **say nothing**.
No all-clear spam.

## Reporting

Errors go to Deval as one short batch:

| Stock # | Cell | Problem |
|---|---|---|

Passes, when useful:

| Stock # | What |
|---|---|

Always give the stock number from Col A **and** the exact cell. Copy the Head of
Accountants only when a rule change needs broadcasting.

**Any ambiguity → ask Deval. Do not invent rules.** An invented rule that reaches the
manufacturers costs more than an unasked question.

---

## Verified column map — NEW

Confirmed against the live sheet on 2026-09-07. `STOCK` and `Multiple Dia Entry` share
this layout. OLD has **no** Category columns E–G, so OLD columns are shifted left by three
from `E` onward.

| Col | STOCK | Multi |
|---|---|---|
| A | Sr. No. | Sr. No. (master rows only) |
| B | DATE | DATE |
| C | DESIGN | DESIGN |
| D | Design Number | Design Number |
| E–G | Category / Sub / Sub-Sub | Category / Sub / Sub-Sub |
| H | LOCATION | LOCATION |
| I | Gold Details | Gold Details |
| J | INCH SIZE | INCH SIZE |
| K | GROSS WEIGHT | GROSS WEIGHT |
| L | NET WEIGHT | NET WEIGHT |
| M | TOTAL DIAMOND WEIGHT | Total Diamond Weight |
| N | DIAMOND WEIGHT BREAKUP | Stone Weight Breakup |
| O | DIA PCS. | Stone Pcs. |
| P | TOTAL DIA PCS. | Total Stone Pcs |
| Q | POINTERS | POINTER |
| R | SHAPE | Shape |
| S | Sieve / Size | Sieve / Size |
| T | PARTY NAME | PARTY NAME |
| U | Product Code | Product Code |
| V W X Y | Diamond $ · Gold $ · Labor $ · Total $ | same |
| Z AA AB AC | Diamond ₹ · Gold ₹ · Labor ₹ · Total ₹ | same |
| AD | COMMENTS | COMMENTS |

## Verified reference row — NEW

`S1805C` (STOCK row 1806), confirmed correct. This is the shape every priced single row
should match:

```
Q  =M1806/O1806                                    pointers = TDW / pcs
V  =N1806*IFERROR(VLOOKUP(U1806,'Price List'!$B$4:$F$68,5,),VLOOKUP(U1806,'Price List'!$J$4:$N$68,5,))
W  =L1806*'Price List'!$R$2                        gold $, 14KT, on NET weight
X  =L1806*'Price List'!$R$3                        labour $, diamond-set
Y  =V1806+W1806+X1806
Z  =N1806*IFERROR(VLOOKUP(U1806,'Price List'!$B$4:$G$68,6,),VLOOKUP(U1806,'Price List'!$J$4:$O$68,6,))
AA =L1806*'Price List'!$S$2
AB =L1806*'Price List'!$S$3
AC =Z1806+AA1806+AB1806
```

Note gold and labour multiply **NET weight (L)**, not gross.

`S1708C` (row 1709) is a correct MIX row: `S` and `U` both read `MIX`, and V–AC are blank
on STOCK because the totals live on the Multi tab.

## Price List rate cells — verified 2026-09-07

| Cell | Is | Value then |
|---|---|---|
| `$R$2` / `$S$2` | 14KT gold $ / ₹ per gram | 106 / 9798 |
| `$T$2` / `$U$2` | 18KT gold $ / ₹ per gram | 145 / 12488 |
| `$R$3` / `$S$3` | Labour, diamond-set $ / ₹ | 14 / 1199 |
| `$R$4` / `$S$4` | Labour, polki $ / ₹ | 18 / 1499 |

18KT labour on R3/S3 is **correct** — same rate. Polki still on R3 is an **error**.

---

## STOCK — identity and basics

| # | Check | Rule |
|---|---|---|
| A1 | Sr. No. (A) | OLD: consecutive integers, no skips. **NEW: `S0001C` style — consecutive-integer rule is OFF** |
| B1 | DATE (B) | Never blank. It is the stock-in date |
| C1 | Design (C) | Never empty. One consistent name per product — variants get flagged with stock # + cell + bad vs expected |
| D1 | Design Number (D) | Compulsory when TDW > 0. Plain gold / no-diamond may be blank |
| H1 | Location (H) | Never blank. Allowed: USA, USA sell, India, India sell, HK, HK sell, DXB, DXB sell, memo, repair, **MELT**, and similar. Unknown values are a **question for Deval**, not an error |
| I1 | Gold details (I) | Never blank. Intent is 14KT/18KT × white/yellow/rose |
| J1 | Inch / size (J) | Earrings and studs may be empty or `NA`. Otherwise required. Prefer `7 inch`. Rings: `US7` / `US10`, **no space** — `US 7` is wrong |
| K1 | Gross weight (K) | Never blank |
| L1 | Net weight (L) | Never blank. If TDW > 0 → net must be **less than** gross; equal is a flag. If TDW = 0 → net should **equal** gross. Use TDW and the stone weight breakup to decide |
| T1 | Party name (T) | Manufacturer. Never blank |

## STOCK — diamonds

| # | Check | Rule |
|---|---|---|
| E1 | Single | Breakup (N) = TDW (M) |
| E2 | MIX | Must have a Multi group for that stock #. Σ of Multi breakup = STOCK TDW |
| E3 | Stone pcs | Σ Multi pcs = STOCK total pcs. If TDW > 0, pcs must not be blank or zero |
| E4 | Pointers | **Must be a formula**, and its value must match. STOCK: TDW / pcs. Multi: breakup / pcs |
| E5 | Sieve (S) | Single → sieve size. MIX → `MIX`, with the detail on the Multi tab. `MIX` with no Multi breakup is an error |
| E6 | Product code (U) | Must exist on the Price List. Required when TDW > 0. STOCK MIX rows use the literal code `MIX`; the real codes sit on the Multi lines |

## Pricing — $ and ₹ follow the same logic

| # | Check | Rule |
|---|---|---|
| P1 | Diamond price | **Must be a VLOOKUP** against the Price List via the product code. A hardcoded `=M*250` or `=M*27000` is an error |
| P2 | Gold price | 14KT → `$R$2` / `$S$2`. 18KT → `$T$2` / `$U$2`. Wrong karat rate is an error |
| P3 | Labour | Diamond-set → `$R$3` / `$S$3`. Polki → `$R$4` / `$S$4`. **Polki still on R3 is an error.** 18KT labour on R3/S3 is fine |
| P4 | Total | Diamond + Gold + Labour. Flag a broken formula, a wrong rate, or a total that is not the sum |
| P5 | VLOOKUP range | Ranges cap at row 68. Flag any product code sitting past the end of the looked-up range — the lookup silently misses it |

> **⚠️ Standing risk, found 2026-09-07.** Both price lists are **exactly full to row 68** —
> 65 round codes in `B4:B68`, and the fancy list in `J` runs to 68 before the rate labels
> at rows 78–83. Every VLOOKUP in both sheets caps at `$68`. **The next product code added
> lands on row 69 and will be invisible to every lookup**, returning `#N/A` or falling
> through to the fancy list. This needs Deval's decision before the next code is added.

## Multi tab — `Multiple Dia Entry` (NEW) / `MULTIPLE DIA JEW` (OLD)

| # | Check | Rule |
|---|---|---|
| M1 | Structure | Master row (Sr filled): identity, weights, gold/labour/totals, manufacturer. Child rows: per-sieve breakup, pcs, pointers, shape, sieve, product code, diamond $/₹ |
| M2 | Link | Sr. No. ↔ STOCK · Stock Code ↔ STOCK Design Number · Mfg Name ↔ STOCK Party |
| M3 | Design | May stay pasted. No formula link required |
| M4 | Stock Code | Compulsory when the STOCK Design Number exists **(OLD)**. NEW Multi has Design Number in `D` and no Stock Code column — **rule still open with Deval** |
| M5 | Date | Multi date must match the STOCK date for the same Sr |
| M6 | Inherited | Every STOCK standing rule above applies on Multi wherever the columns match |

### Two structural conventions found in the live data — 2026-09-07

Both were discovered while validating the rule engine, and both silently break a naive
audit. They are encoded in `stock-audit/audit.py`.

**The master row carries the first sieve line.** A Multi master is not identity-only. On
OLD `A0946` the master holds breakup `1.92` / `74` pcs, and its seven children hold the
rest; `1.92 + 3.52 + 0.17 + 0.31 + 0.45 + 0.29 + 0.34 + 0.26 = 7.26`, matching the STOCK
TDW exactly. **A group total is master + children.** Summing children alone under-reports
every multi group and produces a false mismatch on every one of them.

**A Multi Sr can be compound.** `S1708C/S1709` is one Multi group covering two stock
numbers. An exact-match lookup finds no group for either and wrongly reports both as
"MIX with no Multi breakup". The group is registered under the full string and under each
component.

### Verified reference rows

Use these to calibrate. A finding on one of them is more likely a bug in the rules than an
error in the sheet.

| Sheet | Row | Is |
|---|---|---|
| NEW | `S1805C` | Correct priced single |
| NEW | `S1708C` (STOCK) | Correct MIX row — `S` and `U` both `MIX`, `V`–`AC` blank |
| OLD | `A0945` | Correct single |
| OLD | `A0946` | Correct multi — master plus seven sieve children |

---

## Letter pendants — root cause, found 2026-09-08

Four rows with a blank or hardcoded product code are all **letter pendants**, and they
share one cause: **column R (SHAPE) holds the pendant's letter, or `NA`, instead of a
diamond shape.** With no valid shape, no product code can be selected, and the price then
gets hardcoded to fill the gap.

| Stock # | Design | Shape (R) | Code (U) |
|---|---|---|---|
| S1708C | A LETTER PENDANT | `A` | MIX |
| S1710C | A LETTER PENDANT | `A` | MIX |
| S1060C | S LETTER PENDANT | `NA` | blank |
| S1688C | A LETTER PENDANT | `A` | blank — approved 2026-09-08 while unpriced |

Every fancy stone that passes carries a real shape and therefore a real code — `MQ`→
`MQ : 01`, `EM`→`EM : 02`, `OV`→`OV : 01`. The codes exist; they are unreachable while the
shape column holds a letter.

**`DIA : 01` (Price List row 68) is the code for a large single stone: $250/ct, ₹18,200/ct.**
That is the code the hardcoded rows were reaching for.

### The hardcode is half right

`=M*250` matches `DIA : 01` exactly on the dollar side. `=M*27000` does not match anything
— **₹27,000/ct appears nowhere in the Price List**, and the highest rupee rate in the fancy
list is ₹21,000 (`OV : 04`). On S1060C that overstates the diamond value by **₹45,408** on
one 5.16 ct piece.

When you see `=M*250` paired with `=M*27000`, the dollar figure is probably fine and the
rupee figure is probably invented. Check the rupee side first.

## Approved exceptions

Sign-offs live in `stock-audit/approvals.yaml`, matched on stock number **and** cell. An
approval is a decision about one cell on one row — never a rule change. If a whole class
of rows should stop failing, change the rule in this file instead.

An approval can carry `void_if: priced`, which makes it lapse the moment the row gains a
price. A blank product code is cosmetic on an unpriced row and drives the sell price on a
priced one, so the sign-off should not survive that change.

## Open with Deval — do not invent an answer

These are unresolved. The auditor reports them as **questions**, never as errors, and does
not flood the batch with them.

1. **Gold casing and spacing.** Sheets carry `14KT WHITE` and `14K WHITE`. Accept both, or
   force one exact form? Until answered, casing and spacing variants are **not** flagged.
2. **NEW Multi Stock Code.** NEW Multi has no Stock Code column — Design Number sits in `D`
   instead. How should M4 apply?
3. **OLD Sr scheme.** OLD starts around 4 and then mixes in `A0xxx` codes. Is that intended?
4. **VLOOKUP row-68 cap.** See the standing risk above. Extend the ranges, or is row 68 a
   deliberate boundary?
5. **MELT and the product-code rule.** Put to Deval on 2026-09-08 and **not** carved out —
   S0204 stays open. A melted piece still fails the "product code compulsory when TDW > 0"
   rule. Re-raise if it recurs on other MELT rows.
6. **Compound Multi Sr.** Is `S1708C/S1709` — one Multi group covering two stock numbers —
   a deliberate convention, or two entries that should have been separated? It is handled
   either way, but the reconciliation is only meaningful if it is intentional.
7. **Is rule M5 meant to be exact?** `A0946`, a reference row you called clean, has a Multi
   date of 2026-10-03 against a STOCK date of 2026-09-03. Either the dates genuinely differ
   and the row is clean on other grounds, or M5 is stricter than intended. Until this is
   settled, date mismatches are reported but should be treated as low confidence.

## Rule changes already locked by Deval

- `MELT` is an allowed Location (also applied to the USA lane).
- NEW `S0001C` scheme → the consecutive-integer Col A rule is **off** for NEW.
- Simple tables in audit pings.
- Cadence 12:00 and 17:00 IST only, new entries only, silence when clean.
