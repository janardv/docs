# Feed migration report

Scope: Feed Concepts page with availability note. Flag-gated. Legacy had no docs-new page.

## Pages created

| Target path | Action | Legacy | support-docs | App |
|---|---|---|---|---|
| `concepts/ai-and-agents/feed` | CREATE | — | — | `/feeds`; `FeatureFlagRouteGate` `feeds-enabled`; sidebar Feed |

## Feature flag / availability

| Environment posture (from inventory / registry tests) | `feeds-enabled` |
|---|---|
| local / sandbox | On by default |
| development / staging / production | Off by default |

Publication policy: published with **clear availability note**; not presented as GA across all workspaces.

## Content

### Added
- Availability section with plain-language env posture
- Modest purpose statement when Feed is present

### Omitted
- Deep Feed UX walkthrough as if universally available
- Flag admin / flag name as customer setup procedure (flag name only in report + brief availability parenthetical)

## Terminology

Sidebar / page: **Feed**

## IA gaps

| Item | Status |
|---|---|
| Feed relation to Notifications | Linked lightly; not merged |
| Production GA promotion | Pending product |

## Validation

Page in Concepts nav with availability caveat. No claim of universal GA.

## Unresolved questions

1. When Feed becomes default-on in production.
2. Whether Feed belongs under AI Concepts long-term vs collaboration.
