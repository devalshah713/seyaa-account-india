---
description: Review one employee's log for one day and print the findings
argument-hint: "<employee-id> [YYYY-MM-DD — defaults to today]"
allowed-tools: Read, Grep, Glob, Bash, Agent
---

Review **$1** for **$2** (if `$2` is empty, use today's date from `date +%F`).

If `$1` is empty, list the roster from `team/employees.yaml` and ask which employee.

## Steps

1. Confirm `$1` exists in `team/employees.yaml`. If not, list the valid ids and stop —
   do not guess at a near match, since reviewing the wrong person's work wastes everyone's
   time and can be read as an accusation.

2. Confirm `work-logs/<date>/<$1>.md` exists. If it does not, say so and stop.

3. Launch **in a single message so they run concurrently**:
   - `work-auditor` for this employee and date
   - `numbers-auditor` for this employee and date
   - `compliance-auditor`, if their `handles` involves tax, entries, invoices, filings or
     ledgers

4. Merge the results. Deduplicate — the same defect found by two bots is one finding, and
   say which bots concurred. Re-rank across all three. Drop anything one bot's evidence
   contradicts, and say you dropped it.

5. Print to the terminal. Do not write a file — this is the quick loop, and a file per
   spot-check clutters `reports/` until the real daily reports are hard to find.

## Output

```
<employee name> — <date>
<n> critical · <n> high · <n> medium · <n> low · <n> unverifiable

FIX TODAY
1. <defect> — <where> — should be <correct value>
...

BEFORE CLOSE
...

QUESTIONS
- <the unverifiable items, as questions to ask this person>

CLEAN
- <areas checked with nothing found>
```

Keep it short enough to read on screen without scrolling twice. If there is nothing to
report, say `No findings. <n> areas checked clean.` and list them.

Then stop. Do not offer to fix the underlying records — the employee owns their work, and
a bot silently correcting an accounting entry is exactly the failure mode this system
exists to catch.
