# Standards

The only place content rules are edited. Everything else in the repository is built from, or copied from, these files.

| File | What it holds |
|---|---|
| `voice-and-tone.md` | Voice pillars and tone guidance |
| `style-guide-rules.md` | The full style guide (an example set; replace it with yours) |
| `checks.json` | Machine-readable checks (sentence length, banned patterns) |
| `components/` | One file per UI component, from `components/_template.md` |

Terms to avoid and prefer live in `../terms/terms.json`.

## Rules for writing standards

- State each rule once, in one file.
- Pair every rule with a short good and bad example.
- Keep files short. Several small files are easier to maintain and easier for AI tools to use than one long file.
- After you change a file here, run `python scripts/sync_standards.py` and then `python scripts/validate.py`.
