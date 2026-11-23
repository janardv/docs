# Core concepts migration report (Batch C)

Scope: Core concepts area + real Concepts landing. Legacy untouched. App read-only. Redirects deferred. Settings/Admin and Resources not migrated in this batch.

## Pages created / updated

| Path | Action | Legacy / support sources |
|---|---|---|
| `concepts/index` | REPLACE (landing) | Temporary migration placeholder |
| `concepts/core-concepts/what-is-oculon` | MOVE | `docs-new/getting-started/what-is-oculon` |
| `concepts/core-concepts/how-oculon-is-organized` | MOVE | `docs-new/getting-started/how-oculon-is-organized` |
| `concepts/core-concepts/core-concepts-overview` | RENAME/MOVE | `docs-new/getting-started/core-concepts-overview` |
| `concepts/core-concepts/how-data-flows-through-oculon` | CREATE | Adapted from how-oculon-is-organized + current module map |
| `concepts/core-concepts/glossary` | MOVE | `docs-new/getting-started/glossary` (+ selective terms from `oculon-glossary`) |

`docs.json`: added **Core concepts** group after Overview.

## Migration actions summary

| Action | Count |
|---|---|
| REPLACE | 1 (landing) |
| MOVE | 3 |
| RENAME/MOVE | 1 (overview path) |
| CREATE | 1 (how data flows) |

## Terminology updates

| Legacy / older | Concepts choice |
|---|---|
| Databases | **Transactions** (Database kept as glossary alias) |
| Main Scenario | **Default Scenario** |
| Teamspaces only | **Spaces** umbrella + Teamspace / Private Space |
| Typo “Dimensi'ons.” | Fixed to Dimensions |
| Marketing-only claims | Omitted |

## Content preserved

- Product purpose and spreadsheet contrast from What is Oculon
- Layered organization framing
- Core object intro (variables, dimensions, time, formulas, models/views/boards)
- Glossary definitions updated for current terms
- Hero image `fr-oculon.png`

## Content removed / not promoted as outdated

- Databases as primary public term
- Broken/duplicate definitions from `oculon-glossary` (e.g. wrong Pages/Linked Items copy)
- Templates / Artifacts as GA glossary entries
- Detailed feature duplication (links to modules instead)
- Dedicated Sidebar Concepts page (Resources / How-to later; light mention only)

## Cross-links added

- Landing grouped by current Concepts sidebar modules (only existing / availability-noted pages)
- Core pages cross-link to Workspaces, Spaces, Transactions, Models, Scenarios, Views, Compare, Boards, AI, Projects
- Explicit note that Settings Security/Billing/Workspace settings remain for Batch D / Legacy

## Unresolved conceptual gaps

- Resources (shortcuts, sidebar deep dive, troubleshooting) still Legacy / Batch E
- Settings/Admin deep pages still Batch D
- Library hub / Integrations still not dedicated Concepts parents
- Time rollups still Legacy orphan (non-blocking)
- Using-views-on-boards still Legacy

## Validation

| Check | Result |
|---|---|
| Core files exist | Pass (5 + landing) |
| docs.json Core concepts group | Pass |
| Landing `/concepts/...` targets resolve | Pass (validated by script) |
| Image `fr-oculon.png` | Pass |
| Legacy / support-docs | Untouched |
| Mintlify | Pre-existing Legacy noise only; no new Concepts errors |

## Cutover readiness

**Core concepts is cutover-ready** for the Conceptual entry experience (What is Oculon decision: published under Core concepts). Remaining cutover blockers before full Legacy replacement are **Batch D Settings/Admin** and **Batch E Resources (+ redirects)**, not Core concepts content.
