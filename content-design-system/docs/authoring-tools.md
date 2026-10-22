# Using this with authoring tools

## Terms to validation rules

`python scripts/build.py` turns `terms/terms.json` into `dist/terms.sch`, a Schematron file. Import or reference it in any authoring tool that supports Schematron checks.

1. Open `dist/terms.sch` and adjust the `context` on the `rule` element to match the text-bearing elements in your schema.
2. Import the file into your authoring tool, or point your pipeline at it.
3. Re-import after each release. The agent's sync check can flag a stale copy.

## XML generator skills

`skills/helpfile-xml-generator` and `skills/release-newsletter-xml-generator` draft topics in DocBook 5.1, DITA 1.3, Paligo, or a schema you provide. They ask which format you want. Each has a `terms-reference.md` for reusable terms, which you can build from `terms/terms.json`.

Generated XML is checked for well-formedness only. Validate against your own schema in your authoring tool.
