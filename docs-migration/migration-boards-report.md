# Boards migration report

Scope: Boards module only (`concepts/analysis-and-reporting/boards/**`). Legacy `docs-new/boards/**` and `support-docs/boards/**` left untouched. App repo read-only. Redirects not applied.

## Pages created

| Target path | Migration action | Legacy sources used | support-docs sources used | App sources used |
|---|---|---|---|---|
| `concepts/analysis-and-reporting/boards` | MOVE (landing) | `docs-new/boards/what-is-a-board` | twin | Library Boards; **Create Board** |
| `concepts/analysis-and-reporting/boards/what-is-a-board` | MOVE | Prefer richer `docs-new/boards/what-is-a-board` | twin | CreateEntityMenu **Create Board** |
| `concepts/analysis-and-reporting/boards/board-layout` | MOVE | `docs-new/boards/board-layout` | twin | Slash menu item labels |
| `concepts/analysis-and-reporting/boards/charts` | REPLACE | Salvaged setup/display from `docs-new/boards/charts` | twin | Setup/Display tabs; Chart insert |
| `concepts/analysis-and-reporting/boards/chart-types-catalog` | CREATE | — | — | SetupTab chart type labels (14) |
| `concepts/analysis-and-reporting/boards/chart-interaction` | MOVE | `docs-new/boards/chart-interaction` (+ overlap from `board-interaction`) | twin / board-interaction | Card header Date/Compare/Filter/Config |
| `concepts/analysis-and-reporting/boards/tables-on-boards` | REPLACE | `docs-new/boards/tables-on-boards` | twin | Table vs Pivot vs embeds |
| `concepts/analysis-and-reporting/boards/kpi-and-summary-blocks` | REPLACE | `docs-new/boards/kpi-and-summary-blocks` | twin | Slash **Metric Block** |
| `concepts/analysis-and-reporting/boards/sharing-boards` | MOVE | `docs-new/boards/sharing-boards` | twin | Share roles View/Edit/Full Access |
| `concepts/analysis-and-reporting/boards/board-best-practices` | MOVE | `docs-new/boards/board-best-practices` | twin | Concepts vs How-to boundary note |
| `concepts/analysis-and-reporting/boards/pivot-tables` | CREATE | — | — | Slash **Pivot Table** |
| `concepts/analysis-and-reporting/boards/model-block` | CREATE | — | — | Slash **Model** picker insert |
| `concepts/analysis-and-reporting/boards/dimension-block` | CREATE | — | — | Slash **Dimension** picker insert |
| `concepts/analysis-and-reporting/boards/transactions-block` | CREATE | — | — | Slash **Transactions** picker insert |
| `concepts/analysis-and-reporting/boards/code-block-on-boards` | CREATE | — | — | Slash **Code block (AI)** when artifacts enabled |

Also updated: `docs.json` Concepts → Analysis and reporting → Boards; `concepts/index.mdx`.

## Content merge decisions

### Preserved

- Board purpose, create framing, layout hierarchy
- Chart setup/display concepts and interaction patterns
- KPI summary guidance
- Sharing and best practices
- Screenshots: boards, create, add-card, chart-config, display, interactions, kpi, share

### Rewritten

- **+ New board** / left-nav Boards → Library **Boards** + **Create Board**
- Teamspace → **Space**
- Charts no longer claim only Bar/Line/Metric; catalog documents full Setup set
- KPI page centered on **Metric Block** insert label
- Databases → **Transactions** in sharing/embeds
- Frame/alt markup

### Added

- Chart types catalog (14 Setup labels)
- Pivot / Model / Dimension / Transactions / Code block pages (minimal, app-backed)
- Concepts vs How-to boundary note on best practices
- Availability note for code block

### Omitted

- Exhaustive board collaboration websocket / env details
- Step-by-step operating cadences (How-to)
- Inventing undocumented Metric Block capacity numbers beyond Legacy “up to 4” claim without re-verify — Legacy claim softened to “group related headline metrics”
- Deep publishing/export flows (flag-gated; Sharing basics Legacy link only)

## Terminology decisions

| Legacy / target | Product UI | Choice |
|---|---|---|
| + New board | **Create Board** | Create Board |
| Metric chart type | **Metric Block** | Metric Block |
| Database embed | **Transactions** | Transactions |
| Teamspace | Spaces | **Space** |
| Code block | **Code block (AI)** | Code block (AI), availability-gated |

## IA gaps / Boards IA issues

| Item | Recommendation | Temporary links used? |
|---|---|---|
| `docs-new/boards/board-interaction` | **merge** into Chart interaction (largely done); archive later | conceptual fold |
| `docs-new/views/using-views-on-boards` | **add/merge** under Boards or Views | yes from Tables page |
| Board realtime collaboration depth | **review** later under Boards or Comments | not documented beyond share |
| Exact Metric Block max metrics | Re-verify in UI; Legacy “up to 4” softened | — |
| Code block GA posture | Keep availability note until GA | documented as gated |

## Validation

| Check | Result |
|---|---|
| Files exist | Pass (15) |
| docs.json paths valid | Pass |
| Internal links valid | Pass |
| Referenced images exist | Pass |
| Unrelated Legacy unchanged | Pass |
| Mintlify validate | Pass for Concepts Boards; **5 pre-existing** Legacy missing-nav-page errors unchanged |
| Mintlify broken-links | Pass for Concepts Boards; **15 pre-existing** broken links unchanged |

## Unresolved questions

1. Should board collaboration get its own Concepts child?
2. Promote using-views-on-boards into Boards IA?
3. Confirm Metric Block capacity and display toggles against current Setup/Display UI for a follow-up polish pass.

## Completeness

Mapped Boards target set is safe to mark complete (15/15), with gated code-block availability noted and collaboration depth deferred.
