# Agent

`AGENT.md` defines a steward agent. The files in `tasks/` are its recurring jobs.

## Why an agent, and not only scripts

Scripts and CI handle anything that can be built from the files in this repository: the published site, `rules.json`, validation rules, and checks. They can't sign in to design tools, compare a kit's current guidelines with ours, or judge whether a rule is unclear. The agent covers those jobs.

## Ways to run it

Pick one.

1. **A scheduled task in an agent app.** Give the app `AGENT.md` and the task files, connect the tools it needs, and schedule each task weekly.
2. **A scheduled workflow.** `.github/workflows/agent-review.yml` is a starter that runs an AI coding agent against this repo on demand. It ships with a manual trigger only. Add a schedule once it works.
3. **By hand.** Paste a task into a chat with the repository attached.

## Keep a person in charge

The agent opens issues and pull requests. A code owner approves every change to the standards.
