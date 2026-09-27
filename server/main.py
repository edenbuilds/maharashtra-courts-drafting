"""Maharashtra Courts & Tribunals Drafting — local MCP server.

Runs on the user's machine. No remote publisher endpoint.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations

DEFAULT_DRAFTS_ROOT = Path.home() / "Downloads" / "MH-Courts-Drafts"

ALLOWED_ARTIFACT_NAMES = {
    "case-facts.md",
    "format-shell.md",
    "draft-v1.md",
    "draft-v1.docx",
    "verification-report.md",
    "draft-v2.md",
    "draft-v2.docx",
    "opposing-notes.md",
    "final-draft.md",
    "final-draft.docx",
}

mcp = FastMCP("maharashtra-courts-drafting")

BUNDLE_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = BUNDLE_ROOT / "skills"
AGENTS_DIR = BUNDLE_ROOT / "agents"
FORUM_DIR = BUNDLE_ROOT / "forum-config" / "exemplars"
REFERENCES_DIR = BUNDLE_ROOT / "references"
TEMPLATES_DIR = BUNDLE_ROOT / "templates"

CASE_TYPES: list[str] = [
    "civil-wp",
    "criminal-wp",
    "pil",
    "first-appeal",
    "second-appeal",
    "criminal-appeal",
    "criminal-revision",
    "application-482",
    "bail",
    "anticipatory-bail",
    "contempt-petition",
    "matrimonial-appeal",
    "mact-claim-166",
    "mact-appeal-173",
    "consumer-district-35",
    "consumer-state-47",
    "consumer-appeal-41",
    "drt-oa",
    "drat-appeal",
    "sarfaesi-17",
    "sarfaesi-13-2-notice",
    "sarfaesi-14",
    "ni-138-complaint",
    "ni-138-reply-notice",
    "mat-oa",
    "labour-court-claim",
    "mrtu-pulp-complaint",
    "maharera-complaint",
    "family-court-petition",
    "civil-suit",
    "ibc-section-7",
    "gift-deed",
    "sale-deed-mh",
    "partition-deed",
    "mortgage-deed",
    "title-investigation",
    "wp-reply-affidavit",
    "wp-rejoinder",
    "stay-application",
    "caveat",
    "condonation-of-delay",
    "vakalatnama",
    "additional-affidavit",
    "suspension-of-sentence",
    "mat-reply",
    "mact-written-statement",
    "consumer-written-version",
    "drt-written-statement",
    "civil-written-statement",
]

CASE_TYPE_DESCRIPTIONS: dict[str, str] = {
    "civil-wp": "Civil Writ Petition, Articles 226 / 227, Bombay High Court",
    "criminal-wp": "Criminal Writ Petition, Articles 226 / 227",
    "pil": "Public Interest Litigation, Article 226 + BHC PIL Rules 2010",
    "first-appeal": "First Appeal, CPC s.96",
    "second-appeal": "Second Appeal, CPC s.100",
    "criminal-appeal": "Criminal Appeal, BNSS s.415 / CrPC s.374",
    "criminal-revision": "Criminal Revision, BNSS / CrPC ss.397, 401",
    "application-482": "Quashing / inherent powers, BNSS s.528 / CrPC s.482 (APL)",
    "bail": "Regular bail, BNSS s.483 / CrPC s.439 (BA)",
    "anticipatory-bail": "Anticipatory bail, BNSS s.482 / CrPC s.438 (ABA)",
    "contempt-petition": "Contempt of Courts Act, 1971",
    "matrimonial-appeal": "Matrimonial appeal to Bombay High Court (not MAT)",
    "mact-claim-166": "MACT claim petition, MV Act s.166",
    "mact-appeal-173": "First Appeal from MACT, MV Act s.173",
    "consumer-district-35": "District Commission complaint, CPA 2019 s.35",
    "consumer-state-47": "State Commission complaint, CPA 2019 s.47",
    "consumer-appeal-41": "Appeal District to State Commission, CPA 2019 s.41",
    "drt-oa": "DRT Original Application, RDDBFI Act",
    "drat-appeal": "Appeal to DRAT Mumbai",
    "sarfaesi-17": "Securitisation application, SARFAESI s.17",
    "sarfaesi-13-2-notice": "Bank demand notice, SARFAESI s.13(2)",
    "sarfaesi-14": "CMM / DM assistance, SARFAESI s.14",
    "ni-138-complaint": "Cheque-bounce complaint, NI Act s.138",
    "ni-138-reply-notice": "Reply to NI Act s.138 notice",
    "mat-oa": "Maharashtra Administrative Tribunal Original Application",
    "labour-court-claim": "Labour Court / Industrial Tribunal claim",
    "mrtu-pulp-complaint": "Unfair labour practice, MRTU & PULP Act 1971",
    "maharera-complaint": "MahaRERA complaint / MahaREAT appeal",
    "family-court-petition": "Family Court petition (HMA / SMA / DV / GWA)",
    "civil-suit": "Civil plaint, City Civil / District Court",
    "ibc-section-7": "IBC s.7, NCLT Mumbai Bench",
    "gift-deed": "Gift deed of immovable property, Maharashtra",
    "sale-deed-mh": "Sale / conveyance deed, Maharashtra",
    "partition-deed": "Partition deed, Maharashtra",
    "mortgage-deed": "Mortgage deed, Maharashtra",
    "title-investigation": "Title investigation report, Maharashtra",
    "wp-reply-affidavit": "Affidavit in Reply to a Bombay High Court writ petition",
    "wp-rejoinder": "Rejoinder affidavit of the writ petitioner",
    "stay-application": "Interim / stay application travelling with a writ or appeal",
    "caveat": "Caveat under CPC s.148-A",
    "condonation-of-delay": "Section 5 Limitation Act application",
    "vakalatnama": "Vakalatnama, Bar Council of Maharashtra and Goa practice",
    "additional-affidavit": "Additional / compliance / sur-rejoinder affidavit",
    "suspension-of-sentence": "Suspension of sentence and bail pending criminal appeal",
    "mat-reply": "State reply before the Maharashtra Administrative Tribunal",
    "mact-written-statement": "Written statement of insurer / owner before MACT",
    "consumer-written-version": "Written version of the opposite party before a Consumer Commission",
    "drt-written-statement": "Written statement of borrower / guarantor before DRT",
    "civil-written-statement": "Written statement under Order VIII CPC",
}

TEMPLATE_MAP: dict[str, str] = {
    "civil-wp": "high-court/civil-writ-petition.md",
    "criminal-wp": "high-court/criminal-writ-petition.md",
    "pil": "high-court/pil.md",
    "first-appeal": "high-court/first-appeal.md",
    "second-appeal": "high-court/second-appeal.md",
    "criminal-appeal": "high-court/criminal-appeal.md",
    "criminal-revision": "high-court/criminal-revision.md",
    "application-482": "high-court/application-528-bnss.md",
    "bail": "high-court/regular-bail.md",
    "anticipatory-bail": "high-court/anticipatory-bail.md",
    "contempt-petition": "high-court/contempt-petition.md",
    "matrimonial-appeal": "high-court/matrimonial-appeal.md",
    "mact-appeal-173": "high-court/mact-first-appeal.md",
    "mact-claim-166": "tribunals/mact-claim-166.md",
    "consumer-district-35": "tribunals/consumer-complaint.md",
    "consumer-state-47": "tribunals/consumer-complaint.md",
    "consumer-appeal-41": "tribunals/consumer-appeal.md",
    "drt-oa": "tribunals/drt-original-application.md",
    "sarfaesi-17": "tribunals/sarfaesi-17.md",
    "sarfaesi-13-2-notice": "tribunals/sarfaesi-13-2-notice.md",
    "ni-138-complaint": "tribunals/ni-138-complaint.md",
    "ni-138-reply-notice": "tribunals/ni-138-reply-notice.md",
    "mat-oa": "tribunals/mat-original-application.md",
    "labour-court-claim": "tribunals/labour-claim.md",
    "mrtu-pulp-complaint": "tribunals/mrtu-pulp-complaint.md",
    "maharera-complaint": "tribunals/maharera-complaint.md",
    "family-court-petition": "trial/family-court-petition.md",
    "civil-suit": "trial/civil-plaint.md",
    "gift-deed": "conveyancing/gift-deed.md",
    "sale-deed-mh": "conveyancing/sale-deed.md",
    "partition-deed": "conveyancing/partition-deed.md",
    "mortgage-deed": "conveyancing/mortgage-deed.md",
    "title-investigation": "conveyancing/title-investigation-report.md",
    "wp-reply-affidavit": "high-court/affidavit-in-reply-writ.md",
    "wp-rejoinder": "high-court/rejoinder-affidavit-writ.md",
    "stay-application": "applications/stay-application.md",
    "caveat": "applications/caveat.md",
    "condonation-of-delay": "applications/condonation-of-delay.md",
    "vakalatnama": "applications/vakalatnama.md",
    "additional-affidavit": "applications/additional-affidavit.md",
    "suspension-of-sentence": "applications/suspension-of-sentence.md",
    "mat-reply": "tribunals/mat-reply.md",
    "mact-written-statement": "tribunals/mact-written-statement.md",
    "consumer-written-version": "tribunals/consumer-written-version.md",
    "drt-written-statement": "tribunals/drt-written-statement.md",
    "civil-written-statement": "trial/written-statement.md",
}

ACRONYM_TO_CASE_TYPE: dict[str, str] = {
    "WP": "civil-wp",
    "CRWP": "criminal-wp",
    "PIL": "pil",
    "APL": "application-482",
    "ABA": "anticipatory-bail",
    "BA": "bail",
    "CRA": "criminal-appeal",
    "CRR": "criminal-revision",
    "FA": "first-appeal",
    "SA": "second-appeal",
    "CP": "contempt-petition",
    "MACA": "mact-appeal-173",
    "MACT": "mact-claim-166",
    "MAT": "mat-oa",
    "OA": "drt-oa",
    "RERA": "maharera-complaint",
    "138": "ni-138-complaint",
    "ULP": "mrtu-pulp-complaint",
}

AGENT_NAMES = ["reader", "format", "drafter", "verifier", "refiner", "overseer"]

DISTRICT_TO_HC_BENCH = {
    "mumbai": "bombay-hc-mumbai",
    "mumbai city": "bombay-hc-mumbai",
    "mumbai suburban": "bombay-hc-mumbai",
    "thane": "bombay-hc-mumbai",
    "palghar": "bombay-hc-mumbai",
    "nashik": "bombay-hc-mumbai",
    "pune": "bombay-hc-mumbai",
    "raigad": "bombay-hc-mumbai",
    "daman": "bombay-hc-mumbai",
    "diu": "bombay-hc-mumbai",
    "dadra": "bombay-hc-mumbai",
    "silvassa": "bombay-hc-mumbai",
    "kolhapur": "bombay-hc-kolhapur",
    "satara": "bombay-hc-kolhapur",
    "sangli": "bombay-hc-kolhapur",
    "solapur": "bombay-hc-kolhapur",
    "ratnagiri": "bombay-hc-kolhapur",
    "sindhudurg": "bombay-hc-kolhapur",
    "nagpur": "bombay-hc-nagpur",
    "akola": "bombay-hc-nagpur",
    "amravati": "bombay-hc-nagpur",
    "bhandara": "bombay-hc-nagpur",
    "buldhana": "bombay-hc-nagpur",
    "chandrapur": "bombay-hc-nagpur",
    "wardha": "bombay-hc-nagpur",
    "yavatmal": "bombay-hc-nagpur",
    "gondia": "bombay-hc-nagpur",
    "gadchiroli": "bombay-hc-nagpur",
    "washim": "bombay-hc-nagpur",
    "aurangabad": "bombay-hc-aurangabad",
    "chhatrapati sambhajinagar": "bombay-hc-aurangabad",
    "sambhajinagar": "bombay-hc-aurangabad",
    "ahmednagar": "bombay-hc-aurangabad",
    "ahilyanagar": "bombay-hc-aurangabad",
    "beed": "bombay-hc-aurangabad",
    "dhule": "bombay-hc-aurangabad",
    "jalna": "bombay-hc-aurangabad",
    "jalgaon": "bombay-hc-aurangabad",
    "latur": "bombay-hc-aurangabad",
    "nanded": "bombay-hc-aurangabad",
    "osmanabad": "bombay-hc-aurangabad",
    "dharashiv": "bombay-hc-aurangabad",
    "parbhani": "bombay-hc-aurangabad",
    "nandurbar": "bombay-hc-aurangabad",
    "hingoli": "bombay-hc-aurangabad",
}

DISTRICT_TO_DRT = {
    "mumbai": "drt-mumbai",
    "thane": "drt-mumbai",
    "palghar": "drt-mumbai",
    "nashik": "drt-mumbai",
    "pune": "drt-pune",
    "satara": "drt-pune",
    "sangli": "drt-pune",
    "kolhapur": "drt-pune",
    "solapur": "drt-pune",
    "raigad": "drt-pune",
    "ratnagiri": "drt-pune",
    "sindhudurg": "drt-pune",
    "nagpur": "drt-nagpur",
    "akola": "drt-nagpur",
    "amravati": "drt-nagpur",
    "bhandara": "drt-nagpur",
    "buldhana": "drt-nagpur",
    "chandrapur": "drt-nagpur",
    "wardha": "drt-nagpur",
    "yavatmal": "drt-nagpur",
    "gondia": "drt-nagpur",
    "gadchiroli": "drt-nagpur",
    "washim": "drt-nagpur",
    "aurangabad": "drt-aurangabad",
    "chhatrapati sambhajinagar": "drt-aurangabad",
    "ahmednagar": "drt-aurangabad",
    "ahilyanagar": "drt-aurangabad",
    "beed": "drt-aurangabad",
    "dhule": "drt-aurangabad",
    "jalna": "drt-aurangabad",
    "jalgaon": "drt-aurangabad",
    "latur": "drt-aurangabad",
    "nanded": "drt-aurangabad",
    "osmanabad": "drt-aurangabad",
    "dharashiv": "drt-aurangabad",
    "parbhani": "drt-aurangabad",
    "nandurbar": "drt-aurangabad",
    "hingoli": "drt-aurangabad",
}

DISTRICT_TO_MAT = {
    "mumbai": "mat-mumbai",
    "thane": "mat-mumbai",
    "palghar": "mat-mumbai",
    "raigad": "mat-mumbai",
    "ratnagiri": "mat-mumbai",
    "sindhudurg": "mat-mumbai",
    "pune": "mat-mumbai",
    "nashik": "mat-mumbai",
    "nagpur": "mat-nagpur",
    "akola": "mat-nagpur",
    "amravati": "mat-nagpur",
    "bhandara": "mat-nagpur",
    "buldhana": "mat-nagpur",
    "chandrapur": "mat-nagpur",
    "wardha": "mat-nagpur",
    "yavatmal": "mat-nagpur",
    "gondia": "mat-nagpur",
    "gadchiroli": "mat-nagpur",
    "washim": "mat-nagpur",
    "aurangabad": "mat-aurangabad",
    "chhatrapati sambhajinagar": "mat-aurangabad",
    "ahmednagar": "mat-aurangabad",
    "ahilyanagar": "mat-aurangabad",
    "beed": "mat-aurangabad",
    "dhule": "mat-aurangabad",
    "jalna": "mat-aurangabad",
    "jalgaon": "mat-aurangabad",
    "latur": "mat-aurangabad",
    "nanded": "mat-aurangabad",
    "osmanabad": "mat-aurangabad",
    "dharashiv": "mat-aurangabad",
    "parbhani": "mat-aurangabad",
    "nandurbar": "mat-aurangabad",
    "hingoli": "mat-aurangabad",
}


def _skill_dir(case_type: str) -> Path:
    return SKILLS_DIR / f"{case_type}-draft"


def _list_forums_internal() -> list[str]:
    if not FORUM_DIR.exists():
        return []
    return sorted(p.stem for p in FORUM_DIR.iterdir() if p.is_file() and p.suffix == ".md")


ORCHESTRATION = """
# Maharashtra Courts Drafting — orchestration script

Call this tool first, with no arguments. Then execute every step in order.
Do not write a standalone python-docx or JavaScript generator.

1. Classify the instrument with list_case_types(). Trust the user's acronym.
   APL is application-482. ABA is anticipatory-bail. MAT is mat-oa unless the
   user clearly means a matrimonial appeal.
2. If a district is known, call resolve_bench(district, forum_family).
3. create_case_folder(label). Ask the user to drop source papers into inputs/.
4. Reader: get_agent_instructions("reader") → read_case_folder → save_artifact
   "case-facts.md".
5. Format: get_agent_instructions("format") + get_template(case_type) +
   get_case_type_format + get_forum_config + get_pleading_base →
   save_artifact "format-shell.md". Long-form template loads before the
   short skill note.
6. Drafter: get_agent_instructions("drafter") → save_artifact "draft-v1.md".
7. Verifier: get_agent_instructions("verifier") → save_artifact
   "verification-report.md".
8. Refiner: get_agent_instructions("refiner") → save_artifact "draft-v2.md".
9. Overseer: get_agent_instructions("overseer") → save_artifact
   "opposing-notes.md" and "final-draft.md".
10. save_draft_as_docx on final-draft.md. Re-substitution is local.
11. Stop. The advocate verifies citations, limitation, fees and territoriality.

Do not skip Verifier or Overseer.
""".strip()


@mcp.tool(
    annotations=ToolAnnotations(
        title="List Available Case Types",
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=True,
        openWorldHint=False,
    )
)
def list_case_types() -> dict:
    """List instruments this connector can draft for Maharashtra forums."""
    return {
        "case_types": CASE_TYPES,
        "descriptions": CASE_TYPE_DESCRIPTIONS,
        "acronym_to_case_type": ACRONYM_TO_CASE_TYPE,
        "disambiguation_note": (
            "APL is quashing (application-482). ABA is anticipatory bail. "
            "MAT is the Maharashtra Administrative Tribunal unless the user "
            "clearly asks for a matrimonial appeal. Do not infer from FIR text."
        ),
    }


@mcp.tool(
    annotations=ToolAnnotations(
        title="Get Case Type Drafting Format",
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=True,
        openWorldHint=False,
    )
)
def get_case_type_format(case_type: str) -> str:
    """Return the long-form template + skill + user-facts checklist for one instrument.

    Load order: official template first, then short skill note, then common rules,
    then Index/Synopsis sheets for High Court filings.
    """
    if case_type not in CASE_TYPES:
        return (
            f"Unknown case_type '{case_type}'. "
            f"Available: {', '.join(CASE_TYPES)}."
        )
    parts: list[str] = []
    rel = TEMPLATE_MAP.get(case_type)
    if rel:
        tpath = TEMPLATES_DIR / rel
        if tpath.exists():
            parts.extend(
                [
                    f"# Long-form official template ({rel})",
                    tpath.read_text(encoding="utf-8"),
                ]
            )
    skill_dir = _skill_dir(case_type)
    skill_md = skill_dir / "SKILL.md"
    extra = skill_dir / "format-from-user.md"
    if skill_md.exists():
        if parts:
            parts.append("\n---\n")
        parts.append(skill_md.read_text(encoding="utf-8"))
    elif case_type not in TEMPLATE_MAP:
        return f"Skill file missing for '{case_type}'."
    elif not parts:
        parts.append(f"# Case type: {case_type}\n\nLong-form template missing.")
    if extra.exists():
        parts.extend(["\n---\n", extra.read_text(encoding="utf-8")])
    common = SKILLS_DIR / "_drafting_common" / "SKILL.md"
    if common.exists():
        parts.extend(["\n---\n", common.read_text(encoding="utf-8")])
    sheets = TEMPLATES_DIR / "high-court" / "00-index-synopsis-annexures.md"
    if case_type in {
        "civil-wp",
        "criminal-wp",
        "pil",
        "first-appeal",
        "second-appeal",
        "criminal-appeal",
        "criminal-revision",
        "application-482",
        "contempt-petition",
        "mact-appeal-173",
        "matrimonial-appeal",
        "wp-reply-affidavit",
        "wp-rejoinder",
        "stay-application",
        "suspension-of-sentence",
    } and sheets.exists():
        parts.extend(["\n---\n", sheets.read_text(encoding="utf-8")])
    return "\n".join(parts)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Get Agent Instructions",
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=True,
        openWorldHint=False,
    )
)
def get_agent_instructions(agent_name: str = "") -> str:
    """Mandatory first call with no arguments returns the orchestration script.

    Pass reader / format / drafter / verifier / refiner / overseer for one persona.
    """
    if not agent_name:
        return ORCHESTRATION
    key = agent_name.strip().lower()
    if key not in AGENT_NAMES:
        return f"Unknown agent '{agent_name}'. Use: {', '.join(AGENT_NAMES)}."
    path = AGENTS_DIR / key / f"{key}.md"
    if not path.exists():
        return f"Missing instructions for {key}."
    return path.read_text(encoding="utf-8")


@mcp.tool(
    annotations=ToolAnnotations(
        title="Get Pleading Base",
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=True,
        openWorldHint=False,
    )
)
def get_pleading_base() -> str:
    """Shared Maharashtra pleading skeleton."""
    path = SKILLS_DIR / "_pleading_base" / "SKILL.md"
    if not path.exists():
        return "Pleading base missing."
    return path.read_text(encoding="utf-8")


@mcp.tool(
    annotations=ToolAnnotations(
        title="List Forums",
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=True,
        openWorldHint=False,
    )
)
def list_forums() -> dict:
    """List Bombay benches and Maharashtra tribunal forum-configs."""
    return {
        "forums": _list_forums_internal(),
        "note": "Call get_forum_config(forum_id) for headers and house style.",
    }


@mcp.tool(
    annotations=ToolAnnotations(
        title="Get Forum Config",
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=True,
        openWorldHint=False,
    )
)
def get_forum_config(forum_id: str) -> str:
    """Return the forum-config exemplar (header, separator, annexure, paper)."""
    path = FORUM_DIR / f"{forum_id}.md"
    if not path.exists():
        available = ", ".join(_list_forums_internal())
        return f"Unknown forum_id '{forum_id}'. Available: {available}."
    return path.read_text(encoding="utf-8")


@mcp.tool(
    annotations=ToolAnnotations(
        title="Resolve Bench from District",
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=True,
        openWorldHint=False,
    )
)
def resolve_bench(district: str, forum_family: str = "high-court") -> dict:
    """Map a Maharashtra district to the correct Bombay bench, MAT bench or DRT.

    forum_family: high-court | mat | drt | mact | consumer
    Kolhapur-circuit districts: confirm the circuit is sitting that week; otherwise
    file at the Principal Seat.
    """
    key = district.strip().lower()
    family = forum_family.strip().lower()
    note = ""
    if family in {"high-court", "hc", "bombay"}:
        forum = DISTRICT_TO_HC_BENCH.get(key)
        if forum == "bombay-hc-kolhapur":
            note = (
                "Kolhapur circuit notified August 2025. Confirm the sitting "
                "notification. If the circuit is not sitting, use bombay-hc-mumbai."
            )
    elif family == "mat":
        forum = DISTRICT_TO_MAT.get(key)
    elif family == "drt":
        forum = DISTRICT_TO_DRT.get(key)
        note = "Debts of Rs.100 crore and above may still go to DRT-1 Mumbai. Confirm the live S.O."
    elif family == "mact":
        forum = "mact-mh"
        hc = DISTRICT_TO_HC_BENCH.get(key)
        return {
            "district": district,
            "forum_id": forum,
            "appeal_forum_id": hc,
            "note": "s.173 appeal follows the High Court bench of the MACT district.",
        }
    elif family == "consumer":
        forum = "consumer-district-mh"
        return {
            "district": district,
            "forum_id": forum,
            "state_forum_id": "consumer-state-mh",
            "note": "Pecuniary cap decides District vs State vs NCDRC.",
        }
    else:
        return {"error": f"Unknown forum_family '{forum_family}'."}

    if not forum:
        return {
            "error": f"District '{district}' is not in the Maharashtra map.",
            "hint": "Use the official district name (Thane, Nagpur, Ahilyanagar, Dharashiv, …).",
        }
    return {"district": district, "forum_id": forum, "note": note}


@mcp.tool(
    annotations=ToolAnnotations(
        title="Create Case Folder",
        readOnlyHint=False,
        destructiveHint=False,
        idempotentHint=False,
        openWorldHint=False,
    )
)
def create_case_folder(label: str, root: str = "") -> dict:
    """Create inputs/ and artifacts/ under Downloads/MH-Courts-Drafts (or root)."""
    base = Path(root).expanduser() if root else DEFAULT_DRAFTS_ROOT
    safe = "".join(ch if ch.isalnum() or ch in "-_ " else "-" for ch in label).strip()
    folder = base / safe
    (folder / "inputs").mkdir(parents=True, exist_ok=True)
    (folder / "artifacts").mkdir(parents=True, exist_ok=True)
    return {
        "case_folder": str(folder),
        "inputs": str(folder / "inputs"),
        "artifacts": str(folder / "artifacts"),
    }


@mcp.tool(
    annotations=ToolAnnotations(
        title="Save Artifact",
        readOnlyHint=False,
        destructiveHint=False,
        idempotentHint=True,
        openWorldHint=False,
    )
)
def save_artifact(case_folder: str, filename: str, content: str) -> dict:
    """Save an allow-listed pipeline artifact into the case folder."""
    name = Path(filename).name
    if name not in ALLOWED_ARTIFACT_NAMES and not name.endswith(".txt") and not name.endswith(".md"):
        return {"error": f"'{name}' is not an allow-listed artifact."}
    dest_dir = Path(case_folder) / "artifacts"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / name
    dest.write_text(content, encoding="utf-8")
    return {"saved": str(dest), "bytes": dest.stat().st_size}


@mcp.tool(
    annotations=ToolAnnotations(
        title="Read Case Folder",
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=True,
        openWorldHint=False,
    )
)
def read_case_folder(case_folder: str) -> dict:
    """Read md / txt / pdf / docx under inputs/ and artifacts/."""
    root = Path(case_folder)
    collected: dict[str, str] = {}
    for sub in ("inputs", "artifacts"):
        folder = root / sub
        if not folder.exists():
            continue
        for path in sorted(folder.rglob("*")):
            if not path.is_file():
                continue
            rel = str(path.relative_to(root))
            suffix = path.suffix.lower()
            try:
                if suffix in {".md", ".txt", ".yaml", ".yml", ".json"}:
                    collected[rel] = path.read_text(encoding="utf-8", errors="replace")
                elif suffix == ".pdf":
                    proc = subprocess.run(
                        ["pdftotext", "-layout", str(path), "-"],
                        capture_output=True,
                        text=True,
                        check=False,
                    )
                    collected[rel] = proc.stdout or proc.stderr or "[pdf unreadable]"
                elif suffix == ".docx":
                    proc = subprocess.run(
                        ["pandoc", str(path), "-t", "plain"],
                        capture_output=True,
                        text=True,
                        check=False,
                    )
                    collected[rel] = proc.stdout or proc.stderr or "[docx unreadable]"
                else:
                    collected[rel] = f"[skipped {suffix}]"
            except Exception as exc:  # noqa: BLE001
                collected[rel] = f"[error reading file: {exc}]"
    return {"files": collected, "count": len(collected)}


@mcp.tool(
    annotations=ToolAnnotations(
        title="Save Draft as DOCX",
        readOnlyHint=False,
        destructiveHint=False,
        idempotentHint=True,
        openWorldHint=False,
    )
)
def save_draft_as_docx(case_folder: str, markdown_filename: str = "final-draft.md", output_filename: str = "final-draft.docx") -> dict:
    """Render a markdown draft to a filing-grade docx via pandoc."""
    src = Path(case_folder) / "artifacts" / Path(markdown_filename).name
    dest = Path(case_folder) / "artifacts" / Path(output_filename).name
    if not src.exists():
        return {"error": f"Missing {src}"}
    dest.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["pandoc", str(src), "-o", str(dest), "-f", "markdown", "-t", "docx"]
    ref = SKILLS_DIR / "_pleading_base" / "reference.docx"
    if ref.exists():
        cmd.append(f"--reference-doc={ref}")
    proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if proc.returncode != 0 and not dest.exists():
        proc = subprocess.run(
            ["pandoc", str(src), "-o", str(dest), "-f", "markdown", "-t", "docx"],
            capture_output=True,
            text=True,
            check=False,
        )
    if not dest.exists():
        return {"error": proc.stderr or "pandoc failed", "hint": "Install pandoc."}
    return {"saved": str(dest), "bytes": dest.stat().st_size}


@mcp.tool(
    annotations=ToolAnnotations(
        title="List Long-form Templates",
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=True,
        openWorldHint=False,
    )
)
def list_templates() -> dict:
    """List every official long-form template packed with this connector."""
    files = sorted(
        str(p.relative_to(TEMPLATES_DIR))
        for p in TEMPLATES_DIR.rglob("*.md")
        if p.name != "README.md"
    )
    return {"templates": files, "case_type_to_template": TEMPLATE_MAP}


@mcp.tool(
    annotations=ToolAnnotations(
        title="Get Long-form Template",
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=True,
        openWorldHint=False,
    )
)
def get_template(name: str) -> str:
    """Return a long-form template by case_type key or by relative path.

    Examples: civil-wp, wp-reply-affidavit, high-court/civil-writ-petition.md
    """
    if name in TEMPLATE_MAP:
        path = TEMPLATES_DIR / TEMPLATE_MAP[name]
    else:
        rel = Path(name)
        if rel.is_absolute() or ".." in rel.parts:
            return "Invalid template path."
        path = TEMPLATES_DIR / rel
    if not path.exists() or not path.is_file():
        available = ", ".join(sorted(TEMPLATE_MAP))
        return f"Unknown template '{name}'. Case-type keys: {available}."
    return path.read_text(encoding="utf-8")


@mcp.tool(
    annotations=ToolAnnotations(
        title="Get Reference Note",
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=True,
        openWorldHint=False,
    )
)
def get_reference_note(name: str) -> str:
    """Load a packed reference: territorial-jurisdiction, acronyms, court-fees-stamp, efiling."""
    safe = Path(name).name
    if not safe.endswith(".md"):
        safe = f"{safe}.md"
    path = REFERENCES_DIR / safe
    if not path.exists():
        available = ", ".join(p.stem for p in REFERENCES_DIR.glob("*.md"))
        return f"Unknown reference '{name}'. Available: {available}."
    return path.read_text(encoding="utf-8")


if __name__ == "__main__":
    mcp.run()
