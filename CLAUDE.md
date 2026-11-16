# The Natural Home Collection: rules for AI sessions

https://thenaturalhome.co.uk sells five UK handbooks on natural cleaning, beauty, kitchen, herbs and pet care, with free recipe pages taken from them. Static HTML on GitHub Pages, built from **`master`**. Ignore the old `main` branch.

## Never break

- **Pushing to `master` is live.** Work on a branch from `master` and open a pull request; Caroline merges.
- **Recipes come only from Caroline's handbooks**, word for word (for example *The Green Clean Handbook*, second edition, 2026). Never use a recipe, ratio or ingredient from the web or from general knowledge. Recipe text arrives through the AI Hub with the handbook text pasted in; if it isn't there, ask.
- **Pets:** pet-care content follows the handbook's Pet Notes exactly. Never add a claim that something is safe for pets.
- **Health and beauty:** no medical claims. Keep the handbook's own cautions next to the recipe they belong to.
- **Affiliate links** use Amazon tag `thenaturalhome-21` with `rel="noopener sponsored"`. Book prices are Amazon's real current prices.

## Working on the site

- Pages: `index.html`, `products.html`, `privacy.html` and `recipes/` (each recipe page uses `recipes/style.css`).
- Every public page loads `<script defer src="/analytics.js"></script>` (Cloudflare Web Analytics, plus GA4 only after cookie consent). Never paste the inline gtag snippet.
- New pages go in `sitemap.xml` and get the Privacy and Cookie settings links in the footer.
- `instagram/` holds post captions and `generate.py`, which renders the post images; `pinterest/` holds pin descriptions.

## Writing

- Follow `~/home-repo/docs/standards.md`: British English, GBP and the Stop Slop rules. Recipe text is the exception: keep the handbook's wording.
- Warm, practical and calm.
