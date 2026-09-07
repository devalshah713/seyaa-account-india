# India stock sheet — pass/fail, entries made 2026-09-07

Sheet: NEW (Stock Sheet of Seyaa Factory for India). Audited read-only against
`team/checklists/india-stock-sheet.md`. Export taken 2026-09-07, 11:41 IST.

> **Which rows count as "today".** The export renders today's entries as DATE
> `2026-07-09`, not `2026-09-07`. `S1815C` was watched appearing in the sheet
> during this session and carries `2026-07-09`, which settles it: the sheet's
> `07/09/2026` comes out of the exporter as 9 July. See the date question below.

Scope: 23 row(s) dated 2026-07-09.
**23 PASS · 0 FAIL** out of 23 rows.

| Stock # | Row | Result | Problems |
|---|---|---|---|
| S1802C | 1803 | PASS | — |
| S1803C | 1804 | PASS | — |
| S1804C | 1805 | PASS | — |
| S1805C | 1806 | PASS | — |
| S1806C | 1807 | PASS | — |
| S1807C | 1808 | PASS | — |
| S1808C | 1809 | PASS | — |
| S1809C | 1810 | PASS | — |
| S1810C | 1811 | PASS | — |
| S1811C | 1812 | PASS | — |
| S1812C | 1813 | PASS | — |
| S1813C | 1814 | PASS | — |
| S1814C | 1815 | PASS | — |
| S1815C | 1816 | PASS | — |
| S1816C | 1817 | PASS | — |
| S1817C | 1818 | PASS | — |
| S1818C | 1819 | PASS | — |
| S1819C | 1820 | PASS | — |
| S1820C | 1821 | PASS | — |
| S1821C | 1822 | PASS | — |
| S1822C | 1823 | PASS | — |
| S1823C | 1824 | PASS | — |
| S1824C | 1825 | PASS | — |

---

## Cross-check: rows touched since the 10:14 IST watermark

Scope: 11 row(s) new or changed since 2026-09-07T10:14:16.
**11 PASS · 0 FAIL** out of 11 rows.

| Stock # | Row | Result | Problems |
|---|---|---|---|
| S1799C |  | PASS | — |
| S1815C |  | PASS | — |
| S1816C |  | PASS | — |
| S1817C |  | PASS | — |
| S1818C |  | PASS | — |
| S1819C |  | PASS | — |
| S1820C |  | PASS | — |
| S1821C |  | PASS | — |
| S1822C |  | PASS | — |
| S1823C |  | PASS | — |
| S1824C |  | PASS | — |

---

## Question for Deval — date storage

147 rows carry a stock-in date **in the future** relative to 2026-09-07 as the
export reads them (2026-10-07, 2026-11-07, 2026-12-08 and so on). Every one becomes
a sensible past date if day and month are swapped, and today's own entries read as
`2026-07-09`. That points to the dates being stored day/month transposed rather than
to 147 genuine future dates.

This is not being flagged as 147 errors, because one setting explains all of them.
It needs one answer from you: **is column B storing dates the way you intend?**
Until it is settled, the `--date` filter takes the export's reading literally, and
the "invoice date is not in the future" style checks are held back.
