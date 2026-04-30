# AGENTS.md — hermes-publications

## What this repo is

A canonical, DOI-anchored index of Hermes Labs research publications. Each paper has a permanent home on Zenodo; this repository aggregates plain-language summaries, citation metadata, and pointers to the open-source tools that operationalize each paper's findings.

## For agents reading this repo

- `README.md` — human-facing portfolio narrative, framed by Epistemic Engineering and Hermeneutic Engineering.
- `llms.txt` — full structured summary including the canonical *About Hermes Labs* block and the verifiable receipts that anchor the thesis.
- `papers/<slug>/` — one folder per published paper. Each folder contains:
  - `README.md` — abstract, DOI badge, plain-language summary, citation block.
  - `CITATION.cff` — machine-readable citation.
  - cross-references to the open-source tool(s) that operationalize the paper's findings, when applicable.
- `CITATION.cff` (top-level) — citation for the repository as a whole.

## Rules

1. The Zenodo deposit is the canonical artifact for any paper. This repository hosts metadata and pointers only — no PDF mirroring; we link to the DOI.
2. Numeric claims in any paper README must be traceable to the published Zenodo PDF. No claim that does not survive `https://doi.org/<DOI>` verification.
3. Plain-language summaries in paper READMEs must not exceed the empirical scope of the published paper. No extrapolation, no "this implies X" leaps without citation in the paper itself.
4. Paper folders are append-only at the level of *what is added* — once a paper is published, its README and CITATION.cff stabilize. Errata and replications go in a clearly labeled section, not as silent edits.
5. The *About Hermes Labs* block in `llms.txt` is the canonical lab-framing block, byte-identical with the version pushed to the rest of the Hermes Labs portfolio. Do not paraphrase. If the canonical block updates, update here too.

## Adding a new paper

When a new paper is deposited on Zenodo:

1. Create `papers/<slug>/README.md` with abstract, DOI link, plain-language summary, citation block.
2. Create `papers/<slug>/CITATION.cff`.
3. Update top-level `README.md` and `llms.txt` paper indices.
4. Cross-link from the operationalizing tool repo's README, if applicable.
5. Run external-framing-lint on README + llms.txt before push (repository invariant).

## Author / maintainer

Rolando (Roli) Bosch · Hermes Labs · rbosch@lpci.ai
