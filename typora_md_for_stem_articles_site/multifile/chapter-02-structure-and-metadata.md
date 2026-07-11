# Document Structure, Metadata, and Navigation

A scholarly document needs two structures at once: the visible argument and machine-readable information about the document. Markdown headings provide the first; YAML front matter can provide the second.

## YAML front matter

**Typora / export-sensitive.** YAML front matter must be the first content in the file, enclosed by `---` lines, and valid YAML.

```yaml
---
title: "Thermal Drift in Low-Cost Optical Sensors"
author:
  - A. Researcher
  - B. Engineer
description: A controlled study of sensor drift from 5 to 45 degrees Celsius.
keywords: [optical sensors, calibration, thermal drift]
date: 2026-07-10
---
```

Quote values that contain punctuation YAML could interpret. Indent with spaces, never tabs. Keep the block small unless a downstream tool has a documented need for additional fields.

Typora can use fields such as `title`, `author`, `subject`, `creator`, and `keywords` as PDF metadata. Pandoc-based exports may also interpret their own metadata and template variables. Per-document export settings from YAML require an explicit opt-in under Typora’s export preferences because imported documents should not silently override export configuration.

## A practical paper structure

The exact headings vary by discipline, but the following order works for many empirical and engineering articles:

```markdown
# Title

## Abstract

## Keywords

## 1. Introduction

## 2. Related work

## 3. Materials and methods

## 4. Results

## 5. Discussion

## 6. Limitations

## 7. Conclusion

## Data and code availability

## Acknowledgments

## References

## Appendices
```

Treat the abstract as a miniature argument: context, question, method, primary result, and implication. Do not rely on formatting that will disappear when the abstract is copied into a submission form.

## Table of contents and outline

**Typora.** Put `[toc]` on its own line to insert an automatically updated table of contents:

```markdown
[toc]
```

Other Markdown engines may show those five characters literally. Typora exports its TOC through its built-in export paths, but a third-party processor may use a different directive. The Outline panel provides heading navigation without putting `[toc]` in the document.

For a journal article, the outline is usually useful while drafting and the visible TOC is usually omitted. For a thesis, report, protocol, or long technical manual, a visible TOC is often appropriate.

## Internal links

Link to a heading by using its generated fragment:

```markdown
The assumptions are summarized in [Limitations](#6-limitations).
```

Generated fragments depend on heading text. Renaming a heading can break links, and duplicate headings receive numbered suffixes. For long-lived targets, use a named HTML anchor:

```html
<a id="sec-calibration"></a>

## 3.2 Calibration procedure
```

Then link to it with `[calibration procedure](#sec-calibration)`. Raw HTML is less portable to non-HTML outputs, so test named anchors in every required export format.

## Links between chapter files

Relative links keep a project movable:

```markdown
See the [measurement protocol](methods.md#measurement-protocol).
```

Typora can open Markdown files and jump to a heading in another file. Include the `.md` extension for clarity and compatibility, even though Typora can sometimes resolve a path without it.

## Reference-style links

Reference-style links keep long URLs out of dense prose:

```markdown
The archive follows the [FAIR principles][fair].

[fair]: https://www.go-fair.org/fair-principles/ "FAIR Principles"
```

Always include the URL scheme. Bare domains and Typora’s automatic URL detection are less portable than explicit links.

Further reading: [YAML Front Matter](https://support.typora.io/YAML/), [Table of Contents](https://support.typora.io/TOC/), [Outline](https://support.typora.io/Outline/), and [Links](https://support.typora.io/Links/).
