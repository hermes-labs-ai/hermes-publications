# Evidence and provenance ledger

This ledger records the evidence used by the 2026-08-02 17:51 EDT partial
snapshot. A path or URL is a pointer; the status column states what the cited
observation actually supports.

| ID | Observation | Class | Exact source | Observed or captured | Status / scope limit |
|---|---|---|---|---|---|
| E-001 | The repository indexes four DOI-anchored papers. | `CONFIRMED_LOCAL` | [`../../publications.json`](../../publications.json), repo SHA `6e79f0b967d0e03f67bdb96ac3a5dc2bb9275ba6` | 2026-08-02 17:51 EDT | Current for this checkout only. |
| E-002 | A 30-source distribution audit already covered Scholar, Semantic Scholar, ResearchGate, Zenodo communities, LinkedIn, YouTube, Reddit, ResearchHub, PhilArchive, Substack, Bluesky, Hacker News, LessWrong, attribution, and paid trials. | `CONFIRMED_LOCAL` | `/Users/rbr_lpci/Documents/oth/distribution/GROWTH-TO-2000-1000.md` | Updated 2026-08-01 21:23 EDT | Do not restart the broad channel inventory without a new question. |
| E-003 | Scholar crawl preparation and one-time Search Console/IndexNow requests are already live or accepted; OpenAlex corrections await moderation; Semantic Scholar is not estimable from the earlier probe. | `CONFIRMED_LOCAL` | `/Users/rbr_lpci/Documents/oth/distribution/publication-ops/MORNING-RETURN.md` | 2026-08-01 | Operational handoff; later public readback wins. |
| E-004 | The July 30 Generative Horizon index census found OpenAIRE and DataCite present, Scholar absent at that time, OpenAlex absent at that time, Semantic Scholar rate-limited, and BASE access-challenged. | `CONFIRMED_LOCAL` | `/Users/rbr_lpci/Documents/oth/distribution/receipts/index-census-20260730T173230Z.json` | 2026-07-30 17:32:30 UTC | OpenAlex absence is superseded by E-005. Scholar and BASE are not current global absence claims. |
| E-005 | All four records were present in OpenAlex; citation counts were 2, 2, 2, and 18 by record order in the receipt. DataCite records were present. | `CONFIRMED_PUBLIC_RECEIPT` | `/Users/rbr_lpci/Documents/oth/distribution/receipts/measurement-20260801T070752Z.json` | 2026-08-01 07:07:52 UTC | Counts are historical observations and may drift. |
| E-006 | Exact DOI queries returned one OpenAIRE result for each paper. | `CONFIRMED_PUBLIC_READBACK` | `https://api.openaire.eu/search/publications?doi=10.5281%2Fzenodo.18867694&format=json`; `https://api.openaire.eu/search/publications?doi=10.5281%2Fzenodo.19042469&format=json`; `https://api.openaire.eu/search/publications?doi=10.5281%2Fzenodo.21652317&format=json`; `https://api.openaire.eu/search/publications?doi=10.5281%2Fzenodo.21659634&format=json` | 2026-08-02 | Current readback at cutoff; no submission performed. |
| E-007 | Hub CFF files exist for the repository and all four paper entries. The prior validator receipt explains why paper-root `type: article` CFF files are not valid CFF 1.2 top-level records. | `CONFIRMED_LOCAL` | [`../../CITATION.cff`](../../CITATION.cff); [`../../papers/`](../../papers/); `/Users/rbr_lpci/Documents/oth/distribution/receipts/cff-validation-older-papers-20260730.json` | 2026-08-02 | File presence is confirmed. Do not relabel a paper as software or dataset merely to satisfy a root-file validator. |
| E-008 | Homepage, research pages, `robots.txt`, sitemap, `llms.txt`, `llms-full.txt`, GitHub organization, and tested paper pages were technically reachable; the sentinel did not establish global indexing or ranking. | `CONFIRMED_PRIOR_READBACK` | `/Users/rbr_lpci/Documents/oth/distribution/discoverability-audit/runs/2026-07-31/pilot/baseline-summary.md` | 2026-07-31 | Accessibility is not indexing, ranking, or audience reach. |
| E-009 | Current reconstruction retains Scholar as `UNKNOWN_CURRENT`, Semantic Scholar title reconciliation as `UNEVALUATED`, and BASE as `UNKNOWN`. | `INHERITED_NOT_REVALIDATED` | E-003, E-004, plus 2026-08-02 bounded supporting-agent review | 2026-08-02 | Preserve source-specific uncertainty. |
| E-010 | `/rss.xml`, `/atom.xml`, and `/feed.xml` returned HTTP 404; live `/publications.json` and `/publications.jsonld` endpoints were not found, while local exports exist. | `CONFIRMED_PUBLIC_READBACK` | `https://hermes-labs.ai/rss.xml`; `https://hermes-labs.ai/atom.xml`; `https://hermes-labs.ai/feed.xml`; `https://hermes-labs.ai/publications.json`; `https://hermes-labs.ai/publications.jsonld` | 2026-08-02 | Verified gap at cutoff; recheck before implementation or deployment. |
| E-011 | The user requested an efficient agent-facing distribution folder and explicitly required it to be labeled as a partial August 2 snapshot. | `OWNER_STATED` | Current Codex task, 2026-08-02 | 2026-08-02 17:51 EDT | Authorizes local documentation only, not a public effect. |

## Supersession notes

- E-005 supersedes only the July 30 OpenAlex-absence observation in E-004.
- E-006 supersedes earlier blanket uncertainty about OpenAIRE coverage for the
  four-paper set.
- E-007 resolves “is there hub CFF coverage?” but does not claim every
  paper-specific root repository has a valid top-level CFF.
- A later fresh public readback supersedes this snapshot for the exact surface
  it checks. It does not silently rewrite this ledger.
