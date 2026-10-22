# Customizing

Replace every `[PLACEHOLDER]`. A quick way to find them:

```
grep -rn "\[YOUR_\|\[PLUGIN_ID\|\[RULES_URL\|\[DESIGN" . --include=* --exclude-dir=.git
```

| Where | What to set |
|---|---|
| `standards/` | Your voice, tone, and style rules. Delete anything that isn't yours. |
| `standards/checks.json` | Sentence length and banned patterns |
| `terms/terms.json` | Your terms to avoid and prefer |
| `plugin/manifest.json` and `plugin/ui.html` | Plugin ID, allowed domain, and `RULES_URL` |
| `.github/CODEOWNERS` | Your team's handle |
| `agent/AGENT.md` and `agent/tasks/` | Your tools, sources, and schedule |
| `design-system/README.md` | Your design system's name, source, and links |
| `figma-make/guidelines/` | Your guidelines for generated designs |
| Repository settings | Turn on GitHub Pages (source: GitHub Actions) |

## First run

```
python scripts/sync_standards.py
python scripts/validate.py
python scripts/build.py
```

All three should succeed before your first commit.

## License

Choose a license and add a `LICENSE` file before you make the repository public.
