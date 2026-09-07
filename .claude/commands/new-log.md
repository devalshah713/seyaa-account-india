---
description: Create today's work log for an employee from the template
argument-hint: "<employee-id> [YYYY-MM-DD — defaults to today]"
allowed-tools: Read, Write, Bash
---

Create a work log for **$1** dated **$2** (if `$2` is empty, use today from `date +%F`).

1. Check `$1` is in `team/employees.yaml`. If not, list the valid ids and stop.
2. If `work-logs/<date>/<$1>.md` already exists, **stop and say so.** Do not overwrite it
   — that would silently destroy a day's work. Offer to open it instead.
3. Copy `work-logs/TEMPLATE.md` to `work-logs/<date>/<$1>.md`, creating the folder.
4. Fill in the frontmatter: `employee`, `date`. Leave `hours` at 0.
5. Remove the instructional blockquote under the title — it is guidance for the template,
   not part of a real log.
6. Pre-fill section 4 with anything still open from this employee's previous log: items
   under *Pending / carried forward* and *Blocked on someone*, each marked
   `[carried from <date>]`. This is the point of the command — carried work is what
   silently disappears, and re-typing it is what people skip.
7. Print the path and stop. Do not fill in any work.
