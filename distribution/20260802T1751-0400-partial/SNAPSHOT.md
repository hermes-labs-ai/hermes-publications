# OTH paper distribution snapshot — 2026-08-02 17:51 EDT

> **PARTIAL SNAPSHOT — NOT THE COMPLETE DISTRIBUTION STATE**

```text
state: PARTIAL_SNAPSHOT
captured_at_local: 2026-08-02 17:51 EDT
captured_at_utc: 2026-08-02 21:51 UTC
public_effect: NONE
canonical_state_claim: NONE
goal_relation: EXTENDS
```

## Snapshot identity

- Repository: `/Users/rbr_lpci/Documents/oth/repositories/hermes-publications`
- Branch observed: `codex/public-research-hub-link-20260802`
- Git SHA observed: `6e79f0b967d0e03f67bdb96ac3a5dc2bb9275ba6`
- Canonical paper index: [`../../publications.json`](../../publications.json)
- Operational distribution workspace:
  `/Users/rbr_lpci/Documents/oth/distribution/`
- Unrelated pre-existing dirty state preserved: untracked Python `__pycache__`
  directories under `scripts/` and `tests/`

## Scope

This snapshot reconciles the August 2 discussion with prior local receipts and
fresh read-only verification. It covers the four-paper scholarly-discovery and
machine-distribution surfaces most likely to be accidentally repeated.

It does not establish the complete state of social distribution, email,
newsletters, repository submissions, platform accounts, audience response, or
all prior side-chat work.

## What this snapshot established

| Surface | State at cutoff | Evidence | Continuation consequence |
|---|---|---|---|
| Four-paper DOI index | `CONFIRMED_LOCAL` | E-001 | Do not create a duplicate index or deposit. |
| DataCite DOI registration | `CONFIRMED_PUBLIC` for all four | E-005 | Treat DOI identity as covered. |
| OpenAlex | `CONFIRMED_PUBLIC` for all four | E-005 | Do not resubmit existing corrections; later readback may update counts. |
| OpenAIRE | `CONFIRMED_PUBLIC` for all four | E-006 | No new OpenAIRE deposit or submission is justified. |
| Google Scholar crawl preparation | `WAITING` | E-003, E-004 | Search Console and IndexNow work is already done; do not repeat it. Current exact per-paper Scholar presence remains `UNKNOWN_CURRENT`. |
| Semantic Scholar | `UNEVALUATED_TITLE_RECONCILIATION` | E-003, E-009 | DOI lookup did not establish presence; do not upgrade to a global absence claim. |
| BASE | `UNKNOWN_ACCESS_CHALLENGE` | E-004, E-009 | Do not claim presence or absence without an authorized readback path. |
| Publication hub CFF coverage | `CONFIRMED_LOCAL` for all four paper entries | E-007 | CFF is not a missing hub surface. Root paper-repository semantics remain separate. |
| Site crawl surfaces | `CONFIRMED_PRIOR_READBACK` | E-008 | Sitemap, robots, `llms.txt`, `llms-full.txt`, and paper JSON-LD are already covered. |
| Canonical RSS/Atom feed | `CONFIRMED_GAP` | E-010 | This is additive work; local preparation is safe, deployment is owner-gated. |
| Live publication JSON endpoints | `CONFIRMED_GAP` | E-010 | Local exports exist, but stable website endpoints were not live at cutoff. |

## Highest-value additive direction

The strongest durable addition identified here is a canonical Atom or RSS feed
generated from `publications.json`, plus live website endpoints for the existing
`publications.json` and `publications.jsonld` exports. This is a distribution
infrastructure hypothesis, not evidence of future ranking, traffic, citations,
or downloads.

## Explicit exclusions

- No paper metadata, DOI record, PDF, publication README, or citation export
  was changed.
- No Google Scholar, OpenAIRE, OpenAlex, Semantic Scholar, BASE, ResearchGate,
  Zenodo community, or other submission was made.
- No website, repository, account, email, post, deployment, release, or public
  profile was changed.
- No causal attribution from impressions, views, or downloads was inferred.
