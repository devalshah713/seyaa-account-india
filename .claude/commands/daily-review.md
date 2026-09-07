---
description: Run the full review panel over every employee's log for a date and write the consolidated mistake report
argument-hint: "[YYYY-MM-DD — defaults to today]"
allowed-tools: Read, Write, Grep, Glob, Bash, Agent
---

Run the full daily review for **$1** (if `$1` is empty, use today's date from `date +%F`).

## 1. Establish the date and find the logs

Run `date +%F` for today. Then list `work-logs/<date>/`.

- **No folder for that date** → say so and stop. Do not review a different date.
- **Folder exists but some employees on the roster have no log** → that is itself a
  finding. Every one of them goes in the report under *Logs not filed*, named. A missing
  log is the most common way a mistake escapes review entirely.

## 2. Run the panel

Read `team/employees.yaml` first to get the roster.

Then launch, **all in a single message so they run concurrently**:

- One `work-auditor` per employee who filed a log
- One `numbers-auditor` per employee who filed a log
- One `compliance-auditor` per employee whose `handles` involves tax, entries, invoices,
  filings or ledgers
- Exactly **one** `deadline-tracker` for the whole day — it reads every log itself, so do
  not run it per employee

Give each agent the employee id and the date, and tell it to follow its own instructions.

## 3. Consolidate

Merge the findings into one report. Your job here is judgement, not transcription:

- **Deduplicate.** Three bots will find the same wrong tax head from three angles. It is
  one finding. Keep the clearest statement of it and note which bots concurred — agreement
  across bots raises confidence and is worth recording.
- **Re-rank across the whole day.** Each bot ranks within its own scope. A CRITICAL from
  one bot may be the fourth most urgent thing overall. Order by what must be fixed first.
- **Drop findings that are contradicted by another bot's evidence.** Say in *Bot
  disagreements* that you dropped it and why.
- **Never upgrade a severity to make the report look substantial.** Never invent a finding
  to fill a section. A quiet day is a real result and reporting it honestly is what makes
  the loud days believable.
- **Carry every `UNVERIFIABLE` through.** Do not resolve them yourself by guessing. They
  become the questions list.

## 4. Write it

Write to `reports/<date>-daily-review.md`:

```markdown
# Daily Review — <date>

<n> logs reviewed · <n> not filed · <n> critical · <n> high · <n> medium · <n> low

## Fix today
Numbered, most urgent first. Each: what is wrong, where, the correct value, who fixes it.

## Fix before close
## Questions for the team
Each UNVERIFIABLE, as a plain question addressed to a named person.

## Deadlines
From deadline-tracker: overdue, due within 7 days, stuck.

## Logs not filed
| Employee | Date | Their reviewer |

## Per employee
### <name> — <n> findings (<n> critical)
Findings, with the clean areas listed so coverage is visible.

## Bot disagreements
Where bots reached different conclusions on the same item, and what would settle it.

## Coverage
Which bots ran, over which employees, and what was not covered.
```

## 5. Report back

In the terminal, print **only**: the counts, the *Fix today* list in full, and the path to
the written report. Nothing else — if the day was clean, say so in one line.

Do not commit anything. The report is for reading, and committing it silently would put
findings about named people into git history without anyone deciding to.
