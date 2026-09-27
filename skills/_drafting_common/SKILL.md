---
name: drafting-common
description: Shared drafting rules for the Maharashtra courts pack — privacy firewall, anti-hallucination, accompaniment applications, language.
---

# Common drafting rules

## Privacy firewall (Reader, first)

Replace before any other agent writes:

| Class | Placeholder |
|---|---|
| Parties | `[Petitioner-A]`, `[Respondent-B]`, `[Claimant-A]`, `[Accused-A]` |
| Addresses | `[Address-Placeholder]` |
| Aadhaar / PAN / GSTIN / TAN / DIN | `[Aadhaar-Placeholder]` etc. |
| Case / FIR / OA / WP numbers | `[Case-No-Placeholder]` |
| Phone / email | `[Contact-Placeholder]` |
| Sums in dispute | `[Amount-Placeholder]` |

Keep a local token map. Never write the token map into a file that leaves the case folder.

## Anti-hallucination (Verifier)

Flag and refuse to ship:

- a date not in `case-facts.md`
- a section number not in `case-facts.md` or the case-type skill
- an annexure letter with no source document
- a reported citation the user did not supply
- a limitation period computed without identifying the Article / special statute
- a court-fee or pre-deposit figure computed from memory

## Language

English default. Switch to Marathi only when the forum-config says the district forum sits in Marathi and the user asked for Marathi. Do not mix registers inside one pleading.

## Accompanying applications

If the skill lists an accompanying application, draft it as a separate short petition with its own cause title, prayer and affidavit — not as a paragraph inside the main pleading. Prefer the matching long-form under `templates/applications/` (stay, caveat, condonation, vakalatnama, additional affidavit, suspension of sentence).

## Template-first load order

1. `get_template(<case_type>)` or the path under `templates/`
2. Short skill note under `skills/<case_type>-draft/` (if present)
3. Forum-config exemplar

Opposite-side drafts are first-class instruments. Do not invent a short form when a long-form template exists.
