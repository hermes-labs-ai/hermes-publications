# Distribution status — local website integration

## Complete locally

- `LOCAL_COMMIT` — publication feed, source generator, discovery kit, and
  evidence assets at `1580909`.
- `LOCAL_COMMIT` — website static feed and root discovery link at `eb7b71a`,
  based on current public `origin/main` `ebe8f15`.
- `VERIFIED_LOCAL` — source/feed byte equality, XML parsing, ESLint, Next.js
  production build, HTTP 200, `application/xml`, homepage discovery link, and
  served-byte SHA all passed.

## Still parked

- Push `codex/public-research-hub-link-20260802`, including feed commit
  `1580909` and this snapshot, to `hermes-labs-ai/hermes-publications` after
  re-reading the exact branch head for the owner arm.
- Push `codex/atom-discovery-20260802` at `eb7b71a` to
  `roli-lpci/hermes-labs-v2`, open the exact PR, merge/deploy through the normal
  website route, and perform one public readback.

## Public baseline

- `CONFIRMED_PUBLIC_READBACK` — at 2026-08-02 22:45 UTC, the live Atom URL
  returned HTTP 404 and the live homepage had no Atom discovery link.

## Nonclaims

- The public feed was absent at the exact baseline time; later state requires a
  fresh readback.
- No discovery, indexing, subscription, citation, traffic, or download effect
  is claimed.
- The Atom landing-page semantics do not claim Crossref Event Data support.

PARKED: exact owner authorization is required for the named pushes and deployment.
