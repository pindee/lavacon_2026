# Terms

`terms.json` lists terms to avoid and what to use instead. It feeds three things:

- the review plugin and the agent (through `dist/rules.json`)
- validation rules for your authoring tool (`dist/terms.sch`, a Schematron file)
- the skills, which can be told to use it for term checks

## Format

```json
{ "avoid": "log in", "use": "sign in", "notes": "Optional context.", "case_sensitive": false }
```

- `avoid` is a regular expression. It's matched as a whole word.
- `use` is the preferred term.
- `notes` is optional.
- `case_sensitive` is optional and defaults to false.

Run `python scripts/validate.py` after editing.
