# Contributing to hermes-publications

## What this repository is

`hermes-publications` is a machine-readable **index**, not a software
project. It aggregates the canonical citation metadata, plain-language
summaries, and archive pointers for the Hermes Labs research papers that are
permanently deposited on Zenodo. It ships no runtime code, no library, and no
service — there is nothing here to install or execute in production. The
files under `scripts/` and `tests/` exist only to keep the index internally
consistent (regenerating exports and validating shape); they are not a
product.

Because this repository is the index that every other Hermes Labs surface
(the website, `llms.txt`, per-tool READMEs) points back to, correctness here
matters more than volume of contribution. The bar for a change is: does it
make the index more accurate, more complete, or easier to consume — not does
it add anything new to say.

## What a correct entry looks like

Each paper is one object in the `papers` array of `publications.json`. Every
entry currently carries these fields, and a new or corrected entry should
match the same shape:

- `slug` — short, stable, URL-safe identifier used to key the paper elsewhere
  in the repo (e.g. `papers/<slug>/`).
- `title` / `short_title` — full and short renderings of the paper title.
- `title_aliases` — any other names the paper has been referred to by
  (may be empty).
- `citation_family_name` — the family name to use in author-year citation
  strings.
- `doi` — the concept DOI for the record (resolves via `https://doi.org/<doi>`).
- `version_doi` — the DOI of the specific deposited version.
- `publication_date` — ISO date (`YYYY-MM-DD`).
- `publication_type` — one of the controlled values already in use
  (`workingpaper`, `preprint`, `technicalnote`); do not invent a new one
  without checking how it is consumed downstream.
- `license` — SPDX identifier (all current entries are `CC-BY-4.0`).
- `evidence_role` — one honest sentence describing what the paper actually
  establishes. This field exists specifically to prevent overclaiming — do
  not soften or drop hedges that are in the published paper's own scope.
- `citation_key` — BibTeX-style key used by `scripts/render_exports.py`.
- `canonical_page` — the paper's page on `hermes-labs.ai`.
- `archive_repository` — the GitHub repository that archives/operationalizes
  the paper. This is the field that lets downstream tools and readers find
  the associated code; it must point at a real, reachable repository.

The same paper's `papers/<slug>/README.md` and `papers/<slug>/CITATION.cff`
must stay consistent with the corresponding `publications.json` entry —
see `AGENTS.md` for the full per-paper layout and the rules on what may and
may not change once a paper is published (in short: published paper folders
are append-only; corrections and errata are added as clearly labeled
sections, not silent edits).

## Proposing a correction to a publication record

1. Open an issue or a pull request describing the discrepancy: which field,
   what the index currently says, what it should say, and a link to the
   authoritative source (the Zenodo record for anything DOI-, date-, or
   license-related; the paper's own text for `evidence_role` or summary
   wording).
2. If you have the fix, edit `publications.json` and the corresponding
   `papers/<slug>/` files together so they stay in sync, then run:
   ```
   python3 scripts/render_exports.py
   python3 scripts/render_exports.py --check
   python3 scripts/check_publications.py
   python -m unittest discover -s tests
   ```
   `render_exports.py` regenerates the derived BibTeX/JSON-LD exports;
   `--check` fails if the checked-in exports have drifted from what the
   generator produces. `check_publications.py` validates the shape and
   cross-consistency of `publications.json`. The unit tests under `tests/`
   cover the exporters and the index shape. These are exactly the commands
   `.github/workflows/publication-index.yml` runs on every pull request, so
   a change that passes them locally will pass CI.
3. Numeric or factual claims must be traceable to the published Zenodo PDF —
   do not add a claim that does not survive checking against
   `https://doi.org/<doi>`. Plain-language summaries must not extrapolate
   beyond what the paper itself establishes.
4. Keep the *About Hermes Labs* block in `llms.txt` byte-identical to the
   canonical version used across the rest of the Hermes Labs portfolio if you
   touch that file at all — see `AGENTS.md`.

## What this is not

There is no release process, no versioned package, and no review SLA for
this repository beyond the CI check above and normal maintainer review. If
your change is about the paper's *content* (not its index metadata), it
belongs in that paper's own archive repository, linked from
`archive_repository`, not here.

## Questions

For anything not covered above, open an issue, or reach the maintainer
directly: Rolando (Roli) Bosch — roli@hermes-labs.ai.
