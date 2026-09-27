# Getting started (in-plugin)

**Install:** see `docs/INSTALL.md` and repo-root `START_HERE.md`.  
**Harness:** see `docs/HARNESS.md`.  
**Prompts:** see `USAGE.md`.

## After the host is connected

1. Call `get_agent_instructions()` with **no arguments** — that is the orchestration harness.
2. Call `list_case_types()` if the instrument is unclear.
3. If a district is known: `resolve_bench(district, "high-court"|"mat"|"drt"|"mact"|"consumer")`.
4. `create_case_folder(label)` → ask the user to drop papers into `inputs/`.
5. Run Reader → Format → Drafter → Verifier → Refiner → Overseer.
6. `save_draft_as_docx` on `final-draft.md`.

## Template before skill

`get_template(case_type)` / long-form under `templates/` loads **before** the short skill note.  
Opposite-side keys: `wp-reply-affidavit`, `wp-rejoinder`, `mat-reply`, `mact-written-statement`, `consumer-written-version`, `drt-written-statement`, `civil-written-statement`.

## Acronyms

- APL → `application-482` (not anticipatory bail)
- ABA → `anticipatory-bail`
- BA → `bail`
- MAT → `mat-oa` (Administrative Tribunal), not matrimonial, unless the user clearly says HMA / Family Court

## Default case folder

`~/Downloads/MH-Courts-Drafts/<label>/{inputs,artifacts}/`
