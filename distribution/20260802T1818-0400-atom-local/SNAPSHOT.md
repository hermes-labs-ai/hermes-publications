# OTH paper distribution snapshot — 2026-08-02 18:18 EDT

> **LOCAL IMPLEMENTATION SNAPSHOT — NO PUBLIC DEPLOYMENT**

```text
state: LOCAL_IMPLEMENTATION_READY
captured_at_local: 2026-08-02 18:18 EDT
captured_at_utc: 2026-08-02 22:18 UTC
public_effect: NONE
canonical_public_state_claim: NONE
supersedes_in_part: E-010
```

## What changed

- `publications.json` now deterministically generates an Atom 1.0 feed at
  [`../../atom.xml`](../../atom.xml).
- Each entry keeps its DOI URL as the stable Atom ID and a `related` link,
  while its `alternate` link points to the human-readable Hermes research
  landing page. The feed is newest-first, clock-independent, and covered by
  exporter tests and stale-output checks.
- A reusable [four-paper discovery copy kit](../assets/four-paper-discovery-kit-20260802.md)
  and [asset-use README](../assets/README.md) are locally prepared for a future
  specifically authorized owned surface.

## What did not change

- `https://hermes-labs.ai/atom.xml` was not deployed or rechecked.
- No website, paper metadata, DOI record, repository, account, submission,
  email, post, release, or public profile changed.
- No Crossref Event Data optimization or onboarding is proposed. An earlier
  coordination lead based on the legacy Newsfeed guide is retracted: Crossref's
  current notice says Event Data became unavailable on 2026-04-23.
- The 17:51 snapshot remains the authority for its public readbacks and channel
  reconstruction except where this snapshot records new local implementation.

## Result

The local Atom-generation gap in E-010 is resolved. The public-endpoint gap is
not resolved. The landing-page links are ordinary feed semantics, not a
Crossref-ingestion claim. The copy kit is a prepared asset, not distribution
evidence.

PARKED: expose `atom.xml` on an owned public surface only after an exact website change and deployment are separately authorized.
