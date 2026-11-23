# Concepts migration map

_Planning only. Derived from `current-docs-inventory.md`, `target-concepts-structure.md`, and `app-feature-inventory.md`. No docs.json, MDX, redirects, or app changes in this step._

## How to read actions

| Action | Meaning |
|---|---|
| **KEEP** | Adequate as-is; copy into Concepts with path/nav wiring only |
| **MOVE** | Adapt a docs-new page into the planned Concepts path (Legacy stays until cutover) |
| **RENAME** | MOVE plus title and/or slug change |
| **MERGE** | Combine sources, or split one source across multiple targets |
| **REPLACE** | Keep topic; rewrite using app + legacy |
| **CREATE** | No usable customer docs source |
| **ARCHIVE** | Cleanup of Legacy/support after cutover (see cleanup section) |
| **REVIEW** | Blocked on terminology, IA, or release decision |

**Redirect `yes`:** plan redirect from current public docs-new/support URL when Concepts becomes canonical.

**Totals:** 147 target pages mapped (+ Model History, Scenario governance, Merge scenarios; − Scenarios Compare scenarios as a target). Plus one non-target ARCHIVE row for Legacy Scenarios → Compare scenarios.

_IA decisions applied from `ia-decisions.md` (planning only). Previously completed module migrations (Dimensions, Variables, Time, Formulas, Models, Scenarios published pages) remain intact; this update remaps targets/actions only._

| Action | Count |
|---|---:|
| MOVE | 79 |
| RENAME | 15 |
| MERGE | 4 |
| REPLACE | 8 |
| CREATE | 39 |
| REVIEW | 2 |
| ARCHIVE (non-target cleanup row) | 1 |

## Core concepts

| Target page | Planned path | Parent | Legacy docs-new | support-docs | App / internal | Action | Reason | Preserve | Add from app | Redirect | Flag | Confidence | Open question |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Core concepts overview | concepts/core-concepts/core-concepts-overview | Core concepts overview | docs-new/getting-started/core-concepts-overview | support-docs/getting-started/core-concepts-overview | — | RENAME | Move under Core concepts; leave Legacy until cutover | Concept definitions | Library/FP&A framing; link How data flows | yes | none | high | Also move what-is-oculon / how-oculon-is-organized? |
| Glossary | concepts/core-concepts/glossary | Glossary | docs-new/getting-started/glossary | support-docs/getting-started/glossary | — | MOVE | Solid glossary | Term definitions | Transactions as primary term; Database as alias; Artifacts/Feed/Projects | yes | none | high | — |
| How data flows through Oculon | concepts/core-concepts/how-data-flows-through-oculon | How data flows through Oculon | related: docs-new/getting-started/how-oculon-is-organized | support-docs/getting-started/how-oculon-is-organized | Library → model/boards mental model | CREATE | No dedicated page | N/A | End-to-end entity flow | no | none | medium | MERGE from how-oculon-is-organized? |

## Data and structure

| Target page | Planned path | Parent | Legacy docs-new | support-docs | App / internal | Action | Reason | Preserve | Add from app | Redirect | Flag | Confidence | Open question |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Transactions | concepts/data-and-structure/transactions | Transactions | docs-new/databases/what-is-a-database (landing) | support-docs/databases/what-is-a-database | Library Transactions; /databases/[id]; CreateEntityMenu | RENAME | IA decision A: public term Transactions; Legacy Databases = alias/source | Accurate explanations/screenshots | Create Transactions; Library tab; glossary alias for Database | yes (from /docs-new/databases/*) | none | high | Decided: Transactions publicly |
| What is a transaction | concepts/data-and-structure/transactions/what-is-a-transaction | Transactions | docs-new/databases/what-is-a-database | support-docs/databases/what-is-a-database | Library Transactions; /databases/[id]; CreateEntityMenu | RENAME | Title/slug Database → Transaction | Accurate explanations | Transactions UI labels; optional Legacy alias note | yes | none | high | — |
| Transaction types | concepts/data-and-structure/transactions/transaction-types | Transactions | docs-new/databases/database-types | support-docs/databases/database-types | Library Transactions; /databases/[id]; CreateEntityMenu | RENAME | Noun slug/title → Transaction | Accurate explanations | Any new types | yes | none | high | — |
| Transaction structure | concepts/data-and-structure/transactions/transaction-structure | Transactions | docs-new/databases/database-structure | support-docs/databases/database-structure | Library Transactions; /databases/[id]; CreateEntityMenu | RENAME | Noun slug/title → Transaction | Accurate explanations | Column/property model | yes | none | high | — |
| Working with data | concepts/data-and-structure/transactions/working-with-data | Transactions | docs-new/databases/working-with-data | support-docs/databases/working-with-data | Library Transactions; /databases/[id]; CreateEntityMenu | RENAME | Path root databases → transactions; verb title kept | Accurate explanations | Grid edit/share | yes | none | high | — |
| Linked data | concepts/data-and-structure/transactions/linked-data | Transactions | docs-new/databases/linked-data | support-docs/databases/linked-data | Library Transactions; /databases/[id]; CreateEntityMenu | RENAME | Path root databases → transactions; verb title kept | Accurate explanations | Links to models/dimensions | yes | none | high | — |
| Refresh and sync behavior | concepts/data-and-structure/transactions/refresh-and-sync-behavior | Transactions | docs-new/databases/refresh-and-sync-behavior | support-docs/databases/refresh-and-sync-behavior | Library Transactions; /databases/[id]; CreateEntityMenu | RENAME | Path root databases → transactions; verb title kept | Accurate explanations | Integration sync states | yes | none | high | — |
| Transaction best practices | concepts/data-and-structure/transactions/transaction-best-practices | Transactions | docs-new/databases/database-best-practices | support-docs/databases/database-best-practices | Library Transactions; /databases/[id]; CreateEntityMenu | RENAME | Noun slug/title → Transaction | Accurate explanations | Naming consistency with Transactions | yes | none | high | — |
| Variables | concepts/data-and-structure/variables | Variables | docs-new/variables/what-is-a-variable | support-docs/variables/what-is-a-variable | features/variables; model grid; Planning currency | MOVE | Parent landing | Definitions/examples that still match | Current UI labels | yes | none | high | — |
| What is a variable | concepts/data-and-structure/variables/what-is-a-variable | Variables | docs-new/variables/what-is-a-variable | support-docs/variables/what-is-a-variable | features/variables; model grid; Planning currency | MOVE | Core definition | Definitions/examples that still match | Current UI labels | yes | none | high | — |
| Variable types | concepts/data-and-structure/variables/variable-types | Variables | docs-new/variables/variable-types | support-docs/variables/variable-types | features/variables; model grid; Planning currency | MOVE | Type catalog | Definitions/examples that still match | Current UI labels | yes | none | high | — |
| Create and edit variables | concepts/data-and-structure/variables/create-and-edit-variables | Variables | docs-new/variables/create-and-edit-variables | support-docs/variables/create-and-edit-variables | features/variables; model grid; Planning currency | MOVE | Create/edit flows | Definitions/examples that still match | Current UI labels | yes | none | high | — |
| Variable breakdown | concepts/data-and-structure/variables/variable-breakdown | Variables | docs-new/variables/variable-breakdown | support-docs/variables/variable-breakdown | features/variables; model grid; Planning currency | MOVE | Breakdown | Definitions/examples that still match | Current UI labels | yes | none | high | — |
| Variable formatting | concepts/data-and-structure/variables/variable-formatting | Variables | docs-new/variables/variable-formatting | support-docs/variables/variable-formatting | features/variables; model grid; Planning currency | MOVE | Formatting | Definitions/examples that still match | Current UI labels | yes | none | high | — |
| Variable behavior | concepts/data-and-structure/variables/variable-behavior | Variables | docs-new/variables/variable-behavior | support-docs/variables/variable-behavior | features/variables; model grid; Planning currency | REPLACE | Strengthen actual/planned vs last actual | Definitions/examples that still match | Last actual interaction; currency overlap | yes | none | high | — |
| Variable references | concepts/data-and-structure/variables/variable-references | Variables | docs-new/variables/variable-references | support-docs/variables/variable-references | features/variables; model grid; Planning currency | MOVE | References | Definitions/examples that still match | Current UI labels | yes | none | high | — |
| Variable best practices | concepts/data-and-structure/variables/variable-best-practices | Variables | docs-new/variables/variable-best-practices | support-docs/variables/variable-best-practices | features/variables; model grid; Planning currency | MOVE | Guidance | Definitions/examples that still match | Current UI labels | yes | none | high | — |
| Currency and conversion | concepts/data-and-structure/variables/currency-and-conversion | Variables | — (no docs-new) | support-docs/oculon-basics/currency-and-conversion | features/variables; model grid; Planning currency | CREATE | Only support-docs currency page | Definitions/examples that still match | Last actual interaction; currency overlap | no | none | medium | Shared with Planning defaults? |
| Dimensions | concepts/data-and-structure/dimensions | Dimensions | docs-new/dimensions/what-is-a-dimension | support-docs/dimensions/what-is-a-dimension | Library dimensions; coreV2 | MOVE | Existing | Definitions and workflows | coreV2 properties if docs lag | yes | none | high | — |
| What is a dimension | concepts/data-and-structure/dimensions/what-is-a-dimension | Dimensions | docs-new/dimensions/what-is-a-dimension | support-docs/dimensions/what-is-a-dimension | Library dimensions; coreV2 | MOVE | Existing | Definitions and workflows | coreV2 properties if docs lag | yes | none | high | — |
| Create and edit dimensions | concepts/data-and-structure/dimensions/create-and-edit-dimensions | Dimensions | docs-new/dimensions/create-and-edit-dimension | support-docs/dimensions/create-and-edit-dimension | Library dimensions; coreV2 | RENAME | Target plural slug vs file create-and-edit-dimension | Definitions and workflows | coreV2 properties if docs lag | yes | none | high | Confirm final slug |
| Dimension values | concepts/data-and-structure/dimensions/dimension-values | Dimensions | docs-new/dimensions/dimension-values | support-docs/dimensions/dimension-values | Library dimensions; coreV2 | MOVE | Existing | Definitions and workflows | coreV2 properties if docs lag | yes | none | high | — |
| Using dimensions with variables | concepts/data-and-structure/dimensions/using-dimensions-with-variables | Dimensions | docs-new/dimensions/using-dimensions-with-variables | support-docs/dimensions/using-dimensions-with-variables | Library dimensions; coreV2 | MOVE | Existing | Definitions and workflows | coreV2 properties if docs lag | yes | none | high | — |
| Dimension operations | concepts/data-and-structure/dimensions/dimension-operations | Dimensions | docs-new/dimensions/dimension-operations | support-docs/dimensions/dimension-operations | Library dimensions; coreV2 | MOVE | Existing | Definitions and workflows | coreV2 properties if docs lag | yes | none | high | — |
| Dimension best practices | concepts/data-and-structure/dimensions/dimension-best-practices | Dimensions | docs-new/dimensions/dimension-best-practices | support-docs/dimensions/dimension-best-practices | Library dimensions; coreV2 | MOVE | Existing | Definitions and workflows | coreV2 properties if docs lag | yes | none | high | — |
| Time | concepts/data-and-structure/time | Time | docs-new/time/time-in-oculon | support-docs/time/time-in-oculon | Model time_params; Planning; FISCAL_ROLLUP QA | MOVE | Existing; note Last actual gap | Granularity/relative/aggregation text | Last actual boundary; optional time-rollups orphan | yes | NEXT_PUBLIC_MODEL_TIME_GRANULARITY_ENABLED (partial) | high | Add Last actual date to target? |
| Time in Oculon | concepts/data-and-structure/time/time-in-oculon | Time | docs-new/time/time-in-oculon | support-docs/time/time-in-oculon | Model time_params; Planning; FISCAL_ROLLUP QA | MOVE | Existing | Granularity/relative/aggregation text | Last actual boundary; optional time-rollups orphan | yes | NEXT_PUBLIC_MODEL_TIME_GRANULARITY_ENABLED (partial) | high | — |
| Time granularity | concepts/data-and-structure/time/time-granularity | Time | docs-new/time/time-granularity | support-docs/time/time-granularity | Model time_params; Planning; FISCAL_ROLLUP QA | MOVE | Existing | Granularity/relative/aggregation text | Last actual boundary; optional time-rollups orphan | yes | NEXT_PUBLIC_MODEL_TIME_GRANULARITY_ENABLED (partial) | high | — |
| Relative time | concepts/data-and-structure/time/relative-time | Time | docs-new/time/relative-time | support-docs/time/relative-time | Model time_params; Planning; FISCAL_ROLLUP QA | MOVE | Existing | Granularity/relative/aggregation text | Last actual boundary; optional time-rollups orphan | yes | NEXT_PUBLIC_MODEL_TIME_GRANULARITY_ENABLED (partial) | high | — |
| Time aggregation | concepts/data-and-structure/time/time-aggregation | Time | docs-new/time/time-aggregation | support-docs/time/time-aggregation | Model time_params; Planning; FISCAL_ROLLUP QA | MOVE | Existing | Granularity/relative/aggregation text | Last actual boundary; optional time-rollups orphan | yes | NEXT_PUBLIC_MODEL_TIME_GRANULARITY_ENABLED (partial) | high | — |
| Time best practices | concepts/data-and-structure/time/time-best-practices | Time | docs-new/time/time-best-practices | support-docs/time/time-best-practices | Model time_params; Planning; FISCAL_ROLLUP QA | MOVE | Existing | Granularity/relative/aggregation text | Last actual boundary; optional time-rollups orphan | yes | NEXT_PUBLIC_MODEL_TIME_GRANULARITY_ENABLED (partial) | high | — |

## Modeling

| Target page | Planned path | Parent | Legacy docs-new | support-docs | App / internal | Action | Reason | Preserve | Add from app | Redirect | Flag | Confidence | Open question |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Models | concepts/modeling/models | Models | docs-new/models/what-is-a-model | support-docs/models/what-is-a-model | app/(app)/model; model-grid; FORMULA/PLUGIN docs | MOVE | Existing; map FP&A naming. Migrated landing already published under Concepts. | Structure/settings/linked explanations | Link Model History; tags | yes | none | high | Cloning: no Concepts page (HOLD/ARCHIVE). Organization: HOLD outside Models. |
| What is a model | concepts/modeling/models/what-is-a-model | Models | docs-new/models/what-is-a-model | support-docs/models/what-is-a-model | app/(app)/model; model-grid; FORMULA/PLUGIN docs | MOVE | Existing (migrated) | Structure/settings/linked explanations | Current UI labels | yes | none | high | — |
| Model structure | concepts/modeling/models/model-structure | Models | docs-new/models/model-structure | support-docs/models/model-structure | app/(app)/model; model-grid; FORMULA/PLUGIN docs | MOVE | Existing (migrated) | Structure/settings/linked explanations | Current UI labels | yes | none | high | — |
| Model settings | concepts/modeling/models/model-settings | Models | docs-new/models/model-settings | support-docs/models/model-settings | app/(app)/model; model-grid; FORMULA/PLUGIN docs | MOVE | Existing (migrated) | Structure/settings/linked explanations | Current UI labels | yes | none | high | — |
| Model History | concepts/modeling/models/model-history | Models | docs-new/models/versioning (fold in) | support-docs/models/cloning-and-versioning (thin; do not treat as Clone product) | app/(app)/model/components/history/**; ModelDetailsHeader History; server/modelHistory | CREATE | App History UI; merge usable Legacy versioning into this page | Checkpoint/preview/restore explanations that match app | Toolbar History; Previewing version; Restore | no (versioning Legacy → redirect later to model-history) | none | high | Decided: Models child. No Clone page. |
| Model best practices | concepts/modeling/models/model-best-practices | Models | docs-new/models/model-best-practices | support-docs/models/model-best-practices | app/(app)/model; model-grid; FORMULA/PLUGIN docs | MOVE | Existing (migrated) | Structure/settings/linked explanations | Current UI labels | yes | none | high | — |
| Linked models | concepts/modeling/models/linked-models | Models | docs-new/models/linked-models | support-docs/models/linked-models | app/(app)/model; model-grid; FORMULA/PLUGIN docs | MOVE | Existing (migrated) | Structure/settings/linked explanations | Current UI labels | yes | none | high | — |
| Formulas | concepts/modeling/formulas | Formulas | docs-new/formulas/formula-basics | support-docs/formulas/formula-basics | model formula UI; FORMULA_ARCHITECTURE.md | MOVE | Mature docs-new set | Examples/function lists | Actual vs planned editing notes | yes | none | high | — |
| Formula basics | concepts/modeling/formulas/formula-basics | Formulas | docs-new/formulas/formula-basics | support-docs/formulas/formula-basics | model formula UI; FORMULA_ARCHITECTURE.md | MOVE | Mature docs-new set | Examples/function lists | Actual vs planned editing notes | yes | none | high | — |
| Formula editor | concepts/modeling/formulas/formula-editor | Formulas | docs-new/formulas/formula-editor | support-docs/formulas/formula-editor | model formula UI; FORMULA_ARCHITECTURE.md | MOVE | Mature docs-new set | Examples/function lists | Actual vs planned editing notes | yes | none | high | — |
| Functions | concepts/modeling/formulas/functions | Formulas | docs-new/formulas/functions | support-docs/formulas/functions | model formula UI; FORMULA_ARCHITECTURE.md | MOVE | Mature docs-new set | Examples/function lists | Actual vs planned editing notes | yes | none | high | — |
| Helper variables and modifiers | concepts/modeling/formulas/helper-variables-and-modifiers | Formulas | docs-new/formulas/helper-variables-and-modifiers | support-docs/formulas/helper-variables-and-modifiers | model formula UI; FORMULA_ARCHITECTURE.md | MOVE | Mature docs-new set | Examples/function lists | Actual vs planned editing notes | yes | none | high | — |
| Common formula patterns | concepts/modeling/formulas/common-formula-patterns | Formulas | docs-new/formulas/common-formula-patterns | support-docs/formulas/common-formula-patterns | model formula UI; FORMULA_ARCHITECTURE.md | MOVE | Mature docs-new set | Examples/function lists | Actual vs planned editing notes | yes | none | high | — |
| Formula errors | concepts/modeling/formulas/formula-errors | Formulas | docs-new/formulas/formula-errors | support-docs/formulas/formula-errors | model formula UI; FORMULA_ARCHITECTURE.md | MOVE | Mature docs-new set | Examples/function lists | Actual vs planned editing notes | yes | none | high | — |
| Formula best practices | concepts/modeling/formulas/formula-best-practices | Formulas | docs-new/formulas/formula-best-practices | support-docs/formulas/formula-best-practices | model formula UI; FORMULA_ARCHITECTURE.md | MOVE | Mature docs-new set | Examples/function lists | Actual vs planned editing notes | yes | none | high | — |
| Scenarios | concepts/modeling/scenarios | Scenarios | docs-new/scenarios/what-is-a-scenario | support-docs/scenarios/what-is-a-scenario | ScenarioPicker; SCENARIO_AWARE_CACHE_* | MOVE | Existing (migrated landing). Link to Analysis Compare for comparison. | Create/override/sync guidance | Cross-link governance, merge, Analysis Scenario compare | yes | none | high | — |
| What is a scenario | concepts/modeling/scenarios/what-is-a-scenario | Scenarios | docs-new/scenarios/what-is-a-scenario | support-docs/scenarios/what-is-a-scenario | ScenarioPicker; SCENARIO_AWARE_CACHE_* | MOVE | Existing (migrated) | Create/override/sync guidance | Default Scenario terminology | yes | none | high | — |
| Create and manage scenarios | concepts/modeling/scenarios/create-and-manage-scenarios | Scenarios | docs-new/scenarios/create-and-manage-scenarios | support-docs/scenarios/create-and-manage-scenarios | ScenarioPicker; SCENARIO_AWARE_CACHE_* | MOVE | Existing (migrated) | Create/manage flows | New Scenario; Duplicate | yes | none | high | — |
| Scenario sync behavior | concepts/modeling/scenarios/scenario-sync-behavior | Scenarios | docs-new/scenarios/scenario-sync-behavior | support-docs/scenarios/scenario-sync-behavior | ScenarioPicker; SCENARIO_AWARE_CACHE_* | MOVE | Existing (migrated). Inheritance without inventing auto-sync toggle. | Inheritance explanations that match product | Do not document unverified auto-sync control | yes | none | high | — |
| Scenario overrides | concepts/modeling/scenarios/scenario-overrides | Scenarios | docs-new/scenarios/scenario-overrides | support-docs/scenarios/scenario-overrides | ScenarioPicker; SCENARIO_AWARE_CACHE_* | MOVE | Existing (migrated) | Override mechanics | Current UI labels | yes | none | high | — |
| Scenario governance and access | concepts/modeling/scenarios/scenario-governance-and-access | Scenarios | docs-new/scenarios/scenario-governance-and-access | support twin if present | ScenarioPicker Allow Changes / Allow Merging; Share; Default Scenario delete rules | MOVE | Dedicated child per ia-decisions | Lock/merge/visibility rules | Allow Changes; Allow Merging; Default Scenario safeguards | yes | none | high | Rewrite Main → Default Scenario; drop speculative future copy |
| Merge scenarios | concepts/modeling/scenarios/merge-scenarios | Scenarios | docs-new/scenarios/merge-scenarios | support twin if present | Allow Merging; Merge Changes UI | MOVE | Supported companion to governance | Directional merge guidance matching app | Merge Changes entry points | yes | none | high | — |
| _(non-target)_ Compare scenarios | _(removed from Scenarios IA)_ | — | docs-new/scenarios/compare-scenarios | support-docs/scenarios/compare-scenarios | Comparison via Analysis Compare | ARCHIVE | Dedupe: Analysis → Scenario compare owns deep compare | N/A — do not publish under Scenarios | Scenarios pages link conceptually to Compare | yes → concepts/.../compare/scenario-compare | none | high | Decided: ACCEPT recommendation |
| Versioning and snapshots | concepts/modeling/scenarios/versioning-and-snapshots | Scenarios | docs-new/scenarios/versioning-and-snapshots | support-docs/scenarios/versioning-and-snapshots | ScenarioPicker; SCENARIO_AWARE_CACHE_* | MOVE | Existing (migrated) | Snapshot guidance that still matches | Current UI labels | yes | none | high | Distinct from Model History |
| Scenario best practices | concepts/modeling/scenarios/scenario-best-practices | Scenarios | docs-new/scenarios/scenario-best-practices | support-docs/scenarios/scenario-best-practices | ScenarioPicker; SCENARIO_AWARE_CACHE_* | MOVE | Existing (migrated) | Guidance | Cross-link Analysis Scenario compare | yes | none | high | — |

## Analysis and reporting

| Target page | Planned path | Parent | Legacy docs-new | support-docs | App / internal | Action | Reason | Preserve | Add from app | Redirect | Flag | Confidence | Open question |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Views | concepts/analysis-and-reporting/views | Views | docs-new/views/what-is-a-view | support-docs/views/what-is-a-view | ViewsBar; model/dimension views | MOVE | Existing views docs | Filter/sort/save flows | Library Recents/Favorites/Shared | yes | none | high | Include private-vs-shared orphans? |
| What is a view | concepts/analysis-and-reporting/views/what-is-a-view | Views | docs-new/views/what-is-a-view | support-docs/views/what-is-a-view | ViewsBar; model/dimension views | MOVE | Existing views docs | Filter/sort/save flows | Library Recents/Favorites/Shared | yes | none | high | — |
| Filters, sorts, and grouping | concepts/analysis-and-reporting/views/filters-sorts-and-grouping | Views | docs-new/views/filters-sorts-and-grouping | support-docs/views/filters-sorts-and-grouping | ViewsBar; model/dimension views | MOVE | Existing views docs | Filter/sort/save flows | Library Recents/Favorites/Shared | yes | none | high | — |
| Compare in views | concepts/analysis-and-reporting/views/compare-in-views | Views | docs-new/views/compare-in-views | support-docs/views/compare-in-views | ViewsBar; model/dimension views | MOVE | Existing views docs | Filter/sort/save flows | Library Recents/Favorites/Shared | yes | none | high | — |
| View best practices | concepts/analysis-and-reporting/views/view-best-practices | Views | docs-new/views/view-best-practices | support-docs/views/view-best-practices | ViewsBar; model/dimension views | MOVE | Existing views docs | Filter/sort/save flows | Library Recents/Favorites/Shared | yes | none | high | — |
| Compare | concepts/analysis-and-reporting/compare | Compare | docs-new/compare/what-is-a-compare | support twin if present | COMPARE_QA; ComparisonScenarioPicker | MOVE | Existing compare docs | Compare modes | Cross-link Scenarios | yes | none | high | — |
| What is a compare | concepts/analysis-and-reporting/compare/what-is-a-compare | Compare | docs-new/compare/what-is-a-compare | support twin if present | COMPARE_QA; ComparisonScenarioPicker | MOVE | Existing compare docs | Compare modes | Cross-link Scenarios | yes | none | high | — |
| Time compare | concepts/analysis-and-reporting/compare/time-compare | Compare | docs-new/compare/time-compare | support twin if present | COMPARE_QA; ComparisonScenarioPicker | MOVE | Existing compare docs | Compare modes | Cross-link Scenarios | yes | none | high | — |
| Scenario compare | concepts/analysis-and-reporting/compare/scenario-compare | Compare | docs-new/compare/scenario-compare | support twin if present | COMPARE_QA; ComparisonScenarioPicker | MOVE | Canonical scenario comparison page (ia-decisions). Scenarios module links here; no Scenarios duplicate. | Compare modes | Cross-link Scenarios landing/best practices | yes | none | high | Decided: Analysis owns deep compare |
| Boards | concepts/analysis-and-reporting/boards | Boards | docs-new/boards/what-is-a-board | support-docs/boards/what-is-a-board | boards/[id]; ARTIFACTS_AND_CODE_BLOCKS; BOARD_COLLAB | MOVE | Existing | Layout/sharing basics | Full chart set; embeds; collab | yes | none | high | — |
| What is a board | concepts/analysis-and-reporting/boards/what-is-a-board | Boards | docs-new/boards/what-is-a-board | support-docs/boards/what-is-a-board | boards/[id]; ARTIFACTS_AND_CODE_BLOCKS; BOARD_COLLAB | MOVE | Existing | Layout/sharing basics | Full chart set; embeds; collab | yes | none | high | — |
| Board layout | concepts/analysis-and-reporting/boards/board-layout | Boards | docs-new/boards/board-layout | support-docs/boards/board-layout | boards/[id]; ARTIFACTS_AND_CODE_BLOCKS; BOARD_COLLAB | MOVE | Existing | Layout/sharing basics | Full chart set; embeds; collab | yes | none | high | — |
| Charts | concepts/analysis-and-reporting/boards/charts | Boards | docs-new/boards/charts | support-docs/boards/charts | boards/[id]; ARTIFACTS_AND_CODE_BLOCKS; BOARD_COLLAB | REPLACE | Incomplete chart coverage | Layout/sharing basics | Full chart set; embeds; collab | yes | none | high | — |
| Chart types catalog | concepts/analysis-and-reporting/boards/chart-types-catalog | Boards | — | — | boards/[id]; ARTIFACTS_AND_CODE_BLOCKS; BOARD_COLLAB | CREATE | No docs-new; 14 types in app | N/A | Full chart set; embeds; collab | no | none | high | — |
| Chart interaction | concepts/analysis-and-reporting/boards/chart-interaction | Boards | docs-new/boards/chart-interaction | support-docs/boards/chart-interaction | boards/[id]; ARTIFACTS_AND_CODE_BLOCKS; BOARD_COLLAB | MOVE | Existing | Layout/sharing basics | Full chart set; embeds; collab | yes | none | high | — |
| Tables on boards | concepts/analysis-and-reporting/boards/tables-on-boards | Boards | docs-new/boards/tables-on-boards | support-docs/boards/tables-on-boards | boards/[id]; ARTIFACTS_AND_CODE_BLOCKS; BOARD_COLLAB | REPLACE | Missing embeds/pivot | Layout/sharing basics | Full chart set; embeds; collab | yes | none | high | — |
| KPI and summary blocks | concepts/analysis-and-reporting/boards/kpi-and-summary-blocks | Boards | docs-new/boards/kpi-and-summary-blocks | support-docs/boards/kpi-and-summary-blocks | boards/[id]; ARTIFACTS_AND_CODE_BLOCKS; BOARD_COLLAB | REPLACE | KPI is chartBlock viz | Layout/sharing basics | Full chart set; embeds; collab | yes | none | high | — |
| Sharing boards | concepts/analysis-and-reporting/boards/sharing-boards | Boards | docs-new/boards/sharing-boards | support-docs/boards/sharing-boards | boards/[id]; ARTIFACTS_AND_CODE_BLOCKS; BOARD_COLLAB | MOVE | Existing | Layout/sharing basics | Full chart set; embeds; collab | yes | publishing/exports related | high | — |
| Board best practices | concepts/analysis-and-reporting/boards/board-best-practices | Boards | docs-new/boards/board-best-practices | support-docs/boards/board-best-practices | boards/[id]; ARTIFACTS_AND_CODE_BLOCKS; BOARD_COLLAB | MOVE | Existing | Layout/sharing basics | Full chart set; embeds; collab | yes | none | high | — |
| Pivot tables | concepts/analysis-and-reporting/boards/pivot-tables | Boards | — | — | boards/[id]; ARTIFACTS_AND_CODE_BLOCKS; BOARD_COLLAB | CREATE | App slash Pivot Table | N/A | Full chart set; embeds; collab | no | none | high | — |
| Model block | concepts/analysis-and-reporting/boards/model-block | Boards | — | — | boards/[id]; ARTIFACTS_AND_CODE_BLOCKS; BOARD_COLLAB | CREATE | TipTap modelBlock | N/A | Full chart set; embeds; collab | no | none | high | — |
| Dimension block | concepts/analysis-and-reporting/boards/dimension-block | Boards | — | — | boards/[id]; ARTIFACTS_AND_CODE_BLOCKS; BOARD_COLLAB | CREATE | TipTap dimensionBlock | N/A | Full chart set; embeds; collab | no | none | high | — |
| Transactions block | concepts/analysis-and-reporting/boards/transactions-block | Boards | — | — | boards/[id]; ARTIFACTS_AND_CODE_BLOCKS; BOARD_COLLAB | CREATE | databaseBlock embed; public label Transactions | N/A | Slash menu Transactions; link Concepts Transactions | no | none | high | Decided: Transactions naming |
| Code block on boards | concepts/analysis-and-reporting/boards/code-block-on-boards | Boards | — | — | boards/[id]; ARTIFACTS_AND_CODE_BLOCKS; BOARD_COLLAB | CREATE | Artifacts-gated | N/A | Full chart set; embeds; collab | no | code-artifacts-enabled + ARTIFACTS_ENABLED | medium | — |

## AI and agents

| Target page | Planned path | Parent | Legacy docs-new | support-docs | App / internal | Action | Reason | Preserve | Add from app | Redirect | Flag | Confidence | Open question |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AI overview | concepts/ai-and-agents/ai-overview | AI overview | docs-new/ai/ai-in-oculon | support-docs/ai/ai-in-oculon | AIChat; AI_CHAT_* | REPLACE | Shared landing needs dedicated overview | Capability list | Map to Assistant/Workspace AI/Agents | yes | none | medium | Split vs keep shared page |
| Workspace AI | concepts/ai-and-agents/workspace-ai | Workspace AI | docs-new/ai/ai-in-oculon (inadequate) | — | SettingsWorkspaceAiDrawer | CREATE | No dedicated docs | Reusable blurbs | Defaults/Agents/Approvals/Tools; Lite/Pro/Max | no | none | high | — |
| AI assistant | concepts/ai-and-agents/ai-assistant | AI assistant | docs-new/ai/ai-in-oculon (shared) | — | /chat; AIChat | REPLACE | Needs assistant-specific landing | Entry points | Mentions; skills; floating chat | yes | none | medium | — |
| Modeling with AI | concepts/ai-and-agents/ai-assistant/modeling-with-ai | AI assistant | docs-new/ai/modeling-with-ai | support-docs/ai/modeling-with-ai | components/plan; AI chat | MOVE | Existing | Workflow steps | Plan editor behavior | yes | none | high | — |
| Reporting with AI | concepts/ai-and-agents/ai-assistant/reporting-with-ai | AI assistant | docs-new/ai/reporting-with-ai | support-docs/ai/reporting-with-ai | components/plan; AI chat | MOVE | Existing | Workflow steps | Plan editor behavior | yes | none | high | — |
| Plan mode | concepts/ai-and-agents/ai-assistant/plan-mode | AI assistant | docs-new/ai/plan-mode | support-docs/ai/plan-mode | components/plan; AI chat | REVIEW | Clarify Plan mode naming | Workflow steps | Plan editor behavior | yes | none | medium | Plans vs Planning vs Projects |
| Custom agents | concepts/ai-and-agents/custom-agents | Custom agents | docs-new/custom-agents/what-are-custom-agents | support-docs/custom-agents/what-are-custom-agents | /custom-agents; CUSTOM_AGENTS_FEEDS_*; settings nav commented out | MOVE | Existing; note discoverability | Setup/permissions | Nav/settings state; vs Agent Teams | yes | none | high | GA posture / hidden settings entry |
| What are custom agents | concepts/ai-and-agents/custom-agents/what-are-custom-agents | Custom agents | docs-new/custom-agents/what-are-custom-agents | support-docs/custom-agents/what-are-custom-agents | /custom-agents; CUSTOM_AGENTS_FEEDS_*; settings nav commented out | MOVE | Existing; note discoverability | Setup/permissions | Nav/settings state; vs Agent Teams | yes | none | high | GA posture / hidden settings entry |
| Create a custom agent | concepts/ai-and-agents/custom-agents/create-a-custom-agent | Custom agents | docs-new/custom-agents/create-a-custom-agent | support-docs/custom-agents/create-a-custom-agent | /custom-agents; CUSTOM_AGENTS_FEEDS_*; settings nav commented out | MOVE | Existing; note discoverability | Setup/permissions | Nav/settings state; vs Agent Teams | yes | none | high | GA posture / hidden settings entry |
| Agent context and knowledge | concepts/ai-and-agents/custom-agents/agent-context-and-knowledge | Custom agents | docs-new/custom-agents/agent-context-and-knowledge | support-docs/custom-agents/agent-context-and-knowledge | /custom-agents; CUSTOM_AGENTS_FEEDS_*; settings nav commented out | MOVE | Existing; note discoverability | Setup/permissions | Nav/settings state; vs Agent Teams | yes | none | high | GA posture / hidden settings entry |
| Agent actions | concepts/ai-and-agents/custom-agents/agent-actions | Custom agents | docs-new/custom-agents/agent-actions | support-docs/custom-agents/agent-actions | /custom-agents; CUSTOM_AGENTS_FEEDS_*; settings nav commented out | MOVE | Existing; note discoverability | Setup/permissions | Nav/settings state; vs Agent Teams | yes | none | high | GA posture / hidden settings entry |
| Agent permissions | concepts/ai-and-agents/custom-agents/agent-permissions | Custom agents | docs-new/custom-agents/agent-permissions | support-docs/custom-agents/agent-permissions | /custom-agents; CUSTOM_AGENTS_FEEDS_*; settings nav commented out | MOVE | Existing; note discoverability | Setup/permissions | Nav/settings state; vs Agent Teams | yes | none | high | GA posture / hidden settings entry |
| Agent connections | concepts/ai-and-agents/custom-agents/agent-connections | Custom agents | docs-new/custom-agents/agent-connections | support-docs/custom-agents/agent-connections | /custom-agents; CUSTOM_AGENTS_FEEDS_*; settings nav commented out | MOVE | Existing; note discoverability | Setup/permissions | Nav/settings state; vs Agent Teams | yes | none | high | GA posture / hidden settings entry |
| Agent safety and review | concepts/ai-and-agents/custom-agents/agent-safety-and-review | Custom agents | docs-new/custom-agents/agent-safety-and-review | support-docs/custom-agents/agent-safety-and-review | /custom-agents; CUSTOM_AGENTS_FEEDS_*; settings nav commented out | MOVE | Existing; note discoverability | Setup/permissions | Nav/settings state; vs Agent Teams | yes | none | high | GA posture / hidden settings entry |
| Agent best practices | concepts/ai-and-agents/custom-agents/agent-best-practices | Custom agents | docs-new/custom-agents/agent-best-practices | support-docs/custom-agents/agent-best-practices | /custom-agents; CUSTOM_AGENTS_FEEDS_*; settings nav commented out | MOVE | Existing; note discoverability | Setup/permissions | Nav/settings state; vs Agent Teams | yes | none | high | GA posture / hidden settings entry |
| Context and connections | concepts/ai-and-agents/context-and-connections | Context and connections | docs-new/ai/connectors | support-docs/ai/connectors | Connectors & MCP; Library Integrations | REPLACE | Must distinguish Integrations vs MCP | Connector concepts | Dual surfaces; authorize/mcp | yes | NEXT_PUBLIC_MCP_* | medium | Split Integrations out? |
| MCP | concepts/ai-and-agents/context-and-connections/mcp | Context and connections | docs-new/ai/mcp | support-docs/ai/mcp | /authorize/mcp | MOVE | Existing MCP docs | MCP setup | Authorize flow | yes | NEXT_PUBLIC_MCP_* | high | — |
| Skills | concepts/ai-and-agents/skills | Skills | docs-new/ai/skills | support-docs/ai/skills | SettingsSkillsDrawer | REVIEW | Placement Concepts vs Settings | Skills overview | All/My Skills | yes | none | medium | Keep in Concepts? |
| Knowledge and memory | concepts/ai-and-agents/knowledge-and-memory | Knowledge and memory | fragments only | — | server/memory; Settings AI; project memories | CREATE | No unified page | Agent knowledge blurbs | Personal/agent/project map | no | none | medium | — |
| Feed | concepts/ai-and-agents/feed | Feed | — | — | /feeds; CUSTOM_AGENTS_FEEDS_* | CREATE | Flag-gated; no docs-new | N/A | Feed UX + availability | no | feeds-enabled | high | — |
| Agent teams | concepts/ai-and-agents/agent-teams | Agent teams | — | — | /team; AgentTeams; flag off all envs | CREATE | Experimental default-off | N/A | Only if publishing experimental | no | agent-teams-enabled (off everywhere) | high | Hold from public docs? |

## Workspace and collaboration

| Target page | Planned path | Parent | Legacy docs-new | support-docs | App / internal | Action | Reason | Preserve | Add from app | Redirect | Flag | Confidence | Open question |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Workspaces | concepts/workspace-and-collaboration/workspaces | Workspaces | docs-new/workspace-and-organization/what-is-a-workspace | support-docs twin | /workspaces; onboarding | MOVE | Existing | Invite/request | Onboarding flows | yes | none | high | — |
| Teamspaces and private space | concepts/workspace-and-collaboration/teamspaces-and-private-space | Teamspaces and private space | docs-new/workspace-and-organization/teamspaces-and-organization | support-docs twin | Sidebar Spaces; SPACE_ICONS.md | RENAME | Product Spaces vs target Teamspaces | Teamspace concepts | Favourites/private space | yes | templates (indirect) | high | Spaces vs Teamspaces wording |
| Projects and tasks | concepts/workspace-and-collaboration/projects-and-tasks | Projects and tasks | — | — | /projects; PROJECTS_*.md | CREATE | No docs-new; flag-gated | N/A | App flows + availability callout | no | projects-enabled (+ NEXT_PUBLIC_PROJECTS_ENABLED) | high | — |
| What is a project? | concepts/workspace-and-collaboration/projects-and-tasks/what-is-a-project | Projects and tasks | — | — | /projects; PROJECTS_*.md | CREATE | No docs-new; flag-gated | N/A | App flows + availability callout | no | projects-enabled (+ NEXT_PUBLIC_PROJECTS_ENABLED) | high | — |
| Project structure | concepts/workspace-and-collaboration/projects-and-tasks/project-structure | Projects and tasks | — | — | /projects; PROJECTS_*.md | CREATE | No docs-new; flag-gated | N/A | App flows + availability callout | no | projects-enabled (+ NEXT_PUBLIC_PROJECTS_ENABLED) | high | Sprints in scope? |
| AI in projects | concepts/workspace-and-collaboration/projects-and-tasks/ai-in-projects | Projects and tasks | — | — | /projects; PROJECTS_*.md | CREATE | No docs-new; flag-gated | N/A | App flows + availability callout | no | projects-enabled (+ NEXT_PUBLIC_PROJECTS_ENABLED) | medium | — |
| Project activity | concepts/workspace-and-collaboration/projects-and-tasks/project-activity | Projects and tasks | — | — | /projects; PROJECTS_*.md | CREATE | No docs-new; flag-gated | N/A | App flows + availability callout | no | projects-enabled (+ NEXT_PUBLIC_PROJECTS_ENABLED) | high | — |
| Create and manage projects | concepts/workspace-and-collaboration/projects-and-tasks/create-and-manage-projects | Projects and tasks | — | — | /projects; PROJECTS_*.md | CREATE | No docs-new; flag-gated | N/A | App flows + availability callout | no | projects-enabled (+ NEXT_PUBLIC_PROJECTS_ENABLED) | high | — |
| Project settings and access | concepts/workspace-and-collaboration/projects-and-tasks/project-settings-and-access | Projects and tasks | — | — | /projects; PROJECTS_*.md | CREATE | No docs-new; flag-gated | N/A | App flows + availability callout | no | projects-enabled (+ NEXT_PUBLIC_PROJECTS_ENABLED) | high | — |
| Tasks | concepts/workspace-and-collaboration/projects-and-tasks/tasks | Projects and tasks | — | — | /projects; PROJECTS_*.md | CREATE | No docs-new; flag-gated | N/A | App flows + availability callout | no | projects-enabled (+ NEXT_PUBLIC_PROJECTS_ENABLED) | high | — |
| Sharing and permissions | concepts/workspace-and-collaboration/sharing-and-permissions | Sharing and permissions | docs-new/sharing-and-permissions/sharing-basics (+ roles/inheritance/sensitive-data omitted from target children) | support-docs twins | ShareResource | MOVE | Parent exists; children incomplete vs docs-new | Sharing basics | Decide add roles/inheritance/sensitive-data | yes | none | high | Add missing sharing children? |
| Comments and collaboration | concepts/workspace-and-collaboration/sharing-and-permissions/comments-and-collaboration | Sharing and permissions | docs-new/sharing-and-permissions/comments-and-collaboration | support-docs twin | components/comments | MOVE | Existing | Comment threads | Collab vs comments | yes | board collab env | high | — |
| Publishing | concepts/workspace-and-collaboration/sharing-and-permissions/publishing | Sharing and permissions | docs-new/sharing-and-permissions/external-sharing-and-exports | support-docs twin | publications; /p/[token] | MERGE | Split shared page into Publishing | Publish content from shared page | Flag + public links | yes | publishing-enabled + NEXT_PUBLIC_PUBLISHING_ENABLED | high | — |
| Exports | concepts/workspace-and-collaboration/sharing-and-permissions/exports | Sharing and permissions | docs-new/sharing-and-permissions/external-sharing-and-exports | support-docs twin | Share Export tab | MERGE | Split shared page into Exports | Export content from shared page | Flag availability | yes | exports-enabled | high | — |
| Templates | concepts/workspace-and-collaboration/templates | Templates | — | — | /template | CREATE | Flag-gated; no docs-new | N/A | Gallery/drafts/agent templates | no | templates-enabled | high | — |

## Settings and administration

| Target page | Planned path | Parent | Legacy docs-new | support-docs | App / internal | Action | Reason | Preserve | Add from app | Redirect | Flag | Confidence | Open question |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Workspace settings | concepts/settings-and-administration/workspace-settings | Workspace settings | docs-new/admin-guide/workspace-settings | support-docs/admin-guide/workspace-settings | Admin General | MOVE | Existing | General settings | Admin labels | yes | none | high | — |
| Planning defaults | concepts/settings-and-administration/workspace-settings/planning-defaults | Workspace settings | — | support-docs/oculon-basics/currency-and-conversion | Admin Planning drawer | CREATE | No docs-new; currency only partial | Currency bits | Full Planning fields; disambiguate Plan mode | no | none | medium | Overlap with Variables currency |
| Users, guests and invitations | concepts/settings-and-administration/users-guests-and-invitations | Users, guests and invitations | docs-new/admin-guide/members-and-roles | support-docs twin | /settings/users | RENAME | Product Users & Groups | Members/roles | Guests; invites | yes | none | high | — |
| Roles and access | concepts/settings-and-administration/roles-and-access | Roles and access | docs-new/admin-guide/groups | support-docs twin | Users & Groups | RENAME | From groups page | Groups | Owner/Member/Guest; share roles | yes | none | high | Merge with Users? |
| Security | concepts/settings-and-administration/security | Security | docs-new/admin-guide/security | support-docs twin | Security drawers | MOVE | Existing | Security overview | Account vs admin Security and Access | yes | none | high | — |
| Audit logs | concepts/settings-and-administration/security/audit-logs | Security | docs-new/admin-guide/audit-logs | support-docs twin | Admin audit | MOVE | Existing | Audit concepts | — | yes | none | high | — |
| Login methods | concepts/settings-and-administration/security/login-methods | Security | docs-new/admin-guide/login-methods | support-docs/admin/saml-scim | Login/SAML | REPLACE | SAML/SCIM only on support-docs | Login methods | Bring SAML/SCIM if shipped | yes | none | medium | SAML/SCIM still supported? |
| Billing and usage | concepts/settings-and-administration/billing-and-usage | Billing and usage | docs-new/admin-guide/billing-and-plans | support-docs twin | Plan and Billing; Stripe | RENAME | Product Plan and Billing | Billing concepts | Stripe flows | yes | Stripe public keys | high | — |
| Usage and limits | concepts/settings-and-administration/billing-and-usage/usage-and-limits | Billing and usage | docs-new/admin-guide/usage-and-limits | support-docs twin | Usage drawer | MOVE | Existing | Usage metrics | — | yes | none | high | — |
| Personal settings | concepts/settings-and-administration/personal-settings | Personal settings | docs-new/workspace-and-organization/profile-and-preferences | support-docs twin | My Account | RENAME | Product My Account | Profile/preferences | Map My Account subsections | yes | none | high | — |
| Notifications | concepts/settings-and-administration/personal-settings/notifications | Personal settings | — | support-docs/account/notifications | Inbox; Settings Notifications | CREATE | Only support-docs; Inbox undocumented | support-docs notifications | Inbox vs settings | no | none | medium | — |

## Resources

| Target page | Planned path | Parent | Legacy docs-new | support-docs | App / internal | Action | Reason | Preserve | Add from app | Redirect | Flag | Confidence | Open question |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Keyboard shortcuts | concepts/resources/keyboard-shortcuts | Keyboard shortcuts | docs-new/getting-started/keyboard-shortcuts | support-docs/guides/keyboard-shortcuts | Command palette | MOVE | Existing | Shortcut lists | Palette entry points | yes | none | high | — |
| Sidebar and search | concepts/resources/sidebar-and-search | Sidebar and search | docs-new/your-sidebar/* (4 pages) | support-docs/your-sidebar/* | Sidebar; Spaces; Favourites | MERGE | Multiple pages → single target page | Nav explanations | Current flagged nav items | yes | flagged nav items | medium | Concepts vs How-to |
| Troubleshooting | concepts/resources/troubleshooting | Troubleshooting | docs-new/troubleshooting/* | support-docs/troubleshooting/* | — | MERGE | Many pages vs single parent | Error guidance | Hub vs keep children | yes | none | medium | Expand troubleshooting children? |

## Artifacts

| Target page | Planned path | Parent | Legacy docs-new | support-docs | App / internal | Action | Reason | Preserve | Add from app | Redirect | Flag | Confidence | Open question |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Artifacts | concepts/artifacts/artifacts | Artifacts | — | — | /artifacts; ARTIFACTS_AND_CODE_BLOCKS.md | CREATE | No customer docs; flag-gated | N/A | Types; create menu; board code link | no | artifacts ceiling + type flags | high | — |
| What are artifacts | concepts/artifacts/artifacts/what-are-artifacts | Artifacts | — | — | /artifacts; ARTIFACTS_AND_CODE_BLOCKS.md | CREATE | No customer docs; flag-gated | N/A | Types; create menu; board code link | no | NEXT_PUBLIC_ARTIFACTS_ENABLED | high | — |
| Code artifacts | concepts/artifacts/artifacts/code-artifacts | Artifacts | — | — | /artifacts; ARTIFACTS_AND_CODE_BLOCKS.md | CREATE | No customer docs; flag-gated | N/A | Types; create menu; board code link | no | code-artifacts-enabled | high | — |
| Spreadsheet artifacts | concepts/artifacts/artifacts/spreadsheet-artifacts | Artifacts | — | — | /artifacts; ARTIFACTS_AND_CODE_BLOCKS.md | CREATE | No customer docs; flag-gated | N/A | Types; create menu; board code link | no | spreadsheet-artifacts-enabled | high | — |
| Presentation artifacts | concepts/artifacts/artifacts/presentation-artifacts | Artifacts | — | — | /artifacts; ARTIFACTS_AND_CODE_BLOCKS.md | CREATE | No customer docs; flag-gated | N/A | Types; create menu; board code link | no | presentation-artifacts-enabled | high | — |

## Apps

| Target page | Planned path | Parent | Legacy docs-new | support-docs | App / internal | Action | Reason | Preserve | Add from app | Redirect | Flag | Confidence | Open question |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oculon Revenue | concepts/apps/oculon-revenue | Oculon Revenue | — | — | /apps/revenue/home; oculonApps; OCULON_APPS_EXPANSION.md | CREATE | Switcher exists; domain depth uneven | N/A | Purpose + entry; avoid over-claim | no | none | medium | Include in v1 or park? |
| Apps v2 shells | concepts/apps/oculon-revenue/apps-v2-shells | Oculon Revenue | — | — | /apps/<app>-v2/home; oculonApps; OCULON_APPS_EXPANSION.md | CREATE | Switcher exists; domain depth uneven | N/A | Purpose + entry; avoid over-claim | no | none | low | Include in v1 or park? |
| Oculon Close | concepts/apps/oculon-close | Oculon Close | — | — | /apps/close/close-home; oculonApps; OCULON_APPS_EXPANSION.md | CREATE | Switcher exists; domain depth uneven | N/A | Purpose + entry; avoid over-claim | no | none | low | Include in v1 or park? |
| Oculon Cash | concepts/apps/oculon-cash | Oculon Cash | — | — | /apps/cash/cash-management; oculonApps; OCULON_APPS_EXPANSION.md | CREATE | Switcher exists; domain depth uneven | N/A | Purpose + entry; avoid over-claim | no | none | low | Include in v1 or park? |
| Oculon Spend | concepts/apps/oculon-spend | Oculon Spend | — | — | /apps/spend/spend; oculonApps; OCULON_APPS_EXPANSION.md | CREATE | Switcher exists; domain depth uneven | N/A | Purpose + entry; avoid over-claim | no | none | low | Include in v1 or park? |
| Oculon Tax | concepts/apps/oculon-tax | Oculon Tax | — | — | /apps/tax/tax; oculonApps; OCULON_APPS_EXPANSION.md | CREATE | Switcher exists; domain depth uneven | N/A | Purpose + entry; avoid over-claim | no | none | low | Include in v1 or park? |
| Oculon Performance | concepts/apps/oculon-performance | Oculon Performance | — | — | /apps/performance/performance-my-goals; oculonApps; OCULON_APPS_EXPANSION.md | CREATE | Switcher exists; domain depth uneven | N/A | Purpose + entry; avoid over-claim | no | none | low | Include in v1 or park? |
| Oculon Commission | concepts/apps/oculon-commission | Oculon Commission | — | — | /apps/commission/commission; oculonApps; OCULON_APPS_EXPANSION.md | CREATE | Switcher exists; domain depth uneven | N/A | Purpose + entry; avoid over-claim | no | none | low | Include in v1 or park? |
| FinOps | concepts/apps/finops | FinOps | — | — | /apps/finops/finops; oculonApps; OCULON_APPS_EXPANSION.md | CREATE | Switcher exists; domain depth uneven | N/A | Purpose + entry; avoid over-claim | no | none | low | Include in v1 or park? |
| Oculon Capital | concepts/apps/oculon-capital | Oculon Capital | — | — | /apps/capital/capital; oculonApps; OCULON_APPS_EXPANSION.md | CREATE | Switcher exists; domain depth uneven | N/A | Purpose + entry; avoid over-claim | no | none | low | Include in v1 or park? |

## Global terminology decisions

### Decided (`ia-decisions.md`)

| Conflict | Decision |
|---|---|
| **Transactions vs Databases** | Public Concepts term: **Transactions** (`concepts/data-and-structure/transactions/**`). Database = Legacy alias / search / sparse explanatory copy only. Redirects from `/docs-new/databases/*` at cutover. |
| **Scenario Compare ownership** | Analysis → Compare → **Scenario compare** owns deep compare. Scenarios does not publish a duplicate Compare scenarios page. |
| **Model History** | Models child: `concepts/modeling/models/model-history`. Fold Legacy versioning. No shared History parent. |
| **Model cloning / organization** | No Clone model Concepts page. HOLD/ARCHIVE cloning Legacy. Model organization HOLD outside Models (Library/Workspace later). Library **Copy to** ≠ clone. |

### Still open

| Conflict | Evidence | Decision needed |
|---|---|---|
| **Plans / Planning / Plan mode** | Admin Planning; AI Plan mode; no Plans product | Distinct titles and cross-links |
| **Spaces / Teamspaces / Private space** | Sidebar Spaces; settings Teamspace | Customer-facing umbrella term |
| **Personal settings vs My Account** | Product section My Account | Concepts heading |
| **Users & Groups vs Users / Roles split** | Single settings entry | Keep split or merge |
| **FP&A vs Models vs Apps** | Switcher FP&A opens Library models | How Concepts mentions FP&A |
| **Integrations vs Connectors & MCP** | Library Integrations; Settings Connectors & MCP | One topic or two |
| **Last actual date vs actuals/forecast boundary** | App `last_actual_date`; docs orphans; AGENTS.md | Time IA child name |
| **Non-model History surfaces** | Project activity; Artifact History | Confirm they stay separate from Model History |

## Flag-gated / unreleased content

### Safe to document now

- Core modeling: Models, Variables, Dimensions, Time, Formulas, Scenarios
- Analysis: Views, Compare, Boards (except code-block page)
- Workspaces, Spaces/Teamspaces, Sharing basics, Comments
- Settings admin + My Account surfaces
- AI Assistant core, Custom Agents (note discoverability), MCP/Connectors
- Resources: shortcuts; sidebar (call out flagged items carefully)

### Document only if enabled

| Area | Flag(s) | Target pages |
|---|---|---|
| Projects / Tasks | `projects-enabled`, `NEXT_PUBLIC_PROJECTS_ENABLED` | Projects and tasks tree |
| Templates | `templates-enabled` | Templates |
| Feed | `feeds-enabled` | Feed |
| Publishing | `publishing-enabled`, `NEXT_PUBLIC_PUBLISHING_ENABLED` | Publishing |
| Exports | `exports-enabled` | Exports |
| Artifacts | type flags + `NEXT_PUBLIC_ARTIFACTS_ENABLED` | Artifacts section |
| Board code block | `code-artifacts-enabled` (+ artifacts ceiling) | Code block on boards |

### Hold from public docs

| Area | Why |
|---|---|
| Agent teams | Flag defaults false in **every** environment |
| Deep Apps domain pages / Apps v2 | Uneven native vs legacy; over-promise risk |
| `/settings/feature-flags` | Internal |
| Thin app-switcher stubs without GA confirmation | Low confidence |
| Model cloning (as Clone) | No dedicated Clone UX; do not create Concepts page. Library **Copy to** documented later under Library |
| Model organization under Models | HOLD for Library/Workspace IA; not a Models child |

## Missing target coverage

| Implemented area | Recommendation | Reason |
|---|---|---|
| Library hub | **add to Concepts** | Primary product hub |
| Integrations (Library) | **review** | Distinct from Connectors & MCP; maybe Integrations tab |
| Inbox | **add to Concepts** or Settings | Chrome beyond Notifications settings |
| Command palette | **Resources** or How-to | Discovery |
| Model History | **mapped** — `concepts/modeling/models/model-history` | CREATE; fold Legacy versioning |
| Scenario governance / Merge | **mapped** — Scenarios children | MOVE from Legacy |
| Transactions (was Databases) | **mapped** — `concepts/data-and-structure/transactions/**` | RENAME; unblocked for migration |
| Onboarding / join workspace | **review** | App exists; likely How-to/Getting started |
| Tags | **review** | On models/boards |
| Board realtime collab | **review under Boards** | Distinct from Comments |
| FP&A naming | **note on Models** | Avoid Apps confusion |
| Sprints | **review** | Confirm shipped |
| What is Oculon / How organized | **review** | In Legacy; not in Notion Concepts list |
| Last actual date | **add under Time** | App-critical; orphan docs exist |
| Conditional logic | **review under Formulas** | Strong Legacy orphan; not in target |
| Sharing roles / inheritance / sensitive-data | **add children** or exclude w/ redirects | In docs-new; omitted from target |
| Troubleshooting children | **review** | Many pages vs one parent |
| Library Copy to | **hold** until Library docs | Not Model cloning |

## Legacy cleanup candidates

### Duplicate docs-new vs support-docs

- ~112 slug twins (see current inventory).
- After Concepts cutover: **ARCHIVE** obsolete support-docs twins once redirects cover them.
- Do not delete support-docs until Old docs + twin URLs are redirected.

### Likely ARCHIVE after cutover (keep temporarily for redirects)

| Pattern | Notes |
|---|---|
| `docs-new/**` moved into `concepts/**` | Redirect then archive/unpublish from Legacy nav |
| `support-docs/**` twins | Archive after redirects verified |
| Hidden Old docs `oculon-basics/**` | Long-tail redirects to Concepts modules |
| Superseded orphans (e.g. board-interaction) | Case-by-case |
| Glossary backups / empty indexes | Archive when unused |
| `docs-new/scenarios/compare-scenarios` | Not a Concepts Scenarios target; redirect to Analysis Scenario compare |
| `docs-new/models/versioning` | Fold into Model History; then redirect/archive |
| `support-docs/models/cloning-and-versioning` | HOLD now; ARCHIVE — no Clone Concepts page |
| `support-docs/models/model-organization` (broken Legacy nav twin) | HOLD outside Models; ARCHIVE from Models track |
| `docs-new/databases/**` | Redirect to `concepts/data-and-structure/transactions/**` |

### Keep temporarily for redirects / SEO

- All Concepts Legacy `docs-new` URLs while both tabs live
- Existing `/support-docs → /docs-new` redirects until retargeted to `/concepts/...`
- Broken Legacy targets (actuals-and-forecast-boundary, cloning-and-versioning, model-organization, private-vs-shared-views, view-behavior): fix or redirect when gaps resolved
- `/docs-new/databases/*` → `/concepts/data-and-structure/transactions/*` at cutover

## Migration order

### Completed (content migrated; Legacy untouched)

1. **Dimensions** (pilot)
2. **Variables**
3. **Time**
4. **Formulas**
5. **Models** (published set; Model History still outstanding CREATE)
6. **Scenarios** (published set; governance + merge still outstanding MOVE)

### Next

7. **Scenarios follow-up** — MOVE Scenario governance and access; MOVE Merge scenarios; update cross-links to Analysis Compare (no Scenarios Compare page)
8. **Model History** — CREATE under Models; fold Legacy versioning
9. **Transactions** (was Databases) — RENAME/MOVE under `concepts/data-and-structure/transactions/**` (**unblocked**)
10. Views → Compare (Scenario compare absorbs scenario comparison deep links)
11. Boards (MOVE/REPLACE, then CREATE embeds; Transactions block naming confirmed)
12. Core concepts (glossary add Transactions primary + Database alias; overview; data-flow CREATE)
13. Workspace + Sharing (MERGE publish/export)
14. Settings / admin
15. AI Assistant + Custom Agents + Connectors
16. Resources
17. Flag-gated: Projects, Templates, Feed, Artifacts, Publishing/Exports
18. Hold/late: Agent Teams, Apps suite; Model cloning ARCHIVE; Model organization HOLD

### Pilot success criteria (Dimensions) — met

- Pages under `concepts/data-and-structure/dimensions/**`
- Concepts tab lists Dimensions without removing Concepts Legacy
- Terminology matches Library Dimensions
- Redirects from docs-new dimension URLs drafted (cutover later)
- No support-docs deletion yet

---

_End of migration map. IA decisions from `ia-decisions.md` applied to planning artifacts only. Next content migration only when explicitly requested._
