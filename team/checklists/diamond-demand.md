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

**Always reconcile before sending**: sheet rows and total `DIA PCS` must equal the
message's demand count and total pieces, **after** subtracting anything the ledger
dropped. Show the arithmetic: `sheet 126 pcs - 21 dropped = 105 in the message`.

## Never demand the same stone twice

Mfg re-sends a design while it is still open, so the same stone arrives on request after
request. Demanding it again makes the diamond department issue the stone twice.

Every past demand under `diamond-demand/demands/` is the **ledger**. Before a run goes
out, each row is checked against it and a match is **dropped and reported**. This is on by
default; `--no-ledger` turns it off.

The key is **design number + shape + size**. The piece count is deliberately *not* part
of it:

- Same stone, different count → still a repeat, still dropped. The 2026-09-14 file asked
  19 pcs of `SN-RG-SL-CHU-021` ROUND 1.00 MM where 20 pcs had already gone out on
  2026-09-02, and `SN-BR-TN-MQ-0.40PT-006` MQ 7.50*3.75 at 1 pc against 3 already sent.
  Both read as the request being raised again, not a top-up.
- **Every drop prints both counts.** A count that has gone *up* may be a genuine
  additional need — surface those to Deval rather than deciding alone.

A size or shape the ledger has never seen on that design is **new** and goes out, even
when the design number is familiar.

`diamond-demand/demands/` is therefore load-bearing, not an archive. **It must stay
committed** — if it is lost, every open design gets demanded a second time. The run's own
`--out` file is excluded from its own ledger, so a re-run is safe.

Instructed by Deval on 2026-09-14: *"if any demand is repeated do not put add on demand
of it."*

## The office Diamond Issue Jangad — the real authority on what is issued

Google Sheet `1IhNZlP3YxM8lVTboyxB2EeJkReGN86ONSHi-buNkE3I`,
*Diamond Issue Jangad From Office*. 15 tabs, one per party, ~12,600 rows.
`docs.google.com` is blocked by the execution environment, so the **Google Drive
connector is the only route** — the export is too big to return inline, so it lands in
a file and `stock-audit/decode.py` turns it into a real `.xlsx`.

**A demand we sent is not proof the stone was issued.** The Jangad is. Instructed by
Deval on 2026-09-17: *"if the diamond is already issued then do not make Add on Demand
here. For rest which are not issued make the diamond demand."* So a stone demanded
earlier but never issued **is demanded again** — the earlier demand produced nothing.

### Where the ADD ON tag actually lives

Not in a column of its own. It is appended inside **Sub Design No**: `ADD ON`,
`ADD ON  17`, `002 ADD ON`. 413 such rows across 8 of the 15 tabs.

### Three reasons a plain string compare is useless here

`diamond-demand/issue_match.py` handles each; `test_issue_match.py` guards them.

| | Jangad writes | mfg writes |
|---|---|---|
| Size | `1.3 MM` | `1.30 MM` |
| Shape | `MARQUISE` | `MQ` |
| Design | `SN-BR-AMF-CL-003`, `SN-RG-RAD-SL-WG-012  (ST NO S1205C)` | `SN-BR-AMF-CL-3`, `S1205C` |

Sizes are compared **as numbers**. Shapes are folded to one spelling **for matching
only** — the demand text is never rewritten by the matcher. Each row reduces to a set
of candidate identities (full design, zero-normalised design, design+sub, any
bracketed stock code) and a match on any one counts.

### Every identity must carry the sub-design number

The first version also emitted the bare family — `SN-RG-SL-EM` out of
`SN-RG-SL-EM-20` — so `SN-RG-SL-EM-33` matched the add-on issued for EM-20. It
reported **21 rows issued instead of 5**, and would have dropped 19 stones that were
never issued. **Never emit a family-only key.** The first test in
`test_issue_match.py` is exactly this case.

### Verdicts

- `ISSUED` — design, sub, shape and size all match an add-on row. Dropped.
- `DIFFERS` — design and sub match an issued add-on but the stone is different.
  **Reported, never dropped**: a different stone on a known design is still needed.
- `NEW` — demand it.

A sieve-range size (`+2.5-3`) or a blank size can never produce an `ISSUED` verdict,
so an unparseable size fails towards demanding rather than towards silence.

### Running it

```
python3 diamond-demand/issue_match.py issue.xlsx <request.xlsx ...> \
    --emit-ledger=diamond-demand/issued/<date>-issue-jangad-addons.txt
python3 diamond-demand/convert.py <request.xlsx ...> --ledger diamond-demand/issued \
    --out diamond-demand/demands/<date>-<party>-not-yet-issued.txt
```

The emitted ledger carries the **request** side's spelling of design, shape and size,
so `convert.py`'s string-keyed ledger lands exactly — the numeric matching has already
happened by then.

**Which ledger to point at matters.** `--ledger diamond-demand/issued` excludes what
was *issued*; `--ledger diamond-demand/demands` (the default) excludes what was
*demanded*. When Deval asks for what is not yet issued, it is the former.

## Re-download the Jangad every run

It changes daily. Between 2026-09-17 and 2026-09-21 it went from 12,657 rows / 413
add-on rows to 12,874 / 472, and `S1667C` gained an add-on row in that window — a
stale copy would have demanded a stone that had since been issued. **Never reuse a
saved copy.** Pull it through the Drive connector, `stock-audit/decode.py` it, then
match.

## An already-issued add-on is re-raised as FRESH, not dropped

Instructed by Deval on 2026-09-21: *"If already issued then also make them as a fresh
one."* When mfg asks again for a stone the Jangad shows as already issued, the second
request is not a second add-on — it is a fresh requirement. Pass
`--issued-as=FRESH` and those rows go out with `FRESH` on the demand-type line
instead of `ADD ON`.

That is why the type line is per row, not a single `--type` for the whole run: one
file yields `ADD ON` blocks and `FRESH` blocks side by side. Blocks are keyed on
design + shape + quality + **type**, so an add-on and a fresh demand on the same
design never merge.

Without `--issued-as` the issued rows are still dropped, which is the right default
when the question is "what is outstanding".

## When the quality cannot be read

Rows with no readable CVD/HPHT are **left out** by default. Pass
`--unknown-quality="CVD/HPHT ?"` to include them instead, carrying that label on the
quality line so the gap is visible in the demand rather than guessed at. Use that when
Deval asks for every product in a file; leave the default when he wants only what is
confirmed.

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
5. When a repeat arrives with a **higher** piece count than went out before, is that a
   top-up that should be demanded for the difference, or the same request re-raised?
   Dropped entirely today, and reported.
