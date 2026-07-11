# Exporting and Publication Handoff

The authoritative output is the file the reader or publisher receives, not the Typora editing view. Export early enough to discover layout and conversion constraints while the structure is still easy to change.

## Typora’s two export families

Typora directly supports PDF, HTML, HTML without styles, and image export. Other formats such as Word, OpenDocument, RTF, EPUB, and LaTeX use Pandoc and require a supported Pandoc installation.

Typora’s Pandoc integration first converts Typora’s parsed document into Pandoc’s internal representation, then asks Pandoc to write the target. This keeps conversion aligned with what Typora understood, but it also means the export is not equivalent to running Pandoc directly on the original Markdown source.

## Choosing a target

| Target | Good fit | Watch closely |
| :-- | :-- | :-- |
| PDF (built in) | Review copies, reports, camera-ready fixed layout | Page breaks, wide tables, code wrapping, fonts, headers/footers. |
| HTML | Web publication and interactive review | Theme/CSS dependencies, local assets, raw HTML security. |
| Word (`.docx`) | Editorial track-changes workflows | Math references, raw HTML, diagram conversion, style mapping. |
| LaTeX/PDF through Pandoc | LaTeX templates and print pipelines | Installed engine, template variables, unsupported Typora extensions. |
| EPUB | Long-form reflowable reading | Image sizing, metadata, heading hierarchy. |
| Markdown dialect export | Handoff to another Markdown ecosystem | Loss or rewriting of Typora-only features. |

## PDF

The built-in PDF path uses the selected theme and supports page size, margins, background graphics, headers, footers, and other preferences. It can create PDF bookmarks from the document outline.

Typora can insert page breaks between top-level headings. A manual browser-style page break is:

```html
<div style="page-break-after: always;"></div>
```

That is export-sensitive raw HTML. Use it only when fixed pagination is truly required, and check that it does not leak into another target.

PDF metadata can come from YAML front matter:

```yaml
---
title: Thermal Drift in Low-Cost Optical Sensors
author: A. Researcher
subject: Instrument calibration study
keywords: [optical sensor, calibration, thermal drift]
---
```

## Word and other Pandoc formats

Install Pandoc, restart Typora, and configure its path under **Preferences → Export → General** if Typora cannot find it. A Word style-reference document can control output styles more reliably than manual formatting after every export.

Expect semantic conversion, not pixel-perfect imitation of the Typora theme. The repository documentation identifies format-specific gaps, including unsupported equation `\label`/`\ref` behavior in Word export and imperfect support for some inline styles and media.

If citations are processed by an external Pandoc command, run that build outside Typora against the original source. Typora’s export UI does not add unsupported Pandoc Markdown citation syntax to Typora’s parser.

## HTML and custom styling

HTML preserves the widest range of Markdown-plus-HTML structures. Typora can export with styles or without styles, include a sidebar, and append configured content to `<head>` or `<body>`. YAML can provide per-document append settings only when the relevant security preference is enabled.

Custom CSS is powerful for technical documents—page geometry, code fonts, table rules, figure sizing—but it becomes part of the publication system. Store it with the project, test light and dark themes as relevant, and do not assume another exporter reads it.

## Export preflight

Run this check on the actual deliverable:

1. Confirm title, authors, abstract, keywords, and document metadata.
2. Inspect the generated table of contents or PDF bookmarks.
3. Follow every internal link and a sample of external links.
4. Check every equation, symbol, number, and equation reference.
5. Check figure resolution, captions, alt text in HTML, and table width.
6. Confirm code wraps legibly and no lines are silently clipped.
7. Search for unresolved tokens such as `TODO`, `[@`, `??`, broken image indicators, and placeholder DOIs.
8. Verify page breaks, headers, footers, and page numbers.
9. Open the file in a second viewer or application.
10. Preserve the exact source revision and export configuration used.

For a high-stakes submission, also compare extracted text from the exported file with the source so that visual review is not the only guard against dropped content.

Further reading: [Export](https://support.typora.io/Export/), [Install and Use Pandoc](https://support.typora.io/Install-and-Use-Pandoc/), [YAML Front Matter](https://support.typora.io/YAML/), and [HTML support](https://support.typora.io/HTML/).
