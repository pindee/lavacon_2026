# Task: Sync check

Goal: find any tool that is using an out-of-date copy of the standards.

1. Read `VERSION` and `dist/manifest.json` (or the published `manifest.json`) to get the current version and file hashes.
2. For each destination in the table below, find the version or content it currently uses.
3. Compare it with the current version.
4. For each stale destination, open one issue that says what is stale, which files changed, and the steps to update it (link the matching how-to in `docs/`).

| Destination | How to check | How it gets updated |
|---|---|---|
| Published style guide site | Compare its version with `VERSION` | Automatic (publish workflow) |
| Review plugin | Check the version shown in the plugin | Automatic (reads `rules.json`) |
| AI skills | Compare `skills/content-design-review/style-guide-rules.md` with `standards/style-guide-rules.md` | `scripts/sync_standards.py` |
| `[DESIGN KIT / GUIDELINES FILES]` | `[Open the kit and compare guideline files with figma-make/guidelines/]` | Manual: see `docs/using-with-figma.md` |
| `[AI DESIGN SYSTEM]` | `[Compare its readme with design-system/README.md]` | Manual: see `docs/using-with-claude.md` |
| `[AUTHORING TOOL VALIDATION]` | `[Compare imported rules with dist/terms.sch]` | Manual: see `docs/authoring-tools.md` |

Report anything you couldn't check under "Couldn't check".
