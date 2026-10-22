# LavaCon Claude Skills: Content Design & Structured-Content XML Templates

A starter set of Claude skills for technical writers and content designers. They cover UI copy review, help and release-note XML generation (DocBook, DITA, or your own schema), feature record writing, and survey analysis.

These are **templates**. They show a working pattern, and you adapt them to your own style guide, authoring tools, and XML format. Anything in `[SQUARE_BRACKETS]` is a placeholder you replace with your own value.

## These are examples, not standards

The rules, wording, and conventions in these skills (for example, ALL CAPS buttons, hyphenated ranges, and table-only output) come from one team's standards. They are **examples** to show how a skill can encode a style guide. Don't copy them as they are. Replace them with your own standards. Until you do, Claude applies them as written.

Where a section shows `[bracketed]` prompts or the line "Modify accordingly with your terms", it is blank on purpose. Fill it in with your own rules. The `content-design-review` skill keeps a longer example style guide in `style-guide-rules.md`. Edit it, shorten it, or replace it.

## What's included

| Skill | What it does | Needs |
|---|---|---|
| [`content-design-review`](content-design-review/) | Reviews UI copy (errors, buttons, dialogs, tooltips, and so on) against a style guide and flags issues with suggested rewrites. | Optional: Figma connector |
| [`helpfile-xml-generator`](helpfile-xml-generator/) | Drafts help topics as well-formed XML in plain DocBook 5.1, DITA 1.3, Paligo, or a schema you provide. Includes six topic templates. | Optional: a feature tracker connector (Aha!, Jira, and others) |
| [`release-newsletter-xml-generator`](release-newsletter-xml-generator/) | Drafts release newsletter topics as well-formed XML in plain DocBook 5.1, DITA 1.3, Paligo, or a schema you provide. | Optional: a feature tracker connector (Aha!, Jira, and others) |
| [`feature-record-writer`](feature-record-writer/) | Helps write feature record fields (value proposition, functionality, setup, navigation, release plan) in grade 7 language for Aha!, Jira, or any tracker, always as a strict two-column table. | None |
| [`survey-poll-analysis`](survey-poll-analysis/) | Analyzes survey or poll responses from any tool. It checks for a connected survey tool first, then falls back to a CSV/Excel export or pasted data, and writes a report with counts, themes, and five key insights. | None (optional: a survey tool connector) |

Each folder is self-contained. It has a `SKILL.md`, and some also have reference files such as `templates-reference.md`, `terms-reference.md`, `paligo-notes.md`, or `style-guide-rules.md`.

## Using a skill

1. Pick a skill folder and zip it, with `SKILL.md` at the top level of that folder.
2. Add it as a custom skill in your Claude settings.
3. Ask Claude to do the task, or invoke the skill by name.

You can also copy the folder into a Claude Code skills directory.

## Making them yours

Work through this checklist per skill.

**XML generators (`helpfile-xml-generator`, `release-newsletter-xml-generator`)**
- The skills ask which format you want: DocBook 5.1, DITA 1.3, Paligo, or your own schema (paste a sample topic and Claude mirrors it). No setup needed for the first three.
- Optional: if you use reusable terms (variables, keys, or entities), fill in `terms-reference.md` with your term list and syntax. If you don't, leave it alone and Claude writes plain text.
- Optional, Paligo users only: fill in the `[PLACEHOLDER]` values in `paligo-notes.md` (variable and varset IDs, reusable heading UUIDs) and set your instance URL.
- Adjust the style and content rules in each `SKILL.md` to match your style guide.

**`content-design-review`**
- Replace `style-guide-rules.md` with your own rules. The included set is an example, and some choices in it (ALL CAPS buttons, hyphenated ranges) are house style, not universal standards.
- Edit the "Confirmed Conventions" list in `SKILL.md` so Claude doesn't flag your deliberate choices.
- Set your Figma pattern file URL and fill in the page map node IDs.

**`survey-poll-analysis`**
- Set `[YOUR_REPORTS_FOLDER]` for saved reports.
- Optional: add notes for your own survey tool's connector or export steps in the "Optional: connected sources" section.

**Feature tracker (XML generators)**
- Nothing to set up. The skills check for a connected tracker (Aha!, Jira, or similar) and otherwise ask you to paste the ticket text.
- Optional: add your tracker's field names to the field mapping table in each `SKILL.md`, and replace the example `PROJ-` ticket key with your own.

**`feature-record-writer`**
- Set `[YOUR_FEEDBACK_FORM_URL]`, or delete the feedback step.
- Adjust the section list and rules to match the fields in your tracker.

## Connectors

Some skills work best with MCP connectors turned on in Claude:

- **Figma:** live pattern lookups in `content-design-review`. The skill works without it, using the rules file only.
- **Feature trackers (Aha!, Jira, and others):** optional for the two XML generators. They check for a connected tracker first. Without one, you paste the ticket text or describe the feature.
- **Survey tools (Pendo, SurveyMonkey, and others):** optional for `survey-poll-analysis`. The skill checks for a connected survey tool first and falls back to a CSV or Excel export. Pendo is included as one worked example of a connected source.

None of the skills asks for API keys. Connectors handle authentication.

## Notes and limitations

- Generated XML is checked for well-formedness only. There is no DocBook, DITA, or Paligo schema validation, so run a final check in your authoring tool.
- The DITA templates target the general DITA 1.3 task and topic types. If your project uses specialized or strict DTDs, adjust the elements to match.
- Paligo users: the import wrapper and variable syntax live in `paligo-notes.md`. The core templates don't include them.
- Review all generated content before publishing. These skills speed up drafting and don't replace editorial review.

## License

[Choose a license, for example MIT or CC BY 4.0, and add a LICENSE file.]

## Contributing

Issues and pull requests are welcome. If you adapt a skill for your own stack, a note on what you changed helps others.
