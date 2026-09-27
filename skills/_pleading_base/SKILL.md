---
name: pleading-base
description: Shared Maharashtra pleading skeleton for Bombay High Court and State tribunals. Load with every case-type skill.
---

# Shared pleading skeleton

Every draft in this pack, unless a tribunal form says otherwise, is assembled in this order.

1. Forum header from `forum-config` (full stop at the end of the Bombay HC line).
2. Side / jurisdiction sub-line where the forum uses one (Appellate Side / Original Side / Ordinary Original Civil Jurisdiction).
3. Case number blank + year.
4. Cause title — applicants / petitioners / appellants on the left, respondents on the right.
5. Parties separator from the forum-config (`///VERSUS///` on Bombay HC appeals).
6. Statutory opening paragraph (the section / article that opens the door of the forum).
7. Synopsis (High Court and most appeals). Numbered, two to five lines each.
8. List of dates / events (High Court writs and heavy civil appeals).
9. Statement of facts. One fact per numbered paragraph. Every document gets an inline annexure marker the first time it is relied upon.
10. Grounds. Legal propositions, not a second facts chapter. Cite the section and the proposition. Do not invent citations.
11. Prayer. Numbered clauses. Last clause is the forum-config catch-all.
12. Place, date, counsel block with enrolment number.
13. Verification in the first person, signed by the filing party or authorised signatory, with date and place.
14. Vakalatnama (separate sheet).
15. Index / list of annexures with page numbers left blank for the filing clerk.
16. Accompanying applications the case-type skill lists (stay, exemption, condonation, suspension of sentence, urgency).

## Register

- Formal Indian pleading English. Short sentences. No "moreover", "furthermore", "it is pertinent to note", "delve", "tapestry", em-dash stacks, or emoji.
- Dates as `15 March 2026` in prose; `15.03.2026` in tables.
- Rupees as `Rs. 12,50,000/-` the first time, then `Rs. 12.50 lakh`.
- BNSS / BSA / BNS citations for events after the new codes commenced; CrPC / Evidence Act / IPC citations when the FIR or the impugned order predates commencement. State both when the record is mixed, and say why.
- Never assert a judgment citation that is not in the case folder or expressly supplied by the user.

## Privacy

Draft on placeholders produced by the Reader. Do not restore real identifiers until `save_draft_as_docx`.
