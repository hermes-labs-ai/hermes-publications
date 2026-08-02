# Evidence ledger — local website integration

| ID | Observation | Class | Exact source | Status / scope limit |
|---|---|---|---|---|
| E-017 | Publication feed and discovery assets are frozen in a local repository commit. | `CONFIRMED_LOCAL` | `/Users/rbr_lpci/Documents/oth/repositories/hermes-publications`; commit `1580909` | Local branch only; not pushed. Supersedes E-012 only by adding commit identity. |
| E-018 | The isolated website candidate serves the exact canonical feed and advertises it in root HTML. | `CONFIRMED_LOCAL` | `/Users/rbr_lpci/Documents/oth/tmp/hermes-site-atom-20260802`; commit `eb7b71a`; base `ebe8f15` | Local worktree only; no public endpoint claim. |
| E-019 | The website candidate passed lint and production build; local production HTTP returned the exact feed bytes and discovery link. | `CONFIRMED_LOCAL` | `npm run lint`; `npm run build`; local `next start -p 3210`; served feed SHA-256 `b4012e349550ad3396d2c76726dfc72280cf6e3252b11e03a46fcfeafd38026b` | Deterministic local behavior only. Public availability and downstream effects remain `UNEVALUATED`. |

## Supersession

- E-017 adds a local commit boundary to E-012; it does not change the public
  state.
- E-018 resolves the local website-integration gap identified after E-012.
- E-010 remains current for the absence of a verified public Atom endpoint.

PARKED: no public effect is licensed by this ledger.
