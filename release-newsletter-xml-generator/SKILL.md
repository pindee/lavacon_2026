---
name: "release-newsletter-xml-generator"
description: Use when generating release newsletter topic XML from a feature description. Works with plain DocBook 5.1, DITA 1.3, Paligo, or your own XML schema. Optionally pulls feature details from a connected feature tracker such as Aha! or Jira. Produces well-formed XML with content rules for common release newsletter topic types.
---

# Release Newsletter XML Generator

> **Template note:** This skill is a starter kit. The templates in `templates-reference.md` come in DocBook and DITA. If your schema is different, give Claude one sample topic and it will mirror the structure. Anything marked `[PLACEHOLDER]` is yours to fill in.

## Overview
Drafts release newsletter topics from a feature description and outputs them as well-formed XML in the format you choose. If a feature tracker (Aha!, Jira, or similar) is connected to Claude, feature details can be pulled directly. Otherwise you paste them in or Claude asks for them.

Files in this skill:
- `templates-reference.md` has four topic templates in DocBook 5.1 and DITA 1.3.
- `terms-reference.md` explains how to handle reusable terms (variables, keys, entities). Optional.
- `paligo-notes.md` has the extra conventions Paligo needs. Optional, Paligo users only.

## Template Types

| Template | Use When |
|----------|----------|
| **Product Update** | Standard feature or update (use this most often) |
| **New Marketplace Solution Offerings** | New marketplace or integration partner |
| **Help Hub Updates** | New training content added to your help hub |
| **System Status Notifications** | System status or outage notification |

## Workflow

### Step 0 — Choose the output format
Ask once, with these options:

> "Which XML format should I produce?
> 1. DocBook 5.1 (plain)
> 2. DITA 1.3
> 3. Paligo (DocBook with Paligo conventions)
> 4. Something else: paste one sample topic and I'll mirror it"

- Options 1 and 2: use the matching templates as they are.
- Option 3: use the DocBook templates, then apply `paligo-notes.md`.
- Option 4: use the sample's element names and structure. Keep the content rules below.

Then ask: "Do you use reusable terms (variables, keys, or entities) for words like site or product names? If yes, share your list or fill in `terms-reference.md`."

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
| Problem, value, functionality | `description` | Description | Description or body |
| Navigation path, "Communicate to customer?" flag | Custom fields | Custom fields or labels | Custom fields or labels |
| Product area or module | `product_line` / project | Project or Component | Area, label, or team |
| Release version or date | `release` | Fix Version | Milestone or iteration |

If a field isn't in the record, ask the user for just that detail.

**Step 1b — Manual input** (pasted text or no tracker):
- Problem definition and value proposition
- Navigation path
- Target release and product

Ask only for what is missing.

### Step 2 — Gather remaining inputs
- Navigation path (if not in the tracker record)
- New security permissions? (yes/no)
- Screenshots to include? (add placeholders)

### Step 3 — Select the template
Almost always: Product Update. Use the others only for marketplace, help hub, or status scenarios.

### Step 4 — Draft content
Follow the content rules below BEFORE writing XML.

### Step 5 — Handle reusable terms
- If the user has a terms list, follow the rules in `terms-reference.md`. Use the reusable syntax for every matching term. Never hardcode the plain word.
- If the term is marked **TBD**, ask for the identifier. Don't guess.
- If the user has no terms list, replace each `{{TOKEN}}` in the template with plain text, keep terms consistent, and mention any term that looks like it varies by customer or market.

### Step 6 — Generate the XML
Use the template for the chosen format and fill it in. Output one file per topic.

### Step 7 — Check and name the file
Choose a naming pattern and stick with it. Examples:
- By month: `[FeatureName]_[Mon]_[Year].xml` → `Home_Page_Mar_2026.xml`
- By release number: `[ReleaseNum]_[FeatureName].xml` → `4451-52_Billing_Module.xml`

If you have a code tool, check that the file is well-formed (for example, `xmllint --noout file.xml`). Tell the user that this only confirms well-formedness. It does not validate against a DocBook or DITA schema. Save the file and present it.

### Step 8 — Deliver
In your reply, list anything that needs manual follow-up: screenshots to add and any terms still marked TBD. For Paligo, point to the import steps in `paligo-notes.md`.

---

## Content Rules (template)

These sections are placeholders for your own standards. Modify accordingly. Until you do, Claude follows the structure of the templates.

### Title
- [Your rules for title length, casing, punctuation, and specificity.]

### Introduction (no heading)
- [Your rules for intro length and structure.]

### Navigation Steps
- [Your rules for how navigation paths are written.]
- Use `&gt;` between steps in the XML.

### Security Permissions (optional)
- [When to include this block, and which columns it uses.]

### Standard Role Features (optional)
- [When to include this block, and any required closing note.]

### Language Rules
- [Reading level, voice, pronoun, and number style.]

### Words to avoid
- Modify accordingly with your terms

### Feedback Footer
- [Optional. If you collect draft feedback, put the link in the draft shown to the user and keep it out of the XML: `[YOUR_FEEDBACK_FORM_URL]`.]

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Leaving `{{TOKENS}}` in the final file | Replace every token with your reusable-term syntax or plain text |
| Hardcoding a term that is in the terms table | Use the matching reusable syntax |
| Guessing an identifier for a **TBD** term | Ask the user to confirm it |
| Including the feedback footer in the XML | Remove it; show it in the draft only |
| Using ">" as raw text between nav steps | Use `&gt;` in XML |
| Breaking one of your own content rules | Re-check the draft against the Content Rules section |
| Mixing DocBook and DITA elements | Pick one format per file |
| Asking the user for a tracker API key or a script | Use the connected tracker tools, or ask for the details directly |
