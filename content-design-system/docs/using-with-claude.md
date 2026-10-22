# Using this with Claude

## Skills

The `skills/` folder holds AI skills. Each is a folder with a `SKILL.md`.

- **In the app:** zip a single skill folder (with `SKILL.md` at its top level) and add it as a custom skill in your settings.
- **In a coding agent:** copy the skill folders into the project's skills directory, for example `.claude/skills/`.

When `standards/style-guide-rules.md` changes, run `python scripts/sync_standards.py` so the content review skill gets the new copy. CI fails if the copy is out of date.

## AI design system

`design-system/README.md` is the source for your design system's description. If you keep a design system inside an AI design tool, treat that copy as an output of this repository.

- Keep the readme, tokens, and component notes in the repository, and update the tool from them.
- Some tools don't let you edit a design system directly on its page. In that case, ask the tool to make the change, and paste the exact text from the repository.
- Standalone design tools are changing. Check the current help documentation, including any migration deadlines, before you build a workflow around one.
- Chats and comments in design tools may not survive a migration. Record decisions in `decisions/`.

## The agent

See `agent/README.md`. Connect only the tools the agent needs, and keep a person approving every change.
