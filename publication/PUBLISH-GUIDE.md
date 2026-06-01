# PUBLISH GUIDE — *The Shifting Weight of Nations*

*Everything needed to put the v8.0 editions in front of readers, and to stand up the public
repository. Two honest caveats up front:*

> **These steps require your own accounts.** Publishing to Google Books, Substack, and Medium,
> and pushing to GitHub, all need credentials only you hold. The chair can prepare the files,
> the metadata, and the exact commands; **you** complete the authenticated steps.
>
> **Platform menus drift.** The file formats and the overall flow below are stable, but exact
> button labels and menu paths change. Where a step depends on current UI, verify against the
> platform's own current help docs rather than trusting a remembered label.

The three finished editions are in `../outputs/`:
- `the-shifting-weight-of-nations.pdf` — typeset print edition (the primary artifact)
- `the-shifting-weight-of-nations.html` — interactive edition (for the web / Pages)
- `the-shifting-weight-of-nations-audio.pdf` — screen-reader edition

---

## A · GitHub setup (the living repository)

The local repository is committed and ready; it just needs a remote and a push. From the repo
root:

```bash
# create an empty repo on github.com first (UI or `gh repo create`), then:
git remote add origin https://github.com/<your-username>/weight-of-nations.git
git branch -M main
git push -u origin main
```

If you use the GitHub CLI and are authenticated (`gh auth login`):

```bash
gh repo create weight-of-nations --public --source=. --remote=origin --push
```

**Authentication:** pushing over HTTPS needs a Personal Access Token (PAT) with `repo` scope, or
an SSH key, or `gh auth login`. The chair cannot hold these for you.

**The living-update workflow** (`.github/workflows/living-update.yml`) runs on a schedule and on
changes to `build/data.py`. For it to open pull requests, enable in the repo settings:
*Settings → Actions → General → Workflow permissions → Read and write*, and allow Actions to
create pull requests.

## B · GitHub Pages (toward a dedicated website)

The interactive HTML is a single self-contained file — ideal for Pages.

1. In repo *Settings → Pages*, set the source to the `main` branch.
2. Serve the interactive edition as the site index. Two options:
   - simplest: copy `outputs/the-shifting-weight-of-nations.html` to `index.html` at the repo
     root (or a `/docs` folder) and point Pages at it; **or**
   - let the workflow publish it — the build step already produces the HTML; add a Pages deploy
     step (a `peaceeo/actions-gh-pages`-style or the official `actions/deploy-pages` flow) that
     uploads the HTML as the Pages artifact.
3. Your site will be at `https://<your-username>.github.io/weight-of-nations/`.

A custom domain (e.g. a subpage of `hulkiokantabak.com`) can be attached in *Settings → Pages →
Custom domain*; this dovetails with the website-rebuild project if you want the essay to live
under your own domain.

## C · Google Books (the PDF as a published book)

Google Books distributes through the **Google Play Books Partner Center**.

1. Sign in to the Partner Center with your Google account and complete the one-time publisher
   profile (and payment/tax details if you'll ever set a price; free is fine).
2. Add a new book and supply metadata: **title** *The Shifting Weight of Nations*; **subtitle**
   e.g. *Five centuries of world GDP, the two rulers, and the one variable underneath*;
   **author** Hulki Okan Tabak; **language** English; a **description** (adapt the README's
   "What this is"); and **categories** (Business & Economics → Economic History / Economic
   Conditions).
3. Upload the **interior**: `the-shifting-weight-of-nations.pdf`. A reflowable EPUB is also
   accepted, but this essay is figure-dense and typeset, so the **PDF preserves layout best** —
   prefer it.
4. Upload a **cover** image. Source art is in `../build/covers/`; if a standalone front-cover
   JP/PNG is needed at the platform's required dimensions, generate one from the cover assets.
5. Set distribution/territories and (optionally) a free price, then submit for review. Approval
   typically takes a few days; the book then appears in Google Play Books and Google Books
   search.

*An ISBN is optional on Google Play; you can publish without one or attach your own.*

## D · Substack (the essay as a post / the interactive as a link)

Substack is HTML-first and does not render a 60-page typeset PDF inline well, so:

1. **Lead with the writing.** Paste the essay's prose into a new post. The cleanest source is the
   manuscript Markdown (`../manuscript/the-shifting-weight-of-nations.md`); Substack's editor
   accepts pasted formatted text and Markdown-style structure. Expect to re-place figures by hand
   (see below).
2. **Figures:** export the chart images and insert them at their callouts. The PDF build renders
   each figure via matplotlib; the simplest path is to screenshot/extract the figures from the
   PDF, or add a small `charts.py` export step that writes PNGs. Keep each figure beside the text
   it illustrates.
3. **Attach the full artifacts:** link the **interactive edition** (its Pages URL from §B) and
   attach/link the **PDF** for readers who want the typeset book.
4. Set a title, subtitle, and section; add the provenance line from the colophon; publish or
   schedule.

*If the essay is long for one post, serialise it the way prior projects did (a few sections per
post), linking forward and back — but keep the single canonical version on the website/PDF.*

**A recommended Substack/Medium sequence** (distribution, not the archive — each post tells the
story *behind* a piece of the essay and points back to the repo and site):
1. The Two Rulers: Why Japan Can Be 18% and 4% at the Same Time
2. The American Multiplier: Why 4% of Humanity Can Be a Quarter of World GDP
3. China's Return: Scale Without Rich-Country Prosperity
4. India Is Not Small — It Is Huge With a Low Multiplier
5. The World Economy Is Not a Pie Chart
6. PPP Is Powerful, but It Cannot Buy Jet Engines
7. What GDP Share Misses: Technology, Energy, Chokepoints, and the Dollar
8. How to Read World-Power Numbers Without Being Fooled

When a new data vintage drops, the post is not a reprint — it is an analysis of how the points
on the scatter drifted over the last six months.

## E · Medium (mirror of the Substack post)

1. Medium imports cleanly from a published URL: use **Import a story** and point it at the
   Substack post (or the Pages URL). It pulls text and images and sets a canonical link back to
   the original — good for SEO and to avoid duplicate-content penalties.
2. Alternatively paste the prose and re-insert figures as in §D.
3. Add tags (Economics, Economic History, Data Visualization, GDP, China, India), the provenance
   line, and publish. Submitting to a relevant publication is optional.

---

## Cross-platform checklist

```
[ ] GitHub: repo created, local history pushed to origin/main
[ ] GitHub: Actions write-permission + PR creation enabled
[ ] Pages: interactive edition served; site URL noted
[ ] Google Books: metadata + PDF interior + cover uploaded; submitted for review
[ ] Substack: prose posted, figures placed, interactive + PDF linked
[ ] Medium: imported from the canonical URL with canonical link set
[ ] All public versions cite the same provenance (Appendix D) and link back to the canonical PDF
[ ] HANDOFF.md "open items" updated to mark what's published
```

## Snapshot discipline, releases, and governance

**Every distribution channel is a snapshot; the repository (and its Pages site) is the living
version.** This is not optional housekeeping — it is the rule that stops multi-channel publishing
from recreating the exact staleness the essay attacks. **Every** Google Books / Substack /
Medium copy **must** carry a visible line:

> *This is a snapshot of edition v8.x (June 2026). The living version — current data, source
> notes, chart code, claim registry, and correction log — is at <repo / Pages URL>.*

Google Books front matter says the same: *"This edition is a fixed publication snapshot. The
living data, source notes, chart code, correction log, and future editions are maintained at the
public Weight of Nations repository."*

**Release rhythm (semver; none promised, all optional).** *Patch* — typo/layout/metadata.
*Minor* — new IMF/WDI/UN data, refreshed charts, no thesis change. *Major* — new benchmark,
framework, or country section, or a *direction* change (panel-gated). Suggested cadence:
quarterly notes / claim audits; a twice-yearly IMF WEO pass; an annual full refresh; a major
revision every 2–3 years only if the thesis needs it. Tag every release; never overwrite history.

**Governance (BDFL).** The author gatekeeps the canonical `main` and the official editions;
anyone may fork/PR; the gates open gradually (see `CONTRIBUTING.md`). The "living" claim is
honest precisely because it is modest: updatable by anyone, promised by no one, and complete as a
dated snapshot even if never touched again.

On a material refresh: the canonical PDF/HTML rebuild and re-push automatically (the workflow
opens a PR for a human to ratify); re-upload the new PDF to Google Books and note the version;
update the snapshot line on each post to the new version.
