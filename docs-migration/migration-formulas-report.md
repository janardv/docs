# Formulas migration report

Scope: Formulas module only (target children). Legacy `docs-new/formulas/**` and `support-docs/formulas/**` left untouched. App repo read-only. Redirects not applied.

## Pages created

| Target path | Migration action | Legacy sources used | App sources used |
|---|---|---|---|
| `concepts/modeling/formulas` | MOVE (landing) | `docs-new/formulas/formula-basics` intro + target children | Formula editor; actual/planned formulas |
| `concepts/modeling/formulas/formula-basics` | MOVE | Prefer docs-new | Enhanced formula editor; last actual split |
| `concepts/modeling/formulas/formula-editor` | MOVE | Prefer docs-new | Formula editor; show-formulas shortcut |
| `concepts/modeling/formulas/functions` | MOVE | Prefer docs-new | Formula functions/operators |
| `concepts/modeling/formulas/helper-variables-and-modifiers` | MOVE | Prefer docs-new | Helpers: `lastActualDate`, `timestep`, fiscal modifiers |
| `concepts/modeling/formulas/common-formula-patterns` | MOVE | Prefer docs-new | Actual-to-planned patterns |
| `concepts/modeling/formulas/formula-errors` | MOVE | Prefer docs-new | Debugging from source variable |
| `concepts/modeling/formulas/formula-best-practices` | MOVE | Prefer docs-new | Review habits around cutoff |

Also updated: `docs.json` Concepts → Modeling → Formulas; `concepts/index.mdx`.

**Not created:** `conditional-logic` exists in Legacy but is not a target Concepts child. Temporary Legacy links retained.

## Content merge decisions

### Preserved

- Mature docs-new formula set (basics, editor, functions, helpers, patterns, errors, best practices)
- Actual vs planned formula framing
- Helper/modifier keyword tables
- Common planning patterns and error triage
- Formula screenshot asset

### Rewritten

- Image markup → Frame/alt
- Cross-links to migrated Variables / Time / Dimensions Concepts paths
- Last actual date / conditional-logic / troubleshooting / model best practices kept on Legacy where not migrated

### Added

- Landing Cards into formula children
- Related links to Variable references and Time Concepts pages

### Omitted

- Migrating `docs-new/formulas/conditional-logic` as a Concepts page (not in target IA)
- Pasting `FORMULA_ARCHITECTURE.md` implementation detail
- API/pipeline migration notes from internal task docs

## Terminology decisions

| Legacy / target | Product UI | Choice |
|---|---|---|
| actual formula / planned formula | Actual / planned formula editing | Keep |
| Last actual date / `lastActualDate` | Last actual date setting; helper keyword | UI term in prose; keyword in code examples |
| Helper variables / modifiers | Formula helpers and context keywords | Keep distinction |
| Conditional logic | (Legacy page) | Link Legacy; do not invent Concepts child |
| Plan / Planning / Plan mode | N/A in this module body | Not introduced; avoid collision |

## Validation

| Check | Result |
|---|---|
| Files exist | Pass (8 pages) |
| docs.json paths valid | Pass |
| Internal links valid | Pass |
| Referenced images exist | Pass |
| Unrelated legacy unchanged | Pass |
| Mintlify validate | Pre-existing 5 Legacy orphans only |
| Mintlify broken-links | Pre-existing only; none in Concepts Formulas |

## Unresolved questions

1. Should **Conditional logic** be added to the Formulas target IA (Legacy page is strong and widely linked)?
2. When Last actual date becomes a Concepts Time child, bulk-retarget formula links.
3. Shortcut text `Cmd/Ctrl + Shift + \`` preserved from Legacy; confirm still accurate in current editor UX.

## Planned redirects (later cutover)

| Source | Destination |
|---|---|
| `/docs-new/formulas/formula-basics` | `/concepts/modeling/formulas/formula-basics` |
| `/docs-new/formulas/formula-editor` | `/concepts/modeling/formulas/formula-editor` |
| `/docs-new/formulas/functions` | `/concepts/modeling/formulas/functions` |
| `/docs-new/formulas/helper-variables-and-modifiers` | `/concepts/modeling/formulas/helper-variables-and-modifiers` |
| `/docs-new/formulas/common-formula-patterns` | `/concepts/modeling/formulas/common-formula-patterns` |
| `/docs-new/formulas/formula-errors` | `/concepts/modeling/formulas/formula-errors` |
| `/docs-new/formulas/formula-best-practices` | `/concepts/modeling/formulas/formula-best-practices` |
| `/docs-new/formulas/conditional-logic` | TBD if added to Concepts |

## Learnings

- Formulas are a clean MOVE set once Variables/Time Concepts paths exist for cross-links.
- Target IA omissions (conditional logic, Last actual date) create intentional Legacy link debt; track in cutover.
