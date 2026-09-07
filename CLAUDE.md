# Seyaa Account India — Work Review System

This repository is not a software project. It is a **daily work review system** for the
team. Employees file a short structured log of what they did each day; a panel of
review bots reads those logs and finds the mistakes before a client, an auditor, or the
department does.

## Layout

| Path | What lives here |
|---|---|
| `team/employees.yaml` | The roster. Who works here, what they handle, who reviews them, what each person has historically got wrong. |
| `team/checklists/` | The rules the bots audit against. **This is the only place domain rules live.** Edit these, not the agents. |
| `work-logs/YYYY-MM-DD/<employee-id>.md` | One log per employee per day. Format in `work-logs/TEMPLATE.md`. |
| `reports/` | Bot output. One consolidated report per day, plus weekly summaries. |
| `.claude/agents/` | The review bots. |
| `.claude/commands/` | Slash commands that run them. |

## The bots

| Bot | What it hunts |
|---|---|
| `work-auditor` | General mistake finder over one employee's day. The workhorse. |
| `numbers-auditor` | Recomputes every figure. Arithmetic, tax amounts, totals, balances. |
| `compliance-auditor` | Statutory correctness — GSTIN/PAN validity, GST rates, TDS sections, HSN, invoice rules. |
| `deadline-tracker` | Commitments and statutory due dates. What slipped, what is about to. |
| `pattern-analyst` | Reads across days and people. Repeat mistakes, who needs training, who needs closer review. |

## Rules every bot follows

These are binding. A review that breaks them is worse than no review.

1. **Cite or drop it.** Every finding names the exact file, the exact line or row, quotes
   what is written, states what is wrong, and gives the correct value. A finding that
   says "check the GST treatment" is not a finding — delete it.

2. **Never invent a mistake.** If the log does not contain enough information to judge
   something, that is not a mistake. Record it under `UNVERIFIABLE` with the one specific
   thing you would need to see. Padding a report with speculation trains the team to
   ignore the report.

3. **Never assume a mistake from a round number, an unusual party name, or a large
   amount.** Those are not evidence.

4. **Recompute, don't eyeball.** If a figure can be checked with arithmetic, do the
   arithmetic. Show it: `18% of 45,000 = 8,100, log says 8,010 — digits transposed`.

5. **Rates and thresholds come from `team/checklists/`, never from memory.** If the
   checklist does not cover a case, say so and flag the checklist as needing an entry.
   Tax rates and thresholds change; the checklist is the single point of update.

6. **Judge the work, not the person.** Findings describe what is wrong in the record.
   No commentary on effort, attitude, or capability. `pattern-analyst` may note that a
   mistake type recurs for a person — that is a training signal, stated neutrally.

## Severity

| Level | Meaning | Timing |
|---|---|---|
| `CRITICAL` | Money is wrong, something was filed or sent wrong, or a statutory line was crossed. | Fix today. |
| `HIGH` | Not yet harmful, but becomes CRITICAL at filing or month-end close. | Fix before close. |
| `MEDIUM` | Wrong but recoverable internally. Documentation or process gap. | Fix this week. |
| `LOW` | Hygiene. Naming, narration, missing reference. | Batch it. |
| `UNVERIFIABLE` | Cannot be judged from the log. Names the missing information. | Ask the employee. |

## Conventions

- Employee IDs are lowercase-hyphenated and must match `team/employees.yaml`.
- Dates are `YYYY-MM-DD` everywhere.
- Amounts are INR. Write them plainly (`45000` or `45,000`), never `45k`.
- Financial year runs 1 April – 31 March. `FY 2026-27` means Apr 2026 – Mar 2027.
