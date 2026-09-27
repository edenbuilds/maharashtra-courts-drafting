# Install

This pack is a **local MCP / Claude plugin**, not a website.  
“Deploy” means: clone the repo and point your host at `server/main.py`.

Repo (public):  
**https://github.com/edenbuilds/maharashtra-courts-drafting**

---

## 1. Prerequisites

| Tool | Why |
|---|---|
| Git | Clone the private repo |
| Python ≥ 3.10 | MCP server |
| [uv](https://github.com/astral-sh/uv) | Runs the server with pinned deps (`mcp>=1.2,<2`) |
| [pandoc](https://pandoc.org) | Renders `final-draft.docx` |
| `pdftotext` (poppler) | Reads PDF papers in `inputs/` |

Quick checks:

```bash
python3 --version
uv --version
pandoc --version
pdftotext -v
```

---

## 2. Get the pack

Accept the GitHub collaborator invite, then:

```bash
git clone https://github.com/edenbuilds/maharashtra-courts-drafting.git
cd maharashtra-courts-drafting
```

SSH alternative (if your key is on the account):

```bash
git clone git@github.com:edenbuilds/maharashtra-courts-drafting.git
```

---

## 3. Connect it to your host

### Option A — Claude Code plugin (simplest for daily drafting)

From inside the clone:

```text
/plugin install .
```

If your Claude Code build accepts a GitHub plugin URL:

```text
/plugin install github:edenbuilds/maharashtra-courts-drafting
```

Start a **new** chat after install. First tool call the model should make is `get_agent_instructions()`.

### Option B — Claude Desktop (MCP server)

1. Find your config file:
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Merge this block (use a **real absolute path**):

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

3. Fully quit and reopen Claude Desktop.  
4. In a new chat, open the tools / MCP panel and confirm tools such as:

   - `get_agent_instructions`
   - `list_case_types`
   - `get_template`
   - `create_case_folder`
   - `save_draft_as_docx`

### Option C — Cursor (or another MCP client)

Add the same `uv --directory … run server/main.py` entry in that product’s MCP settings.  
Restart the agent / reload MCP.

### Option D — Run the server yourself (debug)

```bash
cd /path/to/maharashtra-courts-drafting
uv run server/main.py
```

The process speaks MCP on stdio. Point any compatible client at it.

---

## 4. Smoke test (60 seconds)

In a new chat after install:

> Call get_agent_instructions with no arguments, then list_case_types, then list_templates. Do not draft yet — just confirm the harness is loaded.

You should see:

1. The orchestration runbook (Reader → Overseer).  
2. Case-type keys including `civil-wp`, `wp-reply-affidavit`, `mat-oa`, …  
3. Paths under `templates/high-court/`, `templates/tribunals/`, etc.

Then try a real matter:

> Draft a civil writ against TMC, Thane. Demolition notice 3 Jan 2026. Stay + certiorari. Create a case folder and run the full pipeline.

---

## 5. Where drafts land

Default root:

```text
~/Downloads/MH-Courts-Drafts/<your-label>/
  inputs/      ← drop notices, orders, FIR, policy copies here
  artifacts/   ← pipeline outputs (case-facts.md … final-draft.docx)
```

Override the root with `create_case_folder(label, root="/some/path")` if you prefer.

---

## 6. Updating

```bash
cd maharashtra-courts-drafting
git pull origin main
```

Restart the MCP host (or re-run `/plugin install .`) so it picks up server and template changes.

---

## 7. Troubleshooting

| Symptom | Fix |
|---|---|
| No tools appear | Path in config wrong; `uv` not on PATH; host not restarted |
| `mcp` / FastMCP import error | Pack pins `mcp>=1.2,<2` — use `uv run`, do not install mcp 2.x into the env |
| `pandoc failed` | Install pandoc; re-run `save_draft_as_docx` |
| PDF unread | Install poppler (`pdftotext`) |
| Private clone 404 | Accept Write invite; use an account that can see `edenbuilds/maharashtra-courts-drafting` |
| Model skips pipeline | Remind it: first call `get_agent_instructions()`; see [`HARNESS.md`](HARNESS.md) |

---

## 8. Related docs

- [`../START_HERE.md`](../START_HERE.md) — one-page overview  
- [`HARNESS.md`](HARNESS.md) — orchestration & agents  
- [`../USAGE.md`](../USAGE.md) — prompt examples  
- [`INVENTORY.md`](INVENTORY.md) — what ships in the pack  
- [`../DISCLAIMER.md`](../DISCLAIMER.md) — advocate verification duty  
