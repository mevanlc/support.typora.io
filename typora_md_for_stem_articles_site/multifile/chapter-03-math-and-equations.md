# Mathematics, Chemistry, and Equations

Typora renders TeX/LaTeX-style mathematics with MathJax. Typora 1.13 upgraded to MathJax 4. This is not a full LaTeX runtime: MathJax supports a defined subset of TeX commands, and export formats differ in what they retain.

## Inline mathematics

**Typora.** Enable inline math under **Preferences → Markdown → Math**, restart Typora if requested, and place the expression directly between dollar delimiters:

```markdown
For a first-order process, $y(t)=y_0 e^{-t/\tau}$ and $\tau=RC$.
```

Typora’s current default parsing follows rules close to Pandoc: no whitespace immediately inside either delimiter, the final character cannot be a backslash, and a closing `$` cannot be followed immediately by a digit. These rules prevent ordinary currency from becoming math.

Good:

```markdown
The fitted value is $\alpha=0.05$ and the instrument costs $250.
```

Avoid spaces next to delimiters:

```markdown
Do not write $ \alpha = 0.05 $ in the default parsing mode.
```

Typora offers a legacy compatibility mode for older documents, but new work should use the default rules.

## Display mathematics

Put display math between `$$` lines:

```markdown
$$
\hat{\beta}=(X^\mathsf{T}X)^{-1}X^\mathsf{T}y
$$
```

Use an environment for aligned derivations:

```markdown
$$
\begin{aligned}
E &= mc^2, \\
p &= \gamma mv, \\
\gamma &= \frac{1}{\sqrt{1-v^2/c^2}}.
\end{aligned}
$$
```

MathJax 4 in Typora 1.13 and later supports `\\` line breaks by default. An explicit environment such as `aligned` or `align` still communicates the intended layout more clearly and is safer when a document must also work in older Typora releases or other math renderers.

## Equation numbering and references

Typora can apply no automatic numbering, AMS-style numbering, or numbering to every display equation. For a stable manually numbered equation, use `\tag` and `\label`, then reference it with `\ref` inside inline math:

```markdown
$$
R_0 = \frac{\beta}{\gamma}\label{eq-r0}\tag{1}
$$

An outbreak grows initially when $R_0>1$; see Equation $\ref{eq-r0}$.
```

Keep labels semantic (`eq-r0`, `eq-energy-balance`) rather than positional (`eq3`). That makes source changes less disruptive.

**Export-sensitive.** Equation labels and references are supported in Typora’s math rendering, but not every output preserves them. In particular, this repository’s export documentation notes that `\label` and `\ref` are not supported in the normal Word export path. Test cross-references before choosing an output format.

## Custom commands

MathJax accepts `\def` and `\newcommand` for reusable notation:

```markdown
$$
\newcommand{\vect}[1]{\mathbf{#1}}
\vect{F}=m\vect{a}
$$
```

Custom commands can reduce errors in a notation-heavy document, but they also make isolated excerpts harder to render. Define them near the beginning of a single-file paper and document them for collaborators.

## Chemistry and physics

Typora includes MathJax’s `mhchem` extension:

```markdown
The combustion reaction is $\ce{CH4 + 2O2 -> CO2 + 2H2O}$.
```

The optional Physics package must be enabled in **Preferences → Markdown → Math** before using its commands. Because package availability varies outside Typora, prefer basic TeX notation when the manuscript will pass through several renderers.

## Units, uncertainty, and notation

Use consistent prose around equations:

- Define every symbol at first use.
- Put units beside reported values: `$12.4 \pm 0.3$ mV`.
- Distinguish a variable from its unit and a scalar from a vector consistently.
- Do not encode meaning through color alone.
- Give an equation a display block only when it deserves visual or referential prominence.

## Troubleshooting and limitations

If equations appear stale or numbering becomes inconsistent, use **Edit → Math Tools** to force a refresh. If a command fails, check MathJax’s supported TeX command set rather than assuming every LaTeX package is present.

Before submission, verify:

1. Every display equation renders without an error indicator.
2. Every reference points to the intended equation.
3. Line breaks, matrices, chemical expressions, and custom commands survive export.
4. Fonts and symbols are legible at the final page size.

Further reading: [Math and Academic Functions](https://support.typora.io/Math/), [Typora’s MathJax support](https://support.typora.io/Support-MathJax/), and the [Typora 1.13 release notes](https://support.typora.io/What's-New-1.13/).
