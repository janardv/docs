# Current docs inventory

_Generated for the Concepts → Concepts Legacy / new Concepts migration. Analysis only — no docs or navigation were changed._

## Snapshot

| Metric | Count |
|---|---:|
| Top-level nav tabs in repo `docs.json` | 4 |
| Navigated page entries | 152 |
| Live navigated pages (file exists + tab not hidden) | 112 |
| Hidden Old docs pages | 35 |
| Nav refs with missing files | 5 |
| MDX/MD files in repo (excl. meta) | 310 |
| Orphan MDX (not in nav) | 163 |
| Redirects | 110 |
| Exact slug overlaps `docs-new` ↔ `support-docs` | 112 |
| Of those, byte-identical copies | 42 |
| Of those, divergent content | 70 |

## Important: repo vs Mintlify editor

This inventory is based on **this repository’s `docs.json`**.

| Source | Tabs |
|---|---|
| **Git repo `docs.json` (this audit)** | `Concepts` · `How to guides` · `Integrations` · `Old docs` (hidden) |
| **Mintlify dashboard (unpublished)** | `Concepts` (new empty/created tab) · `Concepts Legacy` (rename of former Concepts) · `How to guides` · `Integrations` · `Old docs` (hidden) |

**Interpretation for migration planning:**

- In git, the public conceptual docs live under the tab still named **Concepts**, backed by `docs-new/**`.
- In the Mintlify editor there is an **unpublished** rename: that same structure → **Concepts Legacy**, plus a new empty **Concepts** tab.
- That rename/create is **not yet in this repo**. Treat git as source of truth for file layout; treat the editor rename as the intended naming for the migration.
- **Old docs** (`support-docs/**`, mostly `oculon-basics`) is a separate hidden legacy layer, older than `docs-new`.

## 1. Top-level navigation tabs

| Tab | Hidden | Content root | Role |
|---|---|---|---|
| Concepts | no | `docs-new/` | Current public conceptual docs (editor: becoming Concepts Legacy) |
| How to guides | no | `how-to/` | How-to entry (`how-to/index` only) |
| Integrations | no | `integration-docs/` | Integrations entry (`integration-docs/index` only) |
| Old docs | **yes** | `support-docs/` | Hidden legacy product docs (oculon-basics era) |
| Concepts (new) | n/a in git | _not in repo yet_ | Exists only as unpublished Mintlify nav node |

### Folder ownership

| Folder | In `docs.json` nav? | Notes |
|---|---|---|
| `docs-new/` | Yes — Concepts | Primary current docs tree |
| `how-to/` | Yes — How to guides | Single index page |
| `integration-docs/` | Yes — Integrations | Single index page |
| `support-docs/` | Partially — Old docs (hidden) | Large parallel tree; many pages orphaned from nav |
| `ai-tools/` | No | Mintlify starter leftovers |
| `api-reference/` | No | Mintlify starter leftovers |
| `essentials/` | No | Mintlify starter leftovers |
| `images/` | Asset store | Shared by Concepts + Old docs |
| `snippets/` | No | Template snippet |
| `logo/` | Branding | Via `docs.json` logo |

## 2. Current navigation tree

Legend: `✓` file exists · `✗ MISSING` nav entry without MDX.

- **Concepts**
  - **Start here**
    - **Getting started** _collapsed_
      - [✓] `docs-new/getting-started/what-is-oculon`
      - [✓] `docs-new/getting-started/how-oculon-is-organized`
      - [✓] `docs-new/getting-started/core-concepts-overview`
      - [✓] `docs-new/getting-started/glossary`
      - [✓] `docs-new/getting-started/keyboard-shortcuts`
    - **Workspace and organization** _collapsed_
      - [✓] `docs-new/workspace-and-organization/what-is-a-workspace`
      - [✓] `docs-new/workspace-and-organization/teamspaces-and-organization`
      - [✓] `docs-new/workspace-and-organization/profile-and-preferences`
      - [✓] `docs-new/workspace-and-organization/workspace-access-and-visibility`
    - **Your sidebar** _collapsed_
      - [✓] `docs-new/your-sidebar/navigate-the-sidebar`
      - [✓] `docs-new/your-sidebar/organize-your-workspace`
      - [✓] `docs-new/your-sidebar/search-and-quick-access`
      - [✓] `docs-new/your-sidebar/sidebar-customization`
  - **Planning and analysis**
    - **Variables** _collapsed_
      - [✓] `docs-new/variables/what-is-a-variable`
      - [✓] `docs-new/variables/variable-types`
      - [✓] `docs-new/variables/create-and-edit-variables`
      - [✓] `docs-new/variables/variable-breakdown`
      - [✓] `docs-new/variables/variable-formatting`
      - [✓] `docs-new/variables/variable-behavior`
      - [✓] `docs-new/variables/variable-references`
      - [✓] `docs-new/variables/variable-best-practices`
    - **Dimensions** _collapsed_
      - [✓] `docs-new/dimensions/what-is-a-dimension`
      - [✓] `docs-new/dimensions/create-and-edit-dimension`
      - [✓] `docs-new/dimensions/dimension-values`
      - [✓] `docs-new/dimensions/using-dimensions-with-variables`
      - [✓] `docs-new/dimensions/dimension-operations`
      - [✓] `docs-new/dimensions/dimension-best-practices`
    - **Time** _collapsed_
      - [✓] `docs-new/time/time-in-oculon`
      - [✓] `docs-new/time/time-granularity`
      - [✗ MISSING] `docs-new/time/actuals-and-forecast-boundary`
      - [✓] `docs-new/time/relative-time`
      - [✓] `docs-new/time/time-aggregation`
      - [✓] `docs-new/time/time-best-practices`
    - **Formulas** _collapsed_
      - [✓] `docs-new/formulas/formula-basics`
      - [✓] `docs-new/formulas/formula-editor`
      - [✓] `docs-new/formulas/functions`
      - [✓] `docs-new/formulas/helper-variables-and-modifiers`
      - [✓] `docs-new/formulas/common-formula-patterns`
      - [✓] `docs-new/formulas/formula-errors`
      - [✓] `docs-new/formulas/formula-best-practices`
    - **Models** _collapsed_
      - [✓] `docs-new/models/what-is-a-model`
      - [✓] `docs-new/models/model-structure`
      - [✓] `docs-new/models/linked-models`
      - [✓] `docs-new/models/model-settings`
      - [✗ MISSING] `docs-new/models/cloning-and-versioning`
      - [✗ MISSING] `docs-new/models/model-organization`
      - [✓] `docs-new/models/model-best-practices`
    - **Databases** _collapsed_
      - [✓] `docs-new/databases/what-is-a-database`
      - [✓] `docs-new/databases/database-types`
      - [✓] `docs-new/databases/database-structure`
      - [✓] `docs-new/databases/working-with-data`
      - [✓] `docs-new/databases/linked-data`
      - [✓] `docs-new/databases/refresh-and-sync-behavior`
      - [✓] `docs-new/databases/database-best-practices`
    - **Scenarios** _collapsed_
      - [✓] `docs-new/scenarios/what-is-a-scenario`
      - [✓] `docs-new/scenarios/create-and-manage-scenarios`
      - [✓] `docs-new/scenarios/scenario-sync-behavior`
      - [✓] `docs-new/scenarios/scenario-overrides`
      - [✓] `docs-new/scenarios/compare-scenarios`
      - [✓] `docs-new/scenarios/versioning-and-snapshots`
      - [✓] `docs-new/scenarios/scenario-best-practices`
    - **Views** _collapsed_
      - [✓] `docs-new/views/what-is-a-view`
      - [✓] `docs-new/views/filters-sorts-and-grouping`
      - [✓] `docs-new/views/compare-in-views`
      - [✗ MISSING] `docs-new/views/private-vs-shared-views`
      - [✗ MISSING] `docs-new/views/view-behavior`
      - [✓] `docs-new/views/view-best-practices`
    - **Compare** _collapsed_
      - [✓] `docs-new/compare/what-is-a-compare`
      - [✓] `docs-new/compare/time-compare`
      - [✓] `docs-new/compare/scenario-compare`
    - **Boards** _collapsed_
      - [✓] `docs-new/boards/what-is-a-board`
      - [✓] `docs-new/boards/board-layout`
      - [✓] `docs-new/boards/charts`
      - [✓] `docs-new/boards/chart-interaction`
      - [✓] `docs-new/boards/tables-on-boards`
      - [✓] `docs-new/boards/kpi-and-summary-blocks`
      - [✓] `docs-new/boards/sharing-boards`
      - [✓] `docs-new/boards/board-best-practices`
    - **Sharing & permissions** _collapsed_
      - [✓] `docs-new/sharing-and-permissions/sharing-basics`
      - [✓] `docs-new/sharing-and-permissions/roles-and-permissions`
      - [✓] `docs-new/sharing-and-permissions/members-guests-and-groups`
      - [✓] `docs-new/sharing-and-permissions/permission-inheritance`
      - [✓] `docs-new/sharing-and-permissions/comments-and-collaboration`
      - [✓] `docs-new/sharing-and-permissions/sensitive-data-controls`
      - [✓] `docs-new/sharing-and-permissions/external-sharing-and-exports`
    - **Troubleshooting** _collapsed_
      - [✓] `docs-new/troubleshooting/formula-issues`
      - [✓] `docs-new/troubleshooting/data-mismatches`
      - [✓] `docs-new/troubleshooting/scenario-issues`
      - [✓] `docs-new/troubleshooting/permissions-issues`
      - [✓] `docs-new/troubleshooting/agent-issues`
      - [✓] `docs-new/troubleshooting/performance-issues`
      - [✓] `docs-new/troubleshooting/common-errors`
  - **AI**
    - **Overview** _collapsed_
      - [✓] `docs-new/ai/ai-in-oculon`
      - [✓] `docs-new/ai/modeling-with-ai`
      - [✓] `docs-new/ai/reporting-with-ai`
      - [✓] `docs-new/ai/plan-mode`
    - **Custom agents** _collapsed_
      - [✓] `docs-new/custom-agents/what-are-custom-agents`
      - [✓] `docs-new/custom-agents/create-a-custom-agent`
      - [✓] `docs-new/custom-agents/agent-context-and-knowledge`
      - [✓] `docs-new/custom-agents/agent-actions`
      - [✓] `docs-new/custom-agents/agent-permissions`
      - [✓] `docs-new/custom-agents/agent-connections`
      - [✓] `docs-new/custom-agents/agent-safety-and-review`
      - [✓] `docs-new/custom-agents/agent-best-practices`
    - **Context and connections** _collapsed_
      - [✓] `docs-new/ai/mcp`
      - [✓] `docs-new/ai/skills`
      - [✓] `docs-new/ai/connectors`
  - **Administration**
    - **Workspace setup** _collapsed_
      - [✓] `docs-new/admin-guide/workspace-settings`
      - [✓] `docs-new/admin-guide/groups`
    - **Access and security** _collapsed_
      - [✓] `docs-new/admin-guide/members-and-roles`
      - [✓] `docs-new/admin-guide/login-methods`
      - [✓] `docs-new/admin-guide/security`
    - **Oversight and billing** _collapsed_
      - [✓] `docs-new/admin-guide/audit-logs`
      - [✓] `docs-new/admin-guide/billing-and-plans`
      - [✓] `docs-new/admin-guide/usage-and-limits`
- **How to guides**
  - **Overview**
    - [✓] `how-to/index`
- **Integrations**
  - [✓] `integration-docs/index`
- **Old docs** _hidden_
  - **Getting Started** _expanded_
    - [✓] `support-docs/getting-started/welcome-to-oculon`
    - [✓] `support-docs/getting-started/profile-setup`
    - [✓] `support-docs/getting-started/navigating-oculon`
    - [✓] `support-docs/getting-started/core-concepts`
    - [✓] `support-docs/getting-started/oculon-glossary`
  - **Build & Model** _expanded_
    - [✓] `support-docs/oculon-basics/variable`
    - [✓] `support-docs/oculon-basics/dimensions`
    - [✓] `support-docs/oculon-basics/time`
    - [✓] `support-docs/oculon-basics/database`
    - [✓] `support-docs/oculon-basics/library/query-and-database`
    - [✓] `support-docs/oculon-basics/data-integrations`
  - **Analyze & Use** _expanded_
    - [✓] `support-docs/oculon-basics/boards`
    - [✓] `support-docs/oculon-basics/views`
    - [✓] `support-docs/oculon-basics/compare`
  - **Formulas & Logic** _expanded_
    - [✓] `support-docs/oculon-basics/formulas/creating-formulas`
    - [✓] `support-docs/oculon-basics/formulas/functions`
    - [✓] `support-docs/oculon-basics/formulas/helper-variables`
    - [✓] `support-docs/oculon-basics/currency-and-conversion`
  - **Plan & Collaborate** _expanded_
    - [✓] `support-docs/plan-and-collaborate/scenario`
  - **Guides** _expanded_
    - [✓] `support-docs/guides/build-your-first-model`
    - [✓] `support-docs/guides/keyboard-shortcuts`
    - [✓] `support-docs/guides/function-glossary`
  - **Settings & Access** _expanded_
    - **Account** _expanded_
      - [✓] `support-docs/account/profile`
      - [✓] `support-docs/account/preferences`
      - [✓] `support-docs/account/notifications`
      - [✓] `support-docs/account/access-and-security`
    - **Admin** _expanded_
      - [✓] `support-docs/admin/workspace`
      - [✓] `support-docs/admin/teamspace`
      - [✓] `support-docs/admin/members-and-roles`
      - [✓] `support-docs/admin/security`
      - [✓] `support-docs/admin/billing-and-plans`
      - [✓] `support-docs/admin/audit-logs`
      - [✓] `support-docs/admin/login-methods`
      - [✓] `support-docs/admin/saml-scim`
      - [✓] `support-docs/admin/usage-limits`

## 3. Page inventory

| Title | File path | Navigation group | Parent | Live | Legacy | Notes |
|---|---|---|---|---|---|---|
| Connectors | `docs-new/ai/connectors` | AI > Context and connections | Context and connections | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/ai/connectors.mdx; identical twin at `support-docs/ai/connectors.mdx` |
| MCP | `docs-new/ai/mcp` | AI > Context and connections | Context and connections | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/ai/mcp.mdx; identical twin at `support-docs/ai/mcp.mdx` |
| Skills | `docs-new/ai/skills` | AI > Context and connections | Context and connections | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/ai/skills.mdx; identical twin at `support-docs/ai/skills.mdx` |
| Agent actions | `docs-new/custom-agents/agent-actions` | AI > Custom agents | Custom agents | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/custom-agents/agent-actions.mdx; identical twin at `support-docs/custom-agents/agent-actions.mdx` |
| Agent best practices | `docs-new/custom-agents/agent-best-practices` | AI > Custom agents | Custom agents | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/custom-agents/agent-best-practices.mdx; identical twin at `support-docs/custom-agents/agent-best-practices.mdx` |
| Agent connections | `docs-new/custom-agents/agent-connections` | AI > Custom agents | Custom agents | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/custom-agents/agent-connections.mdx; identical twin at `support-docs/custom-agents/agent-connections.mdx` |
| Agent context and knowledge | `docs-new/custom-agents/agent-context-and-knowledge` | AI > Custom agents | Custom agents | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/custom-agents/agent-context-and-knowledge.mdx; identical twin at `support-docs/custom-agents/agent-context-and-knowledge.mdx` |
| Agent permissions | `docs-new/custom-agents/agent-permissions` | AI > Custom agents | Custom agents | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/custom-agents/agent-permissions.mdx; identical twin at `support-docs/custom-agents/agent-permissions.mdx` |
| Agent safety and review | `docs-new/custom-agents/agent-safety-and-review` | AI > Custom agents | Custom agents | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/custom-agents/agent-safety-and-review.mdx; identical twin at `support-docs/custom-agents/agent-safety-and-review.mdx` |
| Create a custom agent | `docs-new/custom-agents/create-a-custom-agent` | AI > Custom agents | Custom agents | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/custom-agents/create-a-custom-agent.mdx; identical twin at `support-docs/custom-agents/create-a-custom-agent.mdx` |
| What are custom agents | `docs-new/custom-agents/what-are-custom-agents` | AI > Custom agents | Custom agents | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/custom-agents/what-are-custom-agents.mdx; identical twin at `support-docs/custom-agents/what-are-custom-agents.mdx` |
| AI in Oculon | `docs-new/ai/ai-in-oculon` | AI > Overview | Overview | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/ai/ai-in-oculon.mdx; identical twin at `support-docs/ai/ai-in-oculon.mdx` |
| Modeling with AI | `docs-new/ai/modeling-with-ai` | AI > Overview | Overview | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/ai/modeling-with-ai.mdx; identical twin at `support-docs/ai/modeling-with-ai.mdx` |
| Plan mode | `docs-new/ai/plan-mode` | AI > Overview | Overview | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/ai/plan-mode.mdx; identical twin at `support-docs/ai/plan-mode.mdx` |
| Reporting with AI | `docs-new/ai/reporting-with-ai` | AI > Overview | Overview | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/ai/reporting-with-ai.mdx; identical twin at `support-docs/ai/reporting-with-ai.mdx` |
| Login methods | `docs-new/admin-guide/login-methods` | Administration > Access and security | Access and security | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/admin-guide/login-methods.mdx; identical twin at `support-docs/admin-guide/login-methods.mdx` |
| Members and roles | `docs-new/admin-guide/members-and-roles` | Administration > Access and security | Access and security | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/admin-guide/members-and-roles.mdx; divergent twin at `support-docs/admin-guide/members-and-roles.mdx` |
| Security | `docs-new/admin-guide/security` | Administration > Access and security | Access and security | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/admin-guide/security.mdx; divergent twin at `support-docs/admin-guide/security.mdx` |
| Audit logs | `docs-new/admin-guide/audit-logs` | Administration > Oversight and billing | Oversight and billing | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/admin-guide/audit-logs.mdx; identical twin at `support-docs/admin-guide/audit-logs.mdx` |
| Billing and plans | `docs-new/admin-guide/billing-and-plans` | Administration > Oversight and billing | Oversight and billing | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/admin-guide/billing-and-plans.mdx; identical twin at `support-docs/admin-guide/billing-and-plans.mdx` |
| Usage and limits | `docs-new/admin-guide/usage-and-limits` | Administration > Oversight and billing | Oversight and billing | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/admin-guide/usage-and-limits.mdx; identical twin at `support-docs/admin-guide/usage-and-limits.mdx` |
| Groups | `docs-new/admin-guide/groups` | Administration > Workspace setup | Workspace setup | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/admin-guide/groups.mdx; divergent twin at `support-docs/admin-guide/groups.mdx` |
| Workspace settings | `docs-new/admin-guide/workspace-settings` | Administration > Workspace setup | Workspace setup | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/admin-guide/workspace-settings.mdx; divergent twin at `support-docs/admin-guide/workspace-settings.mdx` |
| Board best practices | `docs-new/boards/board-best-practices` | Planning and analysis > Boards | Boards | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/boards/board-best-practices.mdx; identical twin at `support-docs/boards/board-best-practices.mdx` |
| Board layout | `docs-new/boards/board-layout` | Planning and analysis > Boards | Boards | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/boards/board-layout.mdx; divergent twin at `support-docs/boards/board-layout.mdx` |
| Chart interaction | `docs-new/boards/chart-interaction` | Planning and analysis > Boards | Boards | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new) |
| Charts | `docs-new/boards/charts` | Planning and analysis > Boards | Boards | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/boards/charts.mdx; divergent twin at `support-docs/boards/charts.mdx` |
| KPI and summary blocks | `docs-new/boards/kpi-and-summary-blocks` | Planning and analysis > Boards | Boards | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/boards/kpi-and-summary-blocks.mdx; divergent twin at `support-docs/boards/kpi-and-summary-blocks.mdx` |
| Sharing boards | `docs-new/boards/sharing-boards` | Planning and analysis > Boards | Boards | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/boards/sharing-boards.mdx; divergent twin at `support-docs/boards/sharing-boards.mdx` |
| Tables on boards | `docs-new/boards/tables-on-boards` | Planning and analysis > Boards | Boards | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/boards/tables-on-boards.mdx; divergent twin at `support-docs/boards/tables-on-boards.mdx` |
| What is a board | `docs-new/boards/what-is-a-board` | Planning and analysis > Boards | Boards | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/boards/what-is-a-board.mdx; divergent twin at `support-docs/boards/what-is-a-board.mdx` |
| Scenario compare | `docs-new/compare/scenario-compare` | Planning and analysis > Compare | Compare | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new) |
| Time compare | `docs-new/compare/time-compare` | Planning and analysis > Compare | Compare | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new) |
| What is a compare | `docs-new/compare/what-is-a-compare` | Planning and analysis > Compare | Compare | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new) |
| Database best practices | `docs-new/databases/database-best-practices` | Planning and analysis > Databases | Databases | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/databases/database-best-practices.mdx; divergent twin at `support-docs/databases/database-best-practices.mdx` |
| Database structure | `docs-new/databases/database-structure` | Planning and analysis > Databases | Databases | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/databases/database-structure.mdx; divergent twin at `support-docs/databases/database-structure.mdx` |
| Database types | `docs-new/databases/database-types` | Planning and analysis > Databases | Databases | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/databases/database-types.mdx; divergent twin at `support-docs/databases/database-types.mdx` |
| Linked data | `docs-new/databases/linked-data` | Planning and analysis > Databases | Databases | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/databases/linked-data.mdx; divergent twin at `support-docs/databases/linked-data.mdx` |
| Refresh and sync behavior | `docs-new/databases/refresh-and-sync-behavior` | Planning and analysis > Databases | Databases | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/databases/refresh-and-sync-behavior.mdx; divergent twin at `support-docs/databases/refresh-and-sync-behavior.mdx` |
| What is a database | `docs-new/databases/what-is-a-database` | Planning and analysis > Databases | Databases | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/databases/what-is-a-database.mdx; divergent twin at `support-docs/databases/what-is-a-database.mdx` |
| Working with data | `docs-new/databases/working-with-data` | Planning and analysis > Databases | Databases | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/databases/working-with-data.mdx; divergent twin at `support-docs/databases/working-with-data.mdx` |
| Create and edit dimensions | `docs-new/dimensions/create-and-edit-dimension` | Planning and analysis > Dimensions | Dimensions | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new) |
| Dimension best practices | `docs-new/dimensions/dimension-best-practices` | Planning and analysis > Dimensions | Dimensions | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/dimensions/dimension-best-practices.mdx; identical twin at `support-docs/dimensions/dimension-best-practices.mdx` |
| Dimension operations | `docs-new/dimensions/dimension-operations` | Planning and analysis > Dimensions | Dimensions | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/dimensions/dimension-operations.mdx; divergent twin at `support-docs/dimensions/dimension-operations.mdx` |
| Dimension values | `docs-new/dimensions/dimension-values` | Planning and analysis > Dimensions | Dimensions | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/dimensions/dimension-values.mdx; divergent twin at `support-docs/dimensions/dimension-values.mdx` |
| Using dimensions with variables | `docs-new/dimensions/using-dimensions-with-variables` | Planning and analysis > Dimensions | Dimensions | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/dimensions/using-dimensions-with-variables.mdx; identical twin at `support-docs/dimensions/using-dimensions-with-variables.mdx` |
| What is a dimension | `docs-new/dimensions/what-is-a-dimension` | Planning and analysis > Dimensions | Dimensions | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/dimensions/what-is-a-dimension.mdx; identical twin at `support-docs/dimensions/what-is-a-dimension.mdx` |
| Common formula patterns | `docs-new/formulas/common-formula-patterns` | Planning and analysis > Formulas | Formulas | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/formulas/common-formula-patterns.mdx; divergent twin at `support-docs/formulas/common-formula-patterns.mdx` |
| Formula basics | `docs-new/formulas/formula-basics` | Planning and analysis > Formulas | Formulas | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/formulas/formula-basics.mdx; divergent twin at `support-docs/formulas/formula-basics.mdx` |
| Formula best practices | `docs-new/formulas/formula-best-practices` | Planning and analysis > Formulas | Formulas | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/formulas/formula-best-practices.mdx; divergent twin at `support-docs/formulas/formula-best-practices.mdx` |
| Formula editor | `docs-new/formulas/formula-editor` | Planning and analysis > Formulas | Formulas | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/formulas/formula-editor.mdx; divergent twin at `support-docs/formulas/formula-editor.mdx` |
| Formula errors | `docs-new/formulas/formula-errors` | Planning and analysis > Formulas | Formulas | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/formulas/formula-errors.mdx; divergent twin at `support-docs/formulas/formula-errors.mdx` |
| Functions | `docs-new/formulas/functions` | Planning and analysis > Formulas | Formulas | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/formulas/functions.mdx; divergent twin at `support-docs/formulas/functions.mdx` |
| Helper variables and modifiers | `docs-new/formulas/helper-variables-and-modifiers` | Planning and analysis > Formulas | Formulas | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/formulas/helper-variables-and-modifiers.mdx; divergent twin at `support-docs/formulas/helper-variables-and-modifiers.mdx` |
| (missing file) | `docs-new/models/cloning-and-versioning` | Planning and analysis > Models | Models | no | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/models/cloning-and-versioning.mdx; Referenced in nav but file missing |
| Linked models | `docs-new/models/linked-models` | Planning and analysis > Models | Models | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/models/linked-models.mdx; divergent twin at `support-docs/models/linked-models.mdx` |
| Model best practices | `docs-new/models/model-best-practices` | Planning and analysis > Models | Models | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/models/model-best-practices.mdx; divergent twin at `support-docs/models/model-best-practices.mdx` |
| (missing file) | `docs-new/models/model-organization` | Planning and analysis > Models | Models | no | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/models/model-organization.mdx; Referenced in nav but file missing |
| Model settings | `docs-new/models/model-settings` | Planning and analysis > Models | Models | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/models/model-settings.mdx; divergent twin at `support-docs/models/model-settings.mdx` |
| Model structure | `docs-new/models/model-structure` | Planning and analysis > Models | Models | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/models/model-structure.mdx; divergent twin at `support-docs/models/model-structure.mdx` |
| What is a model | `docs-new/models/what-is-a-model` | Planning and analysis > Models | Models | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/models/what-is-a-model.mdx; divergent twin at `support-docs/models/what-is-a-model.mdx` |
| Compare scenarios | `docs-new/scenarios/compare-scenarios` | Planning and analysis > Scenarios | Scenarios | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/scenarios/compare-scenarios.mdx; divergent twin at `support-docs/scenarios/compare-scenarios.mdx` |
| Create and manage scenarios | `docs-new/scenarios/create-and-manage-scenarios` | Planning and analysis > Scenarios | Scenarios | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/scenarios/create-and-manage-scenarios.mdx; divergent twin at `support-docs/scenarios/create-and-manage-scenarios.mdx` |
| Scenario best practices | `docs-new/scenarios/scenario-best-practices` | Planning and analysis > Scenarios | Scenarios | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/scenarios/scenario-best-practices.mdx; divergent twin at `support-docs/scenarios/scenario-best-practices.mdx` |
| Scenario overrides | `docs-new/scenarios/scenario-overrides` | Planning and analysis > Scenarios | Scenarios | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/scenarios/scenario-overrides.mdx; divergent twin at `support-docs/scenarios/scenario-overrides.mdx` |
| Scenario sync behavior | `docs-new/scenarios/scenario-sync-behavior` | Planning and analysis > Scenarios | Scenarios | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/scenarios/scenario-sync-behavior.mdx; divergent twin at `support-docs/scenarios/scenario-sync-behavior.mdx` |
| Versioning and snapshots | `docs-new/scenarios/versioning-and-snapshots` | Planning and analysis > Scenarios | Scenarios | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/scenarios/versioning-and-snapshots.mdx; divergent twin at `support-docs/scenarios/versioning-and-snapshots.mdx` |
| What is a scenario | `docs-new/scenarios/what-is-a-scenario` | Planning and analysis > Scenarios | Scenarios | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/scenarios/what-is-a-scenario.mdx; divergent twin at `support-docs/scenarios/what-is-a-scenario.mdx` |
| Comments and collaboration | `docs-new/sharing-and-permissions/comments-and-collaboration` | Planning and analysis > Sharing & permissions | Sharing & permissions | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/sharing-and-permissions/comments-and-collaboration.mdx; divergent twin at `support-docs/sharing-and-permissions/comments-and-collaboration.mdx` |
| External sharing and exports | `docs-new/sharing-and-permissions/external-sharing-and-exports` | Planning and analysis > Sharing & permissions | Sharing & permissions | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/sharing-and-permissions/external-sharing-and-exports.mdx; divergent twin at `support-docs/sharing-and-permissions/external-sharing-and-exports.mdx` |
| Members, guests, and groups | `docs-new/sharing-and-permissions/members-guests-and-groups` | Planning and analysis > Sharing & permissions | Sharing & permissions | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/sharing-and-permissions/members-guests-and-groups.mdx; divergent twin at `support-docs/sharing-and-permissions/members-guests-and-groups.mdx` |
| Permission inheritance | `docs-new/sharing-and-permissions/permission-inheritance` | Planning and analysis > Sharing & permissions | Sharing & permissions | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/sharing-and-permissions/permission-inheritance.mdx; divergent twin at `support-docs/sharing-and-permissions/permission-inheritance.mdx` |
| Roles and permissions | `docs-new/sharing-and-permissions/roles-and-permissions` | Planning and analysis > Sharing & permissions | Sharing & permissions | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/sharing-and-permissions/roles-and-permissions.mdx; divergent twin at `support-docs/sharing-and-permissions/roles-and-permissions.mdx` |
| Sensitive data controls | `docs-new/sharing-and-permissions/sensitive-data-controls` | Planning and analysis > Sharing & permissions | Sharing & permissions | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/sharing-and-permissions/sensitive-data-controls.mdx; divergent twin at `support-docs/sharing-and-permissions/sensitive-data-controls.mdx` |
| Sharing basics | `docs-new/sharing-and-permissions/sharing-basics` | Planning and analysis > Sharing & permissions | Sharing & permissions | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/sharing-and-permissions/sharing-basics.mdx; divergent twin at `support-docs/sharing-and-permissions/sharing-basics.mdx` |
| (missing file) | `docs-new/time/actuals-and-forecast-boundary` | Planning and analysis > Time | Time | no | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/time/actuals-and-forecast-boundary.mdx; Referenced in nav but file missing |
| Relative time | `docs-new/time/relative-time` | Planning and analysis > Time | Time | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/time/relative-time.mdx; divergent twin at `support-docs/time/relative-time.mdx` |
| Time aggregation | `docs-new/time/time-aggregation` | Planning and analysis > Time | Time | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/time/time-aggregation.mdx; divergent twin at `support-docs/time/time-aggregation.mdx` |
| Time best practices | `docs-new/time/time-best-practices` | Planning and analysis > Time | Time | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/time/time-best-practices.mdx; divergent twin at `support-docs/time/time-best-practices.mdx` |
| Time granularity | `docs-new/time/time-granularity` | Planning and analysis > Time | Time | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/time/time-granularity.mdx; divergent twin at `support-docs/time/time-granularity.mdx` |
| Time in Oculon | `docs-new/time/time-in-oculon` | Planning and analysis > Time | Time | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/time/time-in-oculon.mdx; divergent twin at `support-docs/time/time-in-oculon.mdx` |
| Agent issues | `docs-new/troubleshooting/agent-issues` | Planning and analysis > Troubleshooting | Troubleshooting | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/troubleshooting/agent-issues.mdx; identical twin at `support-docs/troubleshooting/agent-issues.mdx` |
| Common errors | `docs-new/troubleshooting/common-errors` | Planning and analysis > Troubleshooting | Troubleshooting | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/troubleshooting/common-errors.mdx; identical twin at `support-docs/troubleshooting/common-errors.mdx` |
| Data mismatches | `docs-new/troubleshooting/data-mismatches` | Planning and analysis > Troubleshooting | Troubleshooting | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/troubleshooting/data-mismatches.mdx; identical twin at `support-docs/troubleshooting/data-mismatches.mdx` |
| Formula issues | `docs-new/troubleshooting/formula-issues` | Planning and analysis > Troubleshooting | Troubleshooting | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/troubleshooting/formula-issues.mdx; identical twin at `support-docs/troubleshooting/formula-issues.mdx` |
| Performance issues | `docs-new/troubleshooting/performance-issues` | Planning and analysis > Troubleshooting | Troubleshooting | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/troubleshooting/performance-issues.mdx; identical twin at `support-docs/troubleshooting/performance-issues.mdx` |
| Permissions issues | `docs-new/troubleshooting/permissions-issues` | Planning and analysis > Troubleshooting | Troubleshooting | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/troubleshooting/permissions-issues.mdx; identical twin at `support-docs/troubleshooting/permissions-issues.mdx` |
| Scenario issues | `docs-new/troubleshooting/scenario-issues` | Planning and analysis > Troubleshooting | Troubleshooting | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/troubleshooting/scenario-issues.mdx; identical twin at `support-docs/troubleshooting/scenario-issues.mdx` |
| Create and edit variables | `docs-new/variables/create-and-edit-variables` | Planning and analysis > Variables | Variables | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/variables/create-and-edit-variables.mdx; divergent twin at `support-docs/variables/create-and-edit-variables.mdx` |
| Variable behavior | `docs-new/variables/variable-behavior` | Planning and analysis > Variables | Variables | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/variables/variable-behavior.mdx; identical twin at `support-docs/variables/variable-behavior.mdx` |
| Variable best practices | `docs-new/variables/variable-best-practices` | Planning and analysis > Variables | Variables | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/variables/variable-best-practices.mdx; identical twin at `support-docs/variables/variable-best-practices.mdx` |
| Variable breakdown | `docs-new/variables/variable-breakdown` | Planning and analysis > Variables | Variables | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new) |
| Variable formatting | `docs-new/variables/variable-formatting` | Planning and analysis > Variables | Variables | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/variables/variable-formatting.mdx; divergent twin at `support-docs/variables/variable-formatting.mdx` |
| Variable references | `docs-new/variables/variable-references` | Planning and analysis > Variables | Variables | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/variables/variable-references.mdx; identical twin at `support-docs/variables/variable-references.mdx` |
| Variable types | `docs-new/variables/variable-types` | Planning and analysis > Variables | Variables | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/variables/variable-types.mdx; divergent twin at `support-docs/variables/variable-types.mdx` |
| What is a variable | `docs-new/variables/what-is-a-variable` | Planning and analysis > Variables | Variables | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/variables/what-is-a-variable.mdx; divergent twin at `support-docs/variables/what-is-a-variable.mdx` |
| Compare in views | `docs-new/views/compare-in-views` | Planning and analysis > Views | Views | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/views/compare-in-views.mdx; divergent twin at `support-docs/views/compare-in-views.mdx` |
| Filters, sorts, and grouping | `docs-new/views/filters-sorts-and-grouping` | Planning and analysis > Views | Views | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/views/filters-sorts-and-grouping.mdx; divergent twin at `support-docs/views/filters-sorts-and-grouping.mdx` |
| (missing file) | `docs-new/views/private-vs-shared-views` | Planning and analysis > Views | Views | no | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/views/private-vs-shared-views.mdx; Referenced in nav but file missing |
| (missing file) | `docs-new/views/view-behavior` | Planning and analysis > Views | Views | no | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/views/view-behavior.mdx; Referenced in nav but file missing |
| View best practices | `docs-new/views/view-best-practices` | Planning and analysis > Views | Views | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/views/view-best-practices.mdx; divergent twin at `support-docs/views/view-best-practices.mdx` |
| What is a view | `docs-new/views/what-is-a-view` | Planning and analysis > Views | Views | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/views/what-is-a-view.mdx; divergent twin at `support-docs/views/what-is-a-view.mdx` |
| Core concepts overview | `docs-new/getting-started/core-concepts-overview` | Start here > Getting started | Getting started | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/getting-started/core-concepts-overview.mdx; divergent twin at `support-docs/getting-started/core-concepts-overview.mdx` |
| Glossary | `docs-new/getting-started/glossary` | Start here > Getting started | Getting started | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/getting-started/glossary.mdx; divergent twin at `support-docs/getting-started/glossary.mdx` |
| How Oculon is organized | `docs-new/getting-started/how-oculon-is-organized` | Start here > Getting started | Getting started | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/getting-started/how-oculon-is-organized.mdx; divergent twin at `support-docs/getting-started/how-oculon-is-organized.mdx` |
| Keyboard shortcuts | `docs-new/getting-started/keyboard-shortcuts` | Start here > Getting started | Getting started | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/getting-started/keyboard-shortcuts.mdx; divergent twin at `support-docs/getting-started/keyboard-shortcuts.mdx` |
| What is Oculon | `docs-new/getting-started/what-is-oculon` | Start here > Getting started | Getting started | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/getting-started/what-is-oculon.mdx; divergent twin at `support-docs/getting-started/what-is-oculon.mdx` |
| Profile and preferences | `docs-new/workspace-and-organization/profile-and-preferences` | Start here > Workspace and organization | Workspace and organization | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/workspace-and-organization/profile-and-preferences.mdx; divergent twin at `support-docs/workspace-and-organization/profile-and-preferences.mdx` |
| Teamspaces and organization | `docs-new/workspace-and-organization/teamspaces-and-organization` | Start here > Workspace and organization | Workspace and organization | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/workspace-and-organization/teamspaces-and-organization.mdx; divergent twin at `support-docs/workspace-and-organization/teamspaces-and-organization.mdx` |
| What is a workspace | `docs-new/workspace-and-organization/what-is-a-workspace` | Start here > Workspace and organization | Workspace and organization | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/workspace-and-organization/what-is-a-workspace.mdx; divergent twin at `support-docs/workspace-and-organization/what-is-a-workspace.mdx` |
| Workspace access and visibility | `docs-new/workspace-and-organization/workspace-access-and-visibility` | Start here > Workspace and organization | Workspace and organization | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/workspace-and-organization/workspace-access-and-visibility.mdx; divergent twin at `support-docs/workspace-and-organization/workspace-access-and-visibility.mdx` |
| Navigate the sidebar | `docs-new/your-sidebar/navigate-the-sidebar` | Start here > Your sidebar | Your sidebar | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/your-sidebar/navigate-the-sidebar.mdx; divergent twin at `support-docs/your-sidebar/navigate-the-sidebar.mdx` |
| Organize your workspace | `docs-new/your-sidebar/organize-your-workspace` | Start here > Your sidebar | Your sidebar | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/your-sidebar/organize-your-workspace.mdx; identical twin at `support-docs/your-sidebar/organize-your-workspace.mdx` |
| Search and quick access | `docs-new/your-sidebar/search-and-quick-access` | Start here > Your sidebar | Your sidebar | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/your-sidebar/search-and-quick-access.mdx; identical twin at `support-docs/your-sidebar/search-and-quick-access.mdx` |
| Sidebar customization | `docs-new/your-sidebar/sidebar-customization` | Start here > Your sidebar | Your sidebar | yes | becoming Concepts Legacy | Current Concepts tab content (docs-new); Duplicate slug also at support-docs/your-sidebar/sidebar-customization.mdx; identical twin at `support-docs/your-sidebar/sidebar-customization.mdx` |
|  | `how-to/index` | Overview | Overview | yes | no | How to guides tab |
|  | `integration-docs/index` | (tab root) | Integrations | yes | no | Integrations tab |
| Boards | `support-docs/oculon-basics/boards` | Analyze & Use | Analyze & Use | no | yes | Hidden Old docs tab (support-docs) |
| Compare | `support-docs/oculon-basics/compare` | Analyze & Use | Analyze & Use | no | yes | Hidden Old docs tab (support-docs) |
| Views | `support-docs/oculon-basics/views` | Analyze & Use | Analyze & Use | no | yes | Hidden Old docs tab (support-docs) |
| Data Integrations | `support-docs/oculon-basics/data-integrations` | Build & Model | Build & Model | no | yes | Hidden Old docs tab (support-docs) |
| Database | `support-docs/oculon-basics/database` | Build & Model | Build & Model | no | yes | Hidden Old docs tab (support-docs) |
| Dimensions | `support-docs/oculon-basics/dimensions` | Build & Model | Build & Model | no | yes | Hidden Old docs tab (support-docs) |
| Query And Database | `support-docs/oculon-basics/library/query-and-database` | Build & Model | Build & Model | no | yes | Hidden Old docs tab (support-docs) |
| Time | `support-docs/oculon-basics/time` | Build & Model | Build & Model | no | yes | Hidden Old docs tab (support-docs) |
| Variable | `support-docs/oculon-basics/variable` | Build & Model | Build & Model | no | yes | Hidden Old docs tab (support-docs) |
| Currency And Conversion | `support-docs/oculon-basics/currency-and-conversion` | Formulas & Logic | Formulas & Logic | no | yes | Hidden Old docs tab (support-docs) |
| Creating Formulas | `support-docs/oculon-basics/formulas/creating-formulas` | Formulas & Logic | Formulas & Logic | no | yes | Hidden Old docs tab (support-docs) |
| Functions | `support-docs/oculon-basics/formulas/functions` | Formulas & Logic | Formulas & Logic | no | yes | Hidden Old docs tab (support-docs) |
| Helper Variables | `support-docs/oculon-basics/formulas/helper-variables` | Formulas & Logic | Formulas & Logic | no | yes | Hidden Old docs tab (support-docs) |
| Core concepts | `support-docs/getting-started/core-concepts` | Getting Started | Getting Started | no | yes | Hidden Old docs tab (support-docs) |
| Navigating Oculon | `support-docs/getting-started/navigating-oculon` | Getting Started | Getting Started | no | yes | Hidden Old docs tab (support-docs) |
| Oculon Glossary | `support-docs/getting-started/oculon-glossary` | Getting Started | Getting Started | no | yes | Hidden Old docs tab (support-docs) |
| Profile Setup | `support-docs/getting-started/profile-setup` | Getting Started | Getting Started | no | yes | Hidden Old docs tab (support-docs) |
| Welcome To Oculon | `support-docs/getting-started/welcome-to-oculon` | Getting Started | Getting Started | no | yes | Hidden Old docs tab (support-docs) |
| Build your first model | `support-docs/guides/build-your-first-model` | Guides | Guides | no | yes | Hidden Old docs tab (support-docs) |
| Function glossary | `support-docs/guides/function-glossary` | Guides | Guides | no | yes | Hidden Old docs tab (support-docs) |
| Keyboard Shortcuts | `support-docs/guides/keyboard-shortcuts` | Guides | Guides | no | yes | Hidden Old docs tab (support-docs) |
| Scenario | `support-docs/plan-and-collaborate/scenario` | Plan & Collaborate | Plan & Collaborate | no | yes | Hidden Old docs tab (support-docs) |
| Access And Security | `support-docs/account/access-and-security` | Settings & Access > Account | Account | no | yes | Hidden Old docs tab (support-docs) |
| Notifications | `support-docs/account/notifications` | Settings & Access > Account | Account | no | yes | Hidden Old docs tab (support-docs) |
| Preferences | `support-docs/account/preferences` | Settings & Access > Account | Account | no | yes | Hidden Old docs tab (support-docs) |
| Profile | `support-docs/account/profile` | Settings & Access > Account | Account | no | yes | Hidden Old docs tab (support-docs) |
| Audit logs | `support-docs/admin/audit-logs` | Settings & Access > Admin | Admin | no | yes | Hidden Old docs tab (support-docs) |
| Billing and plans | `support-docs/admin/billing-and-plans` | Settings & Access > Admin | Admin | no | yes | Hidden Old docs tab (support-docs) |
| Login methods | `support-docs/admin/login-methods` | Settings & Access > Admin | Admin | no | yes | Hidden Old docs tab (support-docs) |
| Members and roles | `support-docs/admin/members-and-roles` | Settings & Access > Admin | Admin | no | yes | Hidden Old docs tab (support-docs) |
| SAML & SCIM | `support-docs/admin/saml-scim` | Settings & Access > Admin | Admin | no | yes | Hidden Old docs tab (support-docs) |
| Security | `support-docs/admin/security` | Settings & Access > Admin | Admin | no | yes | Hidden Old docs tab (support-docs) |
| Teamspace | `support-docs/admin/teamspace` | Settings & Access > Admin | Admin | no | yes | Hidden Old docs tab (support-docs) |
| Usage limits | `support-docs/admin/usage-limits` | Settings & Access > Admin | Admin | no | yes | Hidden Old docs tab (support-docs) |
| Workspace | `support-docs/admin/workspace` | Settings & Access > Admin | Admin | no | yes | Hidden Old docs tab (support-docs) |

\* Concepts-tab pages are live today; Mintlify editor intends to rename that tab to Concepts Legacy.

## 4. Missing nav targets

These paths are in `docs.json` but have **no** matching MDX under the path. All five have a twin under `support-docs/` that was never copied (or was removed) into `docs-new/`.

| Nav path | Twin exists? | Twin path | Redirect hits this dest? |
|---|---|---|---|
| `docs-new/time/actuals-and-forecast-boundary` | yes | `support-docs/time/actuals-and-forecast-boundary.mdx` | yes (`/support-docs/time/actuals-and-forecast-boundary` → `/docs-new/time/actuals-and-forecast-boundary`) |
| `docs-new/models/cloning-and-versioning` | yes | `support-docs/models/cloning-and-versioning.mdx` | yes (`/support-docs/models/cloning-and-versioning` → `/docs-new/models/cloning-and-versioning`) |
| `docs-new/models/model-organization` | yes | `support-docs/models/model-organization.mdx` | yes (`/support-docs/models/model-organization` → `/docs-new/models/model-organization`) |
| `docs-new/views/private-vs-shared-views` | yes | `support-docs/views/private-vs-shared-views.mdx` | yes (`/support-docs/views/private-vs-shared-views` → `/docs-new/views/private-vs-shared-views`) |
| `docs-new/views/view-behavior` | yes | `support-docs/views/view-behavior.mdx` | yes (`/support-docs/views/view-behavior` → `/docs-new/views/view-behavior`) |

## 5. Redirects

- **110 redirects** defined in `docs.json`.
- Pattern: almost all map `/support-docs/...` → `/docs-new/...` (plus `/` → `/docs-new/getting-started/what-is-oculon`).
- **5 redirect destinations are broken** because the `docs-new` targets are the missing files above.
- Risk: any leftover links or bookmarks to those `support-docs` URLs land on 404s after redirect.

## 6. Duplicate / overlap findings

### A. Parallel trees: `docs-new` vs `support-docs` (same relative slug)

**112** path pairs share the same relative slug under both trees.
- **42** are byte-identical
- **70** have divergent content (usually `docs-new` is longer / more fleshed out)

<details><summary>Identical pairs (click to expand)</summary>

- `admin-guide/audit-logs`
- `admin-guide/billing-and-plans`
- `admin-guide/login-methods`
- `admin-guide/usage-and-limits`
- `ai/ai-in-oculon`
- `ai/connectors`
- `ai/mcp`
- `ai/modeling-with-ai`
- `ai/plan-mode`
- `ai/reporting-with-ai`
- `ai/skills`
- `boards/board-best-practices`
- `custom-agents/agent-actions`
- `custom-agents/agent-best-practices`
- `custom-agents/agent-connections`
- `custom-agents/agent-context-and-knowledge`
- `custom-agents/agent-permissions`
- `custom-agents/agent-safety-and-review`
- `custom-agents/create-a-custom-agent`
- `custom-agents/what-are-custom-agents`
- `dimensions/dimension-best-practices`
- `dimensions/using-dimensions-with-variables`
- `dimensions/what-is-a-dimension`
- `getting-started/core-concepts`
- `getting-started/index`
- `getting-started/navigating-oculon`
- `getting-started/oculon-glossary-backup`
- `getting-started/profile-setup`
- `getting-started/welcome-to-oculon`
- `troubleshooting/agent-issues`
- `troubleshooting/common-errors`
- `troubleshooting/data-mismatches`
- `troubleshooting/formula-issues`
- `troubleshooting/performance-issues`
- `troubleshooting/permissions-issues`
- `troubleshooting/scenario-issues`
- `variables/variable-behavior`
- `variables/variable-best-practices`
- `variables/variable-references`
- `your-sidebar/organize-your-workspace`
- `your-sidebar/search-and-quick-access`
- `your-sidebar/sidebar-customization`

</details>

<details><summary>Divergent pairs (click to expand)</summary>

- `admin-guide/groups`
- `admin-guide/members-and-roles`
- `admin-guide/security`
- `admin-guide/workspace-settings`
- `boards/board-interaction`
- `boards/board-layout`
- `boards/charts`
- `boards/kpi-and-summary-blocks`
- `boards/sharing-boards`
- `boards/tables-on-boards`
- `boards/what-is-a-board`
- `databases/database-best-practices`
- `databases/database-structure`
- `databases/database-types`
- `databases/linked-data`
- `databases/refresh-and-sync-behavior`
- `databases/what-is-a-database`
- `databases/working-with-data`
- `dimensions/dimension-operations`
- `dimensions/dimension-values`
- `formulas/common-formula-patterns`
- `formulas/formula-basics`
- `formulas/formula-best-practices`
- `formulas/formula-editor`
- `formulas/formula-errors`
- `formulas/functions`
- `formulas/helper-variables-and-modifiers`
- `getting-started/core-concepts-overview`
- `getting-started/glossary`
- `getting-started/how-oculon-is-organized`
- `getting-started/keyboard-shortcuts`
- `getting-started/oculon-glossary`
- `getting-started/what-is-oculon`
- `models/linked-models`
- `models/model-best-practices`
- `models/model-settings`
- `models/model-structure`
- `models/what-is-a-model`
- `scenarios/compare-scenarios`
- `scenarios/create-and-manage-scenarios`
- `scenarios/scenario-best-practices`
- `scenarios/scenario-overrides`
- `scenarios/scenario-sync-behavior`
- `scenarios/versioning-and-snapshots`
- `scenarios/what-is-a-scenario`
- `sharing-and-permissions/comments-and-collaboration`
- `sharing-and-permissions/external-sharing-and-exports`
- `sharing-and-permissions/members-guests-and-groups`
- `sharing-and-permissions/permission-inheritance`
- `sharing-and-permissions/roles-and-permissions`
- `sharing-and-permissions/sensitive-data-controls`
- `sharing-and-permissions/sharing-basics`
- `time/relative-time`
- `time/time-aggregation`
- `time/time-best-practices`
- `time/time-granularity`
- `time/time-in-oculon`
- `variables/create-and-edit-variables`
- `variables/variable-formatting`
- `variables/variable-types`
- `variables/what-is-a-variable`
- `views/compare-in-views`
- `views/filters-sorts-and-grouping`
- `views/view-best-practices`
- `views/what-is-a-view`
- `workspace-and-organization/profile-and-preferences`
- `workspace-and-organization/teamspaces-and-organization`
- `workspace-and-organization/what-is-a-workspace`
- `workspace-and-organization/workspace-access-and-visibility`
- `your-sidebar/navigate-the-sidebar`

</details>

### B. Topic overlap: Old docs (`oculon-basics`) vs Concepts (`docs-new`)

Hidden Old docs often collapses a whole topic into one page, while Concepts expands it into a section:

| Topic | Old docs page | Concepts section |
|---|---|---|
| Variables | `support-docs/oculon-basics/variable` | `docs-new/variables/*` |
| Dimensions | `support-docs/oculon-basics/dimensions` | `docs-new/dimensions/*` |
| Time | `support-docs/oculon-basics/time` | `docs-new/time/*` |
| Databases | `support-docs/oculon-basics/database` | `docs-new/databases/*` |
| Boards | `support-docs/oculon-basics/boards` | `docs-new/boards/*` |
| Views | `support-docs/oculon-basics/views` | `docs-new/views/*` |
| Compare | `support-docs/oculon-basics/compare` | `docs-new/compare/*` |
| Scenarios | `support-docs/plan-and-collaborate/scenario` | `docs-new/scenarios/*` |
| Formulas | `support-docs/oculon-basics/formulas/*` | `docs-new/formulas/*` |
| Getting started / glossary | `support-docs/getting-started/*` | `docs-new/getting-started/*` |
| Admin | `support-docs/admin/*` | `docs-new/admin-guide/*` |

### C. Near-duplicate naming inside `docs-new` orphans

| Orphan (not in nav) | Related nav page / gap |
|---|---|
| `docs-new/models/versioning.mdx` | Nav expects `docs-new/models/cloning-and-versioning` (missing) |
| `docs-new/time/last-actual-date.mdx` | Nav expects `docs-new/time/actuals-and-forecast-boundary` (missing); AGENTS.md prefers term “Last actual date” |
| `docs-new/time/time-rollups.mdx` | Related to time aggregation / rollups terminology |
| `docs-new/boards/board-interaction.mdx` | Nav uses `docs-new/boards/chart-interaction` instead |
| `docs-new/getting-started/welcome-to-oculon.mdx` etc. | Older getting-started set; nav uses what-is-oculon / glossary |
| `docs-new/views/creating-and-configuring-views.mdx` | Possibly intended for Views section expansion |
| `docs-new/views/sharing-views.mdx` | Overlaps sharing themes; nav missing private-vs-shared / view-behavior |

## 7. Orphaned pages (exist, not in navigation)

### `docs-new/` orphans (highest migration relevance)

- `docs-new/boards/board-interaction.mdx`
- `docs-new/databases/database-formulas.mdx`
- `docs-new/databases/filters-sorts-and-grouping.mdx`
- `docs-new/formulas/conditional-logic.mdx`
- `docs-new/getting-started/core-concepts.mdx`
- `docs-new/getting-started/index.mdx`
- `docs-new/getting-started/navigating-oculon.mdx`
- `docs-new/getting-started/oculon-glossary-backup.mdx`
- `docs-new/getting-started/oculon-glossary.mdx`
- `docs-new/getting-started/profile-setup.mdx`
- `docs-new/getting-started/welcome-to-oculon.mdx`
- `docs-new/models/versioning.mdx`
- `docs-new/scenarios/merge-scenarios.mdx`
- `docs-new/scenarios/scenario-governance-and-access.mdx`
- `docs-new/time/last-actual-date.mdx`
- `docs-new/time/time-rollups.mdx`
- `docs-new/views/creating-and-configuring-views.mdx`
- `docs-new/views/sharing-views.mdx`
- `docs-new/views/using-views-on-boards.mdx`

### `support-docs/` orphans

127 files under `support-docs/` are not in the Old docs nav. Many are the parallel copies of Concepts pages (see overlaps). Notable non-overlap leftovers:

Orphans with **no** `docs-new` twin (20):

- `support-docs/account/index.mdx`
- `support-docs/admin/groups.mdx`
- `support-docs/admin/index.mdx`
- `support-docs/admin/usage-and-limits.mdx`
- `support-docs/admin/workspace-settings.mdx`
- `support-docs/guides/index.mdx`
- `support-docs/index.mdx`
- `support-docs/models/cloning-and-versioning.mdx`
- `support-docs/models/model-organization.mdx`
- `support-docs/oculon-basics/formulas/index.mdx`
- `support-docs/oculon-basics/index.mdx`
- `support-docs/oculon-basics/library/index.mdx`
- `support-docs/oculon-basics/models.mdx`
- `support-docs/oculon-basics/navigation.mdx`
- `support-docs/plan-and-collaborate/index.mdx`
- `support-docs/plan-and-collaborate/scenario-old.mdx`
- `support-docs/time/actuals-and-forecast-boundary.mdx`
- `support-docs/to-be-categorised/helper-variables.mdx`
- `support-docs/views/private-vs-shared-views.mdx`
- `support-docs/views/view-behavior.mdx`

<details><summary>All support-docs orphans including twins (click)</summary>

- `support-docs/account/index.mdx`
- `support-docs/admin-guide/audit-logs.mdx`
- `support-docs/admin-guide/billing-and-plans.mdx`
- `support-docs/admin-guide/groups.mdx`
- `support-docs/admin-guide/login-methods.mdx`
- `support-docs/admin-guide/members-and-roles.mdx`
- `support-docs/admin-guide/security.mdx`
- `support-docs/admin-guide/usage-and-limits.mdx`
- `support-docs/admin-guide/workspace-settings.mdx`
- `support-docs/admin/groups.mdx`
- `support-docs/admin/index.mdx`
- `support-docs/admin/usage-and-limits.mdx`
- `support-docs/admin/workspace-settings.mdx`
- `support-docs/ai/ai-in-oculon.mdx`
- `support-docs/ai/connectors.mdx`
- `support-docs/ai/mcp.mdx`
- `support-docs/ai/modeling-with-ai.mdx`
- `support-docs/ai/plan-mode.mdx`
- `support-docs/ai/reporting-with-ai.mdx`
- `support-docs/ai/skills.mdx`
- `support-docs/boards/board-best-practices.mdx`
- `support-docs/boards/board-interaction.mdx`
- `support-docs/boards/board-layout.mdx`
- `support-docs/boards/charts.mdx`
- `support-docs/boards/kpi-and-summary-blocks.mdx`
- `support-docs/boards/sharing-boards.mdx`
- `support-docs/boards/tables-on-boards.mdx`
- `support-docs/boards/what-is-a-board.mdx`
- `support-docs/custom-agents/agent-actions.mdx`
- `support-docs/custom-agents/agent-best-practices.mdx`
- `support-docs/custom-agents/agent-connections.mdx`
- `support-docs/custom-agents/agent-context-and-knowledge.mdx`
- `support-docs/custom-agents/agent-permissions.mdx`
- `support-docs/custom-agents/agent-safety-and-review.mdx`
- `support-docs/custom-agents/create-a-custom-agent.mdx`
- `support-docs/custom-agents/what-are-custom-agents.mdx`
- `support-docs/databases/database-best-practices.mdx`
- `support-docs/databases/database-structure.mdx`
- `support-docs/databases/database-types.mdx`
- `support-docs/databases/linked-data.mdx`
- `support-docs/databases/refresh-and-sync-behavior.mdx`
- `support-docs/databases/what-is-a-database.mdx`
- `support-docs/databases/working-with-data.mdx`
- `support-docs/dimensions/dimension-best-practices.mdx`
- `support-docs/dimensions/dimension-operations.mdx`
- `support-docs/dimensions/dimension-values.mdx`
- `support-docs/dimensions/using-dimensions-with-variables.mdx`
- `support-docs/dimensions/what-is-a-dimension.mdx`
- `support-docs/formulas/common-formula-patterns.mdx`
- `support-docs/formulas/formula-basics.mdx`
- `support-docs/formulas/formula-best-practices.mdx`
- `support-docs/formulas/formula-editor.mdx`
- `support-docs/formulas/formula-errors.mdx`
- `support-docs/formulas/functions.mdx`
- `support-docs/formulas/helper-variables-and-modifiers.mdx`
- `support-docs/getting-started/core-concepts-overview.mdx`
- `support-docs/getting-started/glossary.mdx`
- `support-docs/getting-started/how-oculon-is-organized.mdx`
- `support-docs/getting-started/index.mdx`
- `support-docs/getting-started/keyboard-shortcuts.mdx`
- `support-docs/getting-started/oculon-glossary-backup.mdx`
- `support-docs/getting-started/what-is-oculon.mdx`
- `support-docs/guides/index.mdx`
- `support-docs/index.mdx`
- `support-docs/models/cloning-and-versioning.mdx`
- `support-docs/models/linked-models.mdx`
- `support-docs/models/model-best-practices.mdx`
- `support-docs/models/model-organization.mdx`
- `support-docs/models/model-settings.mdx`
- `support-docs/models/model-structure.mdx`
- `support-docs/models/what-is-a-model.mdx`
- `support-docs/oculon-basics/formulas/index.mdx`
- `support-docs/oculon-basics/index.mdx`
- `support-docs/oculon-basics/library/index.mdx`
- `support-docs/oculon-basics/models.mdx`
- `support-docs/oculon-basics/navigation.mdx`
- `support-docs/plan-and-collaborate/index.mdx`
- `support-docs/plan-and-collaborate/scenario-old.mdx`
- `support-docs/scenarios/compare-scenarios.mdx`
- `support-docs/scenarios/create-and-manage-scenarios.mdx`
- `support-docs/scenarios/scenario-best-practices.mdx`
- `support-docs/scenarios/scenario-overrides.mdx`
- `support-docs/scenarios/scenario-sync-behavior.mdx`
- `support-docs/scenarios/versioning-and-snapshots.mdx`
- `support-docs/scenarios/what-is-a-scenario.mdx`
- `support-docs/sharing-and-permissions/comments-and-collaboration.mdx`
- `support-docs/sharing-and-permissions/external-sharing-and-exports.mdx`
- `support-docs/sharing-and-permissions/members-guests-and-groups.mdx`
- `support-docs/sharing-and-permissions/permission-inheritance.mdx`
- `support-docs/sharing-and-permissions/roles-and-permissions.mdx`
- `support-docs/sharing-and-permissions/sensitive-data-controls.mdx`
- `support-docs/sharing-and-permissions/sharing-basics.mdx`
- `support-docs/time/actuals-and-forecast-boundary.mdx`
- `support-docs/time/relative-time.mdx`
- `support-docs/time/time-aggregation.mdx`
- `support-docs/time/time-best-practices.mdx`
- `support-docs/time/time-granularity.mdx`
- `support-docs/time/time-in-oculon.mdx`
- `support-docs/to-be-categorised/helper-variables.mdx`
- `support-docs/troubleshooting/agent-issues.mdx`
- `support-docs/troubleshooting/common-errors.mdx`
- `support-docs/troubleshooting/data-mismatches.mdx`
- `support-docs/troubleshooting/formula-issues.mdx`
- `support-docs/troubleshooting/performance-issues.mdx`
- `support-docs/troubleshooting/permissions-issues.mdx`
- `support-docs/troubleshooting/scenario-issues.mdx`
- `support-docs/variables/create-and-edit-variables.mdx`
- `support-docs/variables/variable-behavior.mdx`
- `support-docs/variables/variable-best-practices.mdx`
- `support-docs/variables/variable-formatting.mdx`
- `support-docs/variables/variable-references.mdx`
- `support-docs/variables/variable-types.mdx`
- `support-docs/variables/what-is-a-variable.mdx`
- `support-docs/views/compare-in-views.mdx`
- `support-docs/views/filters-sorts-and-grouping.mdx`
- `support-docs/views/private-vs-shared-views.mdx`
- `support-docs/views/view-behavior.mdx`
- `support-docs/views/view-best-practices.mdx`
- `support-docs/views/what-is-a-view.mdx`
- `support-docs/workspace-and-organization/profile-and-preferences.mdx`
- `support-docs/workspace-and-organization/teamspaces-and-organization.mdx`
- `support-docs/workspace-and-organization/what-is-a-workspace.mdx`
- `support-docs/workspace-and-organization/workspace-access-and-visibility.mdx`
- `support-docs/your-sidebar/navigate-the-sidebar.mdx`
- `support-docs/your-sidebar/organize-your-workspace.mdx`
- `support-docs/your-sidebar/search-and-quick-access.mdx`
- `support-docs/your-sidebar/sidebar-customization.mdx`

</details>

### Starter / unused folders

**ai-tools/**
- `ai-tools/claude-code.mdx`
- `ai-tools/cursor.mdx`
- `ai-tools/windsurf.mdx`

**api-reference/**
- `api-reference/endpoint/create.mdx`
- `api-reference/endpoint/delete.mdx`
- `api-reference/endpoint/get.mdx`
- `api-reference/endpoint/webhook.mdx`
- `api-reference/introduction.mdx`

**essentials / snippets / root templates**
- `essentials/code.mdx`
- `essentials/images.mdx`
- `essentials/markdown.mdx`
- `essentials/navigation.mdx`
- `essentials/reusable-snippets.mdx`
- `essentials/settings.mdx`
- `snippets/snippet-intro.mdx`
- `development.mdx`
- `quickstart.mdx`

## 8. Assets / images

- `108` files under `images/` (plus DS_Store noise).
- `68` navigated pages embed images; `90` unique image refs from nav pages.
- Concepts and Old docs share the `images/getting-started/` pool but mostly use different filenames (`fr-*` screenshots vs older PNGs).
- Several Concepts pages use `images/databases/*-placeholder.svg` and `images/scenarios/*-placeholder.svg` — migration should track placeholders vs real screenshots.
- Duplicate asset smell: `fr-switch-workspace copy.png`, `fr-spaces-icon copy.png`.

### Images tightly coupled to Concepts (sample of high-use dirs)

- `images/getting-started/fr-*.png` — primary Concepts UI screenshots
- `images/databases/*-placeholder.svg` — Databases section placeholders
- `images/scenarios/*-placeholder.svg` — Scenarios section placeholders

## 9. Risks for migration

1. **Repo/editor drift:** Concepts → Concepts Legacy rename + new Concepts tab exist in Mintlify unpublished state, not in git. Publishing editor-only nav without syncing `docs.json` will confuse branches/PRs.
2. **Five broken Concepts pages** already linked in nav (and redirects): actuals/forecast boundary, model cloning/versioning, model organization, private vs shared views, view behavior.
3. **Triple content layers:** Old docs (`oculon-basics`) + `support-docs` twins + `docs-new` live pages. Easy to edit the wrong copy.
4. **112 slug overlaps** mean URL/redirect strategy must be deliberate when retiring `support-docs` or renaming tabs.
5. **Orphan drafts in `docs-new`** (`last-actual-date`, `versioning`, view helpers, etc.) may be unfinished pages intended for the new Concepts tab — inventory before deleting.
6. **How-to / Integrations are stubs** (`index` only) — new Concepts IA may absorb or expand them.
7. **Starter folders** (`ai-tools`, `api-reference`, `essentials`) are dead weight for Oculon but harmless if left alone.
8. **Shared images:** deleting “old” screenshots can break the other tree; inventory refs before asset cleanup.
9. **Terminology:** AGENTS.md standardizes “Last actual date”; nav still points at missing `actuals-and-forecast-boundary` while orphan `last-actual-date.mdx` exists — naming conflict to resolve in new Concepts.
10. **Hidden Old docs still reachable by URL** unless redirects/noindex cover them; confirm whether URLs should stay for SEO during cutover.

## 10. Recommended next audit steps (no changes yet)

1. Decide whether git or Mintlify editor wins for the Concepts / Concepts Legacy rename, then sync.
2. For each of the 5 missing nav targets: promote twin from `support-docs`, rename orphan (`last-actual-date` / `versioning`), or remove from nav.
3. Classify `docs-new` orphans as keep-for-new-Concepts / merge / archive.
4. Diff the 70 divergent twin pairs if any content in `support-docs` is newer than `docs-new`.
5. Draft target IA for the empty new Concepts tab before moving files.

---

_End of inventory._
