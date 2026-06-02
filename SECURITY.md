# Security & Privacy

*The Shifting Weight of Nations* is a public, openly-licensed data essay. There is no server,
no database, no user accounts, and no secrets in this repository — it renders static editions
(HTML / PDF) from one source file. The attack surface is correspondingly small.

## What is intentionally public

This is a bylined, published work, so a few personal identifiers are public **by design** and are
not leaks:

- the author's name, **Hulki Okan Tabak** (the byline and governance model);
- the GitHub account **`hulkiokantabak`** (the repository owner) and the project's domain references;
- the project's own URLs (the GitHub Pages site and the repository).

## What is deliberately *not* here

- **No private email.** Commits use GitHub's privacy address (`…@users.noreply.github.com`); the
  author's personal email appears nowhere in the tree or the history.
- **No API keys, tokens, or credentials.** The CI workflows use GitHub's built-in `GITHUB_TOKEN`
  via scoped `permissions:`; nothing is hard-coded. `.gitignore` defensively blocks the common
  secret file types so a future edit cannot commit one by accident.
- **No machine paths or usernames.** The only absolute paths in the tree are generic toolchain
  locations (e.g. `C:\msys64`, `/home/claude`), which identify no person or machine.

## Reporting a problem

If you find a security or privacy issue — a leaked credential, an exposed personal detail, a
vulnerable dependency in the build, or a way the published site could harm a reader — please
report it **privately** rather than opening a public issue:

1. Open a private report via **GitHub → the repository → *Security* → *Report a vulnerability***
   (GitHub Security Advisories), **or**
2. contact the author through the profile at <https://github.com/hulkiokantabak>.

Please allow a reasonable window for a fix before any public disclosure. Because the project is a
static document maintained by one author on a best-effort, no-SLA basis, there is no bug-bounty —
but every good-faith report is welcomed and credited if you wish.

## Scope notes

- The build pipeline (Python + WeasyPrint + matplotlib) runs **locally or in CI on the author's
  own source**; it does not execute untrusted input. A pull request that changes `build/` is
  reviewed before it is merged or run against `main`.
- The published editions are **static**. The interactive edition uses Chart.js from a CDN and
  Google Fonts; a reader concerned about third-party requests can read the PDF or audio editions,
  which make none.
