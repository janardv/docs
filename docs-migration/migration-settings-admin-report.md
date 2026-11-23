# Settings / Administration migration report (Batch D)

Scope: Settings and administration Concepts only. Legacy untouched. App read-only. Redirects deferred. Resources not migrated.

## Pages created / updated

| Path | Action | Legacy / support | App sources |
|---|---|---|---|
| `concepts/settings-and-administration/workspace-settings` | MOVE | `docs-new/admin-guide/workspace-settings` | `GeneralProfileDrawer`; Admin nav |
| `.../workspace-settings/planning-defaults` | CREATE | support currency partial | `SettingsPlanningDrawer` Defaults/Currency |
| `.../security` | MOVE | `docs-new/admin-guide/security` | `SettingsSecurityAccessDrawer`; My Account Security |
| `.../security/login-methods` | REPLACE | `docs-new/admin-guide/login-methods`; support SAML | Personal Security; no SSO UI |
| `.../security/audit-logs` | MOVE (availability-noted) | `docs-new/admin-guide/audit-logs` | No dedicated Audit Settings UI |
| `.../billing-and-usage` | RENAME | `docs-new/admin-guide/billing-and-plans` | `WorkspaceUsageSettings`; Plan and Billing / Usage |
| `.../billing-and-usage/usage-and-limits` | MOVE | `docs-new/admin-guide/usage-and-limits` | Cells Used; AI Credits |
| `.../personal-settings` | UPDATE | profile-and-preferences | My Account drawers |
| Users / Roles / Notifications | Already migrated | — | Unchanged structure; Roles copy lightly retargeted |
| Workspace AI | Already under AI | — | Linked from Settings; not duplicated |

Also updated: `docs.json` Settings group; `concepts/index.mdx` Settings table.

## Migration actions

| Action | Count |
|---|---|
| MOVE | 4 |
| CREATE | 1 |
| REPLACE | 1 |
| RENAME | 1 |
| UPDATE existing | 2 (personal-settings, roles-and-access) |

## Settings categories covered

| Category | Coverage |
|---|---|
| Workspace General | Name, picture, Public/Private, Delete Workspace |
| Planning defaults | Period, forecast frequency, fiscal year start, default scenario, default currency, exchange aggregation |
| Users & Groups | Existing Users + Roles pages |
| Teamspace | Linked to Spaces Concepts |
| Workspace AI | Link to AI Concepts |
| Security and Access | Invite only / approved domains, domain join, require 2FA |
| My Account Security | Password, Google, 2FA, sessions |
| Billing / Usage | Current plan, Cells Used, AI Credits |
| Personal preferences | Theme, accent, home, timezone, time format, language |
| Notifications | Existing page |

## Role / permission boundaries

- Admin Settings: **Workspace Owner** only
- My Account: every user for self
- Item sharing: out of scope here; linked to Sharing Concepts
- Groups: Roles and access page; not duplicated as Sharing

## Plan / availability notes

| Topic | Note |
|---|---|
| SSO / SAML / SCIM | Not confirmed in Settings UI — not documented as self-serve GA |
| Audit logs UI | Not confirmed — page documents oversight concept + availability gap |
| Import/Export admin page | Not present; notification event names only |
| Planning defaults persistence | UI confirmed; some client persistence is local — documented as Settings controls, not internal storage |
| Billing pricing | In-product only; no speculative price tables |
| Skills under My Account | Mentioned; Concepts Skills placement remains REVIEW |

## Terminology decisions

| Product label | Concepts title |
|---|---|
| Plan and Billing | Billing and usage (`sidebarTitle`: Plan and Billing) |
| My Account | Personal settings (`sidebarTitle`: My Account) |
| Users & Groups | Split Users + Roles pages (existing) |
| Security and Access | Under Security |
| Admin Planning | Planning defaults (not AI Plan mode) |
| Workspace Owner | Keep |

## Content omitted as outdated / unsupported

- Self-serve SSO setup instructions from older admin docs
- Invented Audit logs click-paths
- Import/Export admin configuration page
- Storybook-only richer billing drawers as GA
- Speculative seat pricing
- Duplicating full Workspace AI tab docs under Settings

## IA gaps

- Connectors & MCP also appear under My Account — detailed under AI Context
- Skills still REVIEW for Concepts vs Settings
- Sensitive-data-controls Legacy page still not a Settings child
- Feature-flags admin never customer Concepts

## Validation

| Check | Result |
|---|---|
| New files exist | Pass (11 Settings MDX pages) |
| docs.json paths | Pass (all Settings nav entries resolve) |
| Internal Concepts links | Pass (`109` Settings/index `/concepts/` links; `0` missing) |
| Images | `fr-workspace-set.png`, `fr-groups.png` exist; no missing Settings images |
| Legacy untouched | Pass (no Legacy MDX edits) |
| Mintlify broken-links | `10` broken links in `7` files — all pre-existing Legacy / essentials / support-docs; **zero** new Concepts Settings links |
| Parsing noise | Pre-existing `docs-migration/*.md` MDX parse warnings only |

Also updated: `concepts/index.mdx` Settings table; `docs-migration/concepts-coverage-sweep.md` Batch D status.

## Cutover readiness

**Batch D is cutover-ready** for Settings/Admin Concepts, with honest availability notes on SSO and Audit.

## Remaining for Batch E

- Resources: keyboard shortcuts, sidebar and search, troubleshooting
- Redirect cutover / Legacy hide
- Non-blocking polish (sensitive-data, Skills REVIEW, Time rollups, using-views-on-boards)
