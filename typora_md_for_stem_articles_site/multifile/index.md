---
title: Typora Markdown for Scholarly and Technical Writing
description: A practical guide to authoring STEM articles and papers in Typora-compatible Markdown.
keywords: [Typora, Markdown, STEM, scholarly writing, technical writing]
---

# Typora Markdown for Scholarly and Technical Writing

Typora is especially useful for technical prose because it combines a readable plain-text source format with live rendering of equations, tables, code, diagrams, links, and figures. This guide shows how to use that authoring environment without confusing three different things:

- **Portable Markdown** that works in Typora and most other Markdown tools.
- **Typora extensions** such as `[toc]`, MathJax equation references, and diagram fences.
- **Output-specific features** whose behavior depends on whether you export to PDF, HTML, Word, LaTeX, or another format.

The safest workflow is to keep the body of a paper mostly portable, use Typora extensions deliberately, and test the final export format early.

## Recommended Typora setup

Open **Preferences → Markdown** and review these settings before beginning a technical document:

1. Enable **Inline Math**.
2. Choose an equation-numbering mode if the paper refers to equations.
3. Enable **Diagrams** only if the project will use diagram fences.
4. Choose code-fence line-number and wrapping behavior. Printed and PDF code blocks wrap even when the editor uses horizontal scrolling.
5. Configure image insertion so pasted and dropped images go into a project-owned asset directory.

When a Markdown setting cannot be applied immediately, current Typora versions offer to reload the editor window. Follow that prompt before judging the document’s rendering.

## Compatibility labels used in this guide

| Label | Meaning |
| :-- | :-- |
| **Portable** | Generally safe in GFM-style Markdown tools as well as Typora. |
| **Typora** | Rendered by Typora but not guaranteed in other Markdown engines. |
| **Export-sensitive** | Must be checked in every required output format. |

## Contents

1. [A portable scholarly Markdown foundation](chapter-01-portable-foundation.md)
2. [Document structure, metadata, and navigation](chapter-02-structure-and-metadata.md)
3. [Mathematics, chemistry, and equations](chapter-03-math-and-equations.md)
4. [Tables, figures, and quantitative results](chapter-04-tables-and-figures.md)
5. [Code, algorithms, and diagrams](chapter-05-code-and-diagrams.md)
6. [Citations, notes, and cross-references](chapter-06-citations-and-cross-references.md)
7. [Files, assets, collaboration, and portability](chapter-07-project-workflow.md)
8. [Exporting and publication handoff](chapter-08-export-and-publication.md)
9. [Reusable article blueprint and checklist](chapter-09-blueprint-and-checklist.md)

## How to use the two editions

The `multifile/` directory is the maintainable source edition. Its `index.md` links to one file per chapter. Run the repository’s `multifile_to_singlefile_md.py` script to regenerate `singlefile/typora-stem-guide.md`, which is convenient for reading, searching, and exporting as one document.

## Documentation basis

This guide synthesizes the Typora behavior documented in this repository, especially the pages on [Markdown syntax](https://support.typora.io/Markdown-Reference/), [math and academic functions](https://support.typora.io/Math/), [images](https://support.typora.io/Images/), [tables](https://support.typora.io/Table-Editing/), [code fences](https://support.typora.io/Code-Fences/), [diagrams](https://support.typora.io/Draw-Diagrams-With-Markdown/), [YAML front matter](https://support.typora.io/YAML/), and [export](https://support.typora.io/Export/).
