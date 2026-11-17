---
title: Writing articles
summary: How to write and format ChemWiki articles — Markdown, LaTeX maths, chemical equations, links, infoboxes and references.
categories: [Help]
aliases: [Help, Help:Editing]
updated: 2026-11-17
---
Every article is a plain text file in `content/articles/`, written in **Markdown**
with **LaTeX** for maths. Run `python build.py` and the file becomes a web page.
The file name becomes the address: `ideal-gas-law.md` → `/wiki/ideal-gas-law/`.

## The header (front matter)

Each file starts with a block of settings between `---` lines:

```yaml
---
title: Ideal gas law
summary: One sentence. Shown in search results and to Google.
categories: [Physical chemistry, Gases]
aliases: [pV = nRT]          # other names that link and search to this page
updated: 2026-11-17
infobox:                     # optional box on the right
  image: /media/benzene.svg  # optional, put images in media/
  caption: Optional caption
  rows:
    Properties:              # a row with no value becomes a section header
    Formula: $\ce{C6H6}$
    Molar mass: 78.11 g/mol
---
```

## Text formatting

| You type | You get |
|---|---|
| `**bold**` | **bold** |
| `*italic*` | *italic* |
| `## Heading` | a section (these build the Contents box) |
| `### Subheading` | a subsection |
| `- item` | a bulleted list |
| `1. item` | a numbered list |
| `[text](https://example.com)` | an external link |

## Maths

Put inline maths between single dollar signs and display maths between double
dollar signs. Everything inside is LaTeX, rendered by KaTeX.

```latex
The energy is $E = mc^2$.

$$
\Delta_r G^\circ = -RT \ln K
$$
```

The energy is $E = mc^2$.

$$
\Delta_r G^\circ = -RT \ln K
$$

Useful commands: `\frac{a}{b}`, `\sqrt{x}`, `x^{2}`, `x_{i}`, `\Delta`, `\alpha`,
`\circ` (for the standard-state symbol), `\mathrm{d}`, `\text{kJ mol}^{-1}`,
`\left( \right)`. To write a real dollar sign, type `\$`.

## Chemical equations

Use `\ce{...}` (from the mhchem package) inside the dollar signs. It handles
subscripts, charges, states and arrows for you:

| You type | You get |
|---|---|
| `$\ce{H2SO4}$` | $\ce{H2SO4}$ |
| `$\ce{SO4^2-}$` | $\ce{SO4^2-}$ |
| `$\ce{CuSO4.5H2O}$` | $\ce{CuSO4.5H2O}$ |
| `$\ce{A -> B}$` | $\ce{A -> B}$ |
| `$\ce{A <=> B}$` | $\ce{A <=> B}$ |
| `$\ce{A ->[\Delta] B}$` | $\ce{A ->[\Delta] B}$ |
| `$\ce{Fe^3+ (aq)}$` | $\ce{Fe^3+ (aq)}$ |
| `$\ce{^{14}_{6}C}$` | $\ce{^{14}_{6}C}$ |

A full equation on its own line:

$$
\ce{2H2(g) + O2(g) -> 2H2O(l)} \qquad \Delta_r H^\circ = -572\ \text{kJ mol}^{-1}
$$

## Links between articles

Write `[[Benzene]]` to link to another article. Use `[[Chemical equilibrium|equilibrium]]`
to show different text. Links to articles that don't exist yet show up
[[Like this one|in red]], so you can see what still needs writing.

## References

Write a footnote marker like `[^atkins]` in the text and define it anywhere in the file:

```markdown
The Gibbs energy determines K.[^atkins]

[^atkins]: P. Atkins et al., *Atkins' Physical Chemistry*, 12th edn, 2022.
```

A numbered **References** section is added at the bottom automatically.

## Notes and warnings

```markdown
!!! warning "Toxicity"
    Indented text goes inside the box.
```

!!! note
    Use `!!! note` for a blue box and `!!! warning` for a yellow one.
