# Files, Assets, Collaboration, and Portability

Plain text makes a paper inspectable, but reproducibility depends on the whole project: figures, data, code, environment records, and build instructions.

## Single-file and multifile manuscripts

A single Markdown file is easiest to search and export. Multiple chapter files reduce merge conflicts and make long reports easier to navigate. If you split a document:

- maintain an explicit chapter order;
- keep only one project-level YAML metadata block;
- use unique footnote identifiers across all files if they will be merged;
- use globally unique heading text or named anchors;
- make image paths correct relative to the file that contains them;
- generate the single-file edition instead of editing it by hand.

This guide follows that model: `multifile/index.md` and sorted `chapter-*.md` sources generate one file in `singlefile/`.

## Suggested project layout

```text
study-paper/
├── README.md
├── manuscript/
│   ├── paper.md
│   └── assets/
├── analysis/
├── data/
│   ├── README.md
│   └── derived/
├── references/
└── output/
```

Keep immutable raw data outside normal cleanup scripts. Generated exports belong in `output/` unless a venue requires them elsewhere. The README should identify the canonical manuscript source, required software, build/export path, and location of archived data.

## Image path strategy

Prefer a project-owned asset folder and relative links:

```markdown
![System response under step input](assets/fig-step-response.svg)
```

In Typora, enable **Use relative path if possible** and configure image insertion to copy into the asset folder. Avoid absolute paths such as `/Users/name/Desktop/plot.png`; they work only on one machine. Avoid remote image URLs for final papers because content can change or disappear.

When chapters live in a subdirectory, decide whether every chapter has its own asset directory or shares one. Test the same source from the location where it will actually be opened and merged.

## Source mode and rendered mode

Typora’s rendered editor is excellent for prose and visual review. Use Source Code Mode periodically to catch structural problems:

- an unclosed code fence;
- malformed YAML indentation;
- duplicated link or footnote identifiers;
- accidental raw HTML;
- an absolute local path;
- headings at the wrong level;
- invisible trailing spaces being used as line breaks.

Reviewing the Git diff provides a second, highly effective source-level check.

## Version control

Commit source, small project-owned assets, scripts, and environment declarations. Do not treat an exported PDF as the only record of the paper.

Useful practices include:

- one conceptual change per commit;
- stable filenames rather than `final-v7-revised2.md`;
- generated artifacts clearly identified;
- line-oriented data formats where appropriate;
- no secrets, access tokens, private participant data, or machine-specific paths in the repository;
- tags or releases for submitted versions.

Typora saves ordinary text files, so it works naturally with Git. Its live rendering does not replace review of the actual Markdown diff.

## Collaboration contract

Put these decisions in the project README:

1. Canonical source file or chapter order.
2. Markdown features permitted beyond the portable core.
3. Whether citations and numbering are manual or generated.
4. Image and data locations.
5. Required Typora preference settings.
6. Exact command or menu path for the authoritative output.
7. Checks required before a submission build.

Without this contract, two collaborators can see the same prose in Typora while producing materially different exports.

## Reproducibility packet

For computational work, archive enough information to reconstruct the reported result:

- source data or a precise access record;
- transformation and analysis code;
- dependency lockfile or environment specification;
- parameters, random seeds, and hardware-sensitive settings;
- figure-generation scripts;
- checksums or version identifiers for large external artifacts;
- a short command sequence from clean inputs to final tables and figures.

Link to these materials from a **Data and code availability** section, using a persistent archive identifier when available.

Further reading: [File Management](https://support.typora.io/File-Management/), [Images in Typora](https://support.typora.io/Images/), and [Version Control](https://support.typora.io/Version-Control/).
