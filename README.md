# LavaCon 2026: A Connected Content Design System

A starter repository for keeping your content standards in one place and connecting them to the tools your team uses: AI skills, a design-tool review plugin, design kits and guidelines, authoring-tool rules, and a published style guide.

**The idea:** write each rule once. CI builds and publishes whatever can be scripted. An agent watches the tools that can't be scripted and opens issues or pull requests when something is stale. People approve every change.

These are **templates**. They show a working pattern, and you adapt them to your own style guide, authoring tools, and XML format. Anything in `[SQUARE_BRACKETS]` is a placeholder you replace with your own value.

## These are examples, not standards

The rules, wording, and conventions in this repository (for example, ALL CAPS buttons, hyphenated ranges, and table-only output) come from one team's standards. They are **examples** to show how a skill or a style guide can encode a standard. Don't copy them as they are. Replace them with your own. Until you do, Claude applies them as written.

Where a section shows `[bracketed]` prompts or the line "Modify accordingly with your terms", it is blank on purpose. Fill it in with your own rules.

## What's in the repository

```
.
├── standards/             # the only place rules are edited
│   ├── voice-and-tone.md
│   ├── style-guide-rules.md
│   ├── checks.json
│   └── components/
├── terms/                 # terms to avoid and prefer (feeds the plugin and validation rules)
├── decisions/             # decision log: why each rule exists
├── skills/                # AI skills for content work (see the table below)
├── plugin/                # design-tool review plugin (reads published rules)
├── design-system/         # description of your design system
├── figma-make/guidelines/ # guidelines for AI design generation
├── agent/                 # steward agent definition and recurring tasks
├── scripts/               # sync, validate, and build
├── docs/                  # architecture, plus one how-to per tool
└── .github/               # workflows, issue forms, code owners
```

## How it stays connected

1. Someone edits `standards/` or `terms/` in a pull request.
2. CI checks that copies are in sync, validates the files, and builds `dist/`.
3. On merge, CI publishes `rules.json`, the Schematron file, and the standards to GitHub Pages.
4. The plugin reads the published `rules.json`, so it's current without a republish.
5. The agent compares each tool with the current `VERSION` and opens an issue for anything stale.

Two layers do the work. **CI** handles everything that can be built from files in this repository. The **agent** handles what scripts can't: tools behind a sign-in, comparing what a design kit is using with the current standards, reviewing recent content, and triaging feedback. See [`docs/architecture.md`](docs/architecture.md) for the diagram and a table of what updates how.

## Skills

| Skill | What it does | Needs |
|---|---|---|
| [`content-design-review`](skills/content-design-review/) | Reviews UI copy (errors, buttons, dialogs, tooltips, and so on) against a style guide and flags issues with suggested rewrites. | Optional: Figma connector |
| [`helpfile-xml-generator`](skills/helpfile-xml-generator/) | Drafts help topics as well-formed XML in plain DocBook 5.1, DITA 1.3, Paligo, or a schema you provide. Includes six topic templates. | Optional: a feature tracker connector (Aha!, Jira, and others) |
| [`release-newsletter-xml-generator`](skills/release-newsletter-xml-generator/) | Drafts release newsletter topics as well-formed XML in the same formats. | Optional: a feature tracker connector |
| [`feature-record-writer`](skills/feature-record-writer/) | Helps write feature record fields (value proposition, functionality, setup, navigation, release plan) for Aha!, Jira, or any tracker, always as a strict two-column table. | None |
| [`survey-poll-analysis`](skills/survey-poll-analysis/) | Analyzes survey or poll responses from any tool. It checks for a connected survey tool first, then falls back to a CSV or Excel export or pasted data, and writes a report with counts, themes, and five key insights. | None (optional: a survey tool connector) |

Each skill folder is self-contained. It has a `SKILL.md`, and some also have reference files such as `templates-reference.md`, `terms-reference.md`, `paligo-notes.md`, or `style-guide-rules.md`.

The `style-guide-rules.md` inside `skills/content-design-review/` is a copy of `standards/style-guide-rules.md`. Edit the one in `standards/`, then run `python scripts/sync_standards.py`. CI fails if the copy is out of date.

### Using a skill

1. Pick a skill folder and zip it, with `SKILL.md` at the top level of that folder.
2. Add it as a custom skill in your Claude settings.
3. Ask Claude to do the task, or invoke the skill by name.

You can also copy the folder into a Claude Code skills directory, for example `.claude/skills/`.

## Quick start

```
python scripts/sync_standards.py   # copy shared files to where they are used
python scripts/validate.py         # check the repository
python scripts/build.py            # build ./dist
```

Python 3 is the only requirement. The scripts use the standard library.

## Making it yours

Replace every `[PLACEHOLDER]`. The full checklist is in [`docs/customizing.md`](docs/customizing.md). The short version:

**The system**
- Set your handle or team in `.github/CODEOWNERS`.
- Set `RULES_URL` in `plugin/ui.html` and `allowedDomains` in `plugin/manifest.json` to the address where your repository publishes `rules.json`.
- In the repository settings, turn on GitHub Pages with **GitHub Actions** as the source.
- Edit `standards/`, `standards/checks.json`, and `terms/terms.json` to match your own standards.
- Edit `agent/AGENT.md` and `agent/tasks/` for your tools and sources.

**The skills**
- **XML generators:** the skills ask which format you want (DocBook 5.1, DITA 1.3, Paligo, or your own schema). No setup is needed for the first three. If you use reusable terms, fill in `terms-reference.md`. Paligo users also fill in `paligo-notes.md`.
- **`content-design-review`:** edit the "Confirmed Conventions" list in `SKILL.md`, and set your Figma pattern file URL and page map node IDs.
- **`feature-record-writer`:** set `[YOUR_FEEDBACK_FORM_URL]` (or delete the feedback step), and adjust the section list to match your tracker.
- **`survey-poll-analysis`:** set `[YOUR_REPORTS_FOLDER]`.

## Connectors

Some skills work best with MCP connectors turned on in Claude. None of the skills asks for API keys, because connectors handle authentication.

- **Figma:** live pattern lookups in `content-design-review`. The skill works without it.
- **Feature trackers (Aha!, Jira, and others):** optional for the two XML generators. They check for a connected tracker first. Without one, you paste the ticket text or describe the feature.
- **Survey tools (Pendo, SurveyMonkey, and others):** optional for `survey-poll-analysis`. It checks for a connected survey tool first and falls back to a CSV or Excel export.

## Notes and limitations

- Generated XML is checked for well-formedness only. There is no DocBook, DITA, or Paligo schema validation, so run a final check in your authoring tool.
- The DITA templates target the general DITA 1.3 task and topic types. If your project uses specialized or strict DTDs, adjust the elements to match.
- The review plugin and the agent workflow are starters. Test them before you rely on them.
- Some tools only accept updates through their own interface. The agent reports what is stale, and a person applies the update.
- Review all generated content before publishing. These skills speed up drafting and don't replace editorial review.

## Docs

- [`docs/architecture.md`](docs/architecture.md)
- [`docs/using-with-claude.md`](docs/using-with-claude.md)
- [`docs/using-with-figma.md`](docs/using-with-figma.md)
- [`docs/authoring-tools.md`](docs/authoring-tools.md)
- [`docs/customizing.md`](docs/customizing.md)
- [`CONTRIBUTING.md`](CONTRIBUTING.md)

## License

[Choose a license, for example MIT or CC BY 4.0, and add a LICENSE file.]
