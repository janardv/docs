# Projects migration report

Scope: Projects landing and project-level Concepts pages (structure, create/manage, AI in projects, settings/access). Tasks and Activity have sibling reports. Legacy untouched. App read-only. Redirects deferred.

## Pages created

| Target path | Action | Legacy | support-docs | App |
|---|---|---|---|---|
| `concepts/workspace-and-collaboration/projects-and-tasks` | CREATE | — | — | `/projects`; sidebar **Projects**; `projects-enabled` |
| `.../what-is-a-project` | CREATE | — | — | Project container; vs Spaces |
| `.../project-structure` | CREATE | — | — | Portfolio tabs; Overview / Tasks / Activity / Chats; optional Sprints |
| `.../create-and-manage-projects` | CREATE | — | — | **New project**; duplicate/archive/complete; Space placement |
| `.../ai-in-projects` | CREATE | — | — | Instructions; project memory; chats; files; agent tasks |
| `.../project-settings-and-access` | CREATE | — | — | Project settings menu; `/projects/settings`; **Workspace access** / **Share projects** |

## Feature availability / flags

| Control | Posture |
|---|---|
| `projects-enabled` | On local/sandbox; off development/staging/production by default |
| `NEXT_PUBLIC_PROJECTS_ENABLED=false` | Hides nav and routes |

Publication: **availability-noted** (same class as Feed). Not presented as GA.

## Content

### Preserved
N/A — no Legacy docs-new Projects pages.

### Rewritten
N/A — CREATE from app evidence.

### Added
- Availability callout on landing
- Projects vs Spaces distinction
- Portfolio and detail structure
- Lifecycle and Space placement without inventing ACL inheritance
- Project AI surfaces with non-claims
- Settings/access entry points; link out to Sharing for generic permission model

### Omitted
- Plans product object (custom board tab name only → REVIEW)
- Project tags as a first-class object
- Deep template/repeat how-to as GA
- Public publishing / anonymous access
- Internal QA bugs and flag admin
- Generic sharing vocabulary duplication
- Standalone Sprints Concepts page (optional feature note only)

## Terminology decisions

| Term | Choice |
|---|---|
| Module title | **Projects and tasks** |
| Sidebar | **Projects** |
| Activity | **Activity** (project-scoped; not History) |
| Sprints | Optional project feature |
| Plans / tags | REVIEW — not published |

## IA gaps

| Item | Status |
|---|---|
| Plans as product concept | REVIEW — not a distinct Projects object |
| Tags | No project tag object documented |
| Sprints depth | Mention only; no dedicated page |
| Templates / Repeat depth | Visible in UI; kept light pending GA |
| Production default-on | Open |

## Validation

8 project-module paths in `docs.json` (including Tasks + Activity). See batch validation in summary. Legacy/support untouched.

## Unresolved questions

1. When Projects becomes default-on in production.
2. Whether Sprints deserve a dedicated Concepts child after GA.
3. Template/repeat documentation depth after product polish.
