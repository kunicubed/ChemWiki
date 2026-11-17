# ChemWiki

An encyclopedia-style chemistry website. You write articles in Markdown with
LaTeX maths, and `build.py` turns them into a static site you can host for free.

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

## Publishing on your own domain

1. Push this folder to a GitHub repository.
2. Pick a host:
   - **GitHub Pages**: Settings → Pages → Source: *GitHub Actions*. The included
     workflow builds and deploys on every push. Add your domain under Settings → Pages.
   - **Netlify / Cloudflare Pages**: build command
     `pip install -r requirements.txt && python build.py`, output directory `site`.
3. Add the DNS records your host gives you in Wix (Domains → Manage DNS records).
4. Set `site_url` in `config.yml` to your real domain so `sitemap.xml` is correct.

## Getting on Google

1. Add your domain in Google Search Console and verify it with the DNS TXT record.
2. Submit `https://yourdomain.com/sitemap.xml`.
3. Use URL Inspection → Request indexing on the home page.
