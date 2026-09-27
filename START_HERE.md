# Start here

**Maharashtra Courts & Tribunals Drafting** is a **local** MCP / Claude plugin.  
It drafts Bombay High Court and Maharashtra tribunal pleadings on your machine. Nothing is sent to a publisher.

---

## Install (pick one)

### A. Claude Code — from GitHub (usual path)

```bash
git clone https://github.com/edenbuilds/maharashtra-courts-drafting.git
cd maharashtra-courts-drafting
```

Then in Claude Code:

```text
/plugin install .
```

Or, if your build supports a GitHub plugin URL:

```text
/plugin install github:edenbuilds/maharashtra-courts-drafting
```

The repo is **public** — no invite needed.

### B. Claude Desktop — MCP extension

1. Install [uv](https://github.com/astral-sh/uv) and [pandoc](https://pandoc.org).
2. Clone the repo (same as above).
3. Open **Claude Desktop → Settings → Developer → Edit Config** and add:

```json
{
  "mcpServers": {
    "maharashtra-courts-drafting": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABS/PATH/TO/maharashtra-courts-drafting",
        "run",
        "server/main.py"
      ]
    }
  }
}
```

4. Restart Claude Desktop. Confirm the server shows tools like `get_agent_instructions`.

### C. Cursor / any MCP host

Same `uv … run server/main.py` block as Claude Desktop, under that host’s MCP settings.  
Point `--directory` at your clone.

**Prerequisites for all paths:** Python ≥ 3.10, `uv`, `pandoc` (for `.docx`), `pdftotext` from poppler (for PDF inputs).

Full detail → [`docs/INSTALL.md`](docs/INSTALL.md)

---

## First chat after install

Paste something like:

> Draft a civil writ against Thane Municipal Corporation. Impugned demolition notice dated 3 January 2026 for a shop at [address]. Prayer for certiorari and stay. Bench follows the district.

The model **must** call `get_agent_instructions()` first (no arguments). That returns the **orchestration harness** — the six-stage pipeline. Do not ask it to “just write a Word file.”

More prompts → [`USAGE.md`](USAGE.md)  
How the harness works → [`docs/HARNESS.md`](docs/HARNESS.md)

---

## What you get

| Piece | Role |
|---|---|
| **MCP server** (`server/main.py`) | Tools the model calls — templates, forums, case folder, docx |
| **Orchestration** (`get_agent_instructions()`) | The mandatory runbook: Reader → … → Overseer |
| **Agents** (`agents/`) | Six persona scripts for each pipeline stage |
| **Templates** (`templates/`) | Fill-in official forms (writ, reply, rejoinder, stay, tribunals…) |
| **Skills** (`skills/`) | Short per-instrument notes + fact checklists |
| **Forum-configs** (`forum-config/`) | Bombay seats + Maharashtra tribunals (headers, paper, annexure scheme) |

Opposite-side drafts are first-class: `wp-reply-affidavit`, `wp-rejoinder`, written statements, etc.

---

## Mental model (the harness)

```
You describe the matter
        ↓
get_agent_instructions()     ← start here, every time
        ↓
create_case_folder → drop papers into inputs/
        ↓
Reader → Format → Drafter → Verifier → Refiner → Overseer
        ↓
final-draft.md  +  final-draft.docx   (advocate still verifies)
```

Artifacts land under `~/Downloads/MH-Courts-Drafts/<label>/artifacts/`.

---

## Hard rules (do not skip)

- **APL** = quashing (`application-482`), not anticipatory bail.  
- **ABA** = anticipatory bail. **BA** = regular bail.  
- **MAT** = Maharashtra Administrative Tribunal (not matrimonial) unless you clearly say HMA / Family Court.  
- No invented citations, fees, or limitation articles.  
- Load the long-form **template before** the short skill note.

Read [`DISCLAIMER.md`](DISCLAIMER.md) before filing anything.
