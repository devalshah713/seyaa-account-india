# General Work Checklist

Applies to every employee regardless of what they handle. `work-auditor` audits against
this file. It is domain-neutral on purpose — if your team's work is not accounting, this
file alone still gives you a working review system.

---

## 1. Completeness

- [ ] Every task the employee says they started has a stated outcome: done, pending, or handed over. A task mentioned once and never resolved is a **MEDIUM** finding.
- [ ] Every entry has a document reference (invoice no., voucher no., ticket, file name). No reference = **MEDIUM**, cannot be verified later.
- [ ] Every handover names the person it went to. "Handed over" with no name is **HIGH** — nobody owns it.
- [ ] Hours logged are roughly consistent with work described. A 30-line day logged as 1 hour, or a 2-line day logged as 9 hours, is **LOW** — ask, don't assume.

## 2. Internal consistency

- [ ] The same figure quoted twice in the log matches both times. A mismatch is **HIGH**.
- [ ] A party/client named several times is spelled and identified the same way each time. Variants are **MEDIUM** — they become duplicate master records.
- [ ] Today's "pending" items include yesterday's unresolved "pending" items, or explain why they dropped off. Silently vanishing work is **HIGH**.
- [ ] Stated conclusions follow from stated facts. If the log says a reconciliation matched but also lists an unexplained difference, that is **CRITICAL**.

## 3. Commitments

- [ ] Every promise to a client, colleague, or manager has a named due date. Undated commitments are **MEDIUM**.
- [ ] No commitment is made for a date already known to be blocked (leave, filing crunch, pending input from someone else). **HIGH** if it is.
- [ ] Anything the employee is waiting on names who they are waiting on and since when. A blocker with no owner never unblocks — **HIGH** past 2 working days.

## 4. Authority and process

- [ ] Work requiring approval says who approved it. Missing approval on anything client-facing or money-moving is **CRITICAL**.
- [ ] Anything sent outside the firm (client, department, bank, portal) is marked as sent, with what was sent and to whom. **CRITICAL** if a submission is implied but unconfirmed.
- [ ] Deviations from standard process are stated and reasoned, not silent. Silent deviation is **HIGH**.
- [ ] Nothing in the log contains a password, OTP, full bank account number, or portal credential. That is **CRITICAL** and must be redacted immediately — flag it, name the line, and do not repeat the value in the report.

## 5. Escalation quality

- [ ] Uncertainties are written down rather than resolved by guessing. An employee who logged a question gets credit, not a finding.
- [ ] A guess presented as a fact is **HIGH**. Look for "I think", "probably", "assumed" attached to a figure or a treatment that was then acted on.
- [ ] Repeated identical questions across days mean the answer was never recorded anywhere — that is a **MEDIUM** finding against the process, not the person.

## 6. What is NOT a finding

Do not report these. They generate noise and get the whole report ignored.

- A short log on a genuinely light day.
- Round-number amounts.
- An unfamiliar party name.
- A large amount, by itself.
- Informal wording, typos in prose, or grammar.
- Work done differently from how you would have done it, where both are correct.
- Anything you would have to speculate about to call wrong — use `UNVERIFIABLE` instead.
