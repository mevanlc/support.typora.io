# A Portable Scholarly Markdown Foundation

Start with the smallest syntax set that expresses the paper clearly. A portable core is easier to review in Git, process with other tools, and preserve when a collaborator does not use Typora.

## Paragraphs and line breaks

Separate paragraphs with a blank line. Do not wrap lines manually merely to control their displayed width; the theme and export format determine that width.

Typora creates a visible soft line break with **Shift+Return**, but many Markdown parsers ignore an ordinary single newline. When a line break is semantically necessary, use two trailing spaces or `<br>` and mark it as export-sensitive. Most technical prose should use separate paragraphs instead.

## Headings are the document skeleton

Use one level-1 heading for the article title, level 2 for major sections, and deeper levels only when needed:

```markdown
# Article title

## Abstract

## 1. Introduction

### 1.1 Motivation

## 2. Methods
```

Do not choose heading levels for visual size. Typora derives its outline, `[toc]`, internal links, and exported PDF bookmarks from heading structure. Skipping from `##` to `####` makes all of those structures harder to understand.

Manual numbers are useful when a venue expects numbered sections, but they become part of the heading text and therefore part of its generated link target. Add them only after deciding who owns numbering: the Markdown source, a stylesheet, or a later publishing system.

## Emphasis and technical identifiers

Use emphasis for meaning rather than decoration:

```markdown
The *a priori* hypothesis predicts a **monotonic** response.
The `sample_id` column is the primary key.
```

- Use `*italics*` for introduced terms, variables in prose when math is unnecessary, and conventional phrases.
- Use `**bold**` sparingly for warnings or conclusions.
- Use backticks for filenames, commands, configuration keys, function names, and literal values.
- Prefer a fenced code block over inline code when a fragment spans multiple lines.

Backticks protect underscores in identifiers such as `raw_sample_count` from being mistaken for emphasis.

## Lists and procedures

Use unordered lists for sets and ordered lists for sequences. A laboratory or computational procedure should state prerequisites and observable outcomes, not merely actions.

```markdown
1. Calibrate the sensor against the 0.5 V reference.
2. Record 100 samples at 1 kHz.
3. Reject the run if drift exceeds 2%.
```

Task lists are a GFM extension supported by Typora. They are excellent for an internal reproducibility checklist but usually inappropriate in a submitted manuscript:

```markdown
- [x] Freeze the analysis environment.
- [ ] Archive the raw data.
- [ ] Record the artifact DOI.
```

## Quotations and callouts

Use blockquotes for quoted or set-apart material:

```markdown
> The calibration applies only within the stated temperature range.
```

GitHub-style alerts are a preference-controlled Typora feature and are not portable. For durable technical warnings, a labeled blockquote is clearer:

```markdown
> **Caution.** Disconnect the supply before changing the probe range.
```

## Escaping literal Markdown

Escape punctuation with a backslash when it would otherwise be parsed:

```markdown
The wildcard is written as \* and the literal variable is price\_usd.
```

For long literal samples of Markdown, surround an inner triple-backtick fence with a four-backtick or tilde fence. This prevents the example from ending its own container.

## A conservative portability profile

For a manuscript that must survive multiple processors:

- Prefer ATX headings (`## Methods`) over decorative heading forms.
- Use explicit `https://` schemes in links.
- Use relative paths for project-owned figures.
- Use GFM tables only for simple tabular data.
- Keep raw HTML, Typora diagrams, `[toc]`, highlights, subscripts, and superscripts optional.
- Put mathematical notation in MathJax/TeX rather than Unicode approximations when the notation is nontrivial.

Typora broadly follows GFM, but no Markdown dialect is universal. Portability is a tested property, not a promise implied by the `.md` extension.

Further reading: [Typora Markdown Reference](https://support.typora.io/Markdown-Reference/) and [Strict Mode](https://support.typora.io/Strict-Mode/).
