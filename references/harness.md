# Harness (in-plugin summary)

Full human doc: `docs/HARNESS.md`. Install: `docs/INSTALL.md` / `START_HERE.md`.

## Start every drafting chat with

`get_agent_instructions()` — no arguments. That is the orchestration runbook.

## Pipeline

Reader (`case-facts.md`) → Format (`format-shell.md`) → Drafter (`draft-v1.md`) → Verifier (`verification-report.md`) → Refiner (`draft-v2.md`) → Overseer (`opposing-notes.md`, `final-draft.md`) → `save_draft_as_docx`.

Do not skip Verifier or Overseer. Do not invent a standalone docx generator.

## Format load order

1. `get_template(case_type)` — long-form official form  
2. `get_case_type_format(case_type)` — short skill + checklist (template already first inside it)  
3. `get_forum_config(forum_id)`  
4. `get_pleading_base()`

## Narrate lightly

One short line per stage to the user. Do not paste this whole script unless asked.

## Acronyms

APL = `application-482`. ABA = `anticipatory-bail`. BA = `bail`. MAT = `mat-oa` unless clearly matrimonial / HMA.
