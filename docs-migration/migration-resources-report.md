# Resources migration report (Batch E)

Scope: Minimum Resources coverage for Concepts cutover. Legacy untouched. App read-only. Redirects deferred.

## Pages created / updated

| Path | Action | Legacy / support sources | App sources |
|---|---|---|---|
| `concepts/resources/keyboard-shortcuts` | MOVE (trimmed) | `docs-new/getting-started/keyboard-shortcuts`; `support-docs/guides/keyboard-shortcuts` | `CommandPaletteProvider` / `isCommandPaletteShortcut`; `useUndoShortcuts`; `useModelClipboardShortcuts`; model Delete key path; formula editor hints; AI chat / board slash menus |
| `concepts/resources/sidebar-and-search` | MERGE | `docs-new/your-sidebar/*` (4 pages) | `Sidebar.tsx`; `helper.tsx` `PAGE_NAVIGATION_LIST` / feature gates; `HomeLists` Recents; `CommandPalette.tsx` destinations/actions/filters |
| `concepts/resources/troubleshooting` | MERGE hub | `docs-new/troubleshooting/*` (7 pages) | N/A (triage + Concepts links) |

Also updated: `docs.json` Resources group; `concepts/index.mdx`; `concepts/core-concepts/how-oculon-is-organized.mdx` Resources link; `docs-migration/concepts-coverage-sweep.md`.

## Migration actions

| Action | Count |
|---|---|
| MOVE | 1 (keyboard shortcuts) |
| MERGE | 2 (sidebar+search; troubleshooting hub) |
| UPDATE supporting | 3 (index, how-organized, coverage sweep) |

## Obsolete content removed

From Legacy shortcut lists (not published as current Concepts shortcuts):

- Dedicated shortcuts panel (`Cmd/Ctrl + /`)
- Separate quick-open (`Cmd/Ctrl + P`)
- Numbered area jumps (`Cmd/Ctrl + 1…9`)
- Filter builder / show-formulas / F9 recalculate chords
- Number-format chords
- Database expand/`E` and attachment chords
- Board builder `V` toggle
- Agent console `Cmd/Ctrl + Shift + A`
- Fill down/right / insert-delete row chords not confirmed in current shortcut handlers

From sidebar Legacy:

- Generic “databases” wording → Transactions
- Assumed universal presence of Projects / Feed / Templates / Artifacts
- Deep customization/runbook tone (kept concise reference)

From troubleshooting Legacy:

- No per-issue child Concepts pages (hub only)
- No internal/feature-flag debugging guidance

## Command / shortcut availability decisions

| Item | Decision |
|---|---|
| `Cmd/Ctrl + K` command palette | Document (confirmed) |
| Model/Transactions clipboard + undo/redo | Document (confirmed) |
| Model `Delete` for selected row/variable | Document with permission note |
| Formula editor Enter / Shift+Enter / Esc | Document |
| Board/AI `/` menus; chat Enter / Esc | Document as context shortcuts |
| Unconfirmed Legacy chords | Omit; called out under “What this page does not claim” |
| Command palette destinations | Document GA destinations; note flag-gated Templates/Artifacts |
| Separate Search vs Command pages | Merged into `sidebar-and-search` (target IA; keeps Resources light) |

## Troubleshooting structure

Single hub with:

1. Triage checklist
2. Models and calculations
3. Transactions / data
4. Integrations and connections
5. Views and boards
6. Sharing and permissions
7. AI and agents
8. Workspace and account
9. Performance
10. Escalation notes

Each section links existing Concepts pages rather than duplicating module docs.

## Remaining resource gaps (non-blocking)

- Deeper How-to runbooks for each Legacy troubleshooting child
- Inbox chrome reference
- Library hub Concepts home
- Integrations Concepts home
- Optional expanded shortcuts if product reintroduces a shortcuts panel
- Screenshot refresh for sidebar if chrome changes

## Validation

| Check | Result |
|---|---|
| Files exist | Pass |
| docs.json paths | Pass |
| Internal Concepts links | Pass (script) |
| Images | `fr-sidebar-full.png` exists |
| Legacy untouched | Pass |
| Mintlify broken-links | Same pre-existing 10 breaks in 7 Legacy/essentials/support-docs files; **zero** Concepts Resources breaks |

## Cutover readiness

**Batch E Resources minimum is cutover-ready.**

**Batch F (redirects + Legacy cleanup) can start** after this batch. Remaining content blockers for full Legacy hide are process/redirects and pre-existing Mintlify Legacy orphans—not missing Resources pages.
