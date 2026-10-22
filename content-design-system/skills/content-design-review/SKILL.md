---
name: "content-design-review"
description: Use when reviewing, checking, or improving product UI copy (error messages, button labels, dialogs, tooltips, empty states, field labels, banners, snackbars, checkboxes, dropdowns, or any other in-product or help text) against your organization's tone, voice, and style standards. Ships with an editable example rule set in style-guide-rules.md.
---

# Content Design Review

> **Template note:** This skill is a starter. The rules in `style-guide-rules.md` and the "Confirmed Conventions" in Step 3a are *examples*. Replace them with your own style guide, and replace the Figma file link and page map in Step 2 with your own pattern library.

## What This Skill Does
1. Reviews content against your tone and style standards.
2. Compares content against known live UI pattern examples (Figma, if available).
3. Flags issues with concrete suggestions.

## Step 0: Gather Input
Before reviewing anything, if none of the following have already been provided, ask the user for just ONE of:
1. The UI copy to review (paste the text), OR
2. The component type, if not obvious from context (see the list in Step 1), OR
3. A Figma link to the specific screen, frame, or page the copy comes from, if one exists.

Make clear that only one of these is needed to get started. Don't ask for all three at once. If they give a Figma link, use it with the Figma MCP connector in Step 2 instead of the bundled page map, since it's a more precise comparison than the general pattern library. If no Figma link is available, say so and fall back to the rules file and page map.

## Step 1: Identify the Component Type
Determine what type of UI content is being reviewed, since this affects which conventions apply:
Error message, button label, dialog box, tooltip, empty state, field label/ghost text, loading indicator, toggle, search field, snackbar, session timeout, banner, email, filter, password/sign-in screen, stepper, navigation, checkbox/radio button, dropdown/list, information message.

## Step 2: Compare Against Live Patterns (via Figma MCP)
Your team can maintain a "Content Pattern Examples" Figma file. Set its URL here:

`https://www.figma.com/design/[YOUR_FILE_KEY]/Content-Pattern-Examples`

If the Figma MCP connector is available in this environment, use it to fetch live reference text. Do not use a Figma API key, personal access token, or `curl` call; the connector handles authentication itself.

1. If the user provided a Figma link in Step 0, use that link directly.
2. Otherwise, build the target URL from the pattern library: take the file link above and append `?node-id=PAGE_ID`, using the page ID for the component type identified in Step 1 (see map below).
3. Call the Figma MCP tool `get_design_context` (or `get_metadata`) with that URL to pull the live text content for the page.
4. For casing questions specifically, call `get_screenshot` on the same node and read the rendered display rather than trusting the source text.

Page map (fill in with your own node IDs):

| Component | Figma Page ID |
|---|---|
| Accordion | [NODE_ID] |
| Authentication / 2FA | [NODE_ID] |
| Banners | [NODE_ID] |
| Buttons / FABs | [NODE_ID] |
| Checkboxes / Radio Buttons | [NODE_ID] |
| Dialogs | [NODE_ID] |
| Dropdowns / Lists | [NODE_ID] |
| Emails | [NODE_ID] |
| Empty States | [NODE_ID] |
| Errors | [NODE_ID] |
| Fields | [NODE_ID] |
| Filters | [NODE_ID] |
| Headings | [NODE_ID] |
| Icons | [NODE_ID] |
| Information Messages | [NODE_ID] |
| Loading Indicators | [NODE_ID] |
| Mobile | [NODE_ID] |
| Navigation Drawer | [NODE_ID] |
| Password Screens | [NODE_ID] |
| Search Field | [NODE_ID] |
| Snackbar | [NODE_ID] |
| Stepper | [NODE_ID] |
| Timeouts | [NODE_ID] |
| Toggles | [NODE_ID] |
| Tooltips | [NODE_ID] |
| Tooltips & Chips | [NODE_ID] |
| MISC patterns | [NODE_ID] |

If the Figma MCP connector is not available, skip live comparison and rely on the confirmed conventions (Step 3a) and `style-guide-rules.md` instead. Say so explicitly in the output rather than guessing at what the live pattern would show.

## Step 3: Check Against Your Tone and Style Standards
Check the content against the rules in `style-guide-rules.md`. These standards are yours to define. Cover the categories that matter to your team. Common ones include:

- **Voice**: [Describe your brand voice.]
- **Person and tense**: [For example, second person and present tense.]
- **Sentence length**: [Your maximum.]
- **Casing**: [Your rules for buttons, headings, labels, and body text.]
- **Contractions**: [Where they are and aren't allowed.]
- **Buttons**: [Your wording rules.]
- **Errors**: [Your rules for error messages.]
- **Inclusive language**: [Your rules. See `style-guide-rules.md`.]
- **Punctuation**: [Your rules for dashes, colons, ampersands, and so on.]

Modify accordingly with your own standards. Until you do, Claude applies the example rules in `style-guide-rules.md`.

## Step 3a: Confirmed Conventions — Do Not Flag These
List conventions your team has verified against live UI so Claude doesn't "correct" them. Each entry names the convention and says why it is right. Modify accordingly.

1. **[Convention name]**: [What it looks like in the live UI, and why it should not be flagged.]
2. **[Convention name]**: [Description.]
3. **[Convention name]**: [Description.]

For example, entries might cover a required prefix on banner messages, the exact wording of a required-field indicator, or rendered casing that differs from source casing.

## Step 3b: Verify Before Flagging
- If the "issue" you're about to flag appears verbatim in the live pattern examples, it is the convention. Do not flag it.
- When citing a style guide rule, quote the exact language from `style-guide-rules.md` rather than paraphrasing or inventing new terminology.

## Step 3c: Be Proactive About Unclear Labels
When a label is technically grammatical but jargon-y, unclear, or domain-specific, suggest a plainer alternative instead of only fixing formatting. Modify accordingly with examples from your product. For example:
- `Amt. ($)` → suggest `Amount`.
- `Acct. Mgmt` → spell out `Account Management` on first use.
- `Recurring Charge Description` → consider `Charge Description`.

## Step 4: Output
```
**Content Design Review**

Component type: [identified type]
Figma reference: [page name + matching example, or "not available — reviewed against style-guide-rules.md and confirmed conventions only"]

Overall: [Pass / Needs Revision]

Issues Found:
- [Original]: "..."
  [Issue]: ...
  [Suggestion]: "..."

Pattern match: [Does it align with known patterns? Yes / Partial / No / Not checked — with notes]
```

## Step 5: Report-Writing Rules (when output is a document; examples)
These are examples of one team's preferences. Replace them with your own.

When generating a written report (markdown, .docx, etc.) for a human reviewer:

1. **Plain language only.** Never use developer terms in the body of the report:
   - "text nodes" → "pieces of text" or "text items"
   - "walked the tree" → "went through every screen and component"
   - "deduped" → "collapsed repeats"
   - raw node IDs like `1437:12175` in body copy → refer by name ("the Settings Page section") and put the ID only inside a link
2. **Use Figma terminology where it helps the reader**: section, frame, screen variant, page, component instance, variable.
3. **Never expose raw file keys.** Always render as a labeled link, for example [Content Pattern Examples](https://www.figma.com/design/[YOUR_FILE_KEY]/Content-Pattern-Examples).
4. **Follow your brand-name rules** (for example, never abbreviate the company name in reports).
5. **Don't critique something you then explain away.** If an inconsistency doesn't affect the user-visible product (for example, source casing that renders uniformly), drop the finding or make it an advisory aside, never a flagged issue.
6. **Be concrete about classifications.** Don't label something a "table" because its Figma layer name contains the word. Verify against the rendered screen.
7. **Match the reader's role.** This is for a content strategist or PM, not a developer. Explain technical fallbacks (for example, no live Figma access) in one short sentence of plain English.

## Reference
Full style guide rules are in `style-guide-rules.md`, bundled with this skill. Quote from it directly when citing a rule.

## Setup: If the Figma MCP Connector Isn't Available
This skill still works without it (see Step 2's fallback), but live pattern comparison needs the Figma connector turned on once per Claude.ai account. No API key is required. It uses your own Figma login.

1. In Claude.ai, go to **Settings → Connectors**.
2. Find **Figma** in the list and select it.
3. Click **Connect**, then log in to Figma and approve access when prompted.
4. Make sure the connector is turned on for the chat or project where you'll run this skill.
5. Re-run the skill. It can now pull live examples from your pattern file.

If you don't have permission to add connectors, ask your workspace admin to enable the Figma connector.
