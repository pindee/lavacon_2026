# Contributing

## Changing a rule

1. Open a **Rule change** issue, or go straight to a pull request for a small fix.
2. Edit the file in `standards/` or `terms/`. Don't edit copies.
3. Run:
   ```
   python scripts/sync_standards.py
   python scripts/validate.py
   python scripts/build.py
   ```
4. If the change affects a rule, add a short note in `decisions/`.
5. Update `CHANGELOG.md`, and bump `VERSION` if published files changed.
6. Open a pull request. A code owner reviews it.

## Versioning

`VERSION` follows `major.minor.patch`.

- **Patch:** wording fixes, no change to what is allowed.
- **Minor:** a new rule, term, or check.
- **Major:** a rule that makes previously correct content wrong.

## Reporting a problem

Use the **Feedback** issue template. Please don't include personal or customer information.
