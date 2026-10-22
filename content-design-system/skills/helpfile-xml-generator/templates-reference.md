# Help File Templates (DocBook 5.1 and DITA 1.3)

Each template appears in two formats. Use the one that matches your toolchain, or mirror the same structure in your own schema. If you use Paligo, start from the DocBook version and read `paligo-notes.md` for the changes it needs.

## How to read these templates

- The wording in these templates (for example, "Complete fields as required." and the section names) is example house style. Change it to match your own standards.
- `[Square brackets]` mark content you replace.
- `{{TOKENS}}` such as `{{SITE}}` and `{{ADMIN_AREA}}` stand for terms that may be reusable text in your system (variables, keys, entities). Swap each token for your project's syntax, or for plain text if you don't use reusable terms. See `terms-reference.md`.
- Each file is a complete, standalone topic. There is no wrapper element or import trick.
- Templates show **well-formed** XML. Validate against your own schema before publishing.

## Template selector

| Template | Use when |
|---|---|
| 1. Config Small | Single setup procedure, no options section |
| 2. Config Big | Single setup procedure plus a Configuration Options section |
| 3. Config Multi-Procedure | Multiple ordered setup procedures plus Configuration Options |
| 4. End-User Small | Single end-user procedure |
| 5. End-User Multi-Procedure | Multiple ordered end-user procedures plus an Options section |
| 6. Dashboard Pane | Dashboard pane documentation |

If your product has more than one area (for example, an admin area and an operations area), the only difference between template variants is the first term in the navigation path. Swap the token.

## Reusable headings

The templates write section headings ("Steps", "Configuration Options", "Options") directly. In DocBook they are `<bridgehead>` elements. If your system reuses headings from a shared component, replace each one with your include syntax. In Paligo, see `paligo-notes.md`.

---

## Template 1 — Config Small

**Use when:** Single setup procedure. No options section.

### DocBook 5.1

```xml
<?xml version="1.0" encoding="UTF-8"?>
<section xmlns="http://docbook.org/ns/docbook"
         xmlns:xlink="http://www.w3.org/1999/xlink"
         version="5.1" xml:lang="en">
  <title>Configuring [Module Name]</title>
  <para>1–2 sentence introduction. Describe what this configuration does and why an admin would do it.</para>
  <!-- Optional: <note><para>Note text.</para></note> -->
  <!-- Optional: <warning><para>Warning text. Use only for data loss or irreversible actions.</para></warning> -->
  <bridgehead renderas="sect2">Steps</bridgehead>
  <procedure>
    <step>
      <para>Do one of the following:</para>
      <itemizedlist>
        <listitem>
          <para>Single {{SITE}}: {{ADMIN_AREA}} &gt; Setup &gt; [Path to feature].</para>
        </listitem>
        <listitem>
          <para>Multi-{{SITE}}: Standards &gt; [Admin Module] &gt; [Path to feature].</para>
        </listitem>
      </itemizedlist>
    </step>
    <step>
      <para>Select <guilabel>New</guilabel>.</para>
    </step>
    <step>
      <para>Complete fields as required.</para>
    </step>
    <step>
      <para>Select <guilabel>Save</guilabel>.</para>
    </step>
  </procedure>
</section>
```

### DITA 1.3

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE task PUBLIC "-//OASIS//DTD DITA Task//EN" "task.dtd">
<task id="configuring-module-name">
  <title>Configuring [Module Name]</title>
  <shortdesc>1–2 sentence introduction. Describe what this configuration does and why an admin would do it.</shortdesc>
  <taskbody>
    <!-- Optional: <note type="note">Note text.</note> -->
    <!-- Optional: <note type="warning">Warning text. Use only for data loss or irreversible actions.</note> -->
    <steps>
      <step>
        <cmd>Do one of the following:</cmd>
        <choices>
          <choice>Single {{SITE}}: {{ADMIN_AREA}} &gt; Setup &gt; [Path to feature].</choice>
          <choice>Multi-{{SITE}}: Standards &gt; [Admin Module] &gt; [Path to feature].</choice>
        </choices>
      </step>
      <step>
        <cmd>Select <uicontrol>New</uicontrol>.</cmd>
      </step>
      <step>
        <cmd>Complete fields as required.</cmd>
      </step>
      <step>
        <cmd>Select <uicontrol>Save</uicontrol>.</cmd>
      </step>
    </steps>
  </taskbody>
</task>
```

---

## Template 2 — Config Big

**Use when:** Single setup procedure plus a Configuration Options section.

### DocBook 5.1

```xml
<?xml version="1.0" encoding="UTF-8"?>
<section xmlns="http://docbook.org/ns/docbook"
         xmlns:xlink="http://www.w3.org/1999/xlink"
         version="5.1" xml:lang="en">
  <title>Configuring [Module Name]</title>
  <para>1–2 sentence introduction.</para>
    <!-- Optional: <note><para>Note text.</para></note> -->
    <!-- Optional: <warning><para>Warning text. Use only for data loss or irreversible actions.</para></warning> -->
    <bridgehead renderas="sect2">Steps</bridgehead>
    <procedure>
      <step>
        <para>Do one of the following:</para>
        <itemizedlist>
          <listitem>
            <para>Single {{SITE}}: {{ADMIN_AREA}} &gt; Setup &gt; [Path to feature].</para>
          </listitem>
          <listitem>
            <para>Multi-{{SITE}}: Standards &gt; [Admin Module] &gt; [Path to feature].</para>
          </listitem>
        </itemizedlist>
      </step>
      <step>
        <para>Select <guilabel>New</guilabel>.</para>
      </step>
      <step>
        <para>Complete fields as required.</para>
      </step>
      <step>
        <para>Select <guilabel>Save</guilabel>.</para>
      </step>
    </procedure>
    <bridgehead renderas="sect2">Configuration Options</bridgehead>
    <para>Below is a list of the configuration options available to you.</para>
    <itemizedlist>
      <listitem>
        <para><emphasis role="bold">Option Name</emphasis> — Select option. (intuitive: short description only)</para>
      </listitem>
      <listitem>
        <para><emphasis role="bold">Option Name</emphasis> — Type information. (intuitive text field: short description)</para>
      </listitem>
      <listitem>
        <para><emphasis role="bold">Option Name</emphasis> — Select or type. Describe the impact when not intuitive. Add sub-bullets for options that need explanation (list customer-facing implications first).</para>
        <itemizedlist>
          <listitem>
            <para><emphasis role="bold">Sub-option 1</emphasis> — Explain what this option does.</para>
          </listitem>
          <listitem>
            <para><emphasis role="bold">Sub-option 2</emphasis> — Explain what this option does.</para>
          </listitem>
        </itemizedlist>
      </listitem>
    </itemizedlist>
</section>
```

### DITA 1.3

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE task PUBLIC "-//OASIS//DTD DITA Task//EN" "task.dtd">
<task id="configuring-module-name">
  <title>Configuring [Module Name]</title>
  <shortdesc>1–2 sentence introduction.</shortdesc>
  <taskbody>
    <!-- Optional: <note type="note">Note text.</note> -->
    <!-- Optional: <note type="warning">Warning text. Use only for data loss or irreversible actions.</note> -->
    <steps>
      <step>
        <cmd>Do one of the following:</cmd>
        <choices>
          <choice>Single {{SITE}}: {{ADMIN_AREA}} &gt; Setup &gt; [Path to feature].</choice>
          <choice>Multi-{{SITE}}: Standards &gt; [Admin Module] &gt; [Path to feature].</choice>
        </choices>
      </step>
      <step>
        <cmd>Select <uicontrol>New</uicontrol>.</cmd>
      </step>
      <step>
        <cmd>Complete fields as required.</cmd>
      </step>
      <step>
        <cmd>Select <uicontrol>Save</uicontrol>.</cmd>
      </step>
    </steps>
    <postreq>
      <p><b>Configuration Options</b></p>
      <p>Below is a list of the configuration options available to you.</p>
      <ul>
          <li><b>Option Name</b> — Select option. (intuitive: short description only)</li>
          <li><b>Option Name</b> — Type information. (intuitive text field: short description)</li>
          <li><b>Option Name</b> — Select or type. Describe the impact when not intuitive. Add sub-bullets for options that need explanation (list customer-facing implications first).
            <ul>
              <li><b>Sub-option 1</b> — Explain what this option does.</li>
              <li><b>Sub-option 2</b> — Explain what this option does.</li>
            </ul>
          </li>
        </ul>
    </postreq>
  </taskbody>
</task>
```

---

## Template 3 — Config Multi-Procedure

**Use when:** Multiple setup procedures that must be done in order, plus a Configuration Options section. Each procedure gets a bold label as its first child. If the procedures can be done in any order, wrap each one in its own `<section>` (DocBook) or keep each as its own task topic (DITA) so readers can jump between them.

### DocBook 5.1

```xml
<?xml version="1.0" encoding="UTF-8"?>
<section xmlns="http://docbook.org/ns/docbook"
         xmlns:xlink="http://www.w3.org/1999/xlink"
         version="5.1" xml:lang="en">
  <title>Configuring [Module Name]</title>
  <para>1–2 sentence introduction. Note if the first procedure must be completed before the next one.</para>
    <!-- Optional: <note><para>Note text.</para></note> -->
    <!-- Optional: <warning><para>Warning text. Use only for data loss or irreversible actions.</para></warning> -->
    <bridgehead renderas="sect2">Steps</bridgehead>
    <!-- PROCEDURE 1 -->
    <procedure>
      <para><emphasis role="bold">To [first task name]</emphasis></para>
      <step>
        <para>Do one of the following:</para>
        <itemizedlist>
          <listitem>
            <para>Single {{SITE}}: {{ADMIN_AREA}} &gt; Setup &gt; [Path].</para>
          </listitem>
          <listitem>
            <para>Multi-{{SITE}}: Standards &gt; [Admin Module] &gt; [Path].</para>
          </listitem>
        </itemizedlist>
      </step>
      <step>
        <para>Select <guilabel>New</guilabel>.</para>
      </step>
      <step>
        <para>Complete fields as required.</para>
      </step>
      <step>
        <para>Select <guilabel>Save</guilabel>.</para>
      </step>
    </procedure>
    <!-- PROCEDURE 2 — repeat for each additional procedure -->
    <procedure>
      <para><emphasis role="bold">To [second task name]</emphasis></para>
      <step>
        <para>Do one of the following:</para>
        <itemizedlist>
          <listitem>
            <para>Single {{SITE}}: {{ADMIN_AREA}} &gt; Setup &gt; [Path].</para>
          </listitem>
          <listitem>
            <para>Multi-{{SITE}}: Standards &gt; [Admin Module] &gt; [Path].</para>
          </listitem>
        </itemizedlist>
      </step>
      <step>
        <para>Select <guilabel>New</guilabel>.</para>
      </step>
      <step>
        <para>Complete fields as required.</para>
      </step>
      <step>
        <para>Select <guilabel>Save</guilabel>.</para>
      </step>
    </procedure>
    <bridgehead renderas="sect2">Configuration Options</bridgehead>
    <para>Below is a list of the configuration options available to you.</para>
    <itemizedlist>
      <listitem>
        <para><emphasis role="bold">Option Name</emphasis> — Select option. (intuitive: short description only)</para>
      </listitem>
      <listitem>
        <para><emphasis role="bold">Option Name</emphasis> — Type information. (intuitive text field: short description)</para>
      </listitem>
      <listitem>
        <para><emphasis role="bold">Option Name</emphasis> — Select or type. Describe the impact when not intuitive. Add sub-bullets for options that need explanation (list customer-facing implications first).</para>
        <itemizedlist>
          <listitem>
            <para><emphasis role="bold">Sub-option 1</emphasis> — Explain what this option does.</para>
          </listitem>
          <listitem>
            <para><emphasis role="bold">Sub-option 2</emphasis> — Explain what this option does.</para>
          </listitem>
        </itemizedlist>
      </listitem>
    </itemizedlist>
</section>
```

### DITA 1.3

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE task PUBLIC "-//OASIS//DTD DITA Task//EN" "task.dtd">
<task id="configuring-module-name">
  <title>Configuring [Module Name]</title>
  <shortdesc>1–2 sentence introduction.</shortdesc>
  <taskbody>
    <context>
      <p>Optional context. Note if the procedures must be done in order. Each procedure below is its own task topic.</p>
    </context>
  </taskbody>
  <!-- PROCEDURE 1 — repeat for each additional procedure -->
  <task id="procedure-1">
    <title>To [first task name]</title>
    <taskbody>
      <steps>
        <step>
          <cmd>Do one of the following:</cmd>
          <choices>
            <choice>Single {{SITE}}: {{ADMIN_AREA}} &gt; Setup &gt; [Path].</choice>
            <choice>Multi-{{SITE}}: Standards &gt; [Admin Module] &gt; [Path].</choice>
          </choices>
        </step>
        <step>
          <cmd>Select <uicontrol>New</uicontrol>.</cmd>
        </step>
        <step>
          <cmd>Complete fields as required.</cmd>
        </step>
        <step>
          <cmd>Select <uicontrol>Save</uicontrol>.</cmd>
        </step>
      </steps>
    </taskbody>
  </task>
  <!-- PROCEDURE 2 — repeat for each additional procedure -->
  <task id="procedure-2">
    <title>To [second task name]</title>
    <taskbody>
      <steps>
        <step>
          <cmd>Do one of the following:</cmd>
          <choices>
            <choice>Single {{SITE}}: {{ADMIN_AREA}} &gt; Setup &gt; [Path].</choice>
            <choice>Multi-{{SITE}}: Standards &gt; [Admin Module] &gt; [Path].</choice>
          </choices>
        </step>
        <step>
          <cmd>Select <uicontrol>New</uicontrol>.</cmd>
        </step>
        <step>
          <cmd>Complete fields as required.</cmd>
        </step>
        <step>
          <cmd>Select <uicontrol>Save</uicontrol>.</cmd>
        </step>
      </steps>
    </taskbody>
  </task>
  <reference id="options">
    <title>Configuration Options</title>
    <refbody>
      <section>
        <p>Below is a list of the configuration options available to you.</p>
        <ul>
          <li><b>Option Name</b> — Select option. (intuitive: short description only)</li>
          <li><b>Option Name</b> — Type information. (intuitive text field: short description)</li>
          <li><b>Option Name</b> — Select or type. Describe the impact when not intuitive. Add sub-bullets for options that need explanation (list customer-facing implications first).
            <ul>
              <li><b>Sub-option 1</b> — Explain what this option does.</li>
              <li><b>Sub-option 2</b> — Explain what this option does.</li>
            </ul>
          </li>
        </ul>
      </section>
    </refbody>
  </reference>
</task>
```

---

## Template 4 — End-User Small

**Use when:** Single end-user procedure. The title is a gerund action phrase ("Adding a Payment", "Reviewing Charges"). No options section. Navigation starts at the admin area with no Setup sub-path. For other product areas, swap `{{ADMIN_AREA}}` for the matching term token.

### DocBook 5.1

```xml
<?xml version="1.0" encoding="UTF-8"?>
<section xmlns="http://docbook.org/ns/docbook"
         xmlns:xlink="http://www.w3.org/1999/xlink"
         version="5.1" xml:lang="en">
  <title>Adding [Item]</title>
  <para>1–2 sentence introduction.</para>
  <!-- Optional: <note><para>Note text.</para></note> -->
  <!-- Optional: <warning><para>Warning text. Use only for data loss or irreversible actions.</para></warning> -->
  <bridgehead renderas="sect2">Steps</bridgehead>
  <procedure>
    <step>
      <para>{{ADMIN_AREA}} &gt; [Path to feature].</para>
    </step>
    <step>
      <para>Select <guilabel>New</guilabel>.</para>
    </step>
    <step>
      <para>Complete fields as required.</para>
    </step>
    <step>
      <para>Select <guilabel>Save</guilabel>.</para>
    </step>
  </procedure>
</section>
```

### DITA 1.3

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE task PUBLIC "-//OASIS//DTD DITA Task//EN" "task.dtd">
<task id="adding-item">
  <title>Adding [Item]</title>
  <shortdesc>1–2 sentence introduction.</shortdesc>
  <taskbody>
    <!-- Optional: <note type="note">Note text.</note> -->
    <!-- Optional: <note type="warning">Warning text. Use only for data loss or irreversible actions.</note> -->
    <steps>
      <step>
        <cmd>{{ADMIN_AREA}} &gt; [Path to feature].</cmd>
      </step>
      <step>
        <cmd>Select <uicontrol>New</uicontrol>.</cmd>
      </step>
      <step>
        <cmd>Complete fields as required.</cmd>
      </step>
      <step>
        <cmd>Select <uicontrol>Save</uicontrol>.</cmd>
      </step>
    </steps>
  </taskbody>
</task>
```

---

## Template 5 — End-User Multi-Procedure

**Use when:** Multiple end-user procedures that must be done in order, ending with an Options section that lists field descriptions. Use "To [task]" as the label for each procedure.

### DocBook 5.1

```xml
<?xml version="1.0" encoding="UTF-8"?>
<section xmlns="http://docbook.org/ns/docbook"
         xmlns:xlink="http://www.w3.org/1999/xlink"
         version="5.1" xml:lang="en">
  <title>Adding/Completing [Things]</title>
  <para>1–2 sentence introduction. Note if the first procedure must be completed before the next.</para>
    <!-- Optional: <note><para>Note text.</para></note> -->
    <!-- Optional: <warning><para>Warning text. Use only for data loss or irreversible actions.</para></warning> -->
    <bridgehead renderas="sect2">Steps</bridgehead>
    <!-- PROCEDURE 1 -->
    <procedure>
      <para><emphasis role="bold">To [first task name]</emphasis></para>
      <step>
        <para>{{ADMIN_AREA}} &gt; [Path to feature].</para>
      </step>
      <step>
        <para>Select <guilabel>New</guilabel>.</para>
      </step>
      <step>
        <para>Complete fields as required.</para>
      </step>
      <step>
        <para>Select <guilabel>Save</guilabel>.</para>
      </step>
    </procedure>
    <!-- PROCEDURE 2 — repeat for each additional procedure -->
    <procedure>
      <para><emphasis role="bold">To [second task name]</emphasis></para>
      <step>
        <para>{{ADMIN_AREA}} &gt; [Path to feature].</para>
      </step>
      <step>
        <para>Select <guilabel>New</guilabel>.</para>
      </step>
      <step>
        <para>Complete fields as required.</para>
      </step>
      <step>
        <para>Select <guilabel>Save</guilabel>.</para>
      </step>
    </procedure>
    <bridgehead renderas="sect2">Options</bridgehead>
    <para>Below is a list of the options available to you.</para>
    <itemizedlist>
      <listitem>
        <para><emphasis role="bold">Field Name</emphasis> — Select option. (intuitive: short description)</para>
      </listitem>
      <listitem>
        <para><emphasis role="bold">Field Name</emphasis> — Type information. (intuitive field: short description)</para>
      </listitem>
      <listitem>
        <para><emphasis role="bold">Field Name</emphasis> — Select or type. Describe impact when not intuitive. List customer-facing implications first.</para>
        <itemizedlist>
          <listitem>
            <para><emphasis role="bold">Option 1</emphasis> — Explain what this option does.</para>
          </listitem>
          <listitem>
            <para><emphasis role="bold">Option 2</emphasis> — Explain what this option does.</para>
          </listitem>
        </itemizedlist>
      </listitem>
    </itemizedlist>
</section>
```

### DITA 1.3

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE task PUBLIC "-//OASIS//DTD DITA Task//EN" "task.dtd">
<task id="adding-completing-things">
  <title>Adding/Completing [Things]</title>
  <shortdesc>1–2 sentence introduction.</shortdesc>
  <taskbody>
    <context>
      <p>Optional context. Note if the procedures must be done in order. Each procedure below is its own task topic.</p>
    </context>
  </taskbody>
  <!-- PROCEDURE 1 — repeat for each additional procedure -->
  <task id="procedure-1">
    <title>To [first task name]</title>
    <taskbody>
      <steps>
        <step>
          <cmd>{{ADMIN_AREA}} &gt; [Path to feature].</cmd>
        </step>
        <step>
          <cmd>Select <uicontrol>New</uicontrol>.</cmd>
        </step>
        <step>
          <cmd>Complete fields as required.</cmd>
        </step>
        <step>
          <cmd>Select <uicontrol>Save</uicontrol>.</cmd>
        </step>
      </steps>
    </taskbody>
  </task>
  <!-- PROCEDURE 2 — repeat for each additional procedure -->
  <task id="procedure-2">
    <title>To [second task name]</title>
    <taskbody>
      <steps>
        <step>
          <cmd>{{ADMIN_AREA}} &gt; [Path to feature].</cmd>
        </step>
        <step>
          <cmd>Select <uicontrol>New</uicontrol>.</cmd>
        </step>
        <step>
          <cmd>Complete fields as required.</cmd>
        </step>
        <step>
          <cmd>Select <uicontrol>Save</uicontrol>.</cmd>
        </step>
      </steps>
    </taskbody>
  </task>
  <reference id="options">
    <title>Options</title>
    <refbody>
      <section>
        <p>Below is a list of the options available to you.</p>
        <ul>
          <li><b>Field Name</b> — Select option. (intuitive: short description)</li>
          <li><b>Field Name</b> — Type information. (intuitive field: short description)</li>
          <li><b>Field Name</b> — Select or type. Describe impact when not intuitive. List customer-facing implications first.
            <ul>
              <li><b>Option 1</b> — Explain what this option does.</li>
              <li><b>Option 2</b> — Explain what this option does.</li>
            </ul>
          </li>
        </ul>
      </section>
    </refbody>
  </reference>
</task>
```

---

## Template 6 — Dashboard Pane

**Use when:** Documenting a dashboard pane: what it shows, how to open it, and how to interact with it.

### DocBook 5.1

```xml
<?xml version="1.0" encoding="UTF-8"?>
<section xmlns="http://docbook.org/ns/docbook"
         xmlns:xlink="http://www.w3.org/1999/xlink"
         version="5.1" xml:lang="en">
  <title>[Name] Dashboard Pane</title>
  <para>1–3 paragraphs describing what the dashboard pane shows and when to use it. Include an example if helpful. Note anything unintuitive (for example, if the pane only shows data from a specific date type).</para>
  <!-- Optional: <note><para>Note text.</para></note> -->
  <!-- Optional: <warning><para>Warning text. Use only for data loss or irreversible actions.</para></warning> -->
  <bridgehead renderas="sect2">Steps</bridgehead>
  <procedure>
    <step>
      <para>Do one of the following:</para>
      <itemizedlist>
        <listitem>
          <para>{{ADMIN_AREA}} &gt; Dashboard &gt; [Pane Name].</para>
        </listitem>
        <listitem>
          <para>Home &gt; {{ADMIN_AREA}} Dashboard &gt; [Pane Name].</para>
        </listitem>
      </itemizedlist>
    </step>
    <step>
      <para>Complete fields as required.</para>
    </step>
    <step>
      <para>Select <guilabel>Save</guilabel>.</para>
    </step>
  </procedure>
</section>
```

### DITA 1.3

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE task PUBLIC "-//OASIS//DTD DITA Task//EN" "task.dtd">
<task id="name-dashboard-pane">
  <title>[Name] Dashboard Pane</title>
  <shortdesc>1–3 sentences describing what the dashboard pane shows and when to use it.</shortdesc>
  <taskbody>
    <context>
      <p>Optional extra paragraphs and an example. Note anything unintuitive (for example, if the pane only shows data from a specific date type).</p>
    </context>
    <steps>
      <step>
        <cmd>Do one of the following:</cmd>
        <choices>
          <choice>{{ADMIN_AREA}} &gt; Dashboard &gt; [Pane Name].</choice>
          <choice>Home &gt; {{ADMIN_AREA}} Dashboard &gt; [Pane Name].</choice>
        </choices>
      </step>
      <step>
        <cmd>Complete fields as required.</cmd>
      </step>
      <step>
        <cmd>Select <uicontrol>Save</uicontrol>.</cmd>
      </step>
    </steps>
  </taskbody>
</task>
```

---

## Screenshots

Add a placeholder in the XML and insert the real image in your editor.

### DocBook

```xml
<!-- SCREENSHOT: Add image here -->
<informalfigure>
  <mediaobject>
    <imageobject>
      <imagedata fileref="ScreenshotFilename.png"/>
    </imageobject>
    <textobject>
      <phrase>[Alt text that describes what the image shows]</phrase>
    </textobject>
  </mediaobject>
</informalfigure>
```

### DITA

```xml
<!-- SCREENSHOT: Add image here -->
<image href="ScreenshotFilename.png" placement="break">
  <alt>[Alt text that describes what the image shows]</alt>
</image>
```
