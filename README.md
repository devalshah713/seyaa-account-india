# Seyaa Account India — Daily Work Review

A panel of review bots that reads what each employee did today and finds the mistakes
before a client, an auditor, or the department does.

Employees file a short structured log at the end of the day. Five bots read those logs
and report what is wrong — with the exact line, the correct value, and what it costs if
it is not fixed. It runs on demand, and once a day on its own.

---

## Daily use

```bash
/new-log rahul-sharma          # employee creates their log, carries forward open items
                               # ...fills it in at end of day...
/daily-review                  # you run the panel over everybody
```

`/daily-review` writes `reports/<date>-daily-review.md` and prints the *Fix today* list.

## The India stock sheet auditor

A second, different job also lives here: `stock-auditor` watches the two India stock
Google Sheets and flags entry and formula errors before they reach a manufacturer's pay
run or a customer's price.

```bash
/stock-audit            # NEW sheet, only rows changed since the last run
/stock-audit old        # OLD sheet
/stock-audit both --full   # complete re-audit of everything
```

It is **read-only** and never edits either sheet. It reports stock # plus the exact cell:

| Stock # | Cell | Problem |
|---|---|---|
| S1708C/S1709 | V1279 | Multi diamond price ($) hardcoded `=M1279*250` — must VLOOKUP the Price List |

The locked rules are in `team/checklists/india-stock-sheet.md`; the deterministic engine
that applies them is `stock-audit/audit.py`. Column positions are resolved by **header
text**, not by letter, so the same rules run against NEW and OLD despite OLD's shifted
columns.

Findings from the day it was built are in `reports/2026-09-07-india-stock-backlog.md`
(232 on NEW, 3364 on OLD — the historical backlog). The watermark in
`stock-audit/state/` is seeded past that, so routine runs report only what changes next.
**That state must stay committed** — the container is wiped between runs, and without it
every check re-reports the whole backlog.

## All commands

| Command | Does |
|---|---|
| `/new-log <id> [date]` | Creates a log from the template, carrying forward yesterday's open items |
| `/review-employee <id> [date]` | Quick review of one person, printed, no file written |
| `/daily-review [date]` | Full panel over everyone, writes the consolidated report |
| `/weekly-summary [start] [end]` | Repeating mistakes and systemic gaps across a range |

## The bots

| Bot | Finds |
|---|---|
| `work-auditor` | Missing outcomes, contradictions, unowned handovers, vanished work, guesses stated as fact |
| `numbers-auditor` | Arithmetic that does not hold — transposed digits, wrong base, totals that do not add |
| `compliance-auditor` | GSTIN and PAN validity, wrong tax head, withdrawn rates, missed RCM, blocked ITC, wrong TDS section |
| `deadline-tracker` | Overdue filings, deadlines inside 7 days, work stuck on someone, promises with no date |
| `pattern-analyst` | Mistakes that repeat — across days, across people, after being corrected |

Each is a file in `.claude/agents/`. Edit them like any other text.

---

## Try it now

A test fixture with deliberately seeded mistakes ships with the repo:

```
/review-employee example-junior 2026-09-07
```

Compare what comes back against `reports/EXPECTED-example-junior.md` — 17 findings across
5 entries, plus 4 things a good report marks *unverifiable* rather than guessing at.

**Judge the bots on two things.** Did they catch the CRITICALs? And did they report
anything not on the list that they cannot defend from the log? A bot that invents findings
is worse than no bot, because it trains everyone to skim past the real ones.

---

## Before you rely on it

**This repository is public.** Anyone can read it. Work logs are about to contain
employee names, client names, invoice numbers, amounts, GSTINs and PANs — none of which
belongs on the public internet, and some of which you are obliged to keep confidential.
**Make the repository private before a single real log is filed.** GitHub → Settings →
General → Danger Zone → Change visibility. Note that anything already pushed while public
should be treated as disclosed, even after the switch.

**`team/checklists/accounting-india.md` carries an unverified banner.** Every rate,
threshold and due date in it was written from general knowledge and has *not* been checked
against a current notification. GST slabs were restructured in September 2025 and TDS
thresholds changed in April 2025 — assume more has moved since.

Someone who owns compliance needs to verify that file and sign the banner. Until they do,
`compliance-auditor` caps its rate-dependent findings at HIGH instead of CRITICAL and says
so at the top of every report. It is the single highest-value hour anyone can spend on
this repo — every bot's accuracy rests on that one file.

**Then replace the roster.** `team/employees.yaml` ships with three example employees.
The ids there must match the log filenames.

---

## Setting it up for your team

1. **Roster** — replace the examples in `team/employees.yaml` with your actual team. Use
   `handles` to control which checklist sections apply to whom.
2. **Verify the checklist** — as above. Set the reviewer name and date in the banner.
3. **Test the template on one person for a week** before rolling it out. The log format is
   the part people will resist; find out what is annoying about it while it is one person's
   problem.
4. **Delete the fixture** — `work-logs/2026-09-07/` and `reports/EXPECTED-*.md` once real
   logs start.

### If your work is not accounting

The system still works. `general-work.md` is domain-neutral — completeness, consistency,
commitments, authority, escalation. Swap `accounting-india.md` for your own domain rules
and update the `checklists:` list in `employees.yaml`. The bots read whatever is there;
none of the domain knowledge is baked into them.

---

## Scheduled run

A Routine runs the panel automatically at **20:00 IST, Monday to Saturday**
(`30 14 * * 1-6` UTC). It starts a fresh session, runs `/daily-review` for the current
IST date, commits the report back to this branch, and sends a push notification with the
*Fix today* list.

It is deliberately quiet when there is nothing to do: if no logs were filed, or only the
test fixture is present, it reports that in one line and stops rather than manufacturing
findings.

The Routine lives against your Claude account, not in this repo. Ask Claude to
"list my routines" to change the time, pause it, or delete it — it is named
**Seyaa — nightly work review**.

---

## The rules the bots follow

Set out in full in `CLAUDE.md`. The two that matter most:

**Cite or drop it.** Every finding names the file, the row, quotes what is written, and
gives the correct value. A finding nobody can locate in ten seconds is not a finding.

**Never invent a mistake.** If the log does not say enough to judge something, that is not
a mistake — it goes under `UNVERIFIABLE` with the one specific thing needed to settle it.

A report that says "three findings, everything else clean" is a good day's output. The
moment these bots start padding, people stop reading them, and then the real findings go
past unread too.

---

## What this system cannot do

It reviews **what people write down**, not what they did. A mistake that never reaches a
log is invisible to it. It will not catch a wrong figure that is internally consistent, a
fabricated entry, or work nobody logged at all.

Treat it as a second pair of eyes over the record — not as assurance, and not as a
substitute for review by someone who signs off.
