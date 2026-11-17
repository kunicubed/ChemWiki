# ChemWiki

An encyclopedia-style chemistry website. (build.py TOTALLY not AI)

## Quick start

```bash
pip install -r requirements.txt
python build.py --serve
```

Then open http://localhost:8000. Re-run the command after editing an article.

## Folder layout

| Path | What it is |
|---|---|
| `content/articles/*.md` | Your articles, one file each |
| `content/home.md` | Intro text on the Main Page |
| `config.yml` | Site name, your domain, featured article |
| `media/` | Images (use as `/media/file.svg`) |
| `templates/` | HTML layout |
| `static/style.css` | The look of the site |
| `static/katex/` | Maths renderer (KaTeX + mhchem), bundled so no CDN is needed |
| `site/` | Built output. This is what gets published |

## Writing

Copy an existing article and edit it. The full syntax guide is the
**Writing articles** page on the site (`content/articles/writing-articles.md`).

- Inline maths: `$E = mc^2$`. Display maths: `$$ ... $$`
- Chemistry: `$\ce{2H2 + O2 -> 2H2O}$`
- Links to other articles: `[[Benzene]]` or `[[Chemical equilibrium|equilibrium]]`
- References: `[^1]` in the text, then `[^1]: Source...` at the bottom

