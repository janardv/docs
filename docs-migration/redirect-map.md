# Redirect map (Batch F)

Source of truth for old Concepts Legacy (`docs-new/**`) → new Concepts URLs.

## Summary

| Action | Count |
|---|---:|
| DIRECT | 81 |
| RENAMED | 18 |
| MERGED | 35 |
| **Total mapped** | **134** |

No `ARCHIVE / NO REDIRECT` or `REVIEW` rows remain for published Legacy URLs: every `docs-new` page and the five missing nav orphans have a useful Concepts destination.

## Rules applied

- One-hop redirects only (never Legacy → Legacy)
- Databases → Transactions
- Scenarios Compare → Analysis Scenario compare
- Versioning / cloning orphans → Model History (or Models landing)
- Merged Resources/Troubleshooting/Sidebar pages share a canonical destination
- Missing nav orphans redirect even though MDX files are absent

## Map

| Old URL | New Concepts URL | Action | Notes | Legacy file |
|---|---|---|---|---|
| `/docs-new/admin-guide/audit-logs` | `/concepts/settings-and-administration/security/audit-logs` | DIRECT |  | yes |
| `/docs-new/admin-guide/billing-and-plans` | `/concepts/settings-and-administration/billing-and-usage` | RENAMED |  | yes |
| `/docs-new/admin-guide/groups` | `/concepts/settings-and-administration/roles-and-access` | MERGED |  | yes |
| `/docs-new/admin-guide/login-methods` | `/concepts/settings-and-administration/security/login-methods` | DIRECT |  | yes |
| `/docs-new/admin-guide/members-and-roles` | `/concepts/settings-and-administration/users-guests-and-invitations` | MERGED |  | yes |
| `/docs-new/admin-guide/security` | `/concepts/settings-and-administration/security` | DIRECT |  | yes |
| `/docs-new/admin-guide/usage-and-limits` | `/concepts/settings-and-administration/billing-and-usage/usage-and-limits` | DIRECT |  | yes |
| `/docs-new/admin-guide/workspace-settings` | `/concepts/settings-and-administration/workspace-settings` | DIRECT |  | yes |
| `/docs-new/ai/ai-in-oculon` | `/concepts/ai-and-agents/ai-overview` | RENAMED |  | yes |
| `/docs-new/ai/connectors` | `/concepts/ai-and-agents/context-and-connections` | RENAMED |  | yes |
| `/docs-new/ai/mcp` | `/concepts/ai-and-agents/context-and-connections/mcp` | DIRECT |  | yes |
| `/docs-new/ai/modeling-with-ai` | `/concepts/ai-and-agents/ai-assistant/modeling-with-ai` | DIRECT |  | yes |
| `/docs-new/ai/plan-mode` | `/concepts/ai-and-agents/ai-assistant` | MERGED | no dedicated Plan mode Concepts page | yes |
| `/docs-new/ai/reporting-with-ai` | `/concepts/ai-and-agents/ai-assistant/reporting-with-ai` | DIRECT |  | yes |
| `/docs-new/ai/skills` | `/concepts/ai-and-agents/ai-assistant` | MERGED | Skills REVIEW; assistant parent | yes |
| `/docs-new/boards/board-best-practices` | `/concepts/analysis-and-reporting/boards/board-best-practices` | DIRECT | leaf match | yes |
| `/docs-new/boards/board-interaction` | `/concepts/analysis-and-reporting/boards/chart-interaction` | MERGED | interaction content → chart-interaction | yes |
| `/docs-new/boards/board-layout` | `/concepts/analysis-and-reporting/boards/board-layout` | DIRECT | leaf match | yes |
| `/docs-new/boards/chart-interaction` | `/concepts/analysis-and-reporting/boards/chart-interaction` | DIRECT | leaf match | yes |
| `/docs-new/boards/charts` | `/concepts/analysis-and-reporting/boards/charts` | DIRECT | leaf match | yes |
| `/docs-new/boards/kpi-and-summary-blocks` | `/concepts/analysis-and-reporting/boards/kpi-and-summary-blocks` | DIRECT | leaf match | yes |
| `/docs-new/boards/sharing-boards` | `/concepts/analysis-and-reporting/boards/sharing-boards` | DIRECT | leaf match | yes |
| `/docs-new/boards/tables-on-boards` | `/concepts/analysis-and-reporting/boards/tables-on-boards` | DIRECT | leaf match | yes |
| `/docs-new/boards/what-is-a-board` | `/concepts/analysis-and-reporting/boards/what-is-a-board` | DIRECT | leaf match | yes |
| `/docs-new/compare/scenario-compare` | `/concepts/analysis-and-reporting/compare/scenario-compare` | DIRECT | leaf match | yes |
| `/docs-new/compare/time-compare` | `/concepts/analysis-and-reporting/compare/time-compare` | DIRECT | leaf match | yes |
| `/docs-new/compare/what-is-a-compare` | `/concepts/analysis-and-reporting/compare/what-is-a-compare` | DIRECT | leaf match | yes |
| `/docs-new/custom-agents/agent-actions` | `/concepts/ai-and-agents/custom-agents/agent-actions` | DIRECT | leaf match | yes |
| `/docs-new/custom-agents/agent-best-practices` | `/concepts/ai-and-agents/custom-agents/agent-best-practices` | DIRECT | leaf match | yes |
| `/docs-new/custom-agents/agent-connections` | `/concepts/ai-and-agents/custom-agents/agent-connections` | DIRECT | leaf match | yes |
| `/docs-new/custom-agents/agent-context-and-knowledge` | `/concepts/ai-and-agents/custom-agents/agent-context-and-knowledge` | DIRECT | leaf match | yes |
| `/docs-new/custom-agents/agent-permissions` | `/concepts/ai-and-agents/custom-agents/agent-permissions` | DIRECT | leaf match | yes |
| `/docs-new/custom-agents/agent-safety-and-review` | `/concepts/ai-and-agents/custom-agents/agent-safety-and-review` | DIRECT | leaf match | yes |
| `/docs-new/custom-agents/create-a-custom-agent` | `/concepts/ai-and-agents/custom-agents/create-a-custom-agent` | DIRECT | leaf match | yes |
| `/docs-new/custom-agents/what-are-custom-agents` | `/concepts/ai-and-agents/custom-agents/what-are-custom-agents` | DIRECT | leaf match | yes |
| `/docs-new/databases/database-best-practices` | `/concepts/data-and-structure/transactions/transaction-best-practices` | RENAMED |  | yes |
| `/docs-new/databases/database-formulas` | `/concepts/data-and-structure/transactions/transaction-formulas` | RENAMED |  | yes |
| `/docs-new/databases/database-structure` | `/concepts/data-and-structure/transactions/transaction-structure` | RENAMED |  | yes |
| `/docs-new/databases/database-types` | `/concepts/data-and-structure/transactions/transaction-types` | RENAMED |  | yes |
| `/docs-new/databases/filters-sorts-and-grouping` | `/concepts/data-and-structure/transactions/filters-sorts-and-grouping` | RENAMED |  | yes |
| `/docs-new/databases/linked-data` | `/concepts/data-and-structure/transactions/linked-data` | RENAMED |  | yes |
| `/docs-new/databases/refresh-and-sync-behavior` | `/concepts/data-and-structure/transactions/refresh-and-sync-behavior` | RENAMED |  | yes |
| `/docs-new/databases/what-is-a-database` | `/concepts/data-and-structure/transactions/what-is-a-transaction` | RENAMED | Databases → Transactions | yes |
| `/docs-new/databases/working-with-data` | `/concepts/data-and-structure/transactions/working-with-data` | RENAMED |  | yes |
| `/docs-new/dimensions/create-and-edit-dimension` | `/concepts/data-and-structure/dimensions/create-and-edit-dimensions` | RENAMED | plural slug | yes |
| `/docs-new/dimensions/dimension-best-practices` | `/concepts/data-and-structure/dimensions/dimension-best-practices` | DIRECT | leaf match | yes |
| `/docs-new/dimensions/dimension-operations` | `/concepts/data-and-structure/dimensions/dimension-operations` | DIRECT | leaf match | yes |
| `/docs-new/dimensions/dimension-values` | `/concepts/data-and-structure/dimensions/dimension-values` | DIRECT | leaf match | yes |
| `/docs-new/dimensions/using-dimensions-with-variables` | `/concepts/data-and-structure/dimensions/using-dimensions-with-variables` | DIRECT | leaf match | yes |
| `/docs-new/dimensions/what-is-a-dimension` | `/concepts/data-and-structure/dimensions/what-is-a-dimension` | DIRECT | leaf match | yes |
| `/docs-new/formulas/common-formula-patterns` | `/concepts/modeling/formulas/common-formula-patterns` | DIRECT | leaf match | yes |
| `/docs-new/formulas/conditional-logic` | `/concepts/modeling/formulas/conditional-logic` | DIRECT | leaf match | yes |
| `/docs-new/formulas/formula-basics` | `/concepts/modeling/formulas/formula-basics` | DIRECT | leaf match | yes |
| `/docs-new/formulas/formula-best-practices` | `/concepts/modeling/formulas/formula-best-practices` | DIRECT | leaf match | yes |
| `/docs-new/formulas/formula-editor` | `/concepts/modeling/formulas/formula-editor` | DIRECT | leaf match | yes |
| `/docs-new/formulas/formula-errors` | `/concepts/modeling/formulas/formula-errors` | DIRECT | leaf match | yes |
| `/docs-new/formulas/functions` | `/concepts/modeling/formulas/functions` | DIRECT | leaf match | yes |
| `/docs-new/formulas/helper-variables-and-modifiers` | `/concepts/modeling/formulas/helper-variables-and-modifiers` | DIRECT | leaf match | yes |
| `/docs-new/getting-started/core-concepts` | `/concepts/core-concepts/core-concepts-overview` | MERGED | legacy alias | yes |
| `/docs-new/getting-started/core-concepts-overview` | `/concepts/core-concepts/core-concepts-overview` | RENAMED | moved under Core concepts | yes |
| `/docs-new/getting-started/glossary` | `/concepts/core-concepts/glossary` | DIRECT |  | yes |
| `/docs-new/getting-started/how-oculon-is-organized` | `/concepts/core-concepts/how-oculon-is-organized` | DIRECT |  | yes |
| `/docs-new/getting-started/index` | `/concepts` | MERGED | getting-started index → Concepts landing | yes |
| `/docs-new/getting-started/keyboard-shortcuts` | `/concepts/resources/keyboard-shortcuts` | DIRECT |  | yes |
| `/docs-new/getting-started/navigating-oculon` | `/concepts/resources/sidebar-and-search` | MERGED |  | yes |
| `/docs-new/getting-started/oculon-glossary` | `/concepts/core-concepts/glossary` | MERGED | legacy glossary alias | yes |
| `/docs-new/getting-started/oculon-glossary-backup` | `/concepts/core-concepts/glossary` | MERGED | backup alias | yes |
| `/docs-new/getting-started/profile-setup` | `/concepts/settings-and-administration/personal-settings` | MERGED |  | yes |
| `/docs-new/getting-started/welcome-to-oculon` | `/concepts/core-concepts/what-is-oculon` | MERGED |  | yes |
| `/docs-new/getting-started/what-is-oculon` | `/concepts/core-concepts/what-is-oculon` | DIRECT |  | yes |
| `/docs-new/models/cloning-and-versioning` | `/concepts/modeling/models/model-history` | MERGED | missing nav orphan; no Clone page | no (orphan path) |
| `/docs-new/models/linked-models` | `/concepts/modeling/models/linked-models` | DIRECT | leaf match | yes |
| `/docs-new/models/model-best-practices` | `/concepts/modeling/models/model-best-practices` | DIRECT | leaf match | yes |
| `/docs-new/models/model-organization` | `/concepts/modeling/models` | MERGED | missing nav orphan; Library/org deferred | no (orphan path) |
| `/docs-new/models/model-settings` | `/concepts/modeling/models/model-settings` | DIRECT | leaf match | yes |
| `/docs-new/models/model-structure` | `/concepts/modeling/models/model-structure` | DIRECT | leaf match | yes |
| `/docs-new/models/versioning` | `/concepts/modeling/models/model-history` | MERGED | versioning → Model History | yes |
| `/docs-new/models/what-is-a-model` | `/concepts/modeling/models/what-is-a-model` | DIRECT | leaf match | yes |
| `/docs-new/scenarios/compare-scenarios` | `/concepts/analysis-and-reporting/compare/scenario-compare` | MERGED | Scenarios Compare → Analysis Compare | yes |
| `/docs-new/scenarios/create-and-manage-scenarios` | `/concepts/modeling/scenarios/create-and-manage-scenarios` | DIRECT | leaf match | yes |
| `/docs-new/scenarios/merge-scenarios` | `/concepts/modeling/scenarios/merge-scenarios` | DIRECT | leaf match | yes |
| `/docs-new/scenarios/scenario-best-practices` | `/concepts/modeling/scenarios/scenario-best-practices` | DIRECT | leaf match | yes |
| `/docs-new/scenarios/scenario-governance-and-access` | `/concepts/modeling/scenarios/scenario-governance-and-access` | DIRECT | leaf match | yes |
| `/docs-new/scenarios/scenario-overrides` | `/concepts/modeling/scenarios/scenario-overrides` | DIRECT | leaf match | yes |
| `/docs-new/scenarios/scenario-sync-behavior` | `/concepts/modeling/scenarios/scenario-sync-behavior` | DIRECT | leaf match | yes |
| `/docs-new/scenarios/versioning-and-snapshots` | `/concepts/modeling/scenarios/versioning-and-snapshots` | DIRECT | leaf match | yes |
| `/docs-new/scenarios/what-is-a-scenario` | `/concepts/modeling/scenarios/what-is-a-scenario` | DIRECT | leaf match | yes |
| `/docs-new/sharing-and-permissions/comments-and-collaboration` | `/concepts/workspace-and-collaboration/sharing-and-permissions/comments-and-collaboration` | DIRECT | leaf match | yes |
| `/docs-new/sharing-and-permissions/external-sharing-and-exports` | `/concepts/workspace-and-collaboration/sharing-and-permissions/exports` | MERGED | exports/publishing split; exports primary | yes |
| `/docs-new/sharing-and-permissions/members-guests-and-groups` | `/concepts/settings-and-administration/users-guests-and-invitations` | MERGED |  | yes |
| `/docs-new/sharing-and-permissions/permission-inheritance` | `/concepts/workspace-and-collaboration/sharing-and-permissions/permission-inheritance` | DIRECT | leaf match | yes |
| `/docs-new/sharing-and-permissions/roles-and-permissions` | `/concepts/workspace-and-collaboration/sharing-and-permissions/roles-and-permissions` | DIRECT | leaf match | yes |
| `/docs-new/sharing-and-permissions/sensitive-data-controls` | `/concepts/workspace-and-collaboration/sharing-and-permissions` | MERGED | no dedicated Concepts page | yes |
| `/docs-new/sharing-and-permissions/sharing-basics` | `/concepts/workspace-and-collaboration/sharing-and-permissions` | RENAMED |  | yes |
| `/docs-new/time/actuals-and-forecast-boundary` | `/concepts/data-and-structure/time/last-actual-date` | MERGED | missing Legacy nav orphan | no (orphan path) |
| `/docs-new/time/last-actual-date` | `/concepts/data-and-structure/time/last-actual-date` | DIRECT |  | yes |
| `/docs-new/time/relative-time` | `/concepts/data-and-structure/time/relative-time` | DIRECT | leaf match | yes |
| `/docs-new/time/time-aggregation` | `/concepts/data-and-structure/time/time-aggregation` | DIRECT | leaf match | yes |
| `/docs-new/time/time-best-practices` | `/concepts/data-and-structure/time/time-best-practices` | DIRECT | leaf match | yes |
| `/docs-new/time/time-granularity` | `/concepts/data-and-structure/time/time-granularity` | DIRECT | leaf match | yes |
| `/docs-new/time/time-in-oculon` | `/concepts/data-and-structure/time/time-in-oculon` | DIRECT | leaf match | yes |
| `/docs-new/time/time-rollups` | `/concepts/data-and-structure/time/time-aggregation` | MERGED | no dedicated Concepts rollups page | yes |
| `/docs-new/troubleshooting/agent-issues` | `/concepts/resources/troubleshooting` | MERGED |  | yes |
| `/docs-new/troubleshooting/common-errors` | `/concepts/resources/troubleshooting` | MERGED |  | yes |
| `/docs-new/troubleshooting/data-mismatches` | `/concepts/resources/troubleshooting` | MERGED |  | yes |
| `/docs-new/troubleshooting/formula-issues` | `/concepts/resources/troubleshooting` | MERGED |  | yes |
| `/docs-new/troubleshooting/performance-issues` | `/concepts/resources/troubleshooting` | MERGED |  | yes |
| `/docs-new/troubleshooting/permissions-issues` | `/concepts/resources/troubleshooting` | MERGED |  | yes |
| `/docs-new/troubleshooting/scenario-issues` | `/concepts/resources/troubleshooting` | MERGED |  | yes |
| `/docs-new/variables/create-and-edit-variables` | `/concepts/data-and-structure/variables/create-and-edit-variables` | DIRECT | leaf match | yes |
| `/docs-new/variables/variable-behavior` | `/concepts/data-and-structure/variables/variable-behavior` | DIRECT | leaf match | yes |
| `/docs-new/variables/variable-best-practices` | `/concepts/data-and-structure/variables/variable-best-practices` | DIRECT | leaf match | yes |
| `/docs-new/variables/variable-breakdown` | `/concepts/data-and-structure/variables/variable-breakdown` | DIRECT | leaf match | yes |
| `/docs-new/variables/variable-formatting` | `/concepts/data-and-structure/variables/variable-formatting` | DIRECT | leaf match | yes |
| `/docs-new/variables/variable-references` | `/concepts/data-and-structure/variables/variable-references` | DIRECT | leaf match | yes |
| `/docs-new/variables/variable-types` | `/concepts/data-and-structure/variables/variable-types` | DIRECT | leaf match | yes |
| `/docs-new/variables/what-is-a-variable` | `/concepts/data-and-structure/variables/what-is-a-variable` | DIRECT | leaf match | yes |
| `/docs-new/views/compare-in-views` | `/concepts/analysis-and-reporting/views/compare-in-views` | DIRECT | leaf match | yes |
| `/docs-new/views/creating-and-configuring-views` | `/concepts/analysis-and-reporting/views/creating-and-configuring-views` | DIRECT | leaf match | yes |
| `/docs-new/views/filters-sorts-and-grouping` | `/concepts/analysis-and-reporting/views/filters-sorts-and-grouping` | DIRECT | leaf match | yes |
| `/docs-new/views/private-vs-shared-views` | `/concepts/analysis-and-reporting/views/sharing-views` | MERGED | missing nav orphan; private views unsupported | no (orphan path) |
| `/docs-new/views/sharing-views` | `/concepts/analysis-and-reporting/views/sharing-views` | DIRECT | leaf match | yes |
| `/docs-new/views/using-views-on-boards` | `/concepts/analysis-and-reporting/boards/tables-on-boards` | MERGED |  | yes |
| `/docs-new/views/view-behavior` | `/concepts/analysis-and-reporting/views/what-is-a-view` | MERGED | missing nav orphan | no (orphan path) |
| `/docs-new/views/view-best-practices` | `/concepts/analysis-and-reporting/views/view-best-practices` | DIRECT | leaf match | yes |
| `/docs-new/views/what-is-a-view` | `/concepts/analysis-and-reporting/views/what-is-a-view` | DIRECT | leaf match | yes |
| `/docs-new/workspace-and-organization/profile-and-preferences` | `/concepts/settings-and-administration/personal-settings` | RENAMED |  | yes |
| `/docs-new/workspace-and-organization/teamspaces-and-organization` | `/concepts/workspace-and-collaboration/teamspaces-and-private-space` | RENAMED |  | yes |
| `/docs-new/workspace-and-organization/what-is-a-workspace` | `/concepts/workspace-and-collaboration/workspaces` | RENAMED |  | yes |
| `/docs-new/workspace-and-organization/workspace-access-and-visibility` | `/concepts/workspace-and-collaboration/workspace-access-and-visibility` | DIRECT |  | yes |
| `/docs-new/your-sidebar/navigate-the-sidebar` | `/concepts/resources/sidebar-and-search` | MERGED |  | yes |
| `/docs-new/your-sidebar/organize-your-workspace` | `/concepts/resources/sidebar-and-search` | MERGED |  | yes |
| `/docs-new/your-sidebar/search-and-quick-access` | `/concepts/resources/sidebar-and-search` | MERGED |  | yes |
| `/docs-new/your-sidebar/sidebar-customization` | `/concepts/resources/sidebar-and-search` | MERGED |  | yes |
