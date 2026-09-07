# Diamond Demand — Locked Output Format

Manufacturing sends a diamond request `.xlsx`. We send the diamond department a demand in
**one fixed format**. This file is the format. `diamond-demand/convert.py` implements it
and `/diamond-demand` runs it.

**Change the format here first, then the script.** Never reformat a demand by hand — a
demand typed freehand is how a size lands on the wrong design number.

---

## The format

```
DIAMOND DEMAND

ADD ON
CVD
EMERALD

6.05*4.10 MM - 1 PCS

SN-BR-AMF-BZ-091
```

Line by line:

| Line | Content | Source |
|---|---|---|
| 1 | `DIAMOND DEMAND` | fixed |
| 2 | blank | |
| 3 | Demand type — `ADD ON` | **operator, not the file** |
| 4 | Diamond type — `CVD` | **operator, not the file** |
| 5 | Shape | `DIA SHAPE`, spelling-normalised |
| 6 | blank | |
| 7+ | `<size> - <n> PCS`, one line per size | `DIA SIZE` · `DIA PCS` |
| | blank | |
| last | Design number | `S DARSHAN DESIGN NO` |

## One block per design number per shape

Two shapes on one design produce **two blocks**, not one block with two shape lines. Two
sizes of the same shape on the same design produce **two size lines in one block**. Blocks
are separated by a single blank line; `DIAMOND DEMAND` appears once, at the top.

The rule exists so that no size can be read against the wrong design number. Do not
"tidy" it by merging blocks.

## Incoming column map

Verified against `Diamond_Rerequest_file_19381925_2078R931636_18462007_15191790.xlsx`
(sheet `REQ.DIAMOND`), received 2026-09-07, `REQ.DATE` 2026-09-02. The workbook itself is
not kept here — mfg sends it each time, and the demand we sent back is the record.

| Col | Header | Used for |
|---|---|---|
| A | `S DARSHAN DESIGN NO` | design number line |
| B | `BAG` | read, not printed |
| C | `SUB DESIGN NO ` | read, not printed |
| D | `DESIGN NO ` | read, not printed |
| E | `DIA SHAPE` | shape line |
| F | `DIA SIZE` | size line |
| G | `DIA PCS` | pcs on the size line |
| H | `DIA WT` | read, not printed |
| I | `CIN-3378` | job reference in the header cell, not a column of data |
| J | `REMARK` | read, not printed |
| K | `REQ.DATE` | read, reported to the operator, not printed |

Row 1 carries the mfg party (`ANIL EXPORTS DIAMOND CHANGING`). Not printed.

The header row is found **by these labels**, never by row number. If the labels change,
the script stops rather than guessing — that stop is correct, do not work around it.

## Shape spellings

Incoming files misspell shapes. The mapping lives in `SHAPE_SPELLINGS` in
`diamond-demand/convert.py`. Confirmed so far: `EMARLD` → `EMERALD`, `RND` → `ROUND`.

**Only add a spelling you have actually seen on a file.** An unknown spelling is passed
through unchanged with a warning — that warning means *ask*, not *ignore*.

## Size normalisation

`2.50x1.80 mm` → `2.50*1.80 MM`. Separator becomes `*`, unit becomes a trailing ` MM`,
digits are never touched. A size with no unit gets ` MM` appended.

## What is NOT in the file

`ADD ON` and `CVD` appear in no column of the request. They are supplied by the operator
and default to `ADD ON` / `CVD` in the script, which prints a `NOT IN FILE` line on every
run. **Confirm both before the demand goes out.** For the 2026-09-07 file the evidence for
`ADD ON` is circumstantial only — the filename says `Rerequest` and `REMARK` says
`EXTRA SET..`. That is a reason to ask, not a reason to assume.

## Open questions for Deval

1. Is `CVD` always the diamond type, or does a natural-diamond demand use a different
   line? If it varies, what in the incoming file tells us which?
2. Is `ADD ON` determined by the operator, or should it be read from `REMARK` /
   the filename? If a rule exists, it goes here and into the script.
3. Should `BAG`, `SUB DESIGN NO` or `REQ.DATE` ever appear in the demand? They are
   dropped today because the given format has no line for them.
