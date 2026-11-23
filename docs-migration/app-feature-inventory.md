# App Feature Inventory

_Analysis only. Compares `docs-migration/target-concepts-structure.md` against the Oculon application at `/Users/vijay/Documents/oculon-app-client` (branch `Docs-repo`). App repo was read-only. No docs.json or MDX changes in this step._

**Sources consulted (examples):**
- Routes/nav: `app/(app)/**`, `components/Sidebar/helper.tsx`, `components/library/CreateEntityMenu.tsx`, `app/(app)/library/(list)/layout.tsx`
- Flags: `lib/featureFlags/registry.generated.ts`, `lib/featureFlags/registry.ts`
- Apps: `features/oculonApps/registry.ts`
- Internal specs: `docs/*.md` (engineering/QA — not customer Concepts)

---

## Summary

| Finding | Detail |
|---|---|
| App shape | Next.js App Router monolith (`app/`, `components/`, `features/`, `server/`, `modules/`) — not a docs monorepo |
| Primary product hub | **Library** (`/library`) with tabs All Files / Models / **Transactions** / Boards / Dimensions / Integrations |
| Modeling surface | **FP&A** app switcher entry → `/library/models`; model workspace `/model/[modelId]` |
| Terminology clash | Resource type `database` is labeled **Transactions** in Library create/list UI |
| Flagged surfaces | Projects, Templates, Feed, Artifacts (3 types), Publishing, Exports — on in local/sandbox defaults; off in development/staging/production defaults |
| Always-off by default | **Agent Teams** (`agent-teams-enabled`) false in every environment |
| Plans ambiguity | Three different “plan” concepts: Admin **Planning** settings, AI chat **Plan mode**, no separate Plans product IA |
| History | Implemented as Model History, Project Activity, Artifact History — no single product “History” module |
| Target IA vs app | Target mostly covers core modeling + AI parents; under-documents Library hub, Integrations, Templates, Inbox, Command palette, Onboarding; Apps/Artifacts/Feed/Projects largely `new` / flag-gated |
| Confidence overall | **High** for routes/labels/flags; **medium** for permissions depth and Apps domain completeness; **low** for production flag overrides (PostHog) |

---

## Feature Inventory

Status columns below refer to **implementation in the app**, not docs coverage.

Legend for **Confidence**: high / medium / low.

### Data and structure / Modeling

| Feature | User-facing terms | App source paths | Internal app docs | Main flows | Important actions | Settings / config | States / statuses | Permissions / roles | Edge cases | Feature flags | Target Concepts page(s) | IA vs implementation | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Models | Models, Create Model, Model settings, History, Comments, Pages; App switcher **FP&A** | `app/(app)/library/(list)/models`, `app/(app)/model/**`, `features/model-grid/**`, `server/model/**` | `docs/FORMULA_ARCHITECTURE.md`, `docs/PLUGIN_*`, scenario-cache docs | Open model grid; edit cells/formulas; switch scenarios; share | Create, rename, share, history checkpoints, tags, link DBs/dimensions | Per-model settings; Admin **Planning** (horizon, granularity, fiscal year, default scenario names) | Locked scenarios, compare mode, last-actual boundary styling | Workspace + share roles on resource | Last actual date drives actual vs planned formula side (`last_actual_date` / `last-actual-boundary`) | `NEXT_PUBLIC_MODEL_TIME_GRANULARITY_ENABLED` | Modeling → Models (+ children) | Target omits cloning/versioning & model-organization that Concepts Legacy still links | high |
| Variables | Variable, actual/planned formulas, formatting, breakdown | In-model panels; `/variables/[variableId]`; `features/variables/**`, `server/variables` | Formula architecture docs | Create/edit variable; attach dimensions; set aggregation/format | Create, rename, override, revert | Format, aggregation, dimension links | Actual vs planned regions relative to last actual | Inherit model/share permissions | Actual/planned split is time-boundary aware | `NEXT_PUBLIC_DIMENSION_VARIABLES_ENABLED` | Data and structure → Variables | Aligns well; currency/conversion only partially surfaced in settings | high |
| Dimensions | Dimensions, Create Dimension | `/library/dimensions`, `/library/dimensions/[id]`, `features/coreV2`, `features/dimensionPages`, `server/dimensions`, `server/coreV2Dimensions` | — | Manage members/values; properties; linked views/models | Create, edit values, map relations | Dimension settings / properties | Dependent models when deleting views | Resource share | Dual “coreV2” / legacy dimension paths | — | Data and structure → Dimensions | Target title “Create and edit dimensions” vs slug `create-and-edit-dimension` | high |
| Time | Time columns, rollups, fiscal year, granularity Monthly/Quarterly/Annual | Model grid hooks (`useColDefs`, date helpers); Admin Planning drawer | `docs/FISCAL_ROLLUP_REFERENCE_QA_2026-11-03.md` | Navigate periods; roll up; compare by time | Change horizon/granularity; set last actual | Planning defaults; model time params | Actuals vs forecast boundary | Admin for workspace planning defaults | Docs AGENTS.md prefers “Last actual date”; target Time children omit that page | `NEXT_PUBLIC_MODEL_TIME_GRANULARITY_ENABLED` | Data and structure → Time | Target missing last-actual / rollups pages that exist as orphans in docs repo | high |
| Formulas | Formula editor, actual/planned formulas, functions, helpers | `app/(app)/model/components/formula/**`, `server/formulas` | `docs/FORMULA_ARCHITECTURE.md`, `TASK_MIGRATE_MODEL_FORMULA_UPDATES_TO_FORMULAS_API.md` | Edit formulas; handle errors; overrides | Edit, revert, compare refresh | — | Formula errors / overrides | Model edit permission | Formula pipeline still migrating APIs per internal task doc | — | Modeling → Formulas | Good match | high |
| Databases / Transactions | **Transactions** (Library tab & Create menu); routes still `/library/databases`, `/databases/[id]` | `app/(app)/library/(list)` layout label Transactions; `CreateEntityMenu`; `server/databases` | — | Create/open transactions grid; comments; embed on boards | Create Transactions, edit rows, share | Sync/refresh behaviors in product | Connection/sync states (integration-driven) | Resource share | Strong terminology mismatch with docs “Databases” | — | Data and structure → Databases | Target parent “Databases”; product says Transactions | high |
| Scenarios | Scenario picker, Compare scenarios, Merge, lock, duplicate | `ScenarioPicker`, merge modal, `server/scenario/**` | `docs/SCENARIO_AWARE_CACHE_*` | Add/switch/lock/merge; compare variance | Create, lock, merge, duplicate | Default scenario names in Planning | Locked vs editable | Model permissions | Scenario-aware cache complexity | — | Modeling → Scenarios | Aligns; compare-scenarios overlaps Analysis Compare | high |

### Analysis and reporting

| Feature | User-facing terms | App source paths | Internal app docs | Main flows | Important actions | Settings / config | States / statuses | Permissions / roles | Edge cases | Feature flags | Target Concepts page(s) | IA vs implementation | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Views | Model view tabs; Library Recents/Favorites/Shared; dimension views | `components/ViewsBar/**`, model views bar, dimension views | — | Save/switch filters & sorts; copy link | Create/reorder/delete views | ViewSpec axes (measure/scenario/dimension) | Active view | Share/copy link | Target omits private-vs-shared / view-behavior still in Legacy nav | — | Analysis → Views | Partial vs Legacy missing pages | high |
| Compare | Compare (scenarios or time), variance columns | Model compare UI, `ComparisonScenarioPicker`, compare hooks | `docs/COMPARE_QA_2026-11-03.md` | Enter compare; pick scenarios or time | Toggle variance/%/value | — | Compare layout active | Edit/view | Overlaps scenario “Compare scenarios” page | — | Analysis → Compare | Good; clarify vs scenario subpage | high |
| Boards | Boards, Create Board; slash embeds (chart, model, dimension, transactions, code) | `/library/boards`, `/boards/[boardId]`, board block components | `docs/BOARD_COLLABORATION_*.md`, `ARTIFACTS_AND_CODE_BLOCKS.md` | Compose board; collab; share/publish/export | Create blocks, comment, share | Collab websocket env | Collab connected | Share roles | Charts page docs only subset of chart types; pivot/model/dimension/transactions/code blocks are newer | `NEXT_PUBLIC_BOARD_COLLAB`; code block → artifacts flags | Analysis → Boards (+ many children) | Target board children match gaps well (pivot, embeds, chart catalog) | high |

### Projects and work

| Feature | User-facing terms | App source paths | Internal app docs | Main flows | Important actions | Settings / config | States / statuses | Permissions / roles | Edge cases | Feature flags | Target Concepts page(s) | IA vs implementation | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Projects | Projects | `/projects`, `/projects/[id]`, `server/projects` | `docs/PROJECTS_*.md` | Create project; overview; files; agents; activity | Duplicate, archive, settings | `/projects/settings`, task types | Archived | Workspace + project access | Also gated by `NEXT_PUBLIC_PROJECTS_ENABLED` | `projects-enabled` (local/sandbox on; prod default off) | Workspace → Projects and tasks | Grouped under Workspace in target — OK; product is primary nav | high |
| Tasks | Tasks, All Tasks / My Tasks, assign, delegate to agents | `/tasks/[taskId]`, project task dialogs, `server/projectTasks` | `PROJECTS_TASKS_QA_2026-11-03.md` | Create/assign/move/bulk edit | Assign, change type, delegate | Task types settings | Task status types (configurable) | Project permissions | Nested under Projects flag | same as projects | Projects children (Tasks, …) | Aligns | high |
| Plans (AI) | Plan mode / plan editor in chat | `components/plan/**`, AI chat session export | AI chat docs | Generate/edit plan tasks from chat | Export plan | — | Plan draft vs applied (product detail TBD) | Chat permissions | **Not** Admin Planning; **not** Projects | — | AI → Plan mode | Target has no “Plans” parent — only Plan mode | medium |
| Planning (Admin) | Settings › Planning | Admin Planning drawer in `modules/profilemenu` | — | Set fiscal defaults | Save planning defaults | Currency, FX aggregation, period, forecast frequency, FY start, default scenarios | — | Admin | Naming collision with Plans/Plan mode | — | Settings → Planning defaults | Exists; only support-docs currency page today | high |

### AI and agents

| Feature | User-facing terms | App source paths | Internal app docs | Main flows | Important actions | Settings / config | States / statuses | Permissions / roles | Edge cases | Feature flags | Target Concepts page(s) | IA vs implementation | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AI overview | Chat entry points; Docs “AI in Oculon” | `components/AIChat/**`, `/chat` | `docs/AI_CHAT_*.md` | Start chat; mention resources | New chat | — | — | — | Multiple parents currently map to one docs page | — | AI overview | Needs dedicated overview vs shared landing | medium |
| Workspace AI | Settings › Admin › **Workspace AI** (Defaults, Agents, Approvals, Tools & Connectors; Lite/Pro/Max) | `SettingsWorkspaceAiDrawer.tsx` | — | Configure workspace AI policy | Set defaults/approvals/tools | Workspace AI drawers | Plan tiers Lite/Pro/Max | Admin | No dedicated docs-new page | — | Workspace AI | Target Partial — correct | high |
| AI Assistant | Chat, New chat, floating assistant, skills dropdown | `/chat`, `components/AIChat/**`, `server/chats` | AI chat implementation docs | Modeling/reporting chat; plan mode | Mentions, skills, export plan | Personal AI settings | — | User | — | — | AI assistant + Modeling/Reporting with AI + Plan mode | Good | high |
| Custom Agents | Custom agents routes; settings entry **commented out** in nav | `/custom-agents`, `/template/agents`, `components/CustomAgent` | `CUSTOM_AGENTS_FEEDS_*`, agent review docs | Create agent; configure context/actions/permissions/connections | Create, review, safety | Drawer exists but nav hidden | Safety/review states | Agent permissions model | Distinct from Agent Teams | — | Custom agents (+ children) | Implementation present; discoverability reduced | high |
| Context and Connections | **Connectors & MCP**; Library **Integrations** | `SettingsConnectorsDrawer`, `/library/integrations`, `/authorize/mcp` | — | Connect MCP/tools; manage integrations | Authorize MCP, create integration | `NEXT_PUBLIC_MCP_*` | Connection status | Admin/user | Integrations (Library) vs Connectors (Settings) may need IA split | — | Context and connections + MCP; Integrations not in Concepts target as Library hub | medium |
| Skills | Settings › My Account › Skills | `SettingsSkillsDrawer`, `components/AIChat/skills` | — | Browse All / My Skills | Enable/use skill in chat | Skills drawers | — | User | Notion note questioned Concepts placement | — | Skills | Present; placement debate | high |
| Knowledge and Memory | Personal memories; agent knowledge/memory; project memories | `SettingsAiDrawer`, `server/memory`, AgentTeams knowledge, project memories modal | — | Add/manage memories | CRUD memory | AI settings | — | User/admin | Fragmented across personal/agent/project | — | Knowledge and memory | Implemented but scattered — target parent is right | medium |
| Feed | Feed | `/feeds`, `components/Feed/**`, `server/feeds` | Custom agents/feeds readiness doc | Browse feed | — | — | — | — | Prod default off | `feeds-enabled` | Feed | Target new — correct | high |
| Agent Teams | Team sidebar tab → `/team` | `/team`, `/team/[agentId]`, `components/AgentTeams/**` | Agent timeline/load docs | Manage agent teams | — | — | — | — | Flag **false in all envs** by default | `agent-teams-enabled` | Agent teams | Target new; experimental | high |
| Artifacts | Artifacts; Create Spreadsheet/Presentation/Artifact; board Code block | `/artifacts`, `app/(app)/artifacts/**`, `server/artifacts` | `docs/ARTIFACTS_AND_CODE_BLOCKS.md` | Create/open artifacts; embed code on boards | Create types, history | Type flags + `NEXT_PUBLIC_ARTIFACTS_ENABLED` creation ceiling | — | Share | Three type flags + build ceiling | code/spreadsheet/presentation-artifacts-enabled | Artifacts (+ children) | Target new — correct; flag-heavy | high |

### Workspace and collaboration

| Feature | User-facing terms | App source paths | Internal app docs | Main flows | Important actions | Settings / config | States / statuses | Permissions / roles | Edge cases | Feature flags | Target Concepts page(s) | IA vs implementation | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Workspaces | Workspaces, invite, request access | `/workspaces`, onboarding | — | Create/switch workspace | Invite, request access | — | Pending invites | Owner/Member/Guest | — | — | Workspaces | Good | high |
| Spaces / Teamspaces / Private | Spaces, Favourites, Teamspace | Sidebar Spaces; `components/teamspaces*`; `server/spaces`, `server/teamspaces` | `docs/SPACE_ICONS.md` | Create space; organize library | Set space defaults | Admin Teamspace | Private vs shared spaces | Teamspace Admin/Member; space share defaults | Templates inside spaces follow templates flag | templates (indirect) | Teamspaces and private space | Good | high |
| Sharing | Share dialog; Viewer / Editor / Full Access / No Access; Publish; Export | `components/ShareResource/**`, `server/shareresources`, `server/publications` | — | Share resource; publish link; export | Add people/groups, change role | Publish/Export tabs | Publication tokens `/p/[token]` | Resource ACL + workspace roles | Publish vs Export separate flags; shared docs page today | publishing-enabled, exports-enabled | Sharing and permissions (+ Publishing, Exports, Comments) | Target under-lists roles/inheritance/sensitive-data pages that exist in docs-new | high |
| Comments | Comments on model/board/DB/dimensions | `components/comments/**`, `server/*Comments` | — | Thread comments | Resolve/reply | — | — | Resource access | Live board collab beyond comments is separate | board collab env | Comments and collaboration | Good | high |
| History / Activity | Model **History**; Project **Activity**; Artifact History | model history components; `ProjectActivityFeed`; artifact history | — | Preview checkpoints; browse activity | Restore/preview (model) | — | Checkpoint states | Edit permissions for restore | **No unified History parent** in target | — | Closest: Project activity | Target gap for model history | high |
| Notifications | Inbox; Settings › Notifications | `components/Inbox/**`, `SettingsNotificationsDrawer`, `server/notifications` | — | Read inbox; configure notifications | — | Notifications settings | Unread | User | Target only has Notifications under Personal settings; Inbox chrome undocumented | — | Personal settings → Notifications | Partial | medium |
| Templates | Templates | `/template`, `/template/agents` | — | Browse/create templates | — | — | Drafts | — | Sidebar gated | `templates-enabled` | Templates | In target Workspace — good | high |

### Settings and administration

| Feature | User-facing terms | App source paths | Internal app docs | Main flows | Important actions | Settings / config | States / statuses | Permissions / roles | Edge cases | Feature flags | Target Concepts page(s) | IA vs implementation | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| My Account | My Account: Profile, Preferences, Security, Notifications, AI, Skills, Connectors & MCP | `modules/profilemenu` drawers; `/settings/profile` | — | Edit profile/prefs | — | Personal drawers | — | Self | Target “Personal settings” ≈ My Account | — | Personal settings | Renamed in target vs product | high |
| Workspace settings | Admin › General; Teamspace | General drawer; `/settings/teamspace` | — | Rename/workspace prefs | — | General | — | Admin/Owner | — | — | Workspace settings | Good | high |
| Users / Groups | Users & Groups | `/settings/users`, members/groups UI | — | Invite, roles, groups | Invite, change role | — | Guest vs member | Owner/Member/Guest; group membership | Target splits Users vs Roles parents | — | Users… + Roles and access | Slight split vs single settings label | high |
| Security | Security (account); Security and Access (admin) | Security drawers | — | Login methods, audit | — | SAML/SCIM noted older docs only | — | Admin | — | — | Security + Login methods + Audit logs | Good | high |
| Billing and Usage | Plan and Billing; Usage | `/settings/billing`, billing/usage drawers | Stripe public env | Manage plan; view usage | — | Stripe | Plan tiers | Admin | — | Stripe `NEXT_PUBLIC_STRIPE_*` | Billing and usage + Usage and limits | Good | high |
| AI settings | My Account › AI; Admin › Workspace AI | AI drawers | — | Personal memories vs workspace policy | — | Dual surfaces | — | User vs Admin | Target separates Workspace AI (AI group) vs Personal AI under settings | — | Workspace AI + Personal/Knowledge | Placement split intentional? | medium |
| Feature flags (internal) | Feature flags page | `/settings/feature-flags` | PostHog docs | Toggle/debug flags | — | — | — | Internal | Not for Concepts customers | remote flags | — | Missing from target (OK if internal-only) | high |

### Apps

| Feature | User-facing terms | App source paths | Internal app docs | Main flows | Important actions | Settings / config | States / statuses | Permissions / roles | Edge cases | Feature flags | Target Concepts page(s) | IA vs implementation | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| App switcher apps | FP&A, Oculon Revenue/Close/Cash/Spend/Tax/Performance/Commission, FinOps, Capital (+ v2) | `features/oculonApps/registry.ts`, `/apps/[appId]/[[...path]]`, `AppsFrame`, v2 pages | `docs/OCULON_APPS_EXPANSION.md` | Switch app; navigate app nav | — | Per-app navigation inventory | Legacy iframe vs v2 native mix | Workspace | Domain depth uneven; FP&A is Models/Library not `/apps/fpa` | none for switcher entries | Apps group | Target lists apps as new parents — accurate; FP&A should map to Models not Apps | medium |

### Resources (target group)

| Feature | User-facing terms | App source paths | Notes vs target | Confidence |
|---|---|---|---|---|
| Keyboard shortcuts | Command palette ⌘K; shortcuts help | Command palette components | Target Resources → Keyboard shortcuts — app has palette + shortcuts | high |
| Sidebar and search | Sidebar, Spaces, Favourites, search | `components/Sidebar/**` | Target Resources; also How-to debate in Notion notes | high |
| Troubleshooting | — | — | Mostly docs-side; not a product module | medium |

---

## Target IA conflicts

### Renamed / terminology mismatches

| Target term | Product term | Notes |
|---|---|---|
| Databases | **Transactions** | Library tab + Create menu; routes still `databases` |
| Personal settings | **My Account** | Product settings section label |
| Users, guests and invitations / Roles and access | **Users & Groups** | Single settings entry |
| Billing and usage | **Plan and Billing** + **Usage** | Two admin items |
| Teamspaces and private space | **Spaces** / **Teamspace** / private space | Sidebar “Spaces” |
| Create and edit dimensions | Create Dimension | Slug singular in docs-new |
| Context and connections | **Connectors & MCP** (+ Library Integrations) | Two surfaces |
| Plan mode / Plans | Plan mode (chat) vs **Planning** (admin) | Collision risk |
| FP&A | App switcher label for models/library | Not an Apps `/apps/...` shell |

### Wrong grouping / placement debates

- **Sidebar and search** under Resources in target; product is global chrome (also candidate for How-to).
- **Skills** in AI group; product lives under My Account (and chat).
- **Workspace AI** in AI group; product under Admin settings.
- **Projects** under Workspace in target; product is primary sidebar nav (peer to Library).
- **Integrations** are first-class in Library but not a Concepts parent (only MCP under AI).

### Missing from target relative to implementation

- Model **History** (checkpoints) as its own Concepts topic
- Library hub (All Files / Recents / Favorites / Shared)
- **Inbox**
- **Command palette**
- **Onboarding** / workspace invite-request flows
- **Tags** on models/boards
- Internal `/settings/feature-flags` (likely exclude from customer Concepts)
- Clear **Last actual date** Concepts page (implemented; docs orphans exist; not in Notion target Time children)

### Obsolete or weak target items

- **Agent Teams**: implemented but flag defaults **off everywhere** — document as experimental or defer
- **Apps** suite parents: shells exist; many domain pages still legacy/iframe — risk of over-promising Concepts coverage
- Blank/deleted Notion Projects sub-item should not become a page

### Target pages with weak/no current implementation signal

| Target page | App signal |
|---|---|
| How data flows through Oculon | Conceptual only — no dedicated UI |
| Knowledge and memory (as one product) | Fragmented features, not one module |
| Chart types catalog / Pivot / embed blocks | Implemented on boards; docs lag |
| Oculon * app parents | Switcher entries exist; content depth varies |
| Agent teams | Code present; effectively experimental |

---

## Product coverage missing from target IA

Implemented (or clearly shipped/gated) product areas under-represented or absent as Concepts parents:

1. **Library** as the file hub (not only per-entity parents)
2. **Integrations** (Library) as distinct from Connectors & MCP
3. **Inbox / notification center** (beyond Settings › Notifications)
4. **Command palette / quick actions**
5. **Model History** (version/checkpoint UX)
6. **Onboarding** and workspace join/request flows
7. **Tags**
8. **Board collaboration** (realtime) as distinct from Comments
9. **FP&A** naming in app switcher (map explicitly to Models)
10. **Analytics** settings route (if customer-facing)
11. **Sprints** within Projects (if still shipped — confirm before IA)
12. Disambiguation page for **Planning vs Plan mode vs Projects**

Flag-gated but real: Templates, Feed, Artifacts, Publishing, Exports, Projects — present in target as mostly `new`/`partial`, which is appropriate if Concepts will cover upcoming GA.

---

## Needs review

Cannot be reliably confirmed from the app repo alone (or needs product decision):

1. **Production flag truth** — defaults say off for many flags; PostHog/`NEXT_PUBLIC_FEATURE_FLAGS_ENVIRONMENT` can override.
2. **Full permissions matrix** — Viewer/Editor/Full Access and Owner/Member/Guest are visible; capability-by-resource map not exhaustively traced.
3. **Apps domain completeness** — which Close/Cash/… pages are native vs legacy runtime.
4. **Custom Agents GA posture** — routes exist; settings nav entry commented out.
5. **Whether Agent Teams should appear in customer Concepts** while default-off.
6. **Last actual date** canonical docs title/placement (AGENTS.md vs missing Notion Time child).
7. **Sprints** and other Projects subfeatures still in IA scope.
8. **Guest** experience differences vs Member.
9. **Plan mode** user-facing name vs internal “Plans” components.
10. **Sensitive data controls / permission inheritance** — docs-new pages exist; confirm still accurate vs ShareResource implementation.

---

## Flag matrix (quick reference)

| Flag | Alias | local/sandbox default | development/staging/production default | Also gated by |
|---|---|---|---|---|
| projects-enabled | projects | true | false | `NEXT_PUBLIC_PROJECTS_ENABLED` |
| feeds-enabled | feeds | true | false | — |
| templates-enabled | templates | true | false | — |
| publishing-enabled | publishing | true | false | `NEXT_PUBLIC_PUBLISHING_ENABLED===true` |
| exports-enabled | exports | true | false | — |
| code-artifacts-enabled | codeArtifacts | true | false | `NEXT_PUBLIC_ARTIFACTS_ENABLED===1` for creation |
| spreadsheet-artifacts-enabled | spreadsheetArtifacts | true | false | same |
| presentation-artifacts-enabled | presentationArtifacts | true | false | same |
| agent-teams-enabled | agentTeams | **false** | **false** | — |

Source: `lib/featureFlags/registry.generated.ts`.

---

## Suggested next analysis steps (not done here)

1. Resolve Databases vs Transactions naming for Concepts.
2. Decide flag-gated features: document now with “availability” callouts vs park until GA.
3. Add/adjust target parents for Library, Integrations, Model History, Inbox (or explicitly defer).
4. Map each target row → migrate / rewrite / new / defer before scaffolding `concepts/**`.

_End of app feature inventory._
