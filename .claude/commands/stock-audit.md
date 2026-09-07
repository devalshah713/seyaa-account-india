---
description: Run the India stock sheet audit (NEW by default) and report new or changed rows
argument-hint: "[new|old|both] [--full]"
allowed-tools: Read, Grep, Glob, Bash, Agent
---

Audit the India stock sheet. `$1` selects the sheet — `new` (default), `old`, or `both`.
Pass `--full` to re-audit every row instead of only what changed.

## Steps

1. Read `team/checklists/india-stock-sheet.md` for the file IDs and the locked rules.

2. Launch `stock-auditor` for the requested sheet. For `both`, launch two in a single
   message so they run concurrently.

3. Relay what comes back **as-is**. Do not re-rank it, do not soften it, and do not add a
   summary paragraph. The tables are the deliverable.

4. **If there is nothing new and nothing wrong, say exactly one line: `No changes.`**
   Do not produce a report. Do not list what was checked. Silence when clean is a locked
   instruction from Deval, not a stylistic preference.

## Notes

- The audit is incremental. State lives in `stock-audit/state/<label>.json` and moves
  forward on every run that is not `--no-save`, so a run you throw away still advances the
  watermark. If you are experimenting, pass `--no-save`.
- Never edit either sheet. This command is read-only and so is everything it calls.
- If the Google Drive connector is unavailable, say so and stop — do not audit stale
  cached data and present it as current.
