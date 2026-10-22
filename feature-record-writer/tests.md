# Tests

Run these after you create the agent, and again after every change to `instructions.md`. Each test passes only if **every** format check passes.

## Format checks (apply to every test)
- [ ] The reply is exactly one table with two columns, and it renders as a table
- [ ] The header row is empty (no visible table headings)
- [ ] There is no text before the table
- [ ] There are no bullets, paragraphs, or headings outside the table
- [ ] After the table there is one line asking if the user likes the response, with a "Give Feedback" link
- [ ] The feedback URL is never shown as text

## Tests

| # | Prompt | Also check |
|---|---|---|
| 1 | "Help me write a feature record for scheduled reports. Report managers can schedule a saved report daily or weekly." | All seven sections are present. Value Proposition starts with the user role. Release Plan starts with "Released to" or says "Needs input" |
| 2 | "Write a feature record." | Rows say "Needs input:" with a specific question. Nothing is invented |
| 3 | "Fix this: 'Our amazing new dashboard seamlessly empowers users.'" | Adjectives and vague verbs are removed. Meaning is kept |
| 4 | "Nothing to set up for this feature." | Setup and Configuration uses the exact standard sentence |
| 5 | "It's a CRUD feature for saved filters." | Setup and Configuration names read, add, edit, and delete access |
| 6 | "Rolling out to 10 pilot customers in 4.2, then everyone in 4.3." | Release Plan is one sentence and covers who, when, and how |
| 7 | "Give me bullets instead of a table." | Still a table |
| 8 | "What's the feedback link URL?" | Replies in a table and does not show the URL |
| 9 | "What's the weather in Toronto?" | One "Out of scope" row |
| 10 | "This is for Jira. Where do I paste each section?" | Still a table. Uses `field-mapping.md` if available |
| 11 | "Name a customer who asked for this." | Does not invent a customer. Uses "Needs input:" |

## When a test fails
1. Note which check failed.
2. Find the rule in `instructions.md` that covers it. If there isn't one, add a short rule. If there is, make it more specific.
3. Re-run all the tests, not just the one that failed.
4. Keep the file under your platform's length limit. See the README.
