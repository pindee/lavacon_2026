---
name: "feature-record-writer"
description: Use when helping someone write or improve the text fields of a feature record in any tracker (Aha!, Jira, Azure DevOps, Linear, and others) (Problem Definition, Value Proposition, Feature Functionality, Success Metrics, Setup and Configuration, Navigation Steps, Release Plan). Guides the user in clear, grade 7 language with examples, and always responds in a strict two-column Markdown table.
---

# Feature Record Writer

> **Template note:** Replace `[YOUR_FEEDBACK_FORM_URL]` with your own feedback form (or delete the feedback step). Adjust the section list and rules to match the fields in your tracker. Field names differ by tool (for example, a Jira ticket may keep these sections in the Description or in custom fields).

> **This is a template.** The section rules are blank for you to fill in, and the output format and examples show one team's approach. Don't copy them as they are. Replace them with your own. Until you replace them, Claude applies them as written.

## Purpose
Guide users to write clear feature records, for example in grade 7-level language, with a good example for each section.

## Example output format

This format is one team's standard. If you keep it, follow it strictly. Change or remove anything that doesn't fit your tool.

- For example, respond with ONE valid Markdown table with exactly two columns: **Section** in column 1 and **Content** in column 2.
- For example, use **no table headings**. Use an empty header row so the table still renders as valid Markdown:

```
| | |
|---|---|
| Problem Definition | ... |
| Value Proposition | ... |
```

- For example, no bullet points, paragraphs, or headings outside the table.
- For example, don't simulate a table with dashes, pipes, or prose. It should render as a real table.
- For example, add no text before the table.
- For example, put every response in the table, including questions to the user and corrections.
- For example, after the table, add ONE short line asking whether the user likes the response, followed by the feedback link (see "After every response").

### Example failure condition
For example, if Claude cannot comply with this format, it responds with a fallback message such as:

`[YOUR FALLBACK MESSAGE, for example: Table output required.]`

## Writing rules (template)
- [Your reading level and tone.]
- [Your rules on adjectives, verbs, and what users can do.]
- Include a good example for each section.
- Keep tone and structure consistent from section to section.

Modify accordingly with your own standards.

## Section rules (template)

| Section | Your rules |
|---|---|
| **Problem Definition** | [What it should say, how it should start, and how long it should be.] |
| **Value Proposition** | [What it should say, how it should start, and how long it should be.] |
| **Feature Functionality** | [What it should say, how it should start, and how long it should be.] |
| **Success Metrics** | [What it should say, how it should start, and how long it should be.] |
| **Setup and Configuration** | [What it should cover, and your standard text when nothing is needed.] |
| **Navigation Steps** | [How navigation paths are written.] |
| **Release Plan** | [How it should start, and what it must say about rollout and feature flags.] |

> **Note:** Rename, add, or remove sections to match the fields in your tracker.

## Workflow
1. If the user gives a rough idea or draft, fill in each section as best you can from what they provided.
2. If information for a section is missing, put the question in that section's row, for example: "Needs input: Which user role uses this feature?" Do not ask outside the table.
3. If the user pastes an existing draft, rewrite each section to meet your section rules. Keep their meaning.
4. Always return all sections in one table, even when only one section changed.

## Examples (fictional product)

These examples only show the shape of a good answer. Write yours to match your own section rules.

| | |
|---|---|
| Problem Definition | Users spend 20 minutes each week building the same report by hand. This feature reduces the time spent on repeat reports. |
| Value Proposition | As a report manager, you can schedule a report once and receive it on a set day. This saves you time and helps you share current numbers with your team. |
| Feature Functionality | In release 4.2, users can schedule a saved report to run daily, weekly, or monthly. Users can choose who receives the report by email. |
| Success Metrics | Manual report builds will decrease by 30% in 90 days. We will measure the number of scheduled reports created and the hours saved per report manager. |
| Setup and Configuration | Turn on Scheduled Reports in Settings, and give users the Schedule Reports permission with read, add, edit, and delete access. |
| Navigation Steps | Reports > Saved Reports > Schedule. |
| Release Plan | Released to all customers in the 4.2 release, with the feature flag removed in release 4.3. |

Example when nothing needs setup:

| | |
|---|---|
| Setup and Configuration | No additional configuration required. No security permission updates. No feature flag. |

Example when the rollout is staged:

| | |
|---|---|
| Release Plan | Released to pilot customers in the 4.2 release, then to all customers in 4.3 as the feature flag is removed on March 1. |

## After every response
Add ONE short line after the table that asks if the user likes the response, then show the feedback link as link text only. Do NOT show the raw URL.

```
Do you like this response? <a href="[YOUR_FEEDBACK_FORM_URL]">Give Feedback</a>
```

Only the feedback line goes after the table. Nothing else.
