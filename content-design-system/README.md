# Content Design System (Template)

A template for keeping a content design system in one repository and connecting it to the tools your team uses: AI skills, a design-tool review plugin, design kits and guidelines, authoring-tool rules, and a published style guide.

**The idea:** write each rule once. CI builds and publishes what can be scripted. An agent watches the tools that can't be scripted and opens issues or pull requests when something is stale. People approve changes.

## What's in the repo

```
content-design-system/
├── standards/            # the only place rules are edited
│   ├── voice-and-tone.md
│   ├── style-guide-rules.md
│   ├── checks.json
│   └── components/
├── terms/                # terms to avoid and prefer (feeds the plugin and validation rules)
├── decisions/            # decision log: why each rule exists
├── skills/               # AI skills for content work
├── plugin/               # design-tool review plugin (reads published rules)
├── design-system/        # description of your design system
├── figma-make/guidelines/# guidelines for AI design generation
├── agent/                # steward agent definition and recurring tasks
├── scripts/              # sync, validate, and build
├── docs/                 # one how-to per tool, plus architecture
└── .github/              # workflows, issue forms, code owners
```

## How it works

1. Someone edits `standards/` or `terms/` in a pull request.
2. CI checks that copies are in sync, validates the files, and builds `dist/`.
3. On merge, CI publishes `rules.json`, the Schematron file, and the standards to GitHub Pages.
4. The plugin reads the published `rules.json`, so it's current without a republish.
5. The agent compares each tool with the current `VERSION` and opens an issue for anything stale.

See `docs/architecture.md` for the diagram and the table of what updates how.

## Quick start

```
python scripts/sync_standards.py   # copy shared files to where they are used
python scripts/validate.py         # check the repository
python scripts/build.py            # build ./dist
```

Python 3 is the only requirement. The scripts use the standard library.

## Make it yours

Everything marked `[PLACEHOLDER]` is yours to fill in. See `docs/customizing.md` for the checklist.

The rules in `standards/` are examples of one team's choices. Replace them with your own. Choose a license before you make this repository public.

## Docs

- `docs/architecture.md`
- `docs/using-with-claude.md`
- `docs/using-with-figma.md`
- `docs/authoring-tools.md`
- `docs/customizing.md`
- `CONTRIBUTING.md`
