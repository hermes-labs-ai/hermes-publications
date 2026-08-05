# Distribution work status at snapshot cutoff

This status is scoped to the evidence in this snapshot. It is not the complete
Hermes Labs distribution queue.

## Completed or already covered

- `CONFIRMED_LOCAL` — four-paper DOI index and generated JSON/JSON-LD/BibTeX
  exports exist in this repository. Evidence: E-001.
- `CONFIRMED_PUBLIC` — DataCite and OpenAlex cover all four records. Evidence:
  E-005.
- `CONFIRMED_PUBLIC` — OpenAIRE exact DOI queries cover all four records.
  Evidence: E-006.
- `CONFIRMED_LOCAL` — hub CFF coverage exists for all four paper entries.
  Evidence: E-007.
- `CONFIRMED_PRIOR_READBACK` — sitemap, robots, paper pages, `llms.txt`,
  `llms-full.txt`, and structured paper metadata are technically reachable.
  Evidence: E-008.
- `WAITING` — Google owned-site crawl preparation, Search Console, and IndexNow
  were already handled. Evidence: E-003.

## Additive open work

- `OPEN_LOCAL` — specify and prepare a canonical Atom or RSS feed generated
  from `publications.json`. Recheck E-010 immediately before work.
- `OPEN_LOCAL` — specify stable website endpoints for the existing
  `publications.json` and `publications.jsonld` exports.
- `UNEVALUATED` — decide whether a GitHub release surface adds discovery value
  without triggering or implying a duplicate Zenodo deposit.
- `UNEVALUATED` — research eligibility for feed-aware scholarly aggregators
  only after a canonical feed exists; Paperity and Rogue Scholar are leads, not
  established routes.

## Unknown or waiting on access/propagation

- `UNKNOWN_CURRENT` — exact current Google Scholar presence for each DOI/title.
  Do not repeat crawl requests merely to answer this.
- `UNEVALUATED_TITLE_RECONCILIATION` — Semantic Scholar.
- `UNKNOWN_ACCESS_CHALLENGE` — BASE exact-DOI presence.
- `WAITING_EXTERNAL` — existing OpenAlex identity/profile corrections.
- `UNKNOWN_CAUSAL_EFFECT` — whether any distribution action caused a view or
  download change.

## Parked or owner-gated

- Deploying a feed or live catalog endpoint.
- Pushing this documentation or any repository change.
- Posting, emailing, submitting, publishing, creating a release, changing a
  profile, or accessing an owner-authenticated account.
- Any paid acquisition experiment.

## Superseded observations

- `SUPERSEDED` — Generative Horizon OpenAlex absence on 2026-07-30; superseded
  by the later all-four OpenAlex readback in E-005.
- `SUPERSEDED` — blanket OpenAIRE uncertainty for the two newer papers;
  superseded by E-006.
- `SUPERSEDED_IN_PART` — blanket “CFF unknown” language; hub coverage is
  confirmed by E-007, while root-repository semantics remain separate.

## One continuation target

`NEXT: inspect the current website source and prepare, without deploying, the
smallest feed and live-catalog implementation contract derived from
publications.json.`
