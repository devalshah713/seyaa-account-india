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

## One demand per design number per shape

**Each design gets its own demand**, carrying its own `DIAMOND DEMAND` header and
standing on its own — that is exactly what the sample above is. The demands then run
together into one message Deval copies and pastes in one go.

Two shapes on one design produce **two demands**. Two sizes of the same shape on the
same design produce **two size lines inside one demand**.

Never fold two designs into a single demand. A size sitting under the wrong design
number is the mistake this entire file exists to prevent — one shape line and one design
number per demand, always.

Demands are divided by a line of 40 dashes, and **the divider goes out with them** — it
is what lets the diamond department see where one demand ends and the next begins. Deval
copies the whole run in one go, so the dashes are part of what he sends, not scaffolding
to strip.

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

Row 1 carries the mfg party (`ANIL EXPORTS DIAMOND CHANGING`). Not printed. Some files
carry a second sheet, `REPORTS..`; only the first sheet is read.

The header row is found **by these labels**, never by row number. If the labels change,
the script stops rather than guessing — that stop is correct, do not work around it.

## Shape spellings

Incoming files misspell shapes. The mapping lives in `SHAPE_SPELLINGS` in
`diamond-demand/convert.py`. Confirmed so far: `EMARLD` → `EMERALD`, `RND` → `ROUND`.

**Only add a spelling you have actually seen on a file.** An unknown spelling is passed
through unchanged with a warning — that warning means *ask*, not *ignore*.

Seen but **not** yet confirmed, so currently passed through as written:

- `MQ` — on the 2026-09-02 and 2026-09-03 files, on designs whose own codes carry `MQ`
  (`SN-RG-MQ-ETERNITY-0.50PT-078`, `SN-BR-TN-MQ-0.40PT-006`). Almost certainly marquise.
  Add `"MQ": "MARQUISE"` once Deval confirms the diamond department wants the full word.

## Size normalisation

`2.50x1.80 mm` → `2.50*1.80 MM`. Separator becomes `*`, unit becomes a trailing ` MM`,
digits are never touched. A size with no unit gets ` MM` appended.

## Continuation rows — the one that bit

Mfg writes the design number **once** and leaves column A blank on the further sizes for
that same design. Those rows carry only `DIA SIZE` and `DIA PCS`.

```
SN-RG-SL-CHU-021 | 26/P/1519 | ROUND | 0.90 MM | 48
                 |           |       | 1.00 MM | 20   <- same design
                 |           |       | 1.20 MM | 22   <- same design
```

On 2026-09-07 the converter dropped every such row and would have under-ordered a live
demand by **122 pieces**. Nothing looked wrong — the message was just short. The fix
attributes a design-number-less row to the design above it; a continuation row with no
design above it **stops the run** rather than guessing.

`diamond-demand/test_convert.py` guards this. Run it after any change to the converter:

```
python3 diamond-demand/test_convert.py
```

**Always reconcile before sending**: total `DIA PCS` on the sheet must equal the total
across the `- N PCS` lines in the message, and the row counts must match too.

## Demand file naming

`diamond-demand/demands/<REQ.DATE>-<party>-bag-<first bag number>.txt` — request date
first, so the folder sorts by when mfg asked, not when we happened to convert. A run
built from several files at once is named for the day it went out
(`2026-09-07-anil-exports-combined.txt`).

`2026-09-07-anil-exports-cin-3378.txt` predates this convention. It was built from a copy
of the bag-1938 request that reached us carrying **one** of its nine rows, and is
superseded by `2026-09-02-anil-exports-bag-1938.txt`. It is kept as the record of what
went out, not as a current demand.

## Where the message goes

**Deval pastes it into a WhatsApp group.** That fixes two things:

- The output is **plain text**, paste-ready. No markdown, no code fence, no bullets, no
  bold. What the script prints is what goes in the group.
- Give him the block **on its own**, so he can copy it without picking up anything else.
  Warnings and questions go **below** it, separately — never mixed into the block and
  never in the middle of it.

Give him **one fenced block containing every demand**, dividers included — one copy, one
paste. Settled on 2026-09-07 after two wrong turns: first three long blocks with several
designs merged into each ("quite difficult to understand"), then 25 separate fences ("too
many"). What he wants is one copyable run with a line between demands.

Several request files at once go into **one** run, in the order he sent them:

```
python3 diamond-demand/convert.py a.xlsx b.xlsx c.xlsx --out diamond-demand/demands/<name>.txt
```

Do not split by source file. The design number identifies the work; which workbook it
arrived in is our bookkeeping, not the department's.

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
2. Should `MQ` be sent as `MARQUISE`? See *Shape spellings*.
3. `ONLY SEMPLE` arrived in the design-number column on the 2026-09-03 file (bag
   `26/P/2077`, 42 pcs of 2.70 MM round). Sent through as written. Should a sample
   request carry a different line, or is the bag number enough for the department?
4. Should `BAG`, `SUB DESIGN NO` or `REQ.DATE` ever appear in the demand? They are
   dropped today because the given format has no line for them.
