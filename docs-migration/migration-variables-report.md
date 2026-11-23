# Variables migration report

Scope: Variables module only. Legacy `docs-new/variables/**` and `support-docs/variables/**` left untouched. App repo read-only. Redirects not applied.

## Pages created

| Target path | Migration action | Legacy sources used | App sources used |
|---|---|---|---|
| `concepts/data-and-structure/variables` | MOVE (landing) | `docs-new/variables/what-is-a-variable` (intro/image) + target child list | Model grid variables; Dimensions cross-links |
| `concepts/data-and-structure/variables/what-is-a-variable` | MOVE | `docs-new/variables/what-is-a-variable` (richer than support twin) | Actual/planned formulas; Last actual date boundary |
| `concepts/data-and-structure/variables/variable-types` | MOVE | `docs-new/variables/variable-types` | Variable type/format UI |
| `concepts/data-and-structure/variables/create-and-edit-variables` | MOVE | `docs-new/variables/create-and-edit-variables` (+ support twin steps ignored where weaker) | `AddVariablePicker` (**Add variable**); drag reorder |
| `concepts/data-and-structure/variables/variable-breakdown` | MOVE | `docs-new/variables/variable-breakdown` | Dimension attach / breakdown UI |
| `concepts/data-and-structure/variables/variable-formatting` | MOVE | `docs-new/variables/variable-formatting` | Format panel; currency_config |
| `concepts/data-and-structure/variables/variable-behavior` | REPLACE | `docs-new/variables/variable-behavior` + `docs-new/time/last-actual-date` concepts | `last_actual_date`; actual/planned formula fields; overrides |
| `concepts/data-and-structure/variables/variable-references` | MOVE | `docs-new/variables/variable-references` | Formula autocomplete / linked models |
| `concepts/data-and-structure/variables/currency-and-conversion` | CREATE | `support-docs/oculon-basics/currency-and-conversion` | Variable Format **Currency**; admin Planning defaults noted |
| `concepts/data-and-structure/variables/variable-best-practices` | MOVE | `docs-new/variables/variable-best-practices` | — |

Also updated: `docs.json` Concepts → Data and structure → Variables; `concepts/index.mdx`.

## Content merge decisions

### Preserved

- Variable definition, parts (type, name, breakdown, trend, actual/planned formulas, time values/overrides)
- Type catalog and formatting options
- Create/edit/reorder/organize guidance
- Breakdown and multi-dimension explanations
- Reference patterns and best practices
- Screenshots under `/images/getting-started/fr-*` and `currency.png`

### Rewritten

- Image markup → `<Frame>` + alt text
- Create control label → **Add variable** (app)
- Actual/planned wording tied explicitly to Last actual date
- “databases” → **Transactions** in one overview sentence (product Library label)
- Breakdown intro “In FP&A” softened to “In planning models”
- Typo `aggreagation` → `aggregation`
- Internal links to Dimensions / Formulas / Time Concepts paths where migrated

### Added

- Landing Cards into all Variable children
- Currency page (display-only) with Format steps and Planning defaults note
- REPLACE behavior page: Last actual date split, overrides, cross-links
- Formatting table row pointing to Currency page
- Best-practice links to Dimensions and Formulas Concepts pages

### Omitted

- Full FX conversion workflows (not evidenced as customer-facing on this page; Note added)
- Deep VariableDetailPanel property catalog beyond Legacy coverage
- `NEXT_PUBLIC_DIMENSION_VARIABLES_ENABLED` internals
- Creating a dedicated Last actual date Concepts child (not in Variables target; linked Legacy)

## Terminology decisions

| Legacy / target | Product UI | Choice |
|---|---|---|
| + add new variable | **Add variable** | Use **Add variable** |
| databases (data connection phrasing) | Library **Transactions** | Prefer Transactions in overview |
| actuals cutoff / actuals range | **Last actual date** | Prefer Last actual date (`AGENTS.md`) |
| actual formula / planned formula | Actual / planned formula fields | Keep canonical terms |
| Currency and conversion | Format **Currency** | Page title per target; body clarifies display vs conversion |
| Planning defaults | Admin **Planning** | Mentioned as related; naming conflict with Plan mode left unresolved globally |

## Validation

| Check | Result |
|---|---|
| Files exist | Pass (10 pages) |
| docs.json paths valid | Pass |
| Internal links valid | Pass (Last actual date / unmigrated pages → Legacy by design) |
| Referenced images exist | Pass |
| Unrelated legacy unchanged | Pass |
| Mintlify validate | Fail only on 5 pre-existing Legacy orphans; no new Concepts Variable errors |
| Mintlify broken-links | 15 pre-existing; none in Concepts Variables |

## Unresolved questions

1. Should Currency stay under Variables only, or also under Settings → Planning defaults?
2. Does display-currency ever imply conversion, or is conversion a separate future surface?
3. Should Last actual date become a first-class Concepts Time child so Variable/Time/Formulas stop linking Legacy?

## Planned redirects (later cutover)

| Source | Destination |
|---|---|
| `/docs-new/variables/*` | `/concepts/data-and-structure/variables/*` |
| `/support-docs/variables/*` | matching Concepts paths |
| `/support-docs/oculon-basics/currency-and-conversion` | `/concepts/data-and-structure/variables/currency-and-conversion` |

## Learnings

- REPLACE pages need Last actual date content even when that child is not yet in Concepts IA.
- CREATE from Old support-docs works if scoped tightly to verified UI.
