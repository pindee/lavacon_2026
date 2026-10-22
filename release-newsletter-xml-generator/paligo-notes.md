# Paligo Notes (Optional)

Read this file only if you publish through Paligo. Everything else in this skill works with plain DocBook or DITA. Paligo accepts DocBook with some extra conventions, listed here.

Replace every `[PLACEHOLDER]` with a value from your own Paligo instance.

---

## 1. Use DocBook 5.0 and the Paligo namespace

Start from the DocBook template. Change the root declaration to:

```xml
<section xmlns="http://docbook.org/ns/docbook"
         xmlns:xinfo="http://ns.expertinfo.se/cms/xmlns/1.0"
         xmlns:xi="http://www.w3.org/2001/XInclude"
         xmlns:xlink="http://www.w3.org/1999/xlink"
         version="5.0" xml:lang="en">
```

Don't add `xinfo:resource-id` or other `xinfo:resource-*` attributes to new content. Paligo generates them on import.

## 2. Import wrapper

Uploading XML to Paligo always creates a publication. Without an `<article>` wrapper, the publication is created with **no topics inside it**. Wrap the `<section>` like this:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<article xmlns="http://docbook.org/ns/docbook"
         xmlns:xinfo="http://ns.expertinfo.se/cms/xmlns/1.0"
         xmlns:xi="http://www.w3.org/2001/XInclude"
         xmlns:xlink="http://www.w3.org/1999/xlink"
         version="5.0" xml:lang="en">

  <title>PUBLICATION IS EMPTY FOR IMPORTING ONLY - REVIEW AND MOVE TOPIC AND DELETE PUBLICATION</title>

  <section>
    <!-- your topic content here -->
  </section>

</article>
```

Import steps:
1. Save the file as `Topic_Title_With_Underscores.xml` (zip it if you like).
2. In Paligo, go to **Create** → **Import content** and choose **DocBook**.
3. Select the file and click **Import**. Paligo creates the placeholder publication and a topic inside it.
4. Right-click the topic, choose **Move**, and move it to the correct folder.
5. Delete the placeholder publication.
6. Open the topic in the Paligo editor to add screenshots.

## 3. Variables

Replace each `{{TOKEN}}` with a variable phrase:

```xml
<phrase xinfo:variable="[VARIABLE_ID]" xinfo:varset="[VARSET_ID]"/>
```

When the variable is a UI element the user must click, wrap it:

```xml
<guilabel><phrase xinfo:variable="[VARIABLE_ID]" xinfo:varset="[VARSET_ID]"/></guilabel>
```

Case and plurality are separate variables in Paligo (`Site`, `site`, `sites`), so match the exact title.

**Finding variable IDs:**
- **REST API:** `GET /api/v2/variables/` (add `?variable_set_id=[ID]` to filter by set). Save the output and copy rows into `terms-reference.md`.
- **Paligo UI:** **Settings** → **Variables**, open a variable set, and note each ID. The ID is also visible through **Global Replace Text with a Variable**.

If a variable's ID isn't confirmed, don't guess. Ask for it.

## 4. Tables

Use HTML-style tables (`<thead>`, `<tbody>`, `<tr>`, `<th>`, `<td>`), as in the templates. Don't use CALS `<tgroup>` markup. Omit table captions.
