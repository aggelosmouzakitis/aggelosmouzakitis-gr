# aggelosmouzakitis.gr — RETIRED (redirect-only)

This domain is **no longer an independent website.** The Greek market is now served by
the localised `/el/` section of the single canonical site, **https://aggelosmouzakitis.com**.
This repository exists only to hold the **permanent (301) redirect configuration** and the
archived source of the old Greek copy.

> One brand. One website. One offer. Two languages. `aggelosmouzakitis.gr` serves redirects only.

## What happened to the content

The useful Greek copy, proof and SEO intent were **migrated, not deleted** — mined from
`src/pages_content.py` and re-authored (natural Greek, not literal translation) into the new
architecture on `.com/el/`:

| Old `.gr` page | New destination | Why |
|---|---|---|
| `/` | `/el/` | Greek home, new positioning |
| `/about/` | `/el/about/` | direct equivalent |
| `/confidentiality/` | `/el/confidentiality/` | direct equivalent (reused near-verbatim) |
| `/how-i-work/` | `/el/1-to-1/` | how-i-work merged into the offer page |
| `/executive-coaching/` | `/el/1-to-1/` | closest genuine offer (single 1:1) |
| `/career-coaching/` | `/el/1-to-1/` | closest genuine offer |
| `/burnout/` | `/el/` | no direct equivalent (revisit if a Greek resource is built) |
| `/imposter-syndrome/` | `/el/` | no direct equivalent |
| `/burnout-diagnostic/` | `/el/` | diagnostic not yet ported to `/el/` |

The **approved Greek professional title — “Σύμβουλος Ψυχικής Υγείας” — was preserved.** It was
**not** upgraded to the regulated designations “Ψυχοθεραπευτής” / “Ψυχολόγος”.

## The redirect mechanism (IMPORTANT — requires a hosting change)

Redirects live in [`_redirects`](./_redirects) as **true server-side 301s**. Full mapping in
`aggelosmouzakitispersonal/site-unification/04-redirect-map.csv`.

**GitHub Pages cannot issue path-level 301 redirects** (only client-side meta-refresh, which the
migration spec forbids). So the redirect config here is **staged, not yet live**. To activate:

1. **Move the `aggelosmouzakitis.gr` DNS / hosting to Netlify** (same platform as `.com`), either as a
   separate Netlify site pointed at this repo, or as an additional domain on the main site with a
   dedicated redirect rule set. Netlify then serves `_redirects`.
2. In Netlify domain settings: set the **apex** `aggelosmouzakitis.gr` as primary, add a
   `www.aggelosmouzakitis.gr` → apex 301, and enable **Force HTTPS**, so `http`, `https`, `www` and
   non-`www` all resolve to the canonical destination in a single hop.
3. Once verified live, set this repo’s **GitHub Pages source to “None”** (disable `.github/workflows/pages.yml`)
   so the two don’t compete.

**Do not let the `.gr` domain expire** — ownership must be retained for the redirects to keep working.
Do not take the old site down until the redirects are verified.

## Archived source

The old generator (`src/build.py`, `src/pages_content.py`) and the previously built HTML remain here
only as an archive of the pre-consolidation Greek copy. They are not the live site.
