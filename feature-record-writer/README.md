# Feature Record Writer (agent)

A standalone agent that helps people write the text fields of a feature record in any tracker, such as Aha! or Jira. It always replies in a two-column table with the section in column 1 and the content in column 2, so the text is easy to copy into your tracker.

The rules in `instructions.md` are examples of one team's standards. Replace them with your own. Until you do, the agent applies them as written.

## Agent or skill?

A skill is loaded on demand inside a Claude conversation. An agent is a dedicated assistant with its own fixed instructions, so people open it and use it without setting anything up. This one is an agent because it has one job, a strict reply format, and a wide audience, including people who use other platforms.

## Files

| File | What it is | Where it goes |
|---|---|---|
| `instructions.md` | The agent's instructions | Paste into the agent's instructions field |
| `profile.md` | Name, description, conversation starters, scope | Use when you create the agent |
| `examples.md` | Good examples for each section | Add as knowledge (optional) |
| `field-mapping.md` | Where each section goes in common trackers | Add as knowledge (optional) |
| `tests.md` | Test prompts and pass checks | Use to test the agent |

## Set it up

### In Microsoft 365 Copilot or Copilot Studio
1. Create a new agent and use the name and description from `profile.md`.
2. Paste `instructions.md` into the instructions field. The documented limit for declarative agent instructions is 8,000 characters. This file is well under that. Check the current limit for your plan.
3. Add the conversation starters from `profile.md`.
4. Upload `examples.md` and `field-mapping.md` as knowledge, if you want.
5. Don't move the instructions into a document and point the agent at it. Keep them in the instructions field.

### In Claude
1. Create a project and paste `instructions.md` into the project instructions.
2. Add `examples.md` and `field-mapping.md` as project knowledge.
3. Share the project with your team.

### In any other platform
Use `instructions.md` as the system prompt, and add the other files as reference material if the platform supports it.

## Make it yours

1. Replace `[YOUR_FEEDBACK_FORM_URL]` in `instructions.md` with your feedback form, or delete the feedback line.
2. Edit the section list and the rules for each section to match your standards and your tracker's fields.
3. Replace `examples.md` with examples from your own product.
4. Fill in the last column of `field-mapping.md`.
5. Run the tests in `tests.md`.

Keep the instructions short. Longer instructions are easier to hit a length limit with, and agents tend to follow short, specific instructions more reliably.

## Optional: connect your tracker

If your platform can connect to your tracker, give the agent **read-only** access so it can open a record you name and improve it. The instructions tell the agent never to change a record unless the user asks and confirms. Leave write access off unless you have a reason.

## Notes

- The "no table headings" rule is met with an empty header row, because a Markdown table needs a header row to render.
- If your platform doesn't render Markdown tables, the reply will look like text with pipes. Check how your platform displays it before you roll the agent out.
- Review all generated text before it goes into a record. The agent speeds up drafting and doesn't replace review.
