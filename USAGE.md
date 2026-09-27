# Usage

## First message in a new chat

> Draft a civil writ for my client against the Thane Municipal Corporation. Impugned notice dated 3 January 2026, demolition of a shop at [address]. Prayer for certiorari and stay. Bench should follow the district.

Expected tool order:

1. `get_agent_instructions()`
2. `list_case_types()` / `resolve_bench("Thane", "high-court")` → `bombay-hc-mumbai`
3. `create_case_folder(...)`
4. Reader through Overseer
5. `save_draft_as_docx`

## More prompts that map cleanly

- "ABA before the Nagpur Bench in FIR from Chandrapur PS under BNS 118."
- "MAT OA at Aurangabad against a promotion order of a Zilla Parishad teacher from Latur."
- "s.166 claim at Pune MACT, death case, private car, United India policy."
- "s.173 appeal against the Wardha MACT award — which bench?"
- "District Commission complaint, Thane, deficient interior-design service, consideration Rs.18 lakh."
- "DRT OA for a cash-credit account, borrower factory at Jalgaon."
- "ULP complaint under Schedule IV item 1, Industrial Court Pune, illegal termination."
- "MahaRERA delay-possession complaint, registered project in Navi Mumbai."
- "s.138 complaint, cheque drawn on a Pune branch, presented at HDFC Thane."
- "Gift deed of a Pune flat from father to daughter, ready-reckoner to be filled by me."

## Opposite-side and accompaniment prompts

> Draft an affidavit in reply for Respondent No. 2 in WP (L) _____ of 2026 at the Principal Seat. Petitioner challenges TMC’s demolition notice. Our record: notice served, hearing given, structure is unauthorised.

> Rejoinder to the State reply in the same writ — only the new suppression objection and the new annexure R-4.

> Stay application travelling with the civil writ — demolition listed for Monday.

Expected extras: `get_template("wp-reply-affidavit")` / `list_templates()`. Case-type keys include `wp-reply-affidavit`, `wp-rejoinder`, `stay-application`, `mat-reply`, `mact-written-statement`, `consumer-written-version`, `drt-written-statement`, `civil-written-statement`.

## Hard rules

- If the user types **APL**, do not draft anticipatory bail.
- If the user types **MAT**, draft an Administrative Tribunal OA unless they clearly say Family Court / HMA.
- Kolhapur-circuit districts: say that the circuit must be sitting that week, otherwise Principal Seat.
- Dual place-names: print the form the forum currently uses on its cause list.
- No reported citation unless the user supplied it.
- Load `templates/` before the short skill note. Opposite-side drafts are first-class.
