# Expected findings — `work-logs/2026-09-07/example-junior.md`

This is the answer key for the test fixture. Run:

```
/review-employee example-junior 2026-09-07
```

and compare. A healthy panel finds **most** of these. Judge it on the CRITICALs — if it
misses a CRITICAL, tighten the relevant checklist section. If it reports findings that
are **not** on this list and cannot be defended from the log, your bots are hallucinating
and rule 2 in `CLAUDE.md` needs reinforcing.

Computed as at **2026-09-07**.

| # | Where | Severity | The mistake | Correct position |
|---|-------|----------|-------------|------------------|
| 1 | Entries, row 1 | CRITICAL | Tax booked as 8,010. 18% of 45,000 = **8,100**. Digits transposed; total should be 53,100, not 53,010. | Understates ITC by ₹90 and will mismatch GSTR-2B. |
| 2 | Entries, row 2 | CRITICAL | CGST+SGST charged on goods dispatched from Gujarat to Pune. | Inter-state supply → **IGST 18%**. Wrong head cannot be fixed by a ledger entry once filed. |
| 3 | Entries, row 2 | CRITICAL | Party stated as Maharashtra but GSTIN `24ABCDE1234F1Z5` carries state code **24 (Gujarat)**. Maharashtra is **27**. | Either the party master or the place of supply is wrong. Both drive #2. |
| 4 | Entries, row 2 | HIGH | PAN embedded in that GSTIN is `ABCDE1234F` — 4th character `D` is not a valid entity code. | Valid codes are P, C, H, F, A, T, B, L, J, G. The GSTIN is not genuine as recorded. |
| 5 | Entries, row 3 | CRITICAL | 12% applied to an invoice dated 2026-09-04. The 12% slab was withdrawn on **22 Sep 2025**. | Must be a currently valid slab on the document date. |
| 6 | Entries, row 3 | CRITICAL | GTA bill booked as a normal forward-charge purchase. The bill is silent on forward charge — silence means the GTA has **not** opted for it. | **RCM applies.** Liability payable in cash, not through the credit ledger. |
| 7 | Entries, row 4 | CRITICAL | Software support fee deducted under **194C**. That is a contract-for-work section. | Software/technical support is **194J**. A 194C entry will not match the deductee's 26AS. |
| 8 | Entries, row 4 | CRITICAL | 1% applied to a **Pvt Ltd**. Even if 194C were right, 1% is the individual/HUF rate. | Companies attract 2% under 194C; 194J is 2% (technical) or 10% (professional). |
| 9 | Entries, row 4 | HIGH | TDS computed on 70,800 — the **GST-inclusive** total. | Base is the taxable value of **60,000**, GST shown separately. Deducted ₹708 against ₹1,200 (194J technical) or ₹6,000 (194J professional). Short deduction either way. |
| 10 | Entries, row 5 | HIGH | No HSN code — "will add later". | HSN is mandatory on the goods line and **blocks GSTR-1 filing**. |
| 11 | Filings | CRITICAL | TDS payment for Aug 2026 is **due today, 2026-09-07**, and is marked pending. | Missing it triggers 1.5% per month from the date of deduction, not from the due date. |
| 12 | Filings | HIGH | GSTR-1 for Aug 2026 due **2026-09-11**, not started. 4 days out. | Late fee plus the customer's credit is held up. |
| 13 | Tasks | CRITICAL | Bank reconciliation reported as "completed and matched" while ₹4,500 sits unexplained in suspense. | A reconciliation with an unexplained difference has not matched. Contradiction inside the same line. |
| 14 | Pending | CRITICAL | Nirmal Traders invoice of 2026-02-20 unpaid, ITC claimed in Feb. **180 days expired on 2026-08-19** — 19 days ago. | ITC must be reversed under Rule 37 with interest at 24% p.a., and may be reclaimed on payment. |
| 15 | Handed over | HIGH | Patel & Sons file handed over with **no recipient named**. | Half-finished ledger scrutiny with no owner. |
| 16 | Commitments | MEDIUM | Ledger promised to Mr. Kothari with **no due date**. | Undated commitments do not get done. |
| 17 | Blocked | HIGH | Waiting on the partner since 2026-09-01 — 6 days, past the 2-working-day rule. | Needs escalation, not continued waiting. |
| 18 | Questions | — *not a finding* | Freight rate assumption. Freight inside a composite supply takes the **principal supply's rate**, so 18% was correct. | Confirm it to the employee. Logging the uncertainty was the right call. |

## Expected `UNVERIFIABLE`

A good report also says what it *cannot* judge, rather than guessing:

- **Row 4 tax head.** IGST used for Vega Softech, but the log never states the supplier's state. Need the vendor's GSTIN.
- **Row 4 TDS rate within 194J.** "Annual software support" could be technical services (2%) or professional services (10%). Need the contract or the invoice narration.
- **E-invoice IRN on rows 2 and 5.** No IRN recorded. Whether one was required depends on the firm's aggregate turnover, which is not in the log.
- **Row 3 correct GTA rate.** RCM on GTA is 5%, but confirm against the current notification before passing the correction.
