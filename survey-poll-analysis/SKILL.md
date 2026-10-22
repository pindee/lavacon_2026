---
name: "survey-poll-analysis"
description: Use when analyzing survey or poll responses from any tool (CSV or Excel export, pasted data, or a connected survey platform such as Pendo, SurveyMonkey, Typeform, Google Forms, or Qualtrics). Counts closed-question answers, themes open-text answers, and writes a structured markdown report with 5 key insights.
---

# Survey and Poll Analysis

> **Template note:** This skill works with data from any survey tool. It first checks whether your survey tool is connected to Claude (an MCP connector) and pulls responses directly if so. If not, it falls back to a file export (CSV or Excel), which every tool supports. See "Optional: connected sources" below.

## Trigger
Invoked with `/survey-poll-analysis`, or when the user asks to analyze survey, poll, or feedback responses.

---

## Step 1 — Find out where the data lives

**First, check your own tool list** for a connector that looks like a survey, feedback, forms, or analytics tool (for example Pendo, SurveyMonkey, Typeform, Qualtrics, or Google Forms). Don't assume the user only has a file.

Then ask immediately, no preamble. Offer the options as a short list, and name any survey connector you found in your tool list:

> "Where are your survey responses?
> 1. In a survey tool connected to Claude (tell me which tool and paste the survey name, link, or ID)
> 2. In a file: upload a CSV or Excel export
> 3. Somewhere else: paste the responses here"

If the user isn't sure whether their tool is connected:
- If you see a matching connector in your tool list, say so and offer to use it.
- If you don't, say you can't see one for that tool, and suggest exporting the results as CSV. Most survey tools have an export option in their results or reports area.

Accepted inputs:
- **Connected platform:** a survey, form, or guide link, name, or ID (see "Optional: connected sources").
- **File upload** (CSV, XLSX, TSV).
- **Pasted data:** a table, or one response per line.

If a file is mentioned but nothing came through, say so and ask the user to upload it again.

---

## Step 2 — Read the data and identify questions

Say in chat: `Reading responses…`

Treat each column (or each question, if the data is grouped) as one question. Ignore columns that are not answers, such as respondent ID, timestamp, IP address, device, and metadata. Keep any column the user says is a segment (for example, role or plan) for optional comparison.

Classify each question:

| Type | How to recognize it |
|---|---|
| **Multiple choice (single answer)** | A small set of repeated values (usually 10 or fewer distinct answers) |
| **Multi-select** | Values with a delimiter such as `;` or `,` between several options, or one column per option |
| **Rating scale** | Numbers on a short scale, such as 1-5 or 1-7, or labels like "Agree" to "Disagree" |
| **NPS** | Numbers 0-10, usually with a question about recommending |
| **Open text** | Mostly unique, longer free-text answers |

If a question's type is unclear, ask ONE short clarifying question about it. Do not ask about each question separately.

**If there are no usable question columns**, report:

> "I couldn't find any survey questions in this data. Check the file and try again."

Then stop.

Say in chat: `Found N question(s) and N response(s)…`

---

## Step 3 — Count and calculate

Use code to compute all counts and percentages when file or code tools are available. Do not do arithmetic by hand for more than a handful of rows.

For each question:
- **Response count:** the number of respondents who answered that question. Blank answers are non-responses. Don't count them as an answer choice.
- **Percentages:** based on respondents who answered that question, rounded to the nearest whole percent. For multi-select, percentages can add up to more than 100%. Say so.
- **Rating scale:** include the average and the distribution.
- **NPS:** promoters are 9-10, passives are 7-8, detractors are 0-6. NPS = % promoters minus % detractors. Show the three groups and the score.
- **Open text:** read all responses before writing themes.

**If a question has no answers**, note it in the report and continue. Don't stop the whole analysis for one empty question.

**Small samples:** for example, if a question has fewer than 30 responses, add a short note that results are directional. Choose a threshold that fits your data.

---

## Step 4 — Build and display the report

Display the full report in chat using this structure:

```
# Survey Analysis: [Survey Name or File Name]
Source: [file name / tool name] | Analyzed: [YYYY-MM-DD] | Total Responses: [N]

---

## Question 1: [Question Text]
**Type:** Multiple Choice
**Responses:** N

| Answer | Count | % |
|--------|-------|---|
| [Option A] | [N] | [N]% |
| [Option B] | [N] | [N]% |
| [Option C] | [N] | [N]% |

---

## Question 2: [Question Text]
**Type:** NPS
**Responses:** N

| Group | Count | % |
|-------|-------|---|
| Promoters (9-10) | [N] | [N]% |
| Passives (7-8) | [N] | [N]% |
| Detractors (0-6) | [N] | [N]% |

**NPS:** [score]

---

## Question 3: [Question Text]
**Type:** Open Text
**Responses:** N

### Themes
- **[Theme name]** ([N] responses): [brief description of what respondents said]
- **[Theme name]** ([N] responses): [brief description]

> "[Direct quote from a respondent]"

---

## 5 Key Insights
1. [Insight: specific, data-backed, tied to a percentage or pattern]
2. [Insight]
3. [Insight]
4. [Insight]
5. [Insight]
```

### Closed questions (multiple choice, multi-select, rating, NPS)
- Include the response table with count and percentage per answer.
- Do NOT include a Themes block.

### Open-text questions
- Omit the response table.
- Include 2-5 synthesized themes based on response patterns, with a rough count for each.
- Include 1-3 direct representative quotes.
- **Privacy:** remove names, email addresses, phone numbers, and other identifying details from quotes. Replace them with `[removed]`. Do not quote anything that could identify a person.

### 5 Key Insights rules
Five insights is an example. Use however many suit your audience.

The insights section synthesizes across ALL questions. For example, each insight should:
- Be specific and data-backed (reference a percentage, count, or trend).
- Surface one of: a dominant pattern, a surprising result, a tension between questions, or a clear action item.

**For example, avoid vague insights.** "Users had mixed opinions" is not an insight. "52% selected Option A, but 38% of open-text responses expressed frustration with that same feature" is an insight.

If the user provided a segment column, add a comparison where the difference is large enough to matter, and say how many respondents are in each segment.

---

## Step 5 — Save the report

Slugify the survey or file name:
- Lowercase everything
- Replace spaces with hyphens
- Remove all special characters except hyphens
- Example: "Onboarding Survey Q2 2026" → `onboarding-survey-q2-2026`

Save the report as:
```
[YOUR_REPORTS_FOLDER]/[survey-name-slug]-[YYYY-MM-DD].md
```

> **Setup note:** Replace `[YOUR_REPORTS_FOLDER]` with a folder on your machine (for example, `~/Documents/Claude/Survey Reports`). In the Claude app with file tools, save to the outputs folder and share the file instead. Create the folder if it does not exist.

After saving, confirm in chat with the file name and location.

---

## Optional: connected sources

If a survey or analytics tool has a Claude connector (MCP) in this environment, pull responses directly instead of using a file. This is the preferred route when it's available, because it avoids export steps and keeps the data current. The flow is the same: find the survey, list its questions, fetch responses for each question, then continue from Step 3.

Example: **Pendo poll guides.**
- Guide URLs follow the pattern `https://app.pendo.io/guides/{GUIDE_ID}/`. Parse the `{GUIDE_ID}` segment. If parsing fails, ask the user to paste the guide ID.
- Use the Pendo connector to retrieve the guide, then keep only poll steps (multiple choice, NPS, rating scale, open text). Ignore tooltips, lightboxes, banners, and redirects.
- For closed questions, fetch aggregated counts per answer. For open text, fetch the raw responses.
- If the guide is not found, say so with the ID used and stop. If a step has no poll, report "This guide has no poll steps. Nothing to analyze." and stop.
- If a response fetch fails for one step, add `_(Response data unavailable for this question — fetch failed.)_` in the report and continue.

Other tools: if a connector exists, use the same pattern. If not, ask the user to export the responses from the tool as CSV.

---

## Error reference

| Situation | Action |
|-----------|--------|
| No file or data came through | Ask the user to upload or paste again |
| User's tool has no connector in this environment | Say so and suggest a CSV export |
| No usable question columns | Say so and stop |
| Question type unclear | Ask one short clarifying question |
| A question has no answers | Note it in the report and continue |
| Few responses for a question (for example, fewer than 30) | Add a "directional results" note |
| Connector can't find the survey | Report the ID or link used, then offer the CSV export route |
| Response fetch fails for one question | Note it inline in the report and continue |
