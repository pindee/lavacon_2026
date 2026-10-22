# 0001. Keep all standards in one repository

- **Date:** [YYYY-MM-DD]
- **Status:** Accepted
- **Decided by:** [Team]

## Context
The same rules were copied by hand into several tools, and the copies drifted apart.

## Decision
All standards are edited in `standards/` and `terms/`. Other tools get their copy from a build or from the agent.

## Why
One place to edit means one place to review. Automation can check that copies match.

## Consequences
Nobody edits rules directly in a design tool. Changes go through a pull request.
