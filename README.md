# Maharashtra Courts & Tribunals Drafting

Local-first drafting pack for pleadings that actually get filed in **Maharashtra**.

Covers the High Court of Judicature at Bombay (Principal Seat at Mumbai and Benches at Nagpur, Aurangabad / Chhatrapati Sambhajinagar, and the Kolhapur circuit) plus the working tribunals and trial forums in the State.

No marketplace branding. No remote publisher. All processing stays on the machine that runs the connector.

---

## Long-form templates

Every instrument has a fill-in official form under `templates/` — including Affidavit in Reply and Rejoinder to a writ, stay, caveat, condonation, vakalatnama, and opposite-side drafts at MAT, MACT, Consumer, DRT and the trial court.

Call `list_templates()` or `get_template("civil-wp")` / `get_template("wp-reply-affidavit")`.

## What this pack drafts

### High Court of Judicature at Bombay

| Case type | Statutory anchor | Usual side |
|---|---|---|
| Civil Writ Petition | Articles 226 / 227 | Appellate / Original (OS only at Principal Seat) |
| Criminal Writ Petition | Articles 226 / 227 + Article 21 | Appellate |
| Public Interest Litigation | Article 226 + BHC PIL Rules, 2010 | Appellate |
| First Appeal | CPC s.96 / Order XLI | Appellate |
| Second Appeal | CPC s.100 | Appellate |
| Criminal Appeal | BNSS s.415 / CrPC s.374 | Appellate |
| Criminal Revision | BNSS s.438 / 442 · CrPC ss.397, 401 | Appellate |
| Application under s.528 BNSS / s.482 CrPC | Inherent jurisdiction (quashing) | Appellate |
| Anticipatory Bail | BNSS s.482 / CrPC s.438 | Appellate |
| Regular Bail | BNSS s.483 / CrPC s.439 | Appellate |
| Contempt Petition | Contempt of Courts Act, 1971 | Appellate / Original |
| MACT First Appeal | MV Act s.173 | Appellate |
| Matrimonial Appeal | HMA / SMA / Divorce Act | Appellate |
| Commercial Appeal / OS Suit skeleton | Commercial Courts Act + BHC OS Rules | Original Side (Mumbai) |

### Maharashtra tribunals and trial forums

| Forum | Seat(s) in the State | Typical instruments |
|---|---|---|
| Maharashtra Administrative Tribunal | Mumbai (P), Nagpur, Aurangabad | Original Application, MA, Review, Contempt |
| District / State Consumer Commission | Every district + SCDRC Mumbai / Nagpur / Chh. Sambhajinagar | CPA 2019 ss.35, 47, 41, 51, 67, 71 |
| MACT | District headquarters | MV Act ss.166, 164, 161, 174; execution |
| DRT-1 / 2 / 3 Mumbai, DRT Pune, DRT Nagpur, DRT Aurangabad | As notified | RDDBFI OA; SARFAESI s.17 |
| DRAT Mumbai | Mumbai | Appeal under RDDBFI / SARFAESI |
| NCLT Mumbai Bench | Mumbai | IBC ss.7, 9, 10, 95 |
| Labour Court / Industrial Tribunal / Industrial Court | Statewide | ID Act; MRTU & PULP Act, 1971 |
| MahaRERA / MahaREAT | Mumbai + regional | RERA complaint / appeal |
| Family Court | Notified districts | HMA / SMA / DV / guardianship |
| City Civil Court, Mumbai | Mumbai | Civil suits, commercial (below HC OS) |
| Small Causes Court | Mumbai, Pune | Rent, Presidency Small Cause |
| Cooperative Court | Divisional | MCS Act disputes |
| Employees' Compensation Commissioner | District | EC Act, 1923 |
| Controlling Authority (Gratuity) / EPFO / ESIC | District / regional | Payment of Gratuity; EPF; ESI s.75 |
| Charity Commissioner | Mumbai + regions | BPT Act, 1950 |
| Competent Authority / SRA / revenue | District | MLRC 1966; slum; land acquisition |

---

## Bombay High Court territorial map (use before choosing the bench)

Official Appellate Side sitting map (confirm on [bombayhighcourt.nic.in](https://bombayhighcourt.nic.in) before filing; Kolhapur circuit notified August 2025):

**Principal Seat, Mumbai**  
Mumbai City · Mumbai Suburban · Thane · Palghar · Nashik · Pune · Raigad · Dadra & Nagar Haveli · Daman · Diu  
*(Kolhapur circuit, when sitting, takes Satara, Sangli, Solapur, Kolhapur, Ratnagiri, Sindhudurg — confirm current sitting notification.)*

**Nagpur Bench**  
Nagpur · Akola · Amravati · Bhandara · Buldhana · Chandrapur · Wardha · Yavatmal · Gondia · Gadchiroli · Washim

**Aurangabad Bench**  
Chhatrapati Sambhajinagar · Ahilyanagar · Beed · Dhule · Jalna · Jalgaon · Latur · Nanded · Dharashiv · Parbhani · Nandurbar · Hingoli

**High Court of Bombay at Goa**  
North Goa · South Goa — *out of State; included only because it is the same High Court. Do not use for Maharashtra district matters.*

Original Side jurisdiction lives at the **Principal Seat only**.

---

## Six-stage pipeline (mandatory)

1. **Reader** — ingest the case folder, build a fact ledger, apply the privacy firewall, halt if a required statute or order is missing.
2. **Format** — load the case-type skill + the forum-config for the chosen Bombay bench or tribunal.
3. **Drafter** — write Cause Title through List of Annexures in the forum's register.
4. **Verifier** — anti-hallucination pass against the fact ledger.
5. **Refiner** — apply verifier flags; strip model-voice; enforce paper, font, margin, annexure prefix.
6. **Overseer** — opposing-counsel read; emit `final-draft.docx` after local re-substitution.

Artifacts written, in order: `case-facts.md` → `format-shell.md` → `draft-v1.md` → `verification-report.md` → `draft-v2.md` → `opposing-notes.md` → `final-draft.docx`.

---

## Install

### Claude Desktop (MCPB)

1. Settings → Extensions → Install Extension
2. Select `maharashtra-courts-drafting.mcpb`
3. Enable. New chat.

### Claude Code plugin

```text
/plugin install ./maharashtra-courts-drafting
```

### From source

Python ≥ 3.10, `pandoc` (docx render), `pdftotext` from poppler (PDF ingest).

```bash
uv --directory /path/to/maharashtra-courts-drafting run server/main.py
```

---

## Tools

| Tool | Purpose |
|---|---|
| `list_case_types` | All supported instruments + acronym map |
| `get_case_type_format` | Long-form template first, then short skill + checklist |
| `get_template` | Long-form official form by case type or path |
| `list_templates` | Every packed fill-in pleading |
| `get_agent_instructions` | Call first, with no arguments, for the orchestration script |
| `list_forums` | Bombay benches + Maharashtra tribunals |
| `get_forum_config` | Header, parties separator, annexure prefix, paper, fees note |
| `get_pleading_base` | Shared skeleton |
| `resolve_bench` | District → correct Bombay bench / MAT bench / DRT |
| `create_case_folder` | `inputs/` + `artifacts/` on disk |
| `save_artifact` | Allow-listed pipeline files only |
| `read_case_folder` | md / txt / pdf / docx |
| `save_draft_as_docx` | Pandoc render, local re-substitution |
| `get_reference_note` | Territorial, acronym, fee or e-filing note |

---

## House style (Bombay HC Appellate Side)

- Court header ends with a full stop: `IN THE HIGH COURT OF JUDICATURE AT BOMBAY.`
- Bench qualifier when not at the Principal Seat: `IN THE HIGH COURT OF JUDICATURE AT BOMBAY BENCH AT NAGPUR.`
- Parties separator preferred on appeals: `///VERSUS///`
- Spaced section heads on many Appellate Side filings: `F A C T S` · `G R O U N D S` · `P R A Y E R`
- Annexures: `ANNEXURE-A` (no skipped letters unless the brief says otherwise)
- Paper A4, Times New Roman 14, 1.5 spacing, left margin ≈ 4 cm
- Court fees: Bombay Court-Fees Act, 1959 (as applicable to Maharashtra)
- Stamp (conveyancing): Maharashtra Stamp Act, 1958
- Language: English default at Mumbai / Pune / HC; Marathi permitted in interior district forums under the State amendment to CPC s.137 — follow the forum-config

---

## Verification duty

AI drafts hallucinate section numbers, dates and annexure letters. The Verifier stage is not a substitute for the filing advocate. Read `DISCLAIMER.md` and `PRIVACY.md` before production use.
