# Target Concepts Structure

_IA specification only. Source of truth: Notion [Support Docs Structure](https://app.notion.com/p/Support-Docs-Structure-410c850f9a03809a8172d86397c81041) → App feature coverage (Section = Concepts)._

This document defines the **target** Concepts tab information architecture. It does **not** migrate content, change `docs.json`, or create the folder hierarchy.

**Path convention (planned):** `concepts/<sidebar-group-slug>/<feature-slug>/...`

**Status values:** `existing` · `renamed` · `new` · `merged` · `needs review`

**Placeholder today:** `concepts/index.mdx` only. Concepts Legacy remains `docs-new/**`.

## Core concepts

### Core concepts overview

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Core concepts overview | `concepts/core-concepts/core-concepts-overview` | renamed | — | docs-new getting-started/core-concepts-overview; Current `docs-new/getting-started/core-concepts-overview` |

### Glossary

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Glossary | `concepts/core-concepts/glossary` | existing | — | Current `docs-new/getting-started/glossary` |

### How data flows through Oculon

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| How data flows through Oculon | `concepts/core-concepts/how-data-flows-through-oculon` | new | — | Planned Concepts page. No published docs-new page yet. |

## Data and structure

### Transactions

_IA decision (`ia-decisions.md`): public terminology is **Transactions**. Legacy “Databases” is source/alias material only. Internal app routes remain `/library/databases` and `/databases/[id]`._

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Transactions | `concepts/data-and-structure/transactions` | renamed | What is a transaction, Transaction types, Transaction structure, Working with data, Linked data, Refresh and sync behavior, Transaction best practices | Public label matches Library tab and **Create Transactions**. Legacy source under `docs-new/databases/**`. App routes still `/library/databases`, `/databases/[databaseId]`. Use “database” only as glossary/Legacy alias in copy. |
| What is a transaction | `concepts/data-and-structure/transactions/what-is-a-transaction` | renamed | — | From `docs-new/databases/what-is-a-database` |
| Transaction types | `concepts/data-and-structure/transactions/transaction-types` | renamed | — | From `docs-new/databases/database-types` |
| Transaction structure | `concepts/data-and-structure/transactions/transaction-structure` | renamed | — | From `docs-new/databases/database-structure` |
| Working with data | `concepts/data-and-structure/transactions/working-with-data` | renamed | — | From `docs-new/databases/working-with-data`; verb-led title kept |
| Linked data | `concepts/data-and-structure/transactions/linked-data` | renamed | — | From `docs-new/databases/linked-data`; verb-led title kept |
| Refresh and sync behavior | `concepts/data-and-structure/transactions/refresh-and-sync-behavior` | renamed | — | From `docs-new/databases/refresh-and-sync-behavior`; verb-led title kept |
| Transaction best practices | `concepts/data-and-structure/transactions/transaction-best-practices` | renamed | — | From `docs-new/databases/database-best-practices` |

### Variables

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Variables | `concepts/data-and-structure/variables` | existing | What is a variable, Variable types, Create and edit variables, Variable breakdown, Variable formatting, Variable behavior, Variable references, Variable best practices, Currency and conversion | Includes types, formatting, behavior, and references, which have their own docs-new pages.; Current `docs-new/variables/what-is-a-variable`; App route: /variables/\[variableId\] |
| What is a variable | `concepts/data-and-structure/variables/what-is-a-variable` | existing | — | Current `docs-new/variables/what-is-a-variable`; App route: /variables/\[variableId\] |
| Variable types | `concepts/data-and-structure/variables/variable-types` | existing | — | Current `docs-new/variables/variable-types`; App route: /variables/\[variableId\] |
| Create and edit variables | `concepts/data-and-structure/variables/create-and-edit-variables` | existing | — | Current `docs-new/variables/create-and-edit-variables`; App route: /variables/\[variableId\] |
| Variable breakdown | `concepts/data-and-structure/variables/variable-breakdown` | existing | — | Current `docs-new/variables/variable-breakdown`; App route: /variables/\[variableId\] |
| Variable formatting | `concepts/data-and-structure/variables/variable-formatting` | existing | — | Current `docs-new/variables/variable-formatting`; App route: /variables/\[variableId\] |
| Variable behavior | `concepts/data-and-structure/variables/variable-behavior` | existing | — | Current `docs-new/variables/variable-behavior`; App route: /variables/\[variableId\] |
| Variable references | `concepts/data-and-structure/variables/variable-references` | existing | — | Current `docs-new/variables/variable-references`; App route: /variables/\[variableId\] |
| Variable best practices | `concepts/data-and-structure/variables/variable-best-practices` | existing | — | Current `docs-new/variables/variable-best-practices`; App route: /variables/\[variableId\] |
| Currency and conversion | `concepts/data-and-structure/variables/currency-and-conversion` | needs review | — | Used in variables and in Planning defaults. Published only on the older support-docs site, not in docs-new.; Current `support-docs/oculon-basics/currency-and-conversion`; App route: /variables/\[variableId\] |

### Dimensions

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Dimensions | `concepts/data-and-structure/dimensions` | existing | What is a dimension, Create and edit dimensions, Dimension values, Using dimensions with variables, Dimension operations, Dimension best practices | Library create action is Create Dimension.; Current `docs-new/dimensions/what-is-a-dimension`; App route: /library/dimensions |
| What is a dimension | `concepts/data-and-structure/dimensions/what-is-a-dimension` | existing | — | Current `docs-new/dimensions/what-is-a-dimension`; App route: /library/dimensions |
| Create and edit dimensions | `concepts/data-and-structure/dimensions/create-and-edit-dimensions` | renamed | — | docs-new slug is create-and-edit-dimension; Current `docs-new/dimensions/create-and-edit-dimension`; App route: /library/dimensions |
| Dimension values | `concepts/data-and-structure/dimensions/dimension-values` | existing | — | Current `docs-new/dimensions/dimension-values`; App route: /library/dimensions |
| Using dimensions with variables | `concepts/data-and-structure/dimensions/using-dimensions-with-variables` | existing | — | Current `docs-new/dimensions/using-dimensions-with-variables`; App route: /library/dimensions |
| Dimension operations | `concepts/data-and-structure/dimensions/dimension-operations` | existing | — | Current `docs-new/dimensions/dimension-operations`; App route: /library/dimensions |
| Dimension best practices | `concepts/data-and-structure/dimensions/dimension-best-practices` | existing | — | Current `docs-new/dimensions/dimension-best-practices`; App route: /library/dimensions |

### Time

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Time | `concepts/data-and-structure/time` | existing | Time in Oculon, Time granularity, Relative time, Time aggregation, Time best practices | Granularity, relative time, and aggregation are documented as part of time. No standalone route.; Current `docs-new/time/time-in-oculon`; App route: /model/\[modelId\] |
| Time in Oculon | `concepts/data-and-structure/time/time-in-oculon` | existing | — | Current `docs-new/time/time-in-oculon`; App route: /model/\[modelId\] |
| Time granularity | `concepts/data-and-structure/time/time-granularity` | existing | — | Current `docs-new/time/time-granularity`; App route: /model/\[modelId\] |
| Relative time | `concepts/data-and-structure/time/relative-time` | existing | — | Current `docs-new/time/relative-time`; App route: /model/\[modelId\] |
| Time aggregation | `concepts/data-and-structure/time/time-aggregation` | existing | — | Current `docs-new/time/time-aggregation`; App route: /model/\[modelId\] |
| Time best practices | `concepts/data-and-structure/time/time-best-practices` | existing | — | Current `docs-new/time/time-best-practices`; App route: /model/\[modelId\] |

## Modeling

### Models

_IA decision (`ia-decisions.md`): add **Model History**. Do not add Clone model or Model organization under Models. Fold Legacy versioning into Model History. Library **Copy to** is not model cloning._

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Models | `concepts/modeling/models` | existing | What is a model, Model structure, Model settings, Model History, Model best practices, Linked models | Core planning workspace. FP&A in the app switcher opens this surface.; Current `docs-new/models/what-is-a-model`; App route: /library/models, /model/\[modelId\] |
| What is a model | `concepts/modeling/models/what-is-a-model` | existing | — | Current `docs-new/models/what-is-a-model`; App route: /model/\[modelId\] |
| Model structure | `concepts/modeling/models/model-structure` | existing | — | Current `docs-new/models/model-structure`; App route: /model/\[modelId\] |
| Model settings | `concepts/modeling/models/model-settings` | existing | — | Current `docs-new/models/model-settings`; App route: /model/\[modelId\] |
| Model History | `concepts/modeling/models/model-history` | new | — | App toolbar **History**; checkpoint preview/restore. Fold useful content from `docs-new/models/versioning`. `sidebarTitle`: History. No shared cross-product History parent. |
| Model best practices | `concepts/modeling/models/model-best-practices` | existing | — | Current `docs-new/models/model-best-practices`; App route: /model/\[modelId\] |
| Linked models | `concepts/modeling/models/linked-models` | existing | — | Connects planning logic across models. Covered by the models concept, not a separate structure row.; Current `docs-new/models/linked-models`; App route: /model/\[modelId\] |

### Formulas

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Formulas | `concepts/modeling/formulas` | existing | Formula basics, Formula editor, Functions, Helper variables and modifiers, Common formula patterns, Formula errors, Formula best practices | Editor, functions, helper variables, and formula errors have their own docs-new pages.; Current `docs-new/formulas/formula-basics`; App route: /model/\[modelId\] |
| Formula basics | `concepts/modeling/formulas/formula-basics` | existing | — | Current `docs-new/formulas/formula-basics` |
| Formula editor | `concepts/modeling/formulas/formula-editor` | existing | — | Current `docs-new/formulas/formula-editor` |
| Functions | `concepts/modeling/formulas/functions` | existing | — | Current `docs-new/formulas/functions` |
| Helper variables and modifiers | `concepts/modeling/formulas/helper-variables-and-modifiers` | existing | — | Current `docs-new/formulas/helper-variables-and-modifiers` |
| Common formula patterns | `concepts/modeling/formulas/common-formula-patterns` | existing | — | Current `docs-new/formulas/common-formula-patterns` |
| Formula errors | `concepts/modeling/formulas/formula-errors` | existing | — | Current `docs-new/formulas/formula-errors` |
| Formula best practices | `concepts/modeling/formulas/formula-best-practices` | existing | — | Current `docs-new/formulas/formula-best-practices` |

### Scenarios

_IA decision (`ia-decisions.md`): remove duplicate **Compare scenarios** child — deep compare lives under Analysis → Compare → Scenario compare. Add **Scenario governance and access** and **Merge scenarios**. Scenarios pages may link to Compare conceptually._

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Scenarios | `concepts/modeling/scenarios` | existing | What is a scenario, Create and manage scenarios, Scenario sync behavior, Scenario overrides, Scenario governance and access, Merge scenarios, Versioning and snapshots, Scenario best practices | Includes create, sync, overrides, governance, and merge. Link comparison workflows to Analysis → Compare.; Current `docs-new/scenarios/what-is-a-scenario`; App route: /model/\[modelId\] |
| What is a scenario | `concepts/modeling/scenarios/what-is-a-scenario` | existing | — | Current `docs-new/scenarios/what-is-a-scenario` |
| Create and manage scenarios | `concepts/modeling/scenarios/create-and-manage-scenarios` | existing | — | Current `docs-new/scenarios/create-and-manage-scenarios` |
| Scenario sync behavior | `concepts/modeling/scenarios/scenario-sync-behavior` | existing | — | Current `docs-new/scenarios/scenario-sync-behavior` |
| Scenario overrides | `concepts/modeling/scenarios/scenario-overrides` | existing | — | Current `docs-new/scenarios/scenario-overrides` |
| Scenario governance and access | `concepts/modeling/scenarios/scenario-governance-and-access` | existing | — | Allow Changes, Allow Merging, share/visibility, Default Scenario delete safeguards. From `docs-new/scenarios/scenario-governance-and-access`. |
| Merge scenarios | `concepts/modeling/scenarios/merge-scenarios` | existing | — | Directional Merge Changes. From `docs-new/scenarios/merge-scenarios`. Governance summarizes and links here. |
| Versioning and snapshots | `concepts/modeling/scenarios/versioning-and-snapshots` | existing | — | Current `docs-new/scenarios/versioning-and-snapshots` |
| Scenario best practices | `concepts/modeling/scenarios/scenario-best-practices` | existing | — | Current `docs-new/scenarios/scenario-best-practices`. Cross-link Analysis → Scenario compare for comparison workflows. |

## Analysis and reporting

### Views

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Views | `concepts/analysis-and-reporting/views` | existing | What is a view, Filters, sorts, and grouping, Compare in views, View best practices | Filters, sorts, and grouping are part of this surface.; Current `docs-new/views/what-is-a-view`; App route: /model/\[modelId\] |
| What is a view | `concepts/analysis-and-reporting/views/what-is-a-view` | existing | — | Current `docs-new/views/what-is-a-view` |
| Filters, sorts, and grouping | `concepts/analysis-and-reporting/views/filters-sorts-and-grouping` | existing | — | Current `docs-new/views/filters-sorts-and-grouping` |
| Compare in views | `concepts/analysis-and-reporting/views/compare-in-views` | existing | — | Current `docs-new/views/compare-in-views` |
| View best practices | `concepts/analysis-and-reporting/views/view-best-practices` | existing | — | Current `docs-new/views/view-best-practices` |

### Compare

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Compare | `concepts/analysis-and-reporting/compare` | existing | What is a compare, Time compare, Scenario compare | Time compare and scenario compare have their own docs-new pages.; Current `docs-new/compare/what-is-a-compare`; App route: /model/\[modelId\] |
| What is a compare | `concepts/analysis-and-reporting/compare/what-is-a-compare` | existing | — | Current `docs-new/compare/what-is-a-compare` |
| Time compare | `concepts/analysis-and-reporting/compare/time-compare` | existing | — | Current `docs-new/compare/time-compare` |
| Scenario compare | `concepts/analysis-and-reporting/compare/scenario-compare` | existing | — | Canonical home for scenario comparison UI. Scenarios module links here; no duplicate Scenarios → Compare scenarios page. Current `docs-new/compare/scenario-compare` |

### Boards

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Boards | `concepts/analysis-and-reporting/boards` | existing | What is a board, Board layout, Charts, Chart types catalog, Chart interaction, Tables on boards, KPI and summary blocks, Sharing boards, Board best practices, Pivot tables, Model block, Dimension block, Transactions block, Code block on boards | Includes charts, chart interaction, tables, and KPI blocks, which have their own docs-new pages.; Current `docs-new/boards/what-is-a-board`; App route: /library/boards, /boards/\[boardId\] |
| What is a board | `concepts/analysis-and-reporting/boards/what-is-a-board` | existing | — | Current `docs-new/boards/what-is-a-board` |
| Board layout | `concepts/analysis-and-reporting/boards/board-layout` | existing | — | Current `docs-new/boards/board-layout` |
| Charts | `concepts/analysis-and-reporting/boards/charts` | needs review | — | docs-new Charts page only documents Bar, Line, and Metric. App has 14 chart types: bar, horizontal\_bar, line, area, combo, pie, donut, treemap, waterfall, funnel, sankey, scatter, bubble, heatmap. Sa; Current `docs-new/boards/charts` |
| Chart types catalog | `concepts/analysis-and-reporting/boards/chart-types-catalog` | new | — | Missing docs for full Setup-tab chart type set: Column, Bar, Line, Area, Combo, Pie, Donut, Treemap, Waterfall, Funnel, Sankey, Scatter, Bubble, Heatmap. Existing Charts page only covers Bar/Line/Metr; App route: /boards/\[boardId\] |
| Chart interaction | `concepts/analysis-and-reporting/boards/chart-interaction` | existing | — | Current `docs-new/boards/chart-interaction` |
| Tables on boards | `concepts/analysis-and-reporting/boards/tables-on-boards` | needs review | — | Tables on boards page is generic. Does not document Pivot Table (chartBlock viz=pivot) or Model / Dimension / Transactions embed blocks.; Current `docs-new/boards/tables-on-boards` |
| KPI and summary blocks | `concepts/analysis-and-reporting/boards/kpi-and-summary-blocks` | needs review | — | KPI/Metric Block page exists, but it is implemented as chartBlock with viz=kpi / card\_type metric\_block, not a separate docs concept for the full chart type set.; Current `docs-new/boards/kpi-and-summary-blocks` |
| Sharing boards | `concepts/analysis-and-reporting/boards/sharing-boards` | existing | — | Current `docs-new/boards/sharing-boards` |
| Board best practices | `concepts/analysis-and-reporting/boards/board-best-practices` | existing | — | Current `docs-new/boards/board-best-practices` |
| Pivot tables | `concepts/analysis-and-reporting/boards/pivot-tables` | new | — | Slash menu Pivot Table; chartBlock viz=pivot. |
| Model block | `concepts/analysis-and-reporting/boards/model-block` | new | — | TipTap modelBlock embed on boards. |
| Dimension block | `concepts/analysis-and-reporting/boards/dimension-block` | new | — | TipTap dimensionBlock embed on boards. |
| Transactions block | `concepts/analysis-and-reporting/boards/transactions-block` | new | — | Slash menu Transactions; databaseBlock embed. |
| Code block on boards | `concepts/analysis-and-reporting/boards/code-block-on-boards` | new | — | Flag `code-artifacts-enabled`; On in local/sandbox; off elsewhere; Requires artifacts creation flags. |

## AI and agents

### AI overview

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| AI overview | `concepts/ai-and-agents/ai-overview` | renamed | — | docs-new ai/ai-in-oculon; Current `docs-new/ai/ai-in-oculon` |

### Workspace AI

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Workspace AI | `concepts/ai-and-agents/workspace-ai` | needs review | — | Admin drawer for workspace instructions, agent access, approval preferences, and tool access. No dedicated docs-new page.; Current `docs-new/ai/ai-in-oculon`; App route: Settings, Workspace AI |

### AI assistant

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| AI assistant | `concepts/ai-and-agents/ai-assistant` | needs review | Modeling with AI, Reporting with AI, Plan mode | Chat for modeling and reporting. Modeling with AI and reporting with AI have their own docs-new pages.; Current `docs-new/ai/ai-in-oculon`; App route: /chat |
| Modeling with AI | `concepts/ai-and-agents/ai-assistant/modeling-with-ai` | existing | — | Current `docs-new/ai/modeling-with-ai` |
| Reporting with AI | `concepts/ai-and-agents/ai-assistant/reporting-with-ai` | existing | — | Current `docs-new/ai/reporting-with-ai` |
| Plan mode | `concepts/ai-and-agents/ai-assistant/plan-mode` | existing | — | Planning mode inside AI assistant. Closest Notion representation of Plans.; Current `docs-new/ai/plan-mode` |

### Custom agents

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Custom agents | `concepts/ai-and-agents/custom-agents` | existing | What are custom agents, Create a custom agent, Agent context and knowledge, Agent actions, Agent permissions, Agent connections, Agent safety and review, Agent best practices | Context, actions, permissions, and connections have their own docs-new pages. Distinct from Agent teams, which are not covered.; Current `docs-new/custom-agents/what-are-custom-agents`; App route: /custom-agents |
| What are custom agents | `concepts/ai-and-agents/custom-agents/what-are-custom-agents` | existing | — | Current `docs-new/custom-agents/what-are-custom-agents` |
| Create a custom agent | `concepts/ai-and-agents/custom-agents/create-a-custom-agent` | existing | — | Current `docs-new/custom-agents/create-a-custom-agent` |
| Agent context and knowledge | `concepts/ai-and-agents/custom-agents/agent-context-and-knowledge` | existing | — | Current `docs-new/custom-agents/agent-context-and-knowledge` |
| Agent actions | `concepts/ai-and-agents/custom-agents/agent-actions` | existing | — | Current `docs-new/custom-agents/agent-actions` |
| Agent permissions | `concepts/ai-and-agents/custom-agents/agent-permissions` | existing | — | Current `docs-new/custom-agents/agent-permissions` |
| Agent connections | `concepts/ai-and-agents/custom-agents/agent-connections` | existing | — | Current `docs-new/custom-agents/agent-connections` |
| Agent safety and review | `concepts/ai-and-agents/custom-agents/agent-safety-and-review` | existing | — | Current `docs-new/custom-agents/agent-safety-and-review` |
| Agent best practices | `concepts/ai-and-agents/custom-agents/agent-best-practices` | existing | — | Current `docs-new/custom-agents/agent-best-practices` |

### Context and connections

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Context and connections | `concepts/ai-and-agents/context-and-connections` | existing | MCP | MCP is documented at [https://oculon.mintlify.site/docs-new/ai/mcp](https://oculon.mintlify.site/docs-new/ai/mcp). Settings label is Connectors & MCP.; Current `docs-new/ai/connectors`; App route: Settings, Connectors & MCP |
| MCP | `concepts/ai-and-agents/context-and-connections/mcp` | existing | — | Current `docs-new/ai/mcp` |

### Skills

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Skills | `concepts/ai-and-agents/skills` | needs review | — | My Account skills. The proposed Concepts list has no Skills row.; Current `docs-new/ai/skills`; App route: Settings, Skills |

### Knowledge and memory

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Knowledge and memory | `concepts/ai-and-agents/knowledge-and-memory` | new | — | Planned Concepts page. No published docs-new page yet. |

### Feed

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Feed | `concepts/ai-and-agents/feed` | new | — | Flag `feeds-enabled`; On in local and sandbox; off in development, staging, and production; Sidebar label is Feed. Not in docs-new.; App route: /feeds |

### Agent teams

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Agent teams | `concepts/ai-and-agents/agent-teams` | new | — | Flag `agent-teams-enabled`; Off in every environment; Separate from Custom agents, which are covered. This flag defaults off in local, sandbox, development, staging, and production.; App route: /team |

## Workspace and collaboration

### Workspaces

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Workspaces | `concepts/workspace-and-collaboration/workspaces` | existing | — | Create, invite, and request-access flows live under this route.; Current `docs-new/workspace-and-organization/what-is-a-workspace`; App route: /workspaces |

### Teamspaces and private space

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Teamspaces and private space | `concepts/workspace-and-collaboration/teamspaces-and-private-space` | renamed | — | docs-new slug teamspaces-and-organization; Sidebar spaces and private space. Templates inside a space follow the templates flag.; Current `docs-new/workspace-and-organization/teamspaces-and-organization`; App route: /settings/teamspace |

### Projects and tasks

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Projects and tasks | `concepts/workspace-and-collaboration/projects-and-tasks` | new | What is a project?, Project structure, AI in projects, Project activity, Create and manage projects, Project settings and access, Tasks | Flag `projects-enabled`; On in local and sandbox; off in development, staging, and production; Also hidden when NEXT\_PUBLIC\_PROJECTS\_ENABLED=false. The structure database reserves Projects and tasks, but docs-new has no projects page.; App route: /projects |
| What is a project? | `concepts/workspace-and-collaboration/projects-and-tasks/what-is-a-project` | new | — | Flag `projects-enabled` |
| Project structure | `concepts/workspace-and-collaboration/projects-and-tasks/project-structure` | new | — | Flag `projects-enabled` |
| AI in projects | `concepts/workspace-and-collaboration/projects-and-tasks/ai-in-projects` | new | — | Flag `projects-enabled`; Instructions and memory; files and resources; custom agents. |
| Project activity | `concepts/workspace-and-collaboration/projects-and-tasks/project-activity` | new | — | Flag `projects-enabled`; Closest Notion stand-in for History within projects. |
| Create and manage projects | `concepts/workspace-and-collaboration/projects-and-tasks/create-and-manage-projects` | new | — | Flag `projects-enabled`; On in local/sandbox; off elsewhere |
| Project settings and access | `concepts/workspace-and-collaboration/projects-and-tasks/project-settings-and-access` | new | — | Flag `projects-enabled` |
| Tasks | `concepts/workspace-and-collaboration/projects-and-tasks/tasks` | new | — | Flag `projects-enabled`; Assign tasks; delegate to AI agents; All Tasks / My Tasks. |

### Sharing and permissions

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Sharing and permissions | `concepts/workspace-and-collaboration/sharing-and-permissions` | existing | Comments and collaboration, Publishing, Exports | Roles, inheritance, and sensitive-data controls have their own docs-new pages.; Current `docs-new/sharing-and-permissions/sharing-basics`; App route: Share dialog |
| Comments and collaboration | `concepts/workspace-and-collaboration/sharing-and-permissions/comments-and-collaboration` | existing | — | Current `docs-new/sharing-and-permissions/comments-and-collaboration` |
| Publishing | `concepts/workspace-and-collaboration/sharing-and-permissions/publishing` | merged | — | Flag `publishing-enabled`; Shares page with Exports; flag-gated.; Current `docs-new/sharing-and-permissions/external-sharing-and-exports` |
| Exports | `concepts/workspace-and-collaboration/sharing-and-permissions/exports` | merged | — | Flag `exports-enabled`; Merged today with Publishing on one docs-new page.; Current `docs-new/sharing-and-permissions/external-sharing-and-exports` |

### Templates

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Templates | `concepts/workspace-and-collaboration/templates` | new | — | Flag `templates-enabled`; On in local and sandbox; off in development, staging, and production; Template gallery, my templates, and drafts. Not in docs-new.; App route: /template |

## Settings and administration

### Workspace settings

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Workspace settings | `concepts/settings-and-administration/workspace-settings` | existing | Planning defaults | Admin general settings.; Current `docs-new/admin-guide/workspace-settings`; App route: Settings, General |
| Planning defaults | `concepts/settings-and-administration/workspace-settings/planning-defaults` | needs review | — | Only on support-docs today.; Current `support-docs/oculon-basics/currency-and-conversion` |

### Users, guests and invitations

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Users, guests and invitations | `concepts/settings-and-administration/users-guests-and-invitations` | renamed | — | docs-new members-and-roles; Settings label is Users & Groups.; Current `docs-new/admin-guide/members-and-roles`; App route: /settings/users |

### Roles and access

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Roles and access | `concepts/settings-and-administration/roles-and-access` | renamed | — | docs-new admin-guide/groups; Managed with members under Users & Groups.; Current `docs-new/admin-guide/groups`; App route: /settings/users |

### Security

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Security | `concepts/settings-and-administration/security` | existing | Audit logs, Login methods | Account security and admin Security and Access.; Current `docs-new/admin-guide/security`; App route: Settings, Security and Access |
| Audit logs | `concepts/settings-and-administration/security/audit-logs` | existing | — | Current `docs-new/admin-guide/audit-logs` |
| Login methods | `concepts/settings-and-administration/security/login-methods` | existing | — | SAML/SCIM only on support-docs.; Current `docs-new/admin-guide/login-methods` |

### Billing and usage

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Billing and usage | `concepts/settings-and-administration/billing-and-usage` | renamed | Usage and limits | docs-new billing-and-plans; Settings overlay label is Plan and Billing.; Current `docs-new/admin-guide/billing-and-plans`; App route: /settings/billing |
| Usage and limits | `concepts/settings-and-administration/billing-and-usage/usage-and-limits` | existing | — | Current `docs-new/admin-guide/usage-and-limits` |

### Personal settings

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Personal settings | `concepts/settings-and-administration/personal-settings` | renamed | Notifications | Maps from docs-new workspace-and-organization/profile-and-preferences (My Account); My Account profile and preferences.; Current `docs-new/workspace-and-organization/profile-and-preferences`; App route: /settings/profile |
| Notifications | `concepts/settings-and-administration/personal-settings/notifications` | needs review | — | Only on support-docs today.; Current `support-docs/account/notifications` |

## Resources

### Keyboard shortcuts

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Keyboard shortcuts | `concepts/resources/keyboard-shortcuts` | existing | — | Current `docs-new/getting-started/keyboard-shortcuts` |

### Sidebar and search

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Sidebar and search | `concepts/resources/sidebar-and-search` | renamed | — | docs-new your-sidebar/* (multiple pages); Search and quick access are documented separately. The proposed structure puts navigation under How to, not Concepts.; Current `docs-new/your-sidebar/navigate-the-sidebar`; App route: App shell |

### Troubleshooting

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Troubleshooting | `concepts/resources/troubleshooting` | existing | — | docs-new has a troubleshooting section. Parent row for the group.; Current `docs-new/troubleshooting/common-errors` |

## Artifacts

### Artifacts

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Artifacts | `concepts/artifacts/artifacts` | new | What are artifacts, Code artifacts, Spreadsheet artifacts, Presentation artifacts | The create menu also requires NEXT\_PUBLIC\_ARTIFACTS\_ENABLED=1. Saved files follow the type flags on the rows below.; App route: /artifacts |
| What are artifacts | `concepts/artifacts/artifacts/what-are-artifacts` | new | — | Also needs NEXT_PUBLIC_ARTIFACTS_ENABLED. |
| Code artifacts | `concepts/artifacts/artifacts/code-artifacts` | new | — | Flag `code-artifacts-enabled` |
| Spreadsheet artifacts | `concepts/artifacts/artifacts/spreadsheet-artifacts` | new | — | Flag `spreadsheet-artifacts-enabled` |
| Presentation artifacts | `concepts/artifacts/artifacts/presentation-artifacts` | new | — | Flag `presentation-artifacts-enabled` |

## Apps

### Oculon Revenue

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Oculon Revenue | `concepts/apps/oculon-revenue` | new | Apps v2 shells | App switcher entry. No registry flag. FP&A itself is the Models surface and is covered.; App route: /apps/revenue/home |
| Apps v2 shells | `concepts/apps/oculon-revenue/apps-v2-shells` | new | — | Combined v2 shells under Revenue parent for inventory. |

### Oculon Close

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Oculon Close | `concepts/apps/oculon-close` | new | — | App switcher entry. No registry flag.; App route: /apps/close/close-home |

### Oculon Cash

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Oculon Cash | `concepts/apps/oculon-cash` | new | — | App switcher entry. No registry flag.; App route: /apps/cash/cash-management |

### Oculon Spend

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Oculon Spend | `concepts/apps/oculon-spend` | new | — | App switcher entry. |

### Oculon Tax

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Oculon Tax | `concepts/apps/oculon-tax` | new | — | App switcher entry. |

### Oculon Performance

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Oculon Performance | `concepts/apps/oculon-performance` | new | — | App switcher entry. |

### Oculon Commission

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Oculon Commission | `concepts/apps/oculon-commission` | new | — | App switcher entry. |

### FinOps

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| FinOps | `concepts/apps/finops` | new | — | App switcher entry. |

### Oculon Capital

| Page | Planned path | Status | Child pages | Notes |
|---|---|---|---|---|
| Oculon Capital | `concepts/apps/oculon-capital` | new | — | App switcher entry. |

## Open IA questions

### Resolved (see `ia-decisions.md`)

- **Databases vs Transactions:** Public Concepts term is **Transactions** (`concepts/data-and-structure/transactions/**`). Legacy Database naming is alias/source only; redirects at cutover.
- **Scenario Compare dedupe:** Analysis → Compare → Scenario compare owns deep compare. Scenarios does not keep a Compare scenarios child.
- **Model History:** Added under Models (`concepts/modeling/models/model-history`). Not a shared History parent.
- **Model cloning / organization:** No Clone model or Model organization Concepts children. Hold/archive Legacy cloning and organization material; Library **Copy to** is separate.
- **Scenario governance + Merge:** Added as Scenarios children.

### Still open

1. **What is Oculon / how Oculon is organized:** Live Concepts Legacy has `docs-new/getting-started/what-is-oculon` and `how-oculon-is-organized`, but Notion Concepts Section starts at Core concepts overview / Glossary / How data flows — confirm whether overview pages move under Core concepts or stay elsewhere.
2. **Sidebar placement:** Notion puts **Sidebar and search** under Resources, with a note that another proposed structure puts navigation under How to — confirm Concepts vs How-to ownership.
3. **Time gaps:** Concepts Legacy nav still references missing `actuals-and-forecast-boundary`; orphans `last-actual-date` / `time-rollups` exist in repo but are **not** in the Notion Concepts inventory — add or drop?
4. **Views gaps:** Notion Views children omit private-vs-shared and view-behavior (missing in docs-new) — intentional?
5. **Sharing depth:** docs-new has roles/inheritance/sensitive-data pages; Notion Sharing parent only lists Publishing, Exports, Comments as subpages — should the other sharing pages be Concepts children or Settings?
6. **AI page fan-out:** AI overview, Workspace AI, and AI assistant all point at `ai-in-oculon` today — split, merge, or keep shared landing?
7. **Skills:** Notion notes Skills may not belong on the proposed Concepts list — keep in Concepts or move to Settings/How-to?
8. **Non-model History surfaces:** Project activity and Artifact History remain separate; confirm no shared History Concepts parent is needed beyond Model History.
9. **Plans:** No Plans product area in Notion Concepts; **Plan mode** under AI assistant is the only Plans-like row — confirm naming/placement.
10. **Apps section:** Nine app switcher parents + Apps v2 shells are all `new` / not covered — include in v1 Concepts migration or park for later?
11. **Artifacts:** Entire group is feature-flagged / not covered — document in Concepts now or wait for GA?
12. **Blank Notion sub-item:** Projects has a deleted/blank related sub-item (`New page`) — clean up in Notion.
13. **Duplicate sidebar group vocab in schema:** Older groups (Getting started, Modeling and forecasting, …) still exist as options but Concepts rows use the newer set (Core concepts, Data and structure, …) — treat newer set as canonical.
14. **Conditional logic:** Strong Legacy/orphan formula content — add as Formulas child?

## Coverage summary

_Counts updated after `ia-decisions.md` application (Transactions rename; Model History; Scenarios governance/merge; Compare scenarios removed)._

| Metric | Count |
|---|---:|
| Sidebar groups | 10 |
| Parent features | 46 |
| Total planned pages (parents + subpages) | 147 |
| Status: existing | 84 |
| Status: renamed | 17 |
| Status: new | 35 |
| Status: merged | 2 |
| Status: needs review | 9 |
| Existing pages represented (existing + renamed) | 101 |
| New planned pages | 35 |
| Areas needing review (needs review + merged) | 11 |

### By sidebar group

| Sidebar group | Parents | Pages |
|---|---:|---:|
| Core concepts | 3 | 3 |
| Data and structure | 4 | 31 |
| Modeling | 3 | 24 |
| Analysis and reporting | 3 | 24 |
| AI and agents | 9 | 21 |
| Workspace and collaboration | 5 | 15 |
| Settings and administration | 6 | 11 |
| Resources | 3 | 3 |
| Artifacts | 1 | 5 |
| Apps | 9 | 10 |

---

_End of target IA. Updated from `ia-decisions.md`. Content migration and `docs.json` changes are separate steps._
