# Concepts coverage sweep (pre-cutover)

_Planning only. No MDX, `docs.json`, Legacy, support-docs, or app changes in this step._  
_Date: 2026-11-23._

## Method

Compared:

1. `docs-migration/target-concepts-structure.md` (~147 planned pages)
2. `docs-migration/concepts-migration-map.md` (147 mapped rows)
3. `docs-migration/app-feature-inventory.md`
4. Completed module reports under `docs-migration/migration-*-report.md`
5. Current Concepts MDX + Concepts tab nav (**113** content pages + `concepts/index`; nav/disk aligned)
6. Strong Legacy `docs-new/**` pages still relied on via temporary links or not represented in Concepts

Completed migration batches in scope: Dimensions, Variables, Time, Formulas, Models (+ Model History), Scenarios (partial), Transactions, Views, Compare, Boards, Workspace/collaboration, AI/agents, Projects/Tasks/Activity.

---

## Snapshot

| Metric | Count / note |
|---|---|
| Target IA pages (planned) | ~147 |
| Concepts content pages published | **113** (+ index) |
| Map rows not yet on disk | **34** |
| Of those 34 clearly HOLD / park / REVIEW-held | ~18 (Apps 10, Artifacts 5, Agent teams, Templates, Plan mode, Skills) |
| Remaining mapped GA/admin/resources work | ~16 |
| Strong Legacy orphans outside target IA | ~15+ (listed below) |
| New Concepts validation / broken-link errors | **0** (pre-existing Legacy noise only) |

---

## Master remaining-items table

Classify each item as **exactly one** recommended action.

| Item | Current source | Current status | Recommended action | Target location | Blocking cutover? | Reason |
|---|---|---|---|---|---|---|
| Core concepts overview | `docs-new/getting-started/core-concepts-overview` | Target mapped; not migrated | ADD TO CONCEPTS | `concepts/core-concepts/core-concepts-overview` | **Yes** | Entry conceptual frame; Legacy would disappear at cutover |
| Glossary | `docs-new/getting-started/glossary` | Target mapped; not migrated | ADD TO CONCEPTS | `concepts/core-concepts/glossary` | **Yes** | Canonical terms (Transactions alias, etc.) needed for cutover |
| How data flows through Oculon | — (new) | Target CREATE; not migrated | ADD TO CONCEPTS | `concepts/core-concepts/how-data-flows-through-oculon` | No | Useful; can ship shortly after overview/glossary |
| What is Oculon / How Oculon is organized | `docs-new/getting-started/what-is-oculon`, `how-oculon-is-organized` | In Legacy; not in Notion Concepts list | REVIEW | Core concepts **or** Getting started / How-to | **Yes** (decide) | Must choose keep-in-Legacy-until-elsewhere vs Concepts home before hiding Legacy Start here |
| Scenario governance and access | `docs-new/scenarios/scenario-governance-and-access` | Mapped MOVE; temporary Legacy links only | ADD TO CONCEPTS | `concepts/modeling/scenarios/scenario-governance-and-access` | **Yes** | Mapped, strong Legacy, Allow Changes / Allow Merging already referenced |
| Merge scenarios | `docs-new/scenarios/merge-scenarios` | Mapped MOVE; temporary Legacy links only | ADD TO CONCEPTS | `concepts/modeling/scenarios/merge-scenarios` | **Yes** | Mapped; Merge Changes is product-visible |
| Compare scenarios (Legacy) | `docs-new/scenarios/compare-scenarios` | REVIEW vs Analysis Compare; no Concepts Scenarios page | ARCHIVE | Redirect → `concepts/analysis-and-reporting/compare/scenario-compare` | No | Deduped by IA decision; redirect at cutover |
| Last actual date | `docs-new/time/last-actual-date` (+ AGENTS.md) | Strong orphan; not in target children; Legacy-linked | ADD TO CONCEPTS | `concepts/data-and-structure/time/last-actual-date` | **Yes** | Canonical product term; Time module incomplete without it |
| Time rollups | `docs-new/time/time-rollups` | Strong orphan; distinction from aggregation documented | ADD TO CONCEPTS **or** MERGE INTO EXISTING PAGE | Time child **or** fold into `time-aggregation` | No | Important but aggregation page already distinguishes; promote or merge |
| Broken Legacy nav: actuals-and-forecast-boundary | Missing file; still in Legacy nav | Pre-existing Mintlify orphan | ARCHIVE | Redirect → Last actual date (once Concepts exists) | No | Fix at cutover redirects |
| Conditional logic | `docs-new/formulas/conditional-logic` | Strong orphan; not in target | ADD TO CONCEPTS | `concepts/modeling/formulas/conditional-logic` | **Yes** | Widely linked; Formulas incomplete without it or an explicit How-to home |
| Creating and configuring views | `docs-new/views/creating-and-configuring-views` | Strong orphan; temporary Legacy links | ADD TO CONCEPTS **or** MERGE INTO EXISTING PAGE | Views child **or** merge into `what-is-a-view` | **Yes** | Substantial setup guidance missing from Concepts Views |
| Sharing views | `docs-new/views/sharing-views` | Strong orphan; temporary Legacy links | ADD TO CONCEPTS | `concepts/analysis-and-reporting/views/sharing-views` | **Yes** | Non-trivial; private-views unsupported note lives here |
| Using views on boards | `docs-new/views/using-views-on-boards` | Strong orphan; temporary Legacy links | MERGE INTO EXISTING PAGE | Boards tables/layout **or** Views child | No | Cross-module; merge preferred to avoid duplication |
| Private vs shared views | `support-docs/views/private-vs-shared-views` (broken Legacy nav) | Conflicts with “private views not supported” | ARCHIVE | Do not promote | No | Contradicts current product/docs-new |
| View behavior | `support-docs/views/view-behavior` (broken Legacy nav) | Partial fold into What is a view | MERGE INTO EXISTING PAGE | Already partially merged; finish + archive twin | No | |
| Database formulas | `docs-new/databases/database-formulas` | Transactions IA gap; Legacy-linked | ADD TO CONCEPTS **or** MERGE INTO EXISTING PAGE | Transactions child **or** `working-with-data` | **Yes** | Strong Legacy; Transactions incomplete |
| Filters/sorts/grouping (databases) | `docs-new/databases/filters-sorts-and-grouping` | Transactions IA gap; distinct from Views filters | ADD TO CONCEPTS **or** MERGE INTO EXISTING PAGE | Transactions child **or** `working-with-data` | **Yes** | Distinct surface from Views filters page |
| Workspace access and visibility | `docs-new/workspace-and-organization/workspace-access-and-visibility` | Spaces report IA gap | ADD TO CONCEPTS **or** MERGE INTO EXISTING PAGE | Workspaces child **or** merge into Workspaces | **Yes** | Access/visibility concepts not fully on Concepts Workspaces |
| Roles and permissions (sharing) | `docs-new/sharing-and-permissions/roles-and-permissions` | Omitted from target children; Legacy-linked | ADD TO CONCEPTS **or** MERGE INTO EXISTING PAGE | Sharing child **or** Settings Roles | **Yes** | Depth beyond Sharing landing |
| Permission inheritance | `docs-new/sharing-and-permissions/permission-inheritance` | Omitted; Legacy-linked | ADD TO CONCEPTS | Sharing child | **Yes** | Inheritance rules not in Concepts |
| Members, guests and groups | `docs-new/sharing-and-permissions/members-guests-and-groups` | Overlaps Users/Roles Concepts | MERGE INTO EXISTING PAGE | Users + Roles Concepts pages | No | Partial coverage already; finish merge then archive Legacy |
| Sensitive data controls | `docs-new/sharing-and-permissions/sensitive-data-controls` | Omitted; Legacy-linked | ADD TO CONCEPTS **or** MOVE TO SETTINGS / ADMIN | Sharing **or** Security | No | Important; can follow Security batch |
| Model versioning (Legacy) | `docs-new/models/versioning` | Folded into Model History; Legacy still live | ARCHIVE | Redirect → `concepts/modeling/models/model-history` | No | Content migrated; cutover redirect |
| Model cloning / organization | Broken Legacy nav + thin support pages | HOLD / no Concepts page (IA decision) | HOLD / UNRELEASED **then** ARCHIVE | Out of Models; Library Copy to later | No | Do not publish Clone |
| Scenario sync “auto-sync toggle” | Legacy wording vs app | Replaced on Concepts sync page | ARCHIVE | Keep Concepts wording; archive Legacy at cutover | No | Already handled in Concepts |
| Skills | `docs-new/ai/skills`; Settings Skills drawer | REVIEW; not published | REVIEW | Concepts AI **or** Settings / How-to | No | Placement unresolved; Legacy retains until decided |
| Plan mode | `docs-new/ai/plan-mode` | REVIEW; not published | REVIEW | AI assistant child **after** naming | No | Plans vs Planning vs Projects collision |
| Agent teams | App `/team`; flag off all envs | HOLD; not published | HOLD / UNRELEASED | — | No | Default-off everywhere |
| Plans / tags (Projects) | Custom view name / no tag object | REVIEW; decision report filed | REVIEW | Do not invent Projects Plans/tags pages | No | Not distinct product objects |
| Feed production availability | Concepts Feed page with note | Published; env-gated | HOLD / UNRELEASED | Keep availability note until prod default-on | No | Already published carefully |
| Projects production availability | Concepts Projects tree with note | Published; env-gated | HOLD / UNRELEASED | Keep availability note until prod default-on | No | Already published carefully |
| Publishing / Exports | Concepts pages with availability notes | Migrated; flag-gated | HOLD / UNRELEASED | Keep notes until GA | No | Content exists; posture not GA |
| Board code block | Concepts page with artifacts gating | Migrated; availability-noted | HOLD / UNRELEASED | Keep note | No | |
| Templates | Target CREATE; not migrated | Flag-gated; no docs-new | HOLD / UNRELEASED | `concepts/workspace-and-collaboration/templates` when product asks | No | Same class as pre-Feed; not required for Legacy cutover of GA modeling |
| Artifacts section (5 pages) | App `/artifacts`; flags | Target CREATE; not migrated | HOLD / UNRELEASED | `concepts/artifacts/**` post-GA | No | Flag-gated; board code-block already bridges lightly |
| Artifact History | App only | No Concepts page | HOLD / UNRELEASED | With Artifacts module | No | Stays separate from Model History / Project Activity |
| Apps suite (9+ pages) | App switcher shells | Target CREATE; uneven depth | HOLD / UNRELEASED | `concepts/apps/**` later or park | No | Over-promise risk; migration rules Hold list |
| Apps v2 shells | Thin shells | Low confidence | HOLD / UNRELEASED | Under Revenue or park | No | |
| Workspace settings | `docs-new/admin-guide/workspace-settings` | **Batch D migrated** | MOVE TO SETTINGS / ADMIN | `concepts/settings-and-administration/workspace-settings` | No | Legacy mirror until redirects |
| Planning defaults | support-docs currency partial; Admin Planning | **Batch D CREATE** | MOVE TO SETTINGS / ADMIN | `concepts/settings-and-administration/workspace-settings/planning-defaults` | No | Disambiguated from AI Plan mode |
| Security | `docs-new/admin-guide/security` | **Batch D migrated** | MOVE TO SETTINGS / ADMIN | `concepts/settings-and-administration/security` | No | Legacy mirror until redirects |
| Audit logs | `docs-new/admin-guide/audit-logs` | **Batch D migrated** (availability-noted) | MOVE TO SETTINGS / ADMIN | Security child | No | No dedicated Audit Settings UI confirmed |
| Login methods (+ SAML/SCIM) | docs-new + support SAML | **Batch D REPLACE** | MOVE TO SETTINGS / ADMIN | Security child | No | SSO/SAML not confirmed as self-serve GA |
| Billing and usage | `docs-new/admin-guide/billing-and-plans` | **Batch D RENAME** | MOVE TO SETTINGS / ADMIN | `concepts/settings-and-administration/billing-and-usage` | No | Legacy mirror until redirects |
| Usage and limits | `docs-new/admin-guide/usage-and-limits` | **Batch D migrated** | MOVE TO SETTINGS / ADMIN | Billing child | No | Cells Used + AI Credits |
| Personal settings / Notifications | Concepts published | **Batch D expanded** | MERGE INTO EXISTING PAGE | personal-settings / notifications | No | Inbox chrome still thin; Skills REVIEW |
| Keyboard shortcuts | `docs-new/getting-started/keyboard-shortcuts` | **Batch E migrated** (app-verified subset) | ADD TO CONCEPTS **or** MOVE TO HOW-TO | `concepts/resources/keyboard-shortcuts` | No | Unconfirmed Legacy shortcuts omitted |
| Sidebar and search | `docs-new/your-sidebar/*` (4 pages) | **Batch E MERGE** (+ command palette) | MOVE TO HOW-TO **or** ADD TO CONCEPTS | `concepts/resources/sidebar-and-search` | No | Flag-gated nav called out |
| Troubleshooting hub | `docs-new/troubleshooting/*` | **Batch E MERGE** hub | MOVE TO HOW-TO **or** ADD TO CONCEPTS | `concepts/resources/troubleshooting` | No | Hub links Concepts; no child duplicates |
| Library hub | App Library; not in target parents | App gap | ADD TO CONCEPTS | New Data/Workspace parent (IA add) | No | Important product hub; not required if entity pages cover create/open |
| Integrations (Library) | Library Integrations | Distinct from Connectors & MCP | MOVE TO INTEGRATIONS | New Integrations Concepts **or** Integrations tab | No | Called out in AI context; needs dedicated home |
| Inbox | App Inbox; Notifications Concepts thin | App gap | ADD TO CONCEPTS **or** MOVE TO HOW-TO | Personal settings child **or** Resources | No | Notifications page exists; Inbox chrome optional |
| Command palette | App palette | App gap | MOVE TO HOW-TO **or** MERGE INTO EXISTING PAGE | Shortcuts / Sidebar-search | No | Discovery chrome |
| Onboarding / join workspace | App flows | App gap | MOVE TO HOW-TO | Getting started How-to | No | Not Concepts-critical |
| Search / navigation depth | Sidebar pages + palette | Partial via Spaces/Workspaces | MOVE TO HOW-TO | How-to + optional Resources | No | |
| Tags (models/boards) | App tags | Not target | REVIEW | Models/Boards note **or** skip | No | Confirm product importance |
| Board realtime collab | App collab env | Distinct from Comments | REVIEW | Boards | No | Comments page exists |
| Sprints (Projects) | Opt-in project feature | Mentioned only | REVIEW | Projects child later | No | Optional; Projects already availability-noted |
| Spaces vs Teamspaces terminology | Concepts Spaces page + product labels | Partially resolved table; still open | REVIEW | Keep terminology table; product copy follow-up | No | Docs already distinguish; polish remaining |
| FP&A vs Models vs Apps naming | App switcher | Open | REVIEW | Note on Models; avoid Apps confusion | No | |
| Users & Groups vs split Users/Roles | Concepts split published | Open merge question | REVIEW | Keep split or merge later | No | Already migrated |
| Personal settings vs My Account title | Concepts Personal settings | Open | REVIEW | sidebarTitle My Account optional | No | |
| Knowledge and memory depth | Minimal Concepts CREATE | Migrated incomplete | MERGE INTO EXISTING PAGE | Expand when persistence confirmed | No | Conservative by design |
| Custom agents discoverability | Concepts published; settings entry hidden | Migrated incomplete | MERGE INTO EXISTING PAGE | Note only until product re-exposes entry | No | |
| Chart types catalog completeness | Concepts CREATE (14 types) | Migrated; may need screenshot polish | MERGE INTO EXISTING PAGE | Boards charts pages | No | Substantively done |
| Model History completeness | Concepts CREATE | Migrated; Artifact History deferred | KEEP IN LEGACY TEMPORARILY | Legacy versioning until redirect | No | Concepts page exists; Legacy mirror until cutover |
| Publishing depth / public links | Concepts availability-noted | Migrated incomplete vs deep token flows | KEEP IN LEGACY TEMPORARILY | External-sharing Legacy until GA deepen | No | |
| Support-docs twins (~112) | support-docs | Parallel Legacy | KEEP IN LEGACY TEMPORARILY | Redirect then ARCHIVE | No | Cutover dependency is redirects, not re-migration |
| Concepts Legacy tab entire `docs-new/**` | Live | Untouched by design | KEEP IN LEGACY TEMPORARILY | Until redirects + Concepts parity for blockers | **Yes** (process) | Cutover = redirects + hide/unpublish Legacy, not content rewrite |
| Daily/weekly granularity docs | UI lists; AGENTS.md excludes | Intentionally omitted | REVIEW | Do not expand without product decision | No | Product-content boundary |
| Feature-flag admin | `/settings/feature-flags` | Internal | ARCHIVE **or** HOLD / UNRELEASED | Never customer Concepts | No | |

---

## Migrated but incomplete (quality / depth)

These pages exist in Concepts but reports flag unfinished depth or Legacy debt:

| Area | Gap | Recommended action | Blocking cutover? |
|---|---|---|---|
| Time | Last actual / rollups still Legacy-linked | ADD / MERGE (see table) | Last actual **Yes** |
| Formulas | Conditional logic Legacy-linked | ADD | **Yes** |
| Scenarios | Governance + Merge not migrated | ADD | **Yes** |
| Views | Creating / sharing / boards orphans | ADD / MERGE | Creating + sharing **Yes** |
| Transactions | Database formulas + filters orphans | ADD / MERGE | **Yes** |
| Sharing | Roles / inheritance / sensitive-data | ADD / MERGE | Roles + inheritance **Yes** |
| Spaces / Workspaces | workspace-access-and-visibility | ADD / MERGE | **Yes** |
| AI Skills / Plan mode | Unresolved | REVIEW | No |
| Knowledge and memory | Minimal claims | Expand later | No |
| Projects / Feed / Publishing / Exports / code-block | Availability-noted, not GA | HOLD notes | No |
| Personal settings / Notifications | Inbox mapping incomplete | MERGE / How-to | No |
| Integrations called out only from MCP | No Integrations Concepts home | MOVE TO INTEGRATIONS | No |

---

## App-visible but not in target IA

| Area | Recommendation | Blocking cutover? |
|---|---|---|
| Library hub | ADD TO CONCEPTS (IA expand) | No |
| Library Integrations | MOVE TO INTEGRATIONS | No |
| Inbox | ADD or How-to | No |
| Command palette | How-to / merge into shortcuts | No |
| Onboarding | How-to | No |
| Tags | REVIEW | No |
| Board realtime collab | REVIEW under Boards | No |
| Sprints | REVIEW under Projects | No |
| Analytics settings (if customer-facing) | REVIEW / Settings | No |

---

## Target IA not migrated (by bucket)

### Must migrate before Legacy cutover (blocking)

- ~~Core concepts: overview, glossary (+ decide What is Oculon / How organized)~~ **Batch C done**
- ~~Scenarios: governance, merge~~ **Batch A done**
- ~~Settings/Admin: workspace settings, security (+ audit, login), billing (+ usage)~~ **Batch D done**
- ~~Resources: keyboard shortcuts; troubleshooting hub (or How-to with redirects)~~ **Batch E done**
- Strong orphans promoted into Concepts: Last actual date; conditional logic; views creating + sharing; transactions formulas + filters; workspace-access; sharing roles + inheritance

### Can wait (non-blocking)

- How data flows (nice-to-have CREATE)
- ~~Planning defaults (after Plan/Planning disambiguation)~~ **Batch D done**
- ~~Sidebar and search (How-to preferred)~~ **Batch E done under Resources**
- Sensitive data (with Security)
- Templates, Artifacts, Apps, Agent teams, Plan mode, Skills
- Library / Integrations / Inbox / palette as IA expansions

---

## Cutover blockers

Resolve **before** the new Concepts tab can replace Concepts Legacy as the customer canonical Concepts surface:

1. ~~**Redirects infrastructure** for all migrated `docs-new` → `concepts` URLs~~ **Batch F done** (see `redirect-map.md`).
2. **Core concepts** (overview + glossary) and a decision for **What is Oculon / How organized**.
3. **Scenario governance + Merge scenarios** Concepts pages (already mapped).
4. **Last actual date** Concepts Time page (promote orphan).
5. **Conditional logic** Concepts Formulas page (promote orphan).
6. **Views:** creating-and-configuring + sharing-views in Concepts (or explicit How-to homes with redirects).
7. **Transactions:** database-formulas + filters/sorts/grouping in Concepts (or merged).
8. **Sharing depth:** roles-and-permissions + permission-inheritance in Concepts (or merged into Settings/Sharing with redirects).
9. **Workspace access and visibility** folded or added.
10. **Settings/Admin pass:** Workspace settings, Security (+ audit, login methods), Billing and usage (+ usage limits).
11. ~~**Resources minimum:** Keyboard shortcuts + Troubleshooting hub~~ **Batch E done** (`concepts/resources/*`).
12. ~~**Mintlify Legacy orphans** cleaned or redirected (5 missing nav files)~~ **Batch F done** (nav removed + redirects).
13. Confirm **flag-gated published pages** (Projects, Feed, Publishing, Exports, board code-block) keep availability notes — do **not** present as GA at cutover.

Do **not** treat Apps, Artifacts, Agent teams, Templates, Skills, or Plan mode as cutover blockers.

---

## Non-blocking follow-ups

- How data flows CREATE
- Time rollups promote or merge
- Using-views-on-boards merge into Boards
- Sensitive-data controls
- Planning defaults + Plan/Planning/Plan mode disambiguation page
- Skills / Plan mode publication after REVIEW
- Templates / Artifacts when GA
- Apps suite when product confirms depth
- Library hub + Integrations Concepts homes
- Inbox / command palette / onboarding How-to
- Knowledge/memory expansion; Custom agents settings discoverability
- Sprints / tags / board realtime collab REVIEW outcomes
- Spaces vs Teamspaces product-copy alignment
- Support-docs twin ARCHIVE after redirects verified
- Agent teams only if flag posture changes

---

## Settings / Admin work remaining

Dedicated migration pass still required for:

| Page | Map action | Notes |
|---|---|---|
| Workspace settings | MOVE | Admin General |
| Planning defaults | CREATE | Disambiguate vs Variables currency and AI Plan mode |
| Security | MOVE | Account vs admin Security and Access |
| Audit logs | MOVE | |
| Login methods | REPLACE | Pull SAML/SCIM from support if still shipped |
| Billing and usage | RENAME | Product **Plan and Billing** |
| Usage and limits | MOVE | |

Already migrated (do not re-do): Users/guests/invitations, Roles and access, Personal settings, Notifications (thin).

Related Sharing orphans may land in this pass or a Sharing follow-up: roles-and-permissions, permission-inheritance, sensitive-data-controls, members-guests-and-groups merge finish.

---

## Suggested final migration batches (minimum before cutover)

Order optimized for Legacy dependency removal:

| Batch | Scope | Why |
|---|---|---|
| **A. Scenarios completion** | Governance + Merge; retarget Compare scenarios → Analysis Compare | Mapped debt; small; high Legacy link use |
| **B. Strong orphans promote** | Last actual date; Conditional logic; Time rollups (add or merge); Transactions formulas + filters; Views creating + sharing; Using-views-on-boards merge; Workspace access; Sharing roles + inheritance | Removes most temporary Legacy links in migrated modules |
| **C. Core concepts** | Overview, Glossary (+ What is Oculon decision) | Cutover entry points |
| **D. Settings / Admin** | Workspace settings, Security trio, Billing duo; optional Planning defaults | Entire admin Legacy section |
| **E. Resources minimum** | Keyboard shortcuts; Troubleshooting hub (or How-to + redirects); optional Sidebar one-pager | Start-here / help surfaces |
| **F. Cutover prep (separate task)** | Redirect map; hide/unpublish Legacy; fix 5 Mintlify orphans; availability-note audit on flag-gated pages | Process cutover — still no premature GA claims |

**Explicitly park until after cutover:** Apps, Artifacts, Templates, Agent teams, Skills, Plan mode, Library/Integrations/Inbox IA expansions.

---

## Duplication / representation notes

| Pattern | Status |
|---|---|
| Concepts + Concepts Legacy both live | Intentional dual-tab; duplicates until cutover |
| support-docs twins | Represented in Legacy ecosystem; ARCHIVE after redirects |
| Scenario compare vs Compare scenarios | Deduped: Concepts owns Analysis Scenario compare |
| Model History vs Legacy versioning | Concepts owns; Legacy temporary |
| Connectors & MCP vs Library Integrations | Partial Concepts (MCP); Integrations still gap |
| Sharing Concepts vs roles/inheritance Legacy | Partial; Legacy still canonical for depth |
| Comments vs board realtime collab | Comments migrated; realtime REVIEW |
| Feed vs Project Activity vs Model History | Correctly separated |

---

## Coverage confidence

| Estimate | Value | Basis |
|---|---|---|
| **% of target IA migrated** | **~77%** (113 / 147) | Published Concepts content pages vs planned target pages |
| **% of intended pre-cutover IA** (excluding parked Apps/Artifacts/Agent teams/Templates/Skills/Plan mode ≈ 18 pages) | **~87%** (113 / ~129) | Same numerator; smaller denominator |
| **% of app-visible GA product covered in Concepts** | **~70–75%** | Core modeling/analysis/AI/workspace/settings-users covered; Library hub, Integrations, Admin settings, Resources, Inbox/palette still thin/missing |
| **% of remaining open items that are REVIEW/HOLD only** | **~55–60%** of the 34 unmigrated map rows + parked app gaps | Apps, Artifacts, Agent teams, Templates, Skills, Plan mode, flag-GA posture items dominate leftovers; true GA content debt is the minority |

---

## Verdict

Main staged Concepts batches are largely done for **core product Concepts**. The new Concepts tab is **not yet safe to replace Concepts Legacy** until batches **A–E** (and redirect cutover **F**) land.

Safe now: continue dual-tab; no new validation debt.

Not safe yet: Legacy cutover / redirects-as-canonical.

_End of coverage sweep._
