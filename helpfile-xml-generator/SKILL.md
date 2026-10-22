---
name: "helpfile-xml-generator"
description: Use when generating help topic XML from a feature description. Works with plain DocBook 5.1, DITA 1.3, Paligo, or your own XML schema. Optionally pulls feature details from a connected feature tracker such as Aha! or Jira. Produces well-formed XML with consistent structure, UI-element markup, and reusable-term handling for common help template types (config and end-user, single and multi-procedure, dashboards).
---

# Help File XML Generator

> **Template note:** This skill is a starter kit. The templates in `templates-reference.md` come in DocBook and DITA. If your schema is different, give Claude one sample topic and it will mirror the structure. Anything marked `[PLACEHOLDER]` is yours to fill in.

## Overview
Drafts help topics from a feature description and outputs them as well-formed XML in the format you choose. If a feature tracker (Aha!, Jira, or similar) is connected to Claude, feature details can be pulled directly. Otherwise you paste them in or Claude asks for them.

Files in this skill:
- `templates-reference.md` has six topic templates in DocBook 5.1 and DITA 1.3.
- `terms-reference.md` explains how to handle reusable terms (variables, keys, entities). Optional.
- `paligo-notes.md` has the extra conventions Paligo needs. Optional, Paligo users only.

## Template Types

| Template | Use When |
|----------|----------|
| **Config Small** | Single setup procedure, no options section |
| **Config Big** | Single setup procedure plus a Configuration Options section |
| **Config Multi-Procedure** | Multiple ordered setup procedures plus Configuration Options |
| **End-User Small** | Single end-user procedure |
| **End-User Multi-Procedure** | Multiple ordered end-user procedures plus an Options section |
| **Dashboard Pane** | Dashboard pane documentation |

If your product has more than one area (for example, admin and operations), the only difference between variants is the first term in the navigation path.

## Workflow

### Step 0 — Choose the output format
Ask once, with these options:

> "Which XML format should I produce?
> 1. DocBook 5.1 (plain)
> 2. DITA 1.3
> 3. Paligo (DocBook with Paligo conventions)
> 4. Something else: paste one sample topic and I'll mirror it"

- Options 1 and 2: use the matching templates as they are.
- Option 3: use the DocBook templates, then apply `paligo-notes.md` (namespaces, import wrapper, variables).
- Option 4: use the sample's element names and structure. Keep the style rules below.

Then ask, in the same message if possible: "Do you use reusable terms (variables, keys, or entities) for words like site or product names? If yes, share your list or fill in `terms-reference.md`."

### Step 1 — Get the feature details
**First, check your tool list** for a connector to a feature or issue tracker (for example Aha!, Jira, Azure DevOps, Linear, GitHub Issues, or Asana). Don't assume the user has one.

Then ask, naming any tracker you found:

> "Where is the feature described?
> 1. In a tracker connected to Claude (give me the ticket key, link, or feature name)
> 2. In text I can read: paste the ticket, spec, or notes here
> 3. Nowhere yet: describe the feature and I'll ask for what's missing"

If the user's tracker isn't connected, say you can't see a connector for it and suggest pasting the ticket text or an export.

**Step 1a — Fetch from the tracker:**
- Use the connector's read and search tools. Don't hardcode tool names, since each tracker names them differently.
- Exact key or link (for example `PROJ-1234`): read that record with full detail.
- Only a name or partial description: search, confirm the right match with the user, then read the full record.
- Never ask for an API key or a manual script. The connector handles auth.

Field names vary by tool. These are common equivalents:

| Detail needed | Aha! | Jira | Other tools |
|---|---|---|---|
| Title | `name` | Summary | Title or name |
| Description, problem, functionality | `description` | Description | Description or body |
| Navigation path, configuration options | Custom fields | Custom fields or Description | Custom fields or comments |
| Product area (guides template choice) | `product_line` / project | Project or Component | Area, label, or team |
| Release (for context) | `release` | Fix Version | Milestone or iteration |

If a field isn't in the record, ask the user for just that detail.

**Step 1b — Manual input** (pasted text or no tracker):
- What the feature does and what users can do with it
- Navigation path (exact menu steps)
- Product area

Ask only for what is missing.

### Step 2 — Gather remaining inputs
- Template type, if unclear
- Single-site only, or single plus multi-site navigation?
- Does the topic need a Configuration Options section?
- Screenshots available? (add placeholders)

### Step 3 — Draft content following the style rules below

### Step 4 — Handle reusable terms
- If the user has a terms list, follow the rules in `terms-reference.md`. Use the reusable syntax for every matching term. Never hardcode the plain word.
- If the term is marked **TBD**, ask for the identifier. Don't guess.
- If the user has no terms list, replace each `{{TOKEN}}` in the template with plain text, keep terms consistent, and mention any term that looks like it varies by customer or market.

### Step 5 — Generate the XML
Use the template for the chosen format and fill it in. Output one file per topic.

### Step 6 — Check and name the file
- Name the file after the topic title with underscores: `Configuring_Report_Builder_Security.xml`.
- If you have a code tool, check that the file is well-formed (for example, `xmllint --noout file.xml`).
- Tell the user that this only confirms well-formedness. It does not validate against a DocBook or DITA schema, or against your own rules. Recommend a final check in their authoring tool.
- Save the file and present it to the user.

### Step 7 — Deliver
In your reply, list anything that needs manual follow-up: screenshots to add, links to convert to cross-references, and any terms still marked TBD. For Paligo, point to the import steps in `paligo-notes.md`.

---

## Style Rules (template)

These sections are placeholders for your own standards. Modify accordingly. Until you do, Claude follows the structure of the templates and the markup rules below.

### Title
- [Your rules for title form, casing, and punctuation.]

### Introduction (no heading)
- [Your rules for intro length, voice, and reading level.]

### Steps
- Use the format's procedure and step elements so numbering is automatic.
- Mark every UI element the user must select (`<guilabel>` in DocBook, `<uicontrol>` in DITA).
- [Your rules for navigation steps, step wording, and punctuation.]

### Notes, Important, Warning
- [Which callout types you use, and when.]

### Things to avoid
- Modify accordingly with your terms

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Leaving `{{TOKENS}}` in the final file | Replace every token with your reusable-term syntax or plain text |
| Hardcoding a term that is in the terms table | Use the matching reusable syntax |
| Guessing an identifier for a **TBD** term | Ask the user to confirm it |
| Numbered steps as plain paragraphs | Use the procedure and step elements |
| Large template for a single procedure | Use the Small template |
| Breaking one of your own style rules | Re-check the draft against the Style Rules section |
| Mixing DocBook and DITA elements | Pick one format per file |
| Asking the user for a tracker API key or a script | Use the connected tracker tools, or ask for the details directly |
