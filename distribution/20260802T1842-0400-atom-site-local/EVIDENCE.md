# Evidence ledger — local website integration

| ID | Observation | Class | Exact source | Status / scope limit |
|---|---|---|---|---|
| E-017 | Publication feed and discovery assets are frozen in a local repository commit. | `CONFIRMED_LOCAL` | `/Users/rbr_lpci/Documents/oth/repositories/hermes-publications`; commit `1580909` | Local branch only; not pushed. Supersedes E-012 only by adding commit identity. |
| E-018 | The isolated website candidate serves the exact canonical feed and advertises it in root HTML. | `CONFIRMED_LOCAL` | `/Users/rbr_lpci/Documents/oth/tmp/hermes-site-atom-20260802`; commit `eb7b71a`; base `ebe8f15` | Local worktree only; no public endpoint claim. |
| E-019 | The website candidate passed lint and production build; local production HTTP returned the exact feed bytes and discovery link. | `CONFIRMED_LOCAL` | `npm run lint`; `npm run build`; local `next start -p 3210`; served feed SHA-256 `b4012e349550ad3396d2c76726dfc72280cf6e3252b11e03a46fcfeafd38026b` | Deterministic local behavior only. Public availability and downstream effects remain `UNEVALUATED`. |
| E-020 | The live Atom endpoint returned HTTP 404 and the rendered live homepage contained no Atom URL or `application/atom+xml` discovery link. | `CONFIRMED_PUBLIC_READBACK` | `https://hermes-labs.ai/atom.xml`; `https://hermes-labs.ai/`; captured 2026-08-02 22:45 UTC; 404 body SHA-256 `69908bf0576a5fe7418059a17f6f0a03cdba14183f5e07fc173a08ccbaed4410` | Contemporaneous absence baseline only; does not predict later state or measure discovery impact. |

## Supersession

- E-017 adds a local commit boundary to E-012; it does not change the public
  state.
- E-018 resolves the local website-integration gap identified after E-012.
- E-020 refreshes E-010 with a direct current public absence baseline.

PARKED: no public effect is licensed by this ledger.
