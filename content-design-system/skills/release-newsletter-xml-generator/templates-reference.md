# Release Newsletter Templates (DocBook 5.1 and DITA 1.3)

Each template appears in two formats. Use the one that matches your toolchain, or mirror the same structure in your own schema. If you use Paligo, start from the DocBook version and read `paligo-notes.md` for the changes it needs.

## How to read these templates

- The wording in these templates (for example, "Complete fields as required." and the section names) is example house style. Change it to match your own standards.
- `[Square brackets]` mark content you replace.
- `{{TOKENS}}` such as `{{SITE}}` and `{{ADMIN_AREA}}` stand for terms that may be reusable text in your system (variables, keys, entities). Swap each token for your project's syntax, or for plain text if you don't use reusable terms. See `terms-reference.md`.
- Each file is a complete, standalone topic. There is no wrapper element or import trick.
- Templates show **well-formed** XML. Validate against your own schema before publishing.
- Optional blocks (security permissions, standard role features, mobile app note) are marked with comments. Delete the blocks you don't need.

---

## Template 1 — Product Update ★ use this most often

**Use when:** Standard feature or product area update.

### DocBook 5.1

```xml
<?xml version="1.0" encoding="UTF-8"?>
<section xmlns="http://docbook.org/ns/docbook"
         xmlns:xlink="http://www.w3.org/1999/xlink"
         version="5.1" xml:lang="en">
  <title>[FEATURE NAME — Title Case, specific to what was updated, no punctuation]</title>

  <para>[INTRO SENTENCE 1 — value statement addressing "you". Max 2 sentences total. No marketing language.]</para>

  <para>
    <emphasis role="bold">Navigation Steps</emphasis>
  </para>

  <!-- Single-site path (always include): -->
  <para>Single {{SITE}}: {{ADMIN_AREA}} &gt; [PATH] &gt; [DESTINATION].</para>

  <!-- Multi-site path (include only if the feature is available in multi-site setups): -->
  <para>Multi-{{SITE}}: [PATH] &gt; [DESTINATION].</para>

  <!-- SECURITY PERMISSIONS — include only if new or changed permissions exist. Delete this block if not applicable.
       Use "New Security Permissions" for brand-new permissions, "Updated Security Permissions" for changed permissions. -->
  <para>
    <emphasis role="bold">New Security Permissions</emphasis>
  </para>
  <informaltable>
    <thead>
      <tr>
        <th><para>Module</para></th>
        <th><para>Item</para></th>
        <th><para>Option</para></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><para>[MODULE — use a term token if it is a product name]</para></td>
        <td><para>[ITEM]</para></td>
        <td><para>[OPTION]</para></td>
      </tr>
    </tbody>
  </informaltable>

  <!-- STANDARD ROLE FEATURES — include only if the feature adds access through standard roles. Delete this block if not applicable. -->
  <para>
    <emphasis role="bold">Standard Role Features</emphasis>
  </para>
  <itemizedlist>
    <listitem><para>[Feature Name]</para></listitem>
  </itemizedlist>
  <note><para>For more information, contact your IT System Administrator.</para></note>

  <!-- MOBILE APP ONLY — include only if the feature affects a mobile app. Delete if not applicable. -->
  <para>If your mobile device is not set to automatically install new app updates, you must manually update to the latest app version when it is available in the app store.</para>

  <!-- SCREENSHOTS — add mediaobject blocks in your editor. -->
</section>
```

### DITA 1.3

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd">
<topic id="feature-name">
  <title>[FEATURE NAME — Title Case, specific to what was updated, no punctuation]</title>
  <body>
    <p>[INTRO SENTENCE 1 — value statement addressing "you". Max 2 sentences total. No marketing language.]</p>
    <p><b>Navigation Steps</b></p>
    <!-- Single-site path (always include): -->
    <p>Single {{SITE}}: {{ADMIN_AREA}} &gt; [PATH] &gt; [DESTINATION].</p>
    <!-- Multi-site path (include only if the feature is available in multi-site setups): -->
    <p>Multi-{{SITE}}: [PATH] &gt; [DESTINATION].</p>
    <!-- SECURITY PERMISSIONS — include only if new or changed permissions exist. Delete this block if not applicable. -->
    <p><b>New Security Permissions</b></p>
    <simpletable>
      <sthead>
        <stentry>Module</stentry>
        <stentry>Item</stentry>
        <stentry>Option</stentry>
      </sthead>
      <strow>
        <stentry>[MODULE — use a term token if it is a product name]</stentry>
        <stentry>[ITEM]</stentry>
        <stentry>[OPTION]</stentry>
      </strow>
    </simpletable>
    <!-- STANDARD ROLE FEATURES — include only if the feature adds access through standard roles. Delete this block if not applicable. -->
    <p><b>Standard Role Features</b></p>
    <ul>
      <li>[Feature Name]</li>
    </ul>
    <note type="note">For more information, contact your IT System Administrator.</note>
    <!-- MOBILE APP ONLY — include only if the feature affects a mobile app. Delete if not applicable. -->
    <p>If your mobile device is not set to automatically install new app updates, you must manually update to the latest app version when it is available in the app store.</p>
    <!-- SCREENSHOTS — add image elements in your editor. -->
  </body>
</topic>
```

---

## Filled example — Product Update

**Use when:** What a completed Template 1 looks like.

### DocBook 5.1

```xml
<?xml version="1.0" encoding="UTF-8"?>
<section xmlns="http://docbook.org/ns/docbook"
         xmlns:xlink="http://www.w3.org/1999/xlink"
         version="5.1" xml:lang="en">
  <title>Order Duration Confirmation</title>

  <para>You can now view and confirm the duration type for orders before submitting. This update adds a duration confirmation step to the {{ORDERS}} creation workflow.</para>

  <para>
    <emphasis role="bold">Navigation Steps</emphasis>
  </para>
  <para>Single {{SITE}}: {{PRODUCT_AREA}} &gt; Orders &gt; Create Order.</para>
  <para>Multi-{{SITE}}: Orders &gt; Create Order.</para>
</section>
```

### DITA 1.3

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd">
<topic id="order-duration-confirmation">
  <title>Order Duration Confirmation</title>
  <body>
    <p>You can now view and confirm the duration type for orders before submitting. This update adds a duration confirmation step to the {{ORDERS}} creation workflow.</p>
    <p><b>Navigation Steps</b></p>
    <p>Single {{SITE}}: {{PRODUCT_AREA}} &gt; Orders &gt; Create Order.</p>
    <p>Multi-{{SITE}}: Orders &gt; Create Order.</p>
  </body>
</topic>
```

---

## Template 2 — New Marketplace Solution Offerings

**Use when:** New marketplace integration partner or solution offering.

### DocBook 5.1

```xml
<?xml version="1.0" encoding="UTF-8"?>
<section xmlns="http://docbook.org/ns/docbook"
         xmlns:xlink="http://www.w3.org/1999/xlink"
         version="5.1" xml:lang="en">
  <title>New Marketplace Solution Offerings</title>

  <itemizedlist>
    <listitem>
      <para><emphasis role="bold">[Application Name]</emphasis> - [Application Name] offers [what it does and value statement].</para>
    </listitem>
    <!-- Add more listitem blocks for additional offerings -->
  </itemizedlist>
</section>
```

### DITA 1.3

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd">
<topic id="new-marketplace-solution-offerings">
  <title>New Marketplace Solution Offerings</title>
  <body>
    <ul>
      <li><b>[Application Name]</b> - [Application Name] offers [what it does and value statement].</li>
      <!-- Add more li elements for additional offerings -->
    </ul>
  </body>
</topic>
```

---

## Template 3 — Help Hub Updates

**Use when:** New training content (courses, guides, interactive assistance) added to your help hub.

### DocBook 5.1

```xml
<?xml version="1.0" encoding="UTF-8"?>
<section xmlns="http://docbook.org/ns/docbook"
         xmlns:xlink="http://www.w3.org/1999/xlink"
         version="5.1" xml:lang="en">
  <title>Help Hub Update</title>

  <para>[Product Name] training is now available in the help hub. If you need help during a task or workflow, you can find answers, guidance, and training directly in the area where you are working. Resources are available in the following help hub sections:</para>

  <itemizedlist>
    <!-- Remove items that do not apply -->
    <listitem>
      <para>Support Portal (Search for Answers | Manage Cases)</para>
    </listitem>
    <listitem>
      <para>Guide Me (Interactive Assistance)</para>
    </listitem>
    <listitem>
      <para>Train Me (Courses)</para>
    </listitem>
  </itemizedlist>

  <!-- Add a screenshot in your editor. -->
</section>
```

### DITA 1.3

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd">
<topic id="help-hub-update">
  <title>Help Hub Update</title>
  <body>
    <p>[Product Name] training is now available in the help hub. If you need help during a task or workflow, you can find answers, guidance, and training directly in the area where you are working. Resources are available in the following help hub sections:</p>
    <ul>
      <!-- Remove items that do not apply -->
      <li>Support Portal (Search for Answers | Manage Cases)</li>
      <li>Guide Me (Interactive Assistance)</li>
      <li>Train Me (Courses)</li>
    </ul>
    <!-- Add a screenshot in your editor. -->
  </body>
</topic>
```

---

## Template 4 — System Status Notifications

**Use when:** System status or outage notification subscription.

### DocBook 5.1

```xml
<?xml version="1.0" encoding="UTF-8"?>
<section xmlns="http://docbook.org/ns/docbook"
         xmlns:xlink="http://www.w3.org/1999/xlink"
         version="5.1" xml:lang="en">
  <title>{{PRODUCT_NAME}} System Status Notifications</title>

  <para>You can subscribe to <link xlink:href="https://status.example.com/">[Your Product] System Status</link> to receive outage notifications.</para>
</section>
```

### DITA 1.3

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd">
<topic id="system-status-notifications">
  <title>{{PRODUCT_NAME}} System Status Notifications</title>
  <body>
    <p>You can subscribe to <xref href="https://status.example.com/" format="html" scope="external">[Your Product] System Status</xref> to receive outage notifications.</p>
  </body>
</topic>
```

---
