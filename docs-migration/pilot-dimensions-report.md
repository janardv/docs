# Dimensions Pilot Migration Report

Pilot module only. Legacy `docs-new/dimensions/**` and `support-docs/dimensions/**` were left untouched. No redirects added. App repo was not modified.

## Pages created

| Target path | Migration action | Legacy sources used | App sources used |
|---|---|---|---|
| `concepts/data-and-structure/dimensions` | MOVE (landing synthesized from parent IA + overview content) | `docs-new/dimensions/what-is-a-dimension` (intro/image); target child list | Library **Dimensions** tab; `/library/dimensions` |
| `concepts/data-and-structure/dimensions/what-is-a-dimension` | MOVE | `docs-new/dimensions/what-is-a-dimension` (= support twin) | Library route; create label **Create Dimension** |
| `concepts/data-and-structure/dimensions/create-and-edit-dimensions` | RENAME | `docs-new/dimensions/create-and-edit-dimension` (no support twin) | `CreateEntityMenu` (**Create Dimension**); Library empty state; model **Add Dimension** / **Breakdown by**; dimension details **+ New Value**; Add column **Linked dimension** / **Lookup** |
| `concepts/data-and-structure/dimensions/dimension-values` | MOVE | `docs-new/dimensions/dimension-values` + support-docs Frame/alt improvement | **+ New Value**; **Hierarchy link** column label |
| `concepts/data-and-structure/dimensions/using-dimensions-with-variables` | MOVE | `docs-new/dimensions/using-dimensions-with-variables` (= support twin) | Variable **Add Dimension**; **Breakdown by** attach/create flow |
| `concepts/data-and-structure/dimensions/dimension-operations` | MOVE | Prefer `docs-new/dimensions/dimension-operations` (richer than support-docs twin) | **+ New Value**; **Linked dimension**; **Lookup** |
| `concepts/data-and-structure/dimensions/dimension-best-practices` | MOVE | `docs-new/dimensions/dimension-best-practices` (= support twin) | Library shared-dimension reuse pattern |

Also updated (pilot-related only):

- `concepts/index.mdx` — points readers at Dimensions and Concepts Legacy
- `docs.json` Concepts tab — minimum nav: Overview + Data and structure → Dimensions children

## Content merge decisions

### Preserved

- Core explanations of what dimensions are, why they matter, and when to add one
- Create from Library vs create while modeling structure
- Dimension values guidance (stability, hierarchy)
- Attach-to-variable, aggregate formula, and reporting impact content
- docs-new operations depth: add/edit values, linked dimensions, lookups, relationship examples, caution/cleanup
- Best-practice bullets and reporting-audience guidance
- Existing screenshot assets under `/images/getting-started/fr-*.png`

### Rewritten

- Image markup: bare `![](...)` → `<Frame>` + descriptive `alt` (aligned with support-docs dimension-values improvement and Mintlify writing standards)
- Headings normalized to sentence case where needed
- Create-flow copy: replaced outdated “page panel” wording with current **Add Dimension** / **Breakdown by**
- Create/edit: replaced unverified “`product 1` / `product 2` auto placeholders” with verified **+ New Value** editing guidance
- Linked-dimension / lookup labels aligned to current Add column menu (**Linked dimension**, **Lookup**)
- Landing page added as a Concepts parent with Cards into child pages
- Internal links retargeted to `/concepts/data-and-structure/dimensions/...`

### Added

- Library **Dimensions** entry point and **Create Dimension** label
- Model attach path via **Add Dimension** / **Breakdown by**
- **Hierarchy link** mention on values (supported in Add column menu)
- Cross-links among new Concepts Dimension pages
- Related sections at page ends

### Omitted

- support-docs `dimension-operations` shortened “Common operations” list (docs-new content is more complete and matches screenshots)
- Deep documentation of dimension property types (Text, Person, URL, etc.) and dimension-variable columns (`NEXT_PUBLIC_DIMENSION_VARIABLES_ENABLED`) — not in legacy customer pages; avoid expanding scope
- Dual coreV2 vs legacy implementation paths — internal only
- Redirects from `/docs-new/dimensions/*` (explicitly deferred)
- Any non-Dimensions modules

## Terminology decisions

| Legacy / target wording | Current product UI | Pilot choice |
|---|---|---|
| Dimensions | Library tab **Dimensions** | Keep **Dimensions** |
| Create and edit dimensions (plural slug) | Button **Create Dimension** | Page title plural per target IA; UI bolded as **Create Dimension** |
| docs-new slug `create-and-edit-dimension` | — | New path uses plural `create-and-edit-dimensions` |
| “Dimension list page” | Library **Dimensions** | Prefer Library **Dimensions** |
| “page panel” (create-from-model) | Variable **Add Dimension** / **Breakdown by** | Use current UI labels |
| Add Values | **+ New Value** | Use **+ New Value** |
| Create Links / linking columns | **Linked dimension** | Use **Linked dimension** |
| Dimension Lookups | **Lookup** | Use **Lookup** |
| Hierarchy (conceptual) | **Hierarchy link** column | Mention **Hierarchy link** where hierarchy is discussed |
| Variables / models / views / boards | Same terms | Unchanged; links stay conceptual (those Concepts pages not migrated yet) |

No Transactions/Databases or Plan/Planning conflicts inside this module.

## Validation

| Check | Result |
|---|---|
| All new MDX files exist | Pass — 7 Dimension pages + updated `concepts/index.mdx` |
| `docs.json` paths valid | Pass — all Concepts Dimension paths resolve to MDX files |
| Internal links in new Dimension pages | Pass — all `/concepts/data-and-structure/dimensions/...` links resolve |
| Referenced images | Pass — all 9 `/images/getting-started/fr-*` assets exist |
| Mintlify `validate` | Fail only on **5 pre-existing** Concepts Legacy missing-nav-page orphans (`actuals-and-forecast-boundary`, `cloning-and-versioning`, `model-organization`, `private-vs-shared-views`, `view-behavior`). **No errors for new Concepts Dimension pages.** |
| Mintlify `broken-links` | 15 broken links in 8 files — **none** in `concepts/data-and-structure/dimensions*`. Pre-existing Legacy/support/essentials issues only. |
| Legacy Dimensions docs untouched | Pass — `git status` clean for `docs-new/dimensions` and `support-docs/dimensions` |

## Issues / questions

1. **Default placeholder members**: Legacy claimed auto `product 1` / `product 2` after create. Client create APIs only send `{ name, workspace_id }`. Softened wording pending product confirmation of server defaults.
2. **Property / dimension-variable columns**: Add column menu exposes Text, Person, Single select, Multi-select, Status, Hierarchy link, Lookup, and (when enabled) dimension variables. Customer depth for these types is still thin; decide whether a later Dimensions or Variables page should cover them.
3. **Relationship cardinality examples** (many-to-one / one-to-many): Preserved from docs-new. Product design should confirm they still match how Linked dimension / multi-select behave.
4. **Screenshot freshness**: Reused existing `fr-*` assets. Some may predate current Library chrome; visual QA recommended.
5. **Redirects**: Not added. When Concepts becomes canonical, map `/docs-new/dimensions/*` (and support twins) → new Concepts paths, including singular → plural create slug.
6. **Concepts index**: Still a migration placeholder; only Dimensions is live under the new tab.

## Pilot learnings

This migration pattern is **safe to reuse** for similar MOVE-heavy modules (Variables, Time, Formulas, Models, Scenarios, Views):

1. Prefer `docs-new` as primary body; merge support-docs only when it improves accessibility (Frame/alt) or unique content.
2. Create a parent landing page even when Legacy only listed children.
3. Apply RENAME carefully (here: plural create slug) without deleting Legacy files.
4. Ground UI labels in app sources before rewriting create/edit flows; drop unverified defaults.
5. Keep Concepts nav minimal: Overview + the migrating sidebar group only.
6. Leave Legacy + redirects until a later cutover step.
7. Expect Mintlify validate noise from known Legacy orphans; treat new-path cleanliness as the pilot gate.

**Caution for next modules:** Databases/Transactions and AI Plan vs Planning need terminology REVIEW before the same MOVE pattern. Flag-gated modules (Projects, Templates, Artifacts, Feed) should not follow this publish-now path.
