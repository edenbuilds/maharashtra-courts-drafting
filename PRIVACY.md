# Privacy

This connector runs entirely on the user's machine. It collects no telemetry, has no remote publisher endpoint, and does not upload case papers.

## Local privacy firewall

The Reader stage substitutes, before any model-facing artifact is written:

- party names → `[Petitioner-A]`, `[Respondent-B]`, `[Claimant-A]`, `[Accused-A]`
- residential / business addresses → `[Address-Placeholder]`
- Aadhaar, PAN, GSTIN, TAN, DIN, passport, driving licence → typed placeholders
- FIR / CR / Crime / Suit / OA / WP / Diary numbers → `[Case-No-Placeholder]`
- phone numbers and emails → `[Contact-Placeholder]`
- currency figures in dispute → `[Amount-Placeholder]`

Downstream stages work on placeholders. Re-substitution happens only at the final local `.docx` render.

Case papers may attract privilege under Section 132 of the Bharatiya Sakshya Adhiniyam, 2023. The user remains the data fiduciary for client personal data under the Digital Personal Data Protection Act, 2023. Section 17(2)(a) of that Act covers processing for legal proceedings; notice, consent and grievance duties remain the user's.
