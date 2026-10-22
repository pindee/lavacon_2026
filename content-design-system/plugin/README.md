# Review Plugin (starter)

A small design-tool plugin that checks the text in your selection against the published rules.

**How it stays current:** the plugin loads `rules.json` from your published site each time it runs. When someone merges a change to `standards/` or `terms/`, the pipeline rebuilds and republishes the file. You don't republish the plugin.

## Set up

1. In `ui.html`, set `RULES_URL` to your published `rules.json`.
2. In `manifest.json`, set `allowedDomains` to the same site, and set `id` to the ID your design tool assigns.
3. Load the plugin as a development plugin to try it, then publish it to your organization.

## What it checks

The starter checks three things, all from `rules.json`: terms to avoid, banned patterns, and sentence length. Extend `checkText` in `ui.html` for more.

## Notes

- This is a starter and hasn't been tested in a live design file. Check it before you rely on it.
- The first publish still needs a person. After that, rule changes need no republish, as long as the rules file stays in the same place.
