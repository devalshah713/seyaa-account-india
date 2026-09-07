# Indian Accounting & Compliance Checklist

Audited against by `compliance-auditor` and `numbers-auditor`.

> ## ⚠️ VERIFY BEFORE RELYING ON RATES
>
> **Last reviewed: FY 2026-27 (as at 2026-09-07). Reviewed by: _unassigned_.**
>
> Rates, thresholds and due dates below were correct to the best of the drafter's
> knowledge on the date above and **have not been verified against a current
> notification**. GST slabs were restructured on 22 Sep 2025 and TDS thresholds changed
> on 1 Apr 2025 — assume more has changed since.
>
> **Whoever owns compliance: verify every figure in this file against the current
> Finance Act, GST notifications and CBDT circulars, then set the reviewer name and date
> above.** Bots are instructed to cite this file as their authority, so an error here
> propagates into every report. Re-verify at each Budget and at each GST Council meeting.

---

## 1. GSTIN validation

Format: **15 characters** — `[2 state code][10 PAN][1 entity code][Z][1 checksum]`

- [ ] Exactly 15 characters, no spaces. **CRITICAL** if not.
- [ ] Chars 1–2 are a valid numeric state code (01 Jammu & Kashmir … 37 Andhra Pradesh, 97 Other Territory). **CRITICAL** if out of range.
- [ ] Chars 3–12 are a valid PAN (see §2).
- [ ] Char 14 is `Z` for a normal taxpayer. Anything else is unusual — **HIGH**, verify the registration type.
- [ ] State code matches the party's stated state. A Gujarat address with a `27` (Maharashtra) GSTIN is **CRITICAL** — wrong party or wrong place of supply.
- [ ] PAN embedded in the GSTIN matches the PAN recorded separately for the same party. Mismatch is **CRITICAL**.

## 2. PAN validation

Format: **10 characters** — `AAAAA9999A` (5 letters, 4 digits, 1 letter).

- [ ] Matches that pattern exactly. **CRITICAL** if not.
- [ ] 4th character is the correct entity type for the party:
  `P` individual · `C` company · `H` HUF · `F` firm/LLP · `A` AOP · `T` trust ·
  `B` body of individuals · `L` local authority · `J` artificial juridical person · `G` government
  A vendor recorded as a company with `P` in position 4 is **HIGH** — wrong master or wrong TDS rate will follow.
- [ ] 5th character is the first letter of the surname (individuals) or entity name. A clear mismatch is **MEDIUM** — likely wrong PAN captured.

## 3. GST rates and treatment

**Current slabs (w.e.f. 22 Sep 2025 — verify):** `0%` · `5%` · `18%` · `40%` (demerit/luxury)
**Retained special rates:** `3%` gold, silver, jewellery · `0.25%` rough diamonds
**Legacy slabs `12%` and `28%`** were withdrawn on 22 Sep 2025 — valid only on transactions **dated before** that.

- [ ] Rate applied is one of the slabs valid **on the document date**, not on today's date. A 12% or 28% rate on a post-22-Sep-2025 invoice is **CRITICAL**. The same rate on an older invoice is correct — do not flag it.
- [ ] CGST + SGST used for intra-state, IGST for inter-state. Wrong head is **CRITICAL** — it cannot be corrected by a simple ledger entry once filed.
- [ ] CGST equals SGST exactly. Any difference is **CRITICAL**.
- [ ] CGST + SGST together equal the IGST rate that would have applied (18% = 9% + 9%). **CRITICAL** if not.
- [ ] Place of supply drives the head, not the billing address. Services to a client in another state billed with CGST+SGST is **CRITICAL**.
- [ ] HSN code present on every goods line, SAC on every service line. Missing is **HIGH** — it blocks return filing.
- [ ] HSN digit count meets the requirement for the entity's turnover (4 / 6 digits by slab). Short codes are **MEDIUM**.
- [ ] Exempt, nil-rated, zero-rated and non-GST are not used interchangeably. Exports and SEZ supplies are **zero-rated**, not exempt — treating an export as exempt wrongly blocks ITC and is **CRITICAL**.
- [ ] Freight, packing and insurance charged on an invoice carry the **same rate as the principal supply** (composite supply). Charging them at a different rate is **HIGH**.

## 4. Reverse charge (RCM)

Flag as **CRITICAL** if any of these were booked as normal forward charge:

- [ ] Legal services from an advocate or firm of advocates
- [ ] Goods Transport Agency, where the GTA has not opted for forward charge
- [ ] Director's services to the company (sitting fees, commission)
- [ ] Sponsorship services
- [ ] Import of services from outside India
- [ ] Security services (manpower supply of security personnel)
- [ ] Renting of motor vehicle from a non-body-corporate to a body corporate
- [ ] Renting of commercial property by an unregistered supplier to a registered recipient (w.e.f. 10 Oct 2024)

Also: **RCM liability must be paid in cash**, never set off against ITC. Booking RCM
payment through the credit ledger is **CRITICAL**.

## 5. Input tax credit

- [ ] ITC claimed only where the invoice appears in **GSTR-2B**. Claiming on a purchase not in 2B is **CRITICAL** — it will be reversed with interest.
- [ ] ITC not claimed on blocked credits under **Sec 17(5)**: motor vehicles up to 13 seats, food and beverages, outdoor catering, club and gym membership, health insurance (unless obligatory under law), works contract and construction of immovable property, goods lost/stolen/destroyed/written off, gifts and free samples, CSR expenditure. Any of these claimed is **CRITICAL**.
- [ ] Supplier paid within **180 days** of invoice date, else ITC reversed under Rule 37. An unpaid invoice past 180 days with ITC retained is **CRITICAL**.
- [ ] ITC for a financial year claimed by **30 November** following the FY end, or the annual return date if earlier. Past that, it is lost — **CRITICAL** if a late claim is being attempted.
- [ ] Common credits apportioned under Rules 42/43 where there are exempt supplies. Not apportioned is **HIGH**.

## 6. TDS

Rates and thresholds below are **FY 2025-26 / FY 2026-27 as understood — verify.**

| Section | Nature | Rate | Threshold |
|---|---|---|---|
| 192 | Salary | Slab rates | Taxable income |
| 194A | Interest (non-securities) | 10% | ₹50,000 bank / ₹10,000 other / ₹1,00,000 senior citizen |
| 194C | Contractor | 1% individual & HUF, 2% others | ₹30,000 single / ₹1,00,000 aggregate p.a. |
| 194H | Commission, brokerage | 2% | ₹20,000 |
| 194I(a) | Rent — plant & machinery | 2% | ₹50,000 per month |
| 194I(b) | Rent — land, building, furniture | 10% | ₹50,000 per month |
| 194J | Professional services | 10% | ₹50,000 |
| 194J | Technical services, call centre | 2% | ₹50,000 |
| 194Q | Purchase of goods | 0.1% on value above ₹50 lakh | ₹50 lakh p.a. |
| 194T | Partner's remuneration, interest, commission | 10% | ₹20,000 |
| 194IA | Purchase of immovable property | 1% | ₹50 lakh |
| 206AA | **No PAN furnished** | **20%** (or higher of specified rate) | — |

- [ ] Section chosen matches the nature of payment. **194C on a professional fee, or 194J on a contractor bill, is CRITICAL** — the deductee's 26AS will not match and the notice comes to us.
- [ ] Rate matches the deductee's **constitution** (194C: 1% for individual/HUF, 2% for company/firm). Wrong rate is **CRITICAL**.
- [ ] TDS computed on the **taxable value excluding GST**, where GST is shown separately. Deducting on the GST-inclusive amount is **HIGH** (over-deduction) and on the wrong base either way.
- [ ] Threshold tested on **aggregate for the year**, not the single bill. Missing TDS because one bill was below threshold while the year's total crossed it is **CRITICAL**.
- [ ] No PAN on record → 20% under 206AA. Deducting at the normal rate without a PAN is **CRITICAL**.
- [ ] Lower/nil deduction certificate (197) on file if a reduced rate was used, with its certificate number quoted. Reduced rate with no certificate reference is **CRITICAL**.

## 7. Invoices and documents

- [ ] Invoice number is from a **continuous series** for the financial year, with no gaps and no duplicates. A repeated number is **CRITICAL**; a gap is **HIGH** (a cancelled invoice must still be recorded as cancelled).
- [ ] Invoice number is at most 16 characters, and uses only letters, digits, `/` and `-`.
- [ ] Invoice date is within the current financial year and **is not in the future**. A future-dated invoice is **CRITICAL**.
- [ ] Both supplier and recipient GSTIN present on a B2B invoice. Missing recipient GSTIN converts it to B2C and the customer loses the credit — **CRITICAL**.
- [ ] E-invoice IRN generated where aggregate turnover exceeds the e-invoicing threshold (₹5 crore). Missing IRN makes the invoice invalid — **CRITICAL**.
- [ ] E-invoice reported to the IRP within **30 days** of the invoice date, for entities above the applicable turnover. Late reporting is **CRITICAL** — the window does not reopen.
- [ ] E-way bill generated for consignments above **₹50,000**. Missing is **CRITICAL**.
- [ ] Credit and debit notes reference the **original invoice number and date**. A note without that link is **HIGH**.
- [ ] Credit note issued no later than **30 November** following the FY of the original supply. Later than that, GST cannot be reduced — **CRITICAL**.

## 8. Ledger and entry hygiene

- [ ] Total debits equal total credits on every voucher. Any imbalance is **CRITICAL**.
- [ ] Entry is posted to the correct financial year and period. A transaction posted after a period was closed and filed is **CRITICAL**.
- [ ] Capital expenditure is not booked to a revenue head, and vice versa. **HIGH** — it distorts both P&L and the depreciation schedule.
- [ ] Every voucher carries a narration that states what, for whom, and against which document. Blank or "being amount paid" narrations are **MEDIUM**.
- [ ] Party ledger used is the correct one where similar names exist. Posting to the wrong "Sharma Traders" is **CRITICAL**.
- [ ] No suspense/temporary account left with a balance at day end. **HIGH**.
- [ ] Bank entries match the bank statement line — date, amount, and direction. A reconciling item created to force a match is **CRITICAL**.
- [ ] Round-sum journal entries at period end are supported by a working. Unsupported is **HIGH**.

## 9. Statutory due dates

| Filing | Due |
|---|---|
| GSTR-1 (monthly) | 11th of following month |
| GSTR-1 (QRMP, quarterly) | 13th of month following the quarter |
| GSTR-3B (monthly) | 20th of following month |
| GSTR-3B (QRMP) | 22nd or 24th of month following quarter, by state group |
| PMT-06 (QRMP monthly payment) | 25th of following month |
| CMP-08 (composition) | 18th of month following quarter |
| GSTR-9 / 9C (annual) | 31 December following FY end |
| TDS payment | 7th of following month — **except March, which is 30 April** |
| TDS return 24Q / 26Q / 27Q | Q1 31 Jul · Q2 31 Oct · Q3 31 Jan · Q4 31 May |
| TCS return 27EQ | Q1 15 Jul · Q2 15 Oct · Q3 15 Jan · Q4 15 May |
| Form 16 | 15 June |
| Form 16A | 15 days from the TDS return due date |
| Advance tax | 15 Jun 15% · 15 Sep 45% · 15 Dec 75% · 15 Mar 100% |
| PF (ECR) and ESI | 15th of following month |
| Tax audit report (3CA/3CB-3CD) | 30 September |
| ITR — non-audit | 31 July |
| ITR — audit cases | 31 October |
| ITR — transfer pricing | 30 November |
| DIR-3 KYC | 30 September |
| AOC-4 | Within 30 days of the AGM |
| MGT-7 | Within 60 days of the AGM |

- [ ] Any of the above falling within the **next 7 days** and not yet actioned is **HIGH**.
- [ ] Any already **past** and not filed is **CRITICAL**, with the late fee and interest exposure stated.
- [ ] Interest on late GST payment runs at **18% p.a.**; excess ITC claimed at **24% p.a.** Late TDS deduction attracts **1% per month**, late payment after deduction **1.5% per month**, counted from the date of deduction — not the due date.
