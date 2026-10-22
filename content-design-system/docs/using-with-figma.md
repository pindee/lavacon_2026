# Using this with Figma

## Review plugin

See `plugin/README.md`. The plugin reads the published `rules.json`, so rule changes don't need a republish.

## Figma Make guidelines

`figma-make/guidelines/` holds guidelines written for Figma Make. Start with `overview.md` and keep each file short. Add one file per component or token set as you need them.

To use them:

1. Open your Make file or Make kit.
2. Copy the contents of `figma-make/guidelines/` into its `guidelines` folder.
3. For a kit, select **Update kit** to apply the change.

Make files don't share guidelines automatically, so repeat this when the files change. The agent's sync check lists which kits are stale.

## Library guidelines

Some design tools let you attach guidelines files to a published library (Markdown, plain text, or JSON). Upload the files from `figma-make/guidelines/` or write library-specific ones. Check the current size limit and whether the feature is still in beta.

## Tips

- Guidelines work best when they hold rules the tool can't infer from the library itself.
- Lead with the rules that most change the output: color, spacing, and the words on buttons and messages.
- Pair each rule with a short good and bad example.
