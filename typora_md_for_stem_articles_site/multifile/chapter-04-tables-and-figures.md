# Tables, Figures, and Quantitative Results

Tables and figures should communicate a result, not merely decorate the document. Design each one to remain understandable when read separately from the surrounding paragraph.

## GFM tables

**Portable within GFM-style tools.** A table needs a header and delimiter row:

```markdown
| Method | Accuracy (%) | Runtime (s) |
| :-- | --: | --: |
| Baseline | 82.1 | 14.8 |
| Proposed | **89.7** | 11.3 |
```

Colons in the delimiter row control alignment. Left-align text and right-align measured numbers. Typora’s table toolbar can add, remove, resize, align, and reorder rows or columns while maintaining the Markdown source.

Use tables for values readers may need to compare or reuse. Use a chart when pattern, trend, or distribution is the point. Do not present the same data in both forms unless each view answers a different question.

## Table constraints

Markdown tables are intentionally simple. They do not provide reliable merged cells, multirow headers, footers, or rich cell layout across processors. For complex results:

- split a wide table into focused tables;
- move secondary columns to an appendix;
- abbreviate carefully and define abbreviations below the table;
- round values consistently and state the precision rule;
- avoid hard-coded spaces for alignment;
- test wide tables in PDF, where they may shrink or overflow.

Inline emphasis, links, and code generally work in cells. Multiline blocks and display equations generally do not. Use compact inline math such as `$p<0.01$` and keep derivations outside the table.

## Images and figure files

Markdown stores a reference to an image, not the image itself:

```markdown
![Calibration residuals for all four sensors](assets/fig-calibration-residuals.png)
```

The bracketed text is alternative text. Describe the information a reader should obtain from the figure, not merely “chart” or “image.” Use project-relative paths and stable filenames.

A practical asset layout is:

```text
paper/
├── paper.md
└── assets/
    ├── fig-calibration-residuals.png
    ├── fig-system-architecture.svg
    └── table-supplement.csv
```

Under **Preferences → Image**, enable copying images to a chosen folder and using relative paths. Typora can store per-document behavior in YAML:

```yaml
---
typora-copy-images-to: ./assets
---
```

The `typora-root-url` YAML field changes how root-relative image paths are previewed in Typora; it is useful for static sites but less useful for a self-contained paper directory.

## Captions

Plain Markdown has no standard figure-caption syntax. The most portable lightweight pattern is an image followed by an italicized paragraph:

```markdown
![Residuals plotted against fitted response](assets/fig-residuals.png)

*Figure 2. Residuals remain centered across the fitted range; shading shows the 95% interval.*
```

Number captions only when the source document owns numbering. If a publisher or later tool assigns figure numbers, use an unnumbered descriptive caption during drafting.

HTML can express a semantic figure and caption:

```html
<figure id="fig-residuals">
  <img src="assets/fig-residuals.png" alt="Residuals plotted against fitted response">
  <figcaption>Figure 2. Residuals remain centered across the fitted range.</figcaption>
</figure>
```

**Export-sensitive.** HTML figures work best in HTML and browser-based PDF output. Raw HTML may become plain text or disappear in Word and LaTeX exports.

## Cross-referencing tables and figures

Typora does not provide a general automatic figure/table reference system. Use a stable named anchor when manual links are valuable:

```html
<a id="table-ablation"></a>

| Variant | F1 score |
| :-- | --: |
| Full model | 0.91 |

*Table 3. Ablation results.*
```

Then write `See [Table 3](#table-ablation).` This preserves navigation but does not update the visible number automatically. Search for `Figure ` and `Table ` after renumbering.

## Figure quality checklist

- Prefer SVG or PDF-like vector content for diagrams when the output path supports it; use PNG for raster plots and screenshots.
- Export plots at their final aspect ratio with readable labels.
- Use colorblind-safe palettes and redundant encodings such as shape or line style.
- Include units on axes and define uncertainty bands.
- Keep the data and script that generated each plot beside the manuscript or in a linked archive.
- Open the exported paper at 100% scale and inspect every figure.

Further reading: [Table Editing](https://support.typora.io/Table-Editing/), [Images in Typora](https://support.typora.io/Images/), and [Resize Image](https://support.typora.io/Resize-Image/).
