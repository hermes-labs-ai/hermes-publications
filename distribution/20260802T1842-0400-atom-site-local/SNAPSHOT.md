# OTH paper distribution snapshot — 2026-08-02 18:42 EDT

> **LOCAL WEBSITE INTEGRATION — NO PUBLIC DEPLOYMENT**

```text
state: LOCAL_WEBSITE_INTEGRATION_READY
captured_at_local: 2026-08-02 18:42 EDT
captured_at_utc: 2026-08-02 22:42 UTC
public_effect: NONE
canonical_public_state_claim: ATOM_ENDPOINT_404_AND_DISCOVERY_LINK_ABSENT
supersedes_in_part: E-010, E-012
```

## Completed artifact

- The canonical publication repository now contains the deterministic Atom
  feed and discovery kit in local commit `1580909`.
- An isolated website worktree based on public `origin/main` commit `ebe8f15`
  now serves the exact feed bytes at `/atom.xml` and advertises them from the
  root HTML with `rel="alternate" type="application/atom+xml"`.
- The website integration is frozen in local commit `eb7b71a` on branch
  `codex/atom-discovery-20260802`.

## Measured local behavior

- A production build completed successfully.
- A local production server returned `/atom.xml` with HTTP 200,
  `Content-Type: application/xml`, and SHA-256
  `b4012e349550ad3396d2c76726dfc72280cf6e3252b11e03a46fcfeafd38026b`.
- The rendered homepage contained the Atom discovery link.

## Boundary

Neither branch was pushed. No PR, deployment, submission, message, or other
public mutation occurred. Crossref Event Data remains excluded as a rationale
because the service was sunset in April 2026.

## Contemporaneous public baseline

At 2026-08-02 22:45 UTC, `https://hermes-labs.ai/atom.xml` returned HTTP 404
from Vercel and the rendered homepage contained neither `/atom.xml` nor an
`application/atom+xml` link. This read-only baseline is the comparison point
for the parked deployment; it is not a distribution effect.

PARKED: owner authorization for the exact two branch pushes and website deployment, followed by readback of `https://hermes-labs.ai/atom.xml` and the homepage discovery link.
