---
description: Find repeating mistakes and systemic gaps across a date range
argument-hint: "[start YYYY-MM-DD] [end YYYY-MM-DD — defaults to the last 7 days]"
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, Agent
---

Analyse patterns from **$1** to **$2**. If both are empty, use the last 7 days ending
today (`date +%F`).

## Steps

1. Establish the range with `Bash`. Print it so there is no ambiguity about what was covered.

2. Count what exists in the range: logs in `work-logs/`, reports in `reports/`, employees
   who filed. **If there are fewer than 5 daily reports in the range, say the sample is
   too thin for pattern analysis and ask whether to continue anyway.** Patterns claimed
   from three days of data are noise with a confident tone, and this report gets read by
   managers.

3. Run `pattern-analyst` over the range.

4. Write to `reports/<end-date>-patterns.md`.

5. On the `Proposed watch_for updates` block — **do not apply it yourself**. Show it and
   ask. These entries sit against a named person in a tracked file and follow them into
   every future review; a human decides what gets recorded. Apply it to
   `team/employees.yaml` only after an explicit yes, and only the entries confirmed.

6. Also check whether the checklists need updating. If `compliance-auditor` reported
   checklist gaps during the range, or `team/checklists/accounting-india.md` still carries
   an unverified banner, list that here as the highest-value fix available — every bot's
   accuracy rests on those files.

## Report back

Print the systemic patterns in full, the count of individual training signals without the
detail, and the file path. The systemic findings are the ones worth a manager's attention;
the individual ones are for a private conversation, not a terminal.
