# Setting up the 12:00 / 17:00 IST scheduled run

**This one cannot be created from a Claude Code session. You have to create it from the
claude.ai Routines UI.** The reason is specific and worth understanding, because it also
tells you when the scheduled run will break.

## Why

The audit must read **formulas**, not displayed values — a hardcoded `=M1279*250` shows a
perfectly ordinary number in the cell, and a value-only check passes it silently. That is
the most damaging error class on these sheets.

Reading formulas means pulling the workbook as an xlsx export, and the only route to that
from a Claude session is the **Google Drive connector**. Two constraints then bite:

- `docs.google.com` is blocked by the execution environment's network policy, so there is
  no direct-download fallback. Verified: the proxy returns `403` on CONNECT.
- A Routine created from inside a Claude Code session fires sessions that carry **no
  connectors**, and the parameter that would attach one is disabled for this organisation.

So a Routine created from here would wake up twice a day, find no Google Drive, and do
nothing — while looking, on the schedule list, exactly like a job that is running. That is
worse than having no Routine at all, so one has not been created.

## How

In **claude.ai → Routines → New**, attach the **Google Drive** connector, point it at this
repository on branch `claude/work-analysis-bots-amf639`, and set:

**Schedule (UTC — IST is UTC+5:30):**

```
30 6,11 * * 1-5
```

06:30 UTC = 12:00 IST · 11:30 UTC = 17:00 IST · Monday to Friday.

**Prompt — paste verbatim:**

---

India stock sheet audit run (A/C INDIA OLD/NEW SHEET). Scheduled check — 12:00 or 17:00 IST.

Repo: devalshah713/seyaa-account-india, branch claude/work-analysis-bots-amf639.

Read `team/checklists/india-stock-sheet.md` and `.claude/agents/stock-auditor.md` first. They hold the locked rules, the file IDs, the verified column map and the reference rows. Do not audit from memory.

AUDIT ONLY. Never edit either Google Sheet, for any reason. You have no write path to them and must not build one.

Scope this run: the NEW sheet only (`1sWcfksBvp42a91q4LIkbx6qYZpi3AHv4DESshysvM-Y`). OLD is audited only when Deval asks.

Steps:

1. Ensure openpyxl is available: `pip install openpyxl -q`

2. Download the workbook through the Google Drive connector, asking for the xlsx export so FORMULAS come with it:
   mcp__Google_Drive__download_file_content(fileId="1sWcfksBvp42a91q4LIkbx6qYZpi3AHv4DESshysvM-Y", exportMimeType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
   It is too large to return inline, so the harness saves it to a path and tells you that path. That is expected.

   If the Google Drive connector is unavailable, STOP. Report that the connector did not reach the session and that no audit ran. Never audit stale or cached data and present it as current, and never fall back to reading displayed values instead of formulas — a value-only check silently passes a hardcoded price, the most damaging error class on these sheets.

3. `python3 stock-audit/decode.py <saved path> /tmp/india-new.xlsx`

4. `python3 stock-audit/audit.py /tmp/india-new.xlsx --label india-new`
   Incremental by default — only rows new or changed since the last run. Do NOT pass --full.

5. Commit and push the updated `stock-audit/state/india-new.json` to branch claude/work-analysis-bots-amf639, message "Stock audit watermark — <date> <time> IST". The container is wiped between runs, so an uncommitted watermark means the next run re-reports the entire backlog. Commit ONLY the state file, plus a findings report under reports/ if you wrote one.

6. Report.

   IF THERE ARE NO NEW OR CHANGED ROWS, OR NO ERRORS: reply with exactly one line — "No changes." Nothing else. No all-clear, no summary, no list of what you checked. Silence when clean is a locked instruction from Deval, not a style preference. A ping carrying no action costs him attention he needs for the ones that do.

   IF THERE ARE ERRORS: one short batch, simple table, no preamble.

   | Stock # | Cell | Problem |
   |---|---|---|

   Every row carries the stock number from Col A and the exact cell.

   Questions go in a separate table and never mix into the errors. Do not re-ask anything already on the open list in the checklist.

   More than about 25 errors: give the count, the breakdown by rule from the script's own summary, and the ten most damaging — wrong money first (hardcoded prices, wrong karat rate, wrong labour rate, breakup that does not reconcile). Then ask whether Deval wants the rest.

If the script cannot find the header row, or a tab is missing, or a whole column of findings appears at once, STOP and say so instead of reporting. That pattern means the sheet layout changed, not that a hundred entries broke at once, and reporting it as entry errors would waste the entry team a day.

Never invent a rule. Anything the checklist does not cover is a question for Deval, not a finding. Do not open a pull request.

---

## Checking it actually works

After the first fire, confirm three things:

1. It reported either `No changes.` or a findings table — **not** a connector error.
2. `stock-audit/state/india-new.json` got a new commit. Without that, every run re-reports
   the whole backlog and the batch becomes unreadable within a day.
3. It did not touch the sheet. `modifiedTime` on the Google Sheet should be unchanged by
   the run.

## Until then

Run it by hand from a Claude Code session, where the connector is present:

```
/stock-audit
```
