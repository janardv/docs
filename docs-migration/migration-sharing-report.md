# Sharing migration report

Scope: Sharing and permissions parent + Publishing + Exports. Comments covered in `migration-comments-report.md`. Legacy untouched.

## Pages created

| Target path | Action | Legacy | support-docs | App |
|---|---|---|---|---|
| `concepts/workspace-and-collaboration/sharing-and-permissions` | MOVE | `sharing-basics` (+ links to roles/inheritance orphans) | twin | ShareResource; View/Edit/Full Access/No Access |
| `.../publishing` | MERGE | `external-sharing-and-exports` (publish half) | twin | Publish tab; flag-gated |
| `.../exports` | MERGE | `external-sharing-and-exports` (export half) | twin | Export controls; flag-gated |

## Content merge

### Preserved
- Smallest useful share surface; dependency gaps; external context caution

### Rewritten
- Transactions wording; Frame markup; availability notes for publish/export

### Added
- Landing Cards; item access table; links to Settings Users/Roles Concepts pages

### Omitted
- Duplicating full roles/inheritance/sensitive-data Legacy pages as Concepts children
- Deep publish token / analytics implementation

## Sharing / access boundary

| Topic | Placement |
|---|---|
| Object sharing + effective access | Concepts Sharing |
| Workspace membership / invites | Settings → Users |
| Groups | Settings → Roles and access |
| Roles / inheritance / sensitive-data depth | Legacy for now (IA gaps) |
| Publish / Export | Concepts children with availability notes |

## IA gaps
| Legacy | Recommendation |
|---|---|
| `roles-and-permissions` | add under Sharing or merge into Roles and access |
| `permission-inheritance` | add under Sharing |
| `members-guests-and-groups` | merge into Users + Roles |
| `sensitive-data-controls` | add under Sharing or Security |

## Validation
Pass for Concepts Sharing pages; pre-existing Mintlify Legacy errors unchanged.

## Unresolved
1. Add roles/inheritance/sensitive-data as Concepts children before cutover?
2. Confirm publish/export GA posture per environment.
