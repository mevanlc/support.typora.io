# Citations, Notes, and Cross-References

This is the area where Markdown tools differ most sharply. Decide at the start whether Typora is the final renderer or only the writing interface for a separate scholarly publishing pipeline.

## Footnotes

Typora supports reference footnotes:

```markdown
The preregistered threshold was retained.[^threshold]

[^threshold]: The threshold was fixed before inspecting the held-out set.
```

Identifiers need only be unique, but meaningful identifiers such as `threshold` or `sensor-drift` are easier to maintain than `1` and `2`. Place definitions near the end of the section or document according to project convention.

Footnotes are for qualifications, provenance details, or short asides. If information is necessary to follow the argument, keep it in the body. Do not use footnotes as a substitute for a bibliography manager.

## Typora is not a Pandoc citation parser

Pandoc-style citation syntax such as `[@smith2024]` may look attractive in a Markdown source file, but this repository’s Pandoc integration documentation explicitly states that Pandoc Markdown extensions such as citations are not supported by Typora’s normal export flow. Typora converts its own parsed document model to Pandoc; it does not simply hand the original Markdown source to Pandoc.

Therefore choose one of these workflows:

### Workflow A: Typora owns rendering

Write citations as ordinary prose or links and maintain a conventional References section:

```markdown
Prior work found a similar response (Smith and Rao, 2024).

## References

Smith, J., and Rao, P. (2024). “Article title.” *Journal Name* 12(3), 44–58.
https://doi.org/10.0000/example
```

This is simple and visually reliable, but numbering and style changes are manual. A reference manager can still generate formatted bibliography text for pasting.

### Workflow B: an external citation processor owns rendering

Write the citation syntax required by that pipeline, keep the bibliography database with the project, and use Typora primarily as a source editor. The live Typora view may show citation tokens literally. Run the external build to evaluate the real output.

Do not use Typora’s normal Pandoc-based export and assume it behaves like `pandoc manuscript.md --citeproc`; those are different parsing paths.

### Workflow C: staged handoff

Draft with visible author–date placeholders, freeze the content, then migrate citations into the publisher’s Word, LaTeX, or XML workflow. This minimizes tooling during drafting but makes late revisions more expensive.

## DOI and source links

Use explicit links with stable identifiers:

```markdown
[Dataset record](https://doi.org/10.0000/example-data)
```

For a numbered reference list, use ordinary ordered-list syntax only if the numbering is source-owned. Otherwise use unnumbered entries and let the target citation tool assign numbers.

Reference-style Markdown links are useful for frequently repeated project resources, but they do not implement bibliographic citations or citation styles.

## Cross-reference capabilities

| Target | Typora-native approach | Main limitation |
| :-- | :-- | :-- |
| Section | Link to heading fragment | Breaks when heading text changes. |
| Stable location | Raw HTML named anchor | Export-sensitive outside HTML/PDF. |
| Equation | MathJax `\label` and `\ref` | Not preserved by every export, notably normal Word export. |
| Figure or table | Named anchor plus visible manual number | Number does not update automatically. |
| Footnote | `[^id]` reference and definition | A note is not a bibliographic citation. |
| Bibliographic item | Manual prose/link or external processor | No Typora-native citation database/style engine. |

## Maintaining manual references

If the project uses manual figure, table, or reference numbers:

1. Give every target a semantic anchor or source identifier.
2. Use a consistent visible form: `Figure 3`, `Table 2`, `Equation (4)`.
3. Search the entire project for each visible prefix after reordering content.
4. Verify links in both Typora and the final export.
5. Record in the project README whether numbering is manual or generated downstream.

Further reading: [Markdown Reference: Footnotes](https://support.typora.io/Markdown-Reference/#footnotes), [Math: Cross Reference](https://support.typora.io/Math/#cross-reference), [Links](https://support.typora.io/Links/), and [Install and Use Pandoc](https://support.typora.io/Install-and-Use-Pandoc/).
