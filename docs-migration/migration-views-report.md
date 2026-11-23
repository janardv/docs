# Views migration report

Scope: Views module only (`concepts/analysis-and-reporting/views/**`). Legacy `docs-new/views/**` and `support-docs/views/**` left untouched. App repo read-only. Redirects not applied.

## Pages created

| Target path | Migration action | Legacy sources used | support-docs sources used | App sources used |
|---|---|---|---|---|
| `concepts/analysis-and-reporting/views` | MOVE (landing) | `docs-new/views/what-is-a-view` | twin (shorter) | ViewsBar; model/Transactions views |
| `concepts/analysis-and-reporting/views/what-is-a-view` | MOVE | Prefer `docs-new/views/what-is-a-view`; folded connection idea from support `view-behavior` | `view-behavior` (partial) | ViewsBar |
| `concepts/analysis-and-reporting/views/filters-sorts-and-grouping` | MOVE | `docs-new/views/filters-sorts-and-grouping` | twin | ViewsBar filters |
| `concepts/analysis-and-reporting/views/compare-in-views` | MOVE | `docs-new/views/compare-in-views` | twin | Views as prep surface; deep compare → Analysis Compare |
| `concepts/analysis-and-reporting/views/view-best-practices` | MOVE | `docs-new/views/view-best-practices` | twin | — |

Also updated: `docs.json` Concepts → Analysis and reporting → Views; `concepts/index.mdx`.

## Content merge decisions

### Preserved

- View definition and source-connected behavior
- Filter / sort / grouping guidance
- Best practices
- Screenshots `fr-views.png`, `fr-view-filter.png`

### Rewritten

- Database → **Transactions** wording
- Compare-in-views points to Analysis Compare for deep comparison (no Scenarios duplicate)
- Frame/alt image markup
- Cross-links to migrated Time / Compare / Views paths

### Added

- Landing Cards
- Temporary Legacy links for creating/configuring, sharing, using-on-boards orphans
- Note that private views are not supported (from Legacy sharing-views)

### Omitted

- Auto-creating Concepts pages for creating-and-configuring, sharing-views, using-views-on-boards, private-vs-shared, view-behavior
- Teaching private views as a current product capability (support-docs private-vs-shared conflicts with docs-new sharing-views)

## Terminology decisions

| Legacy / target | Product UI | Choice |
|---|---|---|
| database view | Transactions views | **Transactions** view |
| Compare scenarios (Legacy link) | Analysis Compare | Link Scenario compare Concepts page |
| Private views | Not supported (docs-new) | State unsupported; do not document as available |

## IA gaps (strong Legacy omitted from target)

| Legacy path | Recommendation | Temporary links used? |
|---|---|---|
| `docs-new/views/creating-and-configuring-views` | **add** under Views or **merge** into What is a view | yes |
| `docs-new/views/sharing-views` | **add** under Views (sharing is substantial) | yes |
| `docs-new/views/using-views-on-boards` | **merge** into Boards tables / layout, or **add** Views child | yes |
| `support-docs/views/private-vs-shared-views` | **archive later** / do not promote; conflicts with “private views not yet supported” | no (content contradicted) |
| `support-docs/views/view-behavior` | **merge** into What is a view (partially done) | conceptual fold only |

## Validation

| Check | Result |
|---|---|
| Files exist | Pass (5) |
| docs.json paths valid | Pass |
| Internal links valid | Pass |
| Referenced images exist | Pass |
| Unrelated Legacy unchanged | Pass |
| Mintlify validate | Pass for Concepts Views; **5 pre-existing** Legacy missing-nav-page errors unchanged |
| Mintlify broken-links | Pass for Concepts Views; **15 pre-existing** broken links unchanged |

## Unresolved questions

1. Promote creating/configuring and sharing into target IA before cutover?
2. Where should using-views-on-boards live long-term — Views or Boards?

## Completeness

Mapped Views target set is safe to mark complete for staged migration (5/5), with orphan IA follow-ups recorded.
