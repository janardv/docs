# Project Activity migration report

Scope: Project Activity Concepts page. Kept separate from Model History. No generic History parent. Legacy untouched. App read-only.

## Pages created

| Target path | Action | Legacy | support-docs | App |
|---|---|---|---|---|
| `concepts/workspace-and-collaboration/projects-and-tasks/project-activity` | CREATE | — | — | Project detail **Activity** tab; `ProjectActivityFeed` filters |

## Feature availability / flags

Gated with Projects (`projects-enabled`). Availability-noted via Projects landing.

## Content

### Added
- Activity as project-scoped event history (creates/edits/comments/attachments)
- Filters: All activity / Project / Tasks / Comments
- Explicit contrast table vs Model History

### Omitted
- Global History Concepts parent
- Artifact History (out of scope)
- Restore/checkpoint semantics (those belong to Model History only)

## Terminology decisions

| Term | Choice |
|---|---|
| Product label | **Activity** |
| Docs title | **Project activity** |
| Model surface | **Model History** (linked, not merged) |

## IA gaps

| Item | Status |
|---|---|
| Artifact History | Deferred with Artifacts module |
| Feed vs Project Activity | Separate surfaces; not merged |

## Validation

Page under Projects nav group. Link to Model History resolves.

## Unresolved questions

1. Whether Activity should cross-link Feed when both are enabled.
2. Full event taxonomy for customer docs (keep high-level for now).
