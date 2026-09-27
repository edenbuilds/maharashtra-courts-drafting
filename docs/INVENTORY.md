# Inventory

## Long-form templates (46)

High Court: civil writ, criminal writ, PIL, first appeal, second appeal, criminal appeal, criminal revision, s.528/482 APL, ABA, regular bail, contempt, matrimonial appeal, MACT first appeal, **affidavit in reply to writ**, **rejoinder**, index-synopsis-annexures.

Applications: stay, caveat, condonation, vakalatnama, additional affidavit, suspension of sentence.

Tribunals: MAT OA + MAT reply, MACT claim + MACT WS, consumer complaint + written version + appeal, DRT OA + DRT WS, SARFAESI s.17 + s.13(2), NI 138 complaint + reply notice, labour claim, MRTU & PULP, MahaRERA.

Trial: Family Court petition, civil plaint, CPC written statement.

Conveyancing: sale, gift, partition, mortgage, title report.

## Forum-configs (20)

bombay-hc-mumbai · nagpur · aurangabad · kolhapur · mat x3 · consumer x2 · mact · drt x4 · drat · nclt · labour · maharera · family · city-civil

## Skills

Every `CASE_TYPES` key has `skills/<case-type>-draft/` (SKILL.md + format-from-user.md), including opposite-side and accompaniment instruments:

`wp-reply-affidavit` · `wp-rejoinder` · `stay-application` · `caveat` · `condonation-of-delay` · `vakalatnama` · `additional-affidavit` · `suspension-of-sentence` · `mat-reply` · `mact-written-statement` · `consumer-written-version` · `drt-written-statement` · `civil-written-statement`

## Agents (6)

reader · format · drafter · verifier · refiner · overseer

## MCP tools (14)

list_case_types · get_case_type_format · get_agent_instructions · get_pleading_base · list_forums · get_forum_config · resolve_bench · create_case_folder · save_artifact · read_case_folder · save_draft_as_docx · get_reference_note · list_templates · get_template

`get_case_type_format` loads the long-form template **before** the short skill note.

`get_reference_note("getting-started")` and `get_reference_note("harness")` return install + orchestration docs (also on disk as `START_HERE.md`, `docs/INSTALL.md`, `docs/HARNESS.md`).

