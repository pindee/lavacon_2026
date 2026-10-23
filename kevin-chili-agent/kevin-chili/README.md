# Kevin's Chili Agent (teaching example)

A made-up agent for a made-up job: planning the office chili. **It can't cook, and that's the point.** The agent is built the way a real agent should be built, with a clear purpose, defined inputs, numbered steps, handoffs to people, guardrails, a fixed output format, failure handling, and tests. Swap chili for your own process and the design stays the same.

An agent is also far less likely than a person to spill the pot in the office. It plans a transport step.

## Start here: the Kevin Chili Test

Before you build an agent, ask whether the process should be an agent or a skill, or whether it needs automation at all. [`kevin-chili-test.md`](kevin-chili-test.md) has the four-question test and a worksheet.

## Files

| File | What it is |
|---|---|
| `kevin-chili-test.md` | The four-question test, red flags, and an agent-or-skill decision list |
| `instructions.md` | The agent's instructions. Paste into any agent platform |
| `recipe.md` | The agent's only knowledge source: a fictional recipe with four signature steps |
| `profile.md` | Name, description, conversation starters, and scope |
| `examples.md` | A full example reply |
| `tests.md` | Test prompts and pass checks |

## What makes it well built

| Part of a good agent | Where to see it in `instructions.md` |
|---|---|
| A single, clear purpose | The opening paragraph |
| Scope: what it does and doesn't do | Scope |
| Inputs, and what to do when they're missing | Inputs |
| Numbered steps in order | Process |
| Handoffs to a person for judgment and risk | Handoffs |
| Rules it always follows, never breaks, or must ask about first | Guardrails |
| A fixed output format | Output format |
| What to do when it can't finish | If you can't finish |
| One trusted source for facts | Process step 1 (`recipe.md`) |
| Tests that check the rules | `tests.md` |

## Try it

1. Paste `instructions.md` into the instructions of an agent, or into a project or chat as a system prompt.
2. Add `recipe.md` as knowledge.
3. Ask: "Plan chili for 20 people on Friday at noon."
4. Then try the prompts in `tests.md`. Ask it to cook, and watch it refuse and offer what it can do.

## Notes

- The recipe is fictional. The details are made up for this example, and it isn't any show's script.
- The food-safety temperatures are general guidance. Check your local rules for real events.
- Keep instructions short. Some platforms limit instruction length, and short, specific instructions are followed more reliably.
