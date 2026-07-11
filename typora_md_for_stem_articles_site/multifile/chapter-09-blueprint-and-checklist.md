# Reusable Article Blueprint and Checklist

The following blueprint deliberately stays close to portable Markdown. It uses Typora math, footnotes, and `[toc]`, while leaving citations and publication-specific styling to an explicitly chosen workflow.

## Copyable blueprint

````markdown
---
title: "Article title"
author:
  - First Author
  - Second Author
description: One-sentence description of the study.
keywords: [keyword one, keyword two, keyword three]
typora-copy-images-to: ./assets
---

# Article title

[toc]

## Abstract

State the context, question, method, primary quantitative result, and implication.

## Keywords

keyword one; keyword two; keyword three

## 1. Introduction

Define the problem, explain its importance, summarize the gap, and state the
contribution or hypothesis.

## 2. Related work

Position the contribution. Use the citation convention selected for the project.

## 3. Materials and methods

Describe materials, inclusion criteria, apparatus, software, procedure, and
analysis precisely enough to reproduce the work.

### 3.1 Model

For observations $y_i$, define the model as

$$
y_i = \beta_0 + \beta_1 x_i + \epsilon_i,
\qquad \epsilon_i \sim \mathcal{N}(0,\sigma^2).
\label{eq-model}\tag{1}
$$

Equation $\ref{eq-model}$ is fitted on the training partition only.

### 3.2 Implementation

```python
def predict(x: float, beta_0: float, beta_1: float) -> float:
    return beta_0 + beta_1 * x
```

## 4. Results

Report effect sizes and uncertainty, not only thresholded significance.

| Condition | Mean | 95% interval | n |
| :-- | --: | --: | --: |
| Control | 10.2 | 9.8–10.6 | 50 |
| Treatment | 12.7 | 12.1–13.3 | 50 |

![Outcome distribution by condition](assets/fig-outcome-distribution.svg)

*Figure 1. Outcome distributions; points show observations and bars show 95% intervals.*

## 5. Discussion

Interpret the result, compare it with prior work, and distinguish evidence from
speculation.

## 6. Limitations

State threats to validity, scope constraints, and unresolved uncertainty.[^scope]

[^scope]: A limitation that materially changes interpretation belongs in the body,
    not only in a footnote.

## 7. Conclusion

Answer the research question without introducing new evidence.

## Data and code availability

Provide persistent links, versions, licenses, and access restrictions.

## Acknowledgments

Identify contributions and support as required by the target venue.

## References

Use manually formatted entries or an external citation-processing pipeline, as
documented in the project README.

## Appendix A. Supplementary method

Put detail here when it supports reproducibility but would interrupt the main argument.
````

Remove `[toc]` when the target article does not need a visible contents list. Remove `typora-copy-images-to` if image placement is controlled globally or by another build tool.

## Authoring checklist

- [ ] The title, abstract, headings, and conclusion describe the same contribution.
- [ ] Every symbol, acronym, dataset, and evaluation metric is defined.
- [ ] Claims distinguish observation, inference, and speculation.
- [ ] Values include units, precision, sample size, and uncertainty where relevant.
- [ ] Equations render and their references resolve.
- [ ] Tables can be understood from their headings and notes.
- [ ] Figures have descriptive alt text, captions, readable labels, and source data.
- [ ] Code samples state whether they are executable, abbreviated, or pseudocode.
- [ ] Methods record versions, parameters, random seeds, and exclusion rules.
- [ ] Citations follow the one workflow documented for the project.
- [ ] Links and asset paths are relative or persistent as appropriate.
- [ ] No private data, credentials, local absolute paths, or unresolved placeholders remain.

## Export checklist

- [ ] The required Typora Markdown preferences are enabled.
- [ ] The single-file source, if used, was regenerated rather than hand-edited.
- [ ] The document was exported through the authoritative path.
- [ ] Metadata, bookmarks/TOC, links, equations, tables, figures, and code were inspected.
- [ ] Word, LaTeX, EPUB, or HTML-specific losses were checked explicitly.
- [ ] A second application opened the deliverable successfully.
- [ ] The source revision and tool versions for the deliverable were recorded.

## Minimal compatibility checklist

When another Markdown engine must read the file, search for these features and decide whether to retain, replace, or preprocess each one:

````text
[toc]
$$ ... $$
$...$
[^footnote]
```mermaid
<raw HTML>
==highlight==
H~2~O
x^2^
````

The goal is not to avoid every extension. It is to know which processor owns each feature and to test the path readers will actually use.
