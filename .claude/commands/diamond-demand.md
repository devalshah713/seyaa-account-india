---
description: Turn a diamond request xlsx from mfg into the fixed diamond demand format
argument-hint: "<path-to.xlsx> [more.xlsx ...] [--type \"ADD ON\"] [--quality CVD]"
allowed-tools: Read, Write, Bash
---

Convert the diamond request workbook at **$1** into the demand we send the diamond
department.

## Steps

1. Read `team/checklists/diamond-demand.md`. The format is locked there. Do not format a
   demand from memory and do not retype one by hand.

2. Run the converter:

   ```
   python3 diamond-demand/convert.py "$1" [more.xlsx ...] \
       --out diamond-demand/demands/$(date +%F)-<party-or-file>.txt
   ```

   It uses the standard library only — no `pip install`, no Google Drive, no network.

3. **Relay the whole run as one fenced block**, exactly as printed, dividers and all.
   One copy, one paste. Never split it into a fence per demand and never merge two
   designs into a single demand — the dashes are the divider and they go out with it.
   Inside the fence: no preamble, no summary, no reformatting, no bullets, no bold.

   Twenty-five demands is still one fence.

   Several files in one go: pass them all in one command so they come back as one run,
   in the order he sent them. Do not produce one block per file.

4. Then, **below the block**, surface only what needs him:
   - any `WARNING` — an unrecognised shape spelling, or a row skipped for a blank field.
     A skipped row is a question for mfg, never something to fill in yourself.
   - `CVD` if it is still unconfirmed in the checklist, asked **once** and then dropped.

   `ADD ON` is confirmed standing (checklist, 2026-09-07) — do not re-ask it. If nothing
   needs him, say nothing. He gets these every day; a message that is only the block is
   the good outcome, not an incomplete one.

5. Commit the saved demand under `diamond-demand/demands/`. It is the record of what was
   asked for, and it is what a later dispute is settled against.

## Stop conditions

- **The script says it cannot find the header row.** The file layout changed. Stop and
  say so. Do not map the columns by eye and do not pass a guessed layout back in — a
  demand built on a guessed column map sends the wrong stones.
- **A shape spelling is unrecognised.** Send the demand only after the spelling is
  confirmed, then add it to `SHAPE_SPELLINGS` in the script and to the checklist.
- **A row is missing design number, shape, size or pcs.** Ask mfg. Never infer.
