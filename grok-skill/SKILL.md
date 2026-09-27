---
name: maharashtra-courts-drafting
description: Draft official Maharashtra pleadings for the Bombay High Court (Mumbai, Nagpur, Aurangabad, Kolhapur circuit) and State tribunals including MAT, MACT, Consumer Commissions, DRT DRAT, NCLT Mumbai, Labour and Industrial Courts, MahaRERA and Family Courts. Use when the user asks for a writ, APL, ABA, bail, appeal, MACT claim, consumer complaint, DRT OA, SARFAESI, NI 138, MAT OA, ULP, RERA or a Maharashtra deed.
---

# Maharashtra Courts Drafting

Draft in the forum's own register. This skill is Maharashtra-only.

## Load first

Read as needed from this skill's `references/`:

- `territorial-jurisdiction.md` — district → Bombay bench / MAT / DRT
- `acronyms.md` — APL is not ABA; MAT is the Administrative Tribunal
- `court-fees-stamp.md`
- `efiling.md`

Plugin root is the directory that contains this `grok-skill/` folder (sibling of `templates/`, `skills/`, `server/`).

When drafting a named instrument, load in this order:
1. `templates/` long-form official form (writ, reply affidavit, rejoinder, stay, MACT, consumer, DRT, deeds)
2. matching `skills/<case-type>-draft/SKILL.md` if it exists
3. `forum-config/exemplars/` for the bench or tribunal

Opposite-side drafts are first-class. A writ reply is `templates/high-court/affidavit-in-reply-writ.md`. A rejoinder is `templates/high-court/rejoinder-affidavit-writ.md`. Do not invent a short form when a long-form template exists.

## Pipeline

Reader (privacy firewall + fact ledger) → Format (forum header + skeleton) → Drafter → Verifier (no invented citations) → Refiner (strip model-voice) → Overseer (opposing-counsel notes) → filing-grade markdown / docx.

## House style — Bombay High Court

- `IN THE HIGH COURT OF JUDICATURE AT BOMBAY.` at the Principal Seat.
- `IN THE HIGH COURT OF JUDICATURE AT BOMBAY BENCH AT NAGPUR.` (or AURANGABAD / KOLHAPUR) at a bench.
- Appeals prefer `///VERSUS///`.
- Annexures `ANNEXURE-A`. A4, Times New Roman 14, 1.5, left margin ~4 cm.
- Court fees cite the Bombay Court-Fees Act, 1959. Deeds cite the Maharashtra Stamp Act, 1958.

## Routing

- State service matters → Maharashtra Administrative Tribunal, not a writ in the first instance.
- Unfair labour practice / union recognition → Industrial Court under MRTU and PULP Act, 1971.
- IBC first instance → NCLT Mumbai, not the High Court.
- s.173 MV appeal follows the High Court bench of the MACT district.
- Kolhapur circuit districts — confirm the circuit is sitting; otherwise Principal Seat.

## Never

- Invent a reported citation, fee, or limitation article.
- Treat APL as anticipatory bail.
- File a Maharashtra district matter at the Goa Bench.
- Restore real identifiers until the final local render.
- Advertise legal services or guarantee Registry acceptance.

Every draft is a starting point for a practising advocate.
