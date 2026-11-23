# Spaces / Workspaces migration report

Scope: Workspaces + Teamspaces and private space. Legacy untouched. App read-only. Redirects deferred.

## Pages created

| Target path | Action | Legacy | support-docs | App |
|---|---|---|---|---|
| `concepts/workspace-and-collaboration/workspaces` | MOVE | `docs-new/workspace-and-organization/what-is-a-workspace` | twin | `/workspaces`; Switch Workspace |
| `concepts/workspace-and-collaboration/teamspaces-and-private-space` | RENAME | `docs-new/workspace-and-organization/teamspaces-and-organization` | twin | Sidebar **Spaces**; **Create New Teamspace**; Private Space |

## Content merge

### Preserved
- Workspace framing; Spaces create/manage/settings structure; best practices; screenshots

### Rewritten
- Workspace roles → **Workspace Owner** / **Member** (not Admin)
- Databases → Transactions
- Open/Closed permission copy aligned to create dialog
- Terminology table for Spaces / Teamspace / Private Space

### Added
- Explicit product terminology table
- Closed = request-to-join wording from app

### Omitted
- Invented inheritance rules
- Deep admin Teamspace security beyond Legacy tabs

## Terminology decisions

| Term | Choice |
|---|---|
| Sidebar umbrella | **Spaces** |
| Shared area create label | **Create New Teamspace** / teamspace |
| Personal area | **Private Space** |
| Target page title | Keep **Teamspaces and private space** (`sidebarTitle`: Spaces) |

## IA gaps
| Legacy | Recommendation |
|---|---|
| `workspace-access-and-visibility` | keep Legacy; link from Workspaces |

## Validation
Files/nav/links/images pass for these pages. Mintlify: no new Concepts errors (pre-existing Legacy noise unchanged).

## Unresolved
1. Unify product copy so Spaces vs Teamspace naming is fully consistent in UI.
2. Promote workspace-access-and-visibility into target IA?
