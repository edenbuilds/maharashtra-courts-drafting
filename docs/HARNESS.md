# Harness — orchestration, agents, artifacts

This document is for **humans** (how the pipeline works) and for the **model** (how to run it).  
The live runbook is also returned by the MCP tool:

```text
get_agent_instructions()          → full orchestration script
get_agent_instructions("reader")  → one stage persona
… format | drafter | verifier | refiner | overseer
```

---

## Why a harness at all?

A single free-form “write a writ” prompt invents citations, skips stay applications, and mixes Bombay and Delhi house style.

The harness forces a fixed loop:

1. Classify the instrument and forum.  
2. Work from a **long-form official template**.  
3. Write through six named stages.  
4. Leave a trail of artifacts the advocate can audit.

Nothing in this loop uploads papers. Case folders stay on the user’s disk.

---

## Big picture

```
┌─────────────────────────────────────────────────────────────┐
│  USER                                                       │
│  “Draft WP reply for Resp. No. 2 — TMC demolition…”         │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  ORCHESTRATION  =  get_agent_instructions()                 │
│  Classify → resolve bench → case folder → 6 agents → docx   │
└───────────────────────────┬─────────────────────────────────┘
                            │
     ┌──────────────────────┼──────────────────────┐
     ▼                      ▼                      ▼
 templates/            forum-config/            skills/
 (fill-in form)        (seat / tribunal)        (short note)
     │                      │                      │
     └──────────────────────┼──────────────────────┘
                            ▼
              ~/Downloads/MH-Courts-Drafts/<label>/
                 inputs/     artifacts/
```

---

## Stage-by-stage

| # | Agent | Tool load | Writes | Job in one line |
|---|---|---|---|---|
| 0 | **Orchestrator** | `get_agent_instructions()` | — | Runbook. Call this first, every chat. |
| 1 | **Reader** | `read_case_folder` | `case-facts.md` | Privacy firewall + fact ledger. No pleading yet. |
| 2 | **Format** | `get_template` → `get_case_type_format` → `get_forum_config` → `get_pleading_base` | `format-shell.md` | Empty pleading in the forum’s register; facts still slots. |
| 3 | **Drafter** | (uses shell + facts) | `draft-v1.md` | Pour facts into the template order: title → facts → grounds → prayer → verification. |
| 4 | **Verifier** | (reads facts + draft) | `verification-report.md` | Flag invented dates, sections, annexures, citations, fees. |
| 5 | **Refiner** | (applies flags) | `draft-v2.md` | Fix flags; strip model-voice; enforce paper / annexure scheme. |
| 6 | **Overseer** | (opposing-counsel read) | `opposing-notes.md`, `final-draft.md` | Weak points a respondent would attack. |
| 7 | **Render** | `save_draft_as_docx` | `final-draft.docx` | Local pandoc. Re-substitution of real IDs stays local. |

**Do not skip Verifier or Overseer.**

---

## Load order inside Format (important)

1. **Long-form template** — `get_template("civil-wp")` or `get_template("wp-reply-affidavit")`  
2. **Short skill note** — `skills/<case-type>-draft/SKILL.md` (also bundled inside `get_case_type_format`)  
3. **Forum-config** — e.g. `bombay-hc-mumbai`  
4. **Pleading base** — shared skeleton  

Opposite-side instruments use their **own** templates. Never recycle a petitioner form for a reply.

---

## Case folder layout

Created by `create_case_folder("TMC-WP-reply-2026")`:

```text
MH-Courts-Drafts/TMC-WP-reply-2026/
├── inputs/                  ← user drops source papers here
│   ├── demolition-notice.pdf
│   └── hearing-order.pdf
└── artifacts/
    ├── case-facts.md
    ├── format-shell.md
    ├── draft-v1.md
    ├── verification-report.md
    ├── draft-v2.md
    ├── opposing-notes.md
    ├── final-draft.md
    └── final-draft.docx
```

`save_artifact` only accepts the allow-listed pipeline names (plus plain `.md` / `.txt`).

---

## Tool map (what the model should call)

| When | Call |
|---|---|
| Start of every drafting chat | `get_agent_instructions()` |
| “What can you draft?” | `list_case_types()` |
| Need the fill-in form | `get_template("wp-reply-affidavit")` or `list_templates()` |
| District → bench | `resolve_bench("Thane", "high-court")` |
| Seat house style | `get_forum_config("bombay-hc-mumbai")` |
| Skill + template + checklist | `get_case_type_format("civil-wp")` |
| New matter on disk | `create_case_folder("label")` |
| Read papers / prior artifacts | `read_case_folder(path)` |
| Save a stage output | `save_artifact(folder, "draft-v1.md", content)` |
| Word file | `save_draft_as_docx(folder)` |
| Fees / territory / acronyms / how-to | `get_reference_note("getting-started")` etc. |

---

## Acronym traps (orchestration must respect these)

| User says | Case type | Not |
|---|---|---|
| APL | `application-482` (BNSS s.528 / CrPC s.482) | anticipatory bail |
| ABA | `anticipatory-bail` | regular bail |
| BA | `bail` | anticipatory bail |
| MAT | `mat-oa` | matrimonial appeal (unless user clearly says HMA / Family Court) |
| WP | `civil-wp` | — |
| reply / counter | `wp-reply-affidavit` | a second writ |

---

## Narration to the user (keep it light)

While running the harness, tell the user which stage you are on in one short line, e.g.:

- “Reader — building the fact ledger from your inputs.”  
- “Format — loading the Affidavit in Reply template for the Principal Seat.”  
- “Verifier — checking dates and annexures against case-facts.”  

Do **not** dump the whole orchestration script into the chat unless they ask how the harness works.

---

## What the harness will not do

- Invent a reported citation, court-fee figure, or limitation article.  
- Guarantee Registry acceptance.  
- Replace the filing advocate’s verification duty ([`../DISCLAIMER.md`](../DISCLAIMER.md)).  
- Send case papers to any remote publisher.

---

## Quick self-check for the model

Before saying “done”:

- [ ] `get_agent_instructions()` was called at the start  
- [ ] Correct case-type key (reply ≠ writ)  
- [ ] Forum matched via `resolve_bench` when a district was given  
- [ ] Template loaded before the short skill  
- [ ] All six agents produced artifacts  
- [ ] `final-draft.docx` rendered (or user declined docx)  
- [ ] User reminded to verify citations, limitation, fees, territoriality  
