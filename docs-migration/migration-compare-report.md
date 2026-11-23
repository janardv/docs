# Compare migration report

Scope: Compare module only (`concepts/analysis-and-reporting/compare/**`). Legacy `docs-new/compare/**` and `docs-new/scenarios/compare-scenarios` left untouched. App repo read-only. Redirects not applied.

## Pages created

| Target path | Migration action | Legacy sources used | support-docs sources used | App sources used |
|---|---|---|---|---|
| `concepts/analysis-and-reporting/compare` | MOVE (landing) | `docs-new/compare/what-is-a-compare` | none dedicated | Model/board compare surfaces |
| `concepts/analysis-and-reporting/compare/what-is-a-compare` | MOVE | `docs-new/compare/what-is-a-compare` | — | Compare modes |
| `concepts/analysis-and-reporting/compare/time-compare` | MOVE | `docs-new/compare/time-compare` | — | Model grid + board chart compare |
| `concepts/analysis-and-reporting/compare/scenario-compare` | MOVE (+ merge decision content) | `docs-new/compare/scenario-compare` + useful decision framing from `docs-new/scenarios/compare-scenarios` | — | ComparisonScenarioPicker; Default Scenario |

Also updated: `docs.json` Concepts → Analysis and reporting → Compare; `concepts/index.mdx`.

## Scenario Compare handling

- Canonical Concepts page: `concepts/analysis-and-reporting/compare/scenario-compare`
- Merged decision-focused content from Legacy Scenarios → Compare scenarios (baseline, focus, pre-governance compare)
- Rewrote `Main Scenario` → **Default Scenario**
- Cross-linked Scenarios module for create/lock/merge ownership
- No Scenarios Concepts duplicate page (per `ia-decisions.md`)

## Content merge decisions

### Preserved

- Time vs scenario compare split
- Model grid variance / multi-compare framing
- Board chart comparison framing
- Scenario decision examples and baseline guidance
- Screenshot `fr-scenario-compare.png`

### Rewritten

- Default Scenario terminology
- Transactions wording (formerly databases) in time-compare surfaces list
- Cross-links to Concepts Scenarios / Views / Boards / Time
- Omitted broken `fr-time-compare.png` reference (file missing; known pre-existing broken link)

### Added

- Landing Cards
- Explicit statement that this module owns deep scenario comparison
- Link to Legacy merge scenarios until that page migrates

### Omitted

- Publishing a Scenarios → Compare scenarios Concepts page
- Inventing compare UI chrome beyond Legacy + inventory

## Terminology decisions

| Legacy / target | Product UI | Choice |
|---|---|---|
| Main Scenario | Default Scenario | **Default Scenario** |
| Compare scenarios (Scenarios child) | Analysis Compare | Canonical under Compare |
| databases | Transactions | **Transactions** |

## IA gaps

| Legacy path | Recommendation | Temporary links used? |
|---|---|---|
| `docs-new/scenarios/compare-scenarios` | **ARCHIVE from Scenarios target** / redirect to Scenario compare at cutover | content merged; source untouched |
| Missing `fr-time-compare.png` | Replace screenshot later | image omitted |

## Validation

| Check | Result |
|---|---|
| Files exist | Pass (4) |
| docs.json paths valid | Pass |
| Internal links valid | Pass |
| Referenced images exist | Pass (`fr-scenario-compare.png`; time-compare image intentionally omitted) |
| Unrelated Legacy unchanged | Pass |
| Mintlify validate | Pass for Concepts Compare; **5 pre-existing** Legacy missing-nav-page errors unchanged |
| Mintlify broken-links | Pass for Concepts Compare; **15 pre-existing** broken links unchanged (includes Legacy `fr-time-compare.png`) |

## Unresolved questions

1. Capture a current time-compare screenshot to replace the missing Legacy asset.
2. How deep should board-specific compare controls be documented here versus Boards → Chart interaction?

## Completeness

Mapped Compare target set is safe to mark complete (4/4). Scenario Compare is canonical here.
