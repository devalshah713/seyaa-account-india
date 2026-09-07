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

## Where the message goes

**Deval pastes it into a WhatsApp group.** That fixes two things:

- The output is **plain text**, paste-ready. No markdown, no code fence, no bullets, no
  bold. What the script prints is what goes in the group.
- Give him the block **on its own**, so he can copy it without picking up anything else.
  Warnings and questions go **below** it, separately — never mixed into the block and
  never in the middle of it.

Watch item, not yet observed: WhatsApp reads `*text*` as bold. Our size separator is `*`
(`6.05*4.10 MM`). It should be safe, because WhatsApp only opens bold at a word boundary
and ours always follows a digit — but this has not been seen on a real multi-size message
yet. **If any part of a demand ever arrives bold in the group, switch the separator to
`x` in `as_size()` and record it here.**

## What is NOT in the file

Neither `ADD ON` nor `CVD` appears in any column of the request. Both are supplied by the
script, which prints a `NOT IN FILE` line on every run.

- **`ADD ON` — confirmed by Deval, 2026-09-07.** The files he sends are add-on diamond
  requests, so `ADD ON` is the standing type. Use `--type` only if he says otherwise on a
  specific file. Do not ask about it again.
- **`CVD` — still unconfirmed.** Ask once, then stop asking; raise it again only if a
  file carries something that contradicts CVD.

## Open questions for Deval

1. Is `CVD` always the diamond type, or does a natural-diamond demand use a different
   line? If it varies, what in the incoming file tells us which?
2. Should `BAG`, `SUB DESIGN NO` or `REQ.DATE` ever appear in the demand? They are
   dropped today because the given format has no line for them.
