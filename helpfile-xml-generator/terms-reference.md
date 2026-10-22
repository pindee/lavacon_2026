# Terms Reference (Reusable Text and Variables)

Many documentation teams keep some terms out of the text itself, so one source can serve different customers or markets. Examples: "site" vs "location", "order" vs "prescription", product names, and regional spelling. Different systems call this variables, keys, entities, or snippets.

This file tells Claude which terms in your content are reusable, and what syntax to use for each. **If you don't use reusable terms, skip this file.** Claude will write plain text and keep terms consistent.

---

## 1. Tokens used in the templates

The templates use `{{TOKENS}}` as stand-ins. Replace each token with your syntax (section 2), or with plain text.

| Token | Meaning | Your value (plain text or key/variable name) |
|---|---|---|
| `{{SITE}}` | The "site / location" term, which may differ by customer type | [fill in] |
| `{{ADMIN_AREA}}` | The admin-area navigation label | [fill in] |
| `{{PRODUCT_AREA}}` | Another product-area navigation label | [fill in] |
| `{{PRODUCT_NAME}}` | Your product name | [fill in] |
| `{{ORDERS}}` | A regional term, for example "orders" vs "prescriptions" | [fill in] |

---

## 2. Syntax by format

Pick the row that matches your system.

| System | How a reusable term looks | Notes |
|---|---|---|
| **Plain text (no reusable terms)** | Write the word. | Keep the term consistent across topics. |
| **DocBook (entities)** | `&site;` | Declare the entity in your DTD or internal subset. Not every toolchain supports this. |
| **DocBook (custom markup)** | `<phrase role="term-site"/>` or your own convention | Use whatever your publishing pipeline resolves. |
| **DITA (keys)** | `<ph keyref="site"/>` | Define each key in a key map with `<keydef keys="site">`. |
| **Paligo** | `<phrase xinfo:variable="[ID]" xinfo:varset="[VARSET_ID]"/>` | See `paligo-notes.md`. |
| **Other** | Ask the user for one example and copy its pattern. | |

---

## 3. Your terms table

List every reusable term here. Keep **case and plural variants as separate rows**, because most systems treat `Site`, `site`, and `sites` as different entries.

The rows below are fictional examples. Replace them.

| Term (as it appears) | Meaning | Key / variable / entity | Notes |
|---|---|---|---|
| site | Place where the product is used | `site` | Lowercase singular |
| Site | Same, sentence start | `Site-cap` | Capitalized |
| sites | Plural | `sites` | |
| Admin | Admin area label in navigation | `admin-area` | |
| Order | Regional term (US) | `order` | Prescription in other markets |

Mark a term as **TBD** in the "Key / variable / entity" column when you know it is reusable but don't have its identifier yet. Claude will ask for it instead of guessing.

---

## 4. Rules Claude follows

- If a term is in your table with a confirmed identifier, use the reusable syntax. Never write the plain word.
- If a term is marked **TBD**, don't guess the identifier and don't silently use plain text. Ask the user to confirm it. If they say to proceed, use a clearly marked placeholder such as `<!-- TERM NEEDED: site -->site`.
- Match case and plurality to the exact row.
- This applies to every piece of text in the file: titles, intros, steps, table cells, notes, and navigation paths.
- If a term isn't in your table but looks like it might vary by customer or market, use plain text and mention it in the summary so you can add it later.
