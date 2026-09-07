---
description: Turn a diamond request xlsx from mfg into the fixed diamond demand format
argument-hint: "<path-to.xlsx> [--type \"ADD ON\"] [--quality CVD]"
allowed-tools: Read, Write, Bash
---

Convert the diamond request workbook at **$1** into the demand we send the diamond
department.

## Steps

1. Read `team/checklists/diamond-demand.md`. The format is locked there. Do not format a
   demand from memory and do not retype one by hand.

2. Run the converter:

   ```
   python3 diamond-demand/convert.py "$1" $2 $3 \
       --out diamond-demand/demands/$(date +%F)-<party-or-file>.txt
   ```

   It uses the standard library only — no `pip install`, no Google Drive, no network.

3. **Relay the demand text exactly as printed.** No preamble, no summary, no reformatting,
   no markdown fence around it if it is going to be pasted onward. The block is the
   deliverable.

4. Then, separately, surface every line the script wrote to stderr:
   - the `NOT IN FILE` line — `ADD ON` and `CVD` are operator-supplied, so say which
     values were used and ask for confirmation if this file gives no evidence for them;
   - any `WARNING` — an unrecognised shape spelling or a row skipped for a blank field.
     A skipped row is a question for mfg, never something to fill in yourself.

5. Commit the saved demand under `diamond-demand/demands/`. It is the record of what was
   asked for, and it is what a later dispute is settled against.

## Stop conditions

- **The script says it cannot find the header row.** The file layout changed. Stop and
  say so. Do not map the columns by eye and do not pass a guessed layout back in — a
  demand built on a guessed column map sends the wrong stones.
- **A shape spelling is unrecognised.** Send the demand only after the spelling is
  confirmed, then add it to `SHAPE_SPELLINGS` in the script and to the checklist.
- **A row is missing design number, shape, size or pcs.** Ask mfg. Never infer.
