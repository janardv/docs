# Comments migration report

Scope: Comments and collaboration only. Nested under Sharing and permissions. Legacy untouched.

## Pages created

| Target path | Action | Legacy | support-docs | App |
|---|---|---|---|---|
| `.../comments-and-collaboration` | MOVE | `docs-new/sharing-and-permissions/comments-and-collaboration` | twin | `components/comments/**`; surfaces: model/board/Transactions/dimensions |

## Content merge

### Preserved
- Decision-oriented commenting; smallest useful object; resolve loops; screenshot

### Rewritten
- Cross-links to Notifications / Compare / Sharing Concepts paths
- Mentions note tied to Inbox without inventing delivery rules

### Added
- Confirmed surfaces list (model, board, Transactions, dimensions)

### Omitted
- Realtime board collaboration beyond comments (separate REVIEW)
- Invented mention UX details not confirmed in customer docs

## IA gaps
None unique beyond board realtime collab already tracked under Boards.

## Validation
Pass; no new Mintlify Concepts errors.

## Unresolved
1. Document board realtime collab separately from comments?
