# Transactions migration report

Scope: Transactions module only (`concepts/data-and-structure/transactions/**`). Legacy `docs-new/databases/**` and `support-docs/databases/**` left untouched. App repo read-only. Redirects not applied.

Public terminology follows `ia-decisions.md` choice **A**: **Transactions** everywhere in Concepts; **database** only as Legacy alias / sparse explanatory copy.

## Pages created

| Target path | Migration action | Legacy sources used | support-docs sources used | App sources used |
|---|---|---|---|---|
| `concepts/data-and-structure/transactions` | RENAME (landing) | `docs-new/databases/what-is-a-database` (overview framing) | twin (shorter; not primary) | Library **Transactions** tab; **Create Transactions** |
| `concepts/data-and-structure/transactions/what-is-a-transaction` | RENAME | Prefer richer `docs-new/databases/what-is-a-database` | twin for comparison | CreateEntityMenu; Library list; Command palette label Transactions |
| `concepts/data-and-structure/transactions/transaction-types` | RENAME | `docs-new/databases/database-types` | twin | Library create vs integration canvas **Create Transactions** |
| `concepts/data-and-structure/transactions/transaction-structure` | RENAME | `docs-new/databases/database-structure` | twin | Transactions grid / column model (conceptual) |
| `concepts/data-and-structure/transactions/working-with-data` | RENAME | `docs-new/databases/working-with-data` | twin | **Create Transactions**; **Transactions Settings**; **Share Transactions** |
| `concepts/data-and-structure/transactions/linked-data` | RENAME | `docs-new/databases/linked-data` | twin | Linked models / boards embeds (conceptual) |
| `concepts/data-and-structure/transactions/refresh-and-sync-behavior` | RENAME | `docs-new/databases/refresh-and-sync-behavior` | twin | Connection/refresh status UI; integration sync |
| `concepts/data-and-structure/transactions/transaction-best-practices` | RENAME | `docs-new/databases/database-best-practices` | twin | — |

Also updated:

- `docs.json` — Concepts → Data and structure → **Transactions** group (`expanded: true`)
- `concepts/index.mdx` — listed Transactions among migrated modules

**Not created as Concepts children (IA gaps):**

- `docs-new/databases/database-formulas`
- `docs-new/databases/filters-sorts-and-grouping`

Temporary Legacy links from Working with data keep those topics reachable.

## Content merge decisions

### Preserved

- Source-layer framing (Transactions vs models vs views/boards)
- Manual vs external-source ownership guidance
- Structure / grain / typed-field guidance
- Linked-data dependency and ownership guidance
- Refresh/sync operating rhythm and failure modes
- Best-practice checklist and governance habits
- Screenshots: `fr-db.png`, `db-config.png`, `fr-connection-status.png`
- Placeholder SVGs under `/images/databases/*` (reused; filenames still say database)

### Rewritten

- All public nouns/titles: Database(s) → Transaction(s) per target IA
- Entry points: Library **Transactions**, **Create Transactions**, **Transactions Settings**, **Share Transactions**
- “Query-backed database” → **integration-backed Transactions** (matches Create from integration UI without inventing product jargon)
- Image markup upgraded to `<Frame>` + descriptive `alt`
- Cross-links to migrated Concepts Models / Dimensions paths
- Landing Cards for all target children
- One-line Legacy alias note (“Older docs called these Databases”) on landing + overview

### Added

- Parent landing page (Legacy had no dedicated Transactions/Databases landing beyond “What is…”)
- Product UI chrome for create/settings/share
- Temporary links to Legacy orphans (formulas; filters/sorts/grouping)

### Omitted

- Internal route names (`/databases`, `/library/databases`) as customer terminology
- Resource type `database` as a public noun
- Auto-creating Concepts pages for Database formulas / Filters sorts and grouping
- Speculative sync scheduling UI details beyond Legacy’s manual vs scheduled framing
- Documenting stale banner copy that still says “database” internally as a customer instruction

## Terminology decisions

| Legacy / target wording | Current product UI | Choice |
|---|---|---|
| Database / Databases | Library **Transactions**; **Create Transactions** | Public term **Transactions** |
| What is a database | — | **What is a transaction** |
| Database types / structure / best practices | — | **Transaction** titles |
| Manual database | Library **Create Transactions** | **Manual Transactions** |
| Query-backed database | Integration **Create Transactions** | **Integration-backed Transactions** |
| database (internal type/route) | — | Not documented as product terminology |
| Database formulas (Legacy title) | — | Keep temporary Legacy link; title remains Legacy until that orphan migrates |
| Transactions block (Boards) | Slash menu **Transactions** | Out of scope this module; naming already decided |

## Validation

| Check | Result |
|---|---|
| Files exist | Pass (8) |
| docs.json paths valid | Pass (Transactions nav resolves) |
| Internal links valid | Pass (Concepts + temporary Legacy orphans + troubleshooting) |
| Referenced images exist | Pass (3 PNGs + 4 placeholder SVGs) |
| Unrelated Legacy unchanged | Pass (`docs-new/databases/**`, `support-docs/databases/**` clean) |
| Mintlify validate | Pass for Concepts Transactions; **5 pre-existing** Legacy missing-nav-page errors unchanged |
| Mintlify broken-links | Pass for Concepts Transactions; **15 pre-existing** broken links unchanged (none under `concepts/data-and-structure/transactions`) |

### Pre-existing Mintlify validate errors (unchanged)

- `docs-new/time/actuals-and-forecast-boundary`
- `docs-new/models/cloning-and-versioning`
- `docs-new/models/model-organization`
- `docs-new/views/private-vs-shared-views`
- `docs-new/views/view-behavior`

### Pre-existing broken links (unchanged)

Legacy/support/essentials and the five missing-nav docs.json targets above. No new Concepts Transactions link failures.

## Unresolved questions

1. Should **Database formulas** and **Filters, sorts, and grouping** be added to the Transactions target IA, merged into Working with data, or kept Legacy-only until a follow-up decision?
2. Placeholder SVGs still live under `/images/databases/` with database filenames — rename assets later for consistency, or leave paths stable?
3. Some in-product status strings may still say “database” (implementation residue). Confirm whether product will fully reword those before cutover screenshots refresh.
4. Exact customer-facing labels for scheduled vs manual refresh controls should be re-verified against current integration UI before deepening the Refresh page beyond Legacy framing.

## IA gaps (strong Legacy omitted from target)

| Legacy path | Recommendation | Temporary links used? |
|---|---|---|
| `docs-new/databases/database-formulas` | **add to target IA** under Transactions, or **merge** into Working with data after product confirms formula surface | yes |
| `docs-new/databases/filters-sorts-and-grouping` | **add to target IA** under Transactions, or **merge** into Working with data (distinct from Views filters page) | yes |

## Product-content boundary / REVIEW items

| UI or code signal | Established docs/product guidance | Handling |
|---|---|---|
| Internal routes `/databases`, type `database` | Public term Transactions (`ia-decisions.md`) | Omit routes from customer copy |
| Pipeline/status copy may still say “database” | Prefer Library/Create labels | Document Transactions UI labels; do not teach internal route names |
| Full chart of integration sync states | Legacy high-level refresh guidance | Preserve Legacy depth; do not invent state machine |

## Planned redirects (for later cutover)

| Source | Destination |
|---|---|
| `/docs-new/databases/what-is-a-database` | `/concepts/data-and-structure/transactions/what-is-a-transaction` |
| `/docs-new/databases/database-types` | `/concepts/data-and-structure/transactions/transaction-types` |
| `/docs-new/databases/database-structure` | `/concepts/data-and-structure/transactions/transaction-structure` |
| `/docs-new/databases/working-with-data` | `/concepts/data-and-structure/transactions/working-with-data` |
| `/docs-new/databases/linked-data` | `/concepts/data-and-structure/transactions/linked-data` |
| `/docs-new/databases/refresh-and-sync-behavior` | `/concepts/data-and-structure/transactions/refresh-and-sync-behavior` |
| `/docs-new/databases/database-best-practices` | `/concepts/data-and-structure/transactions/transaction-best-practices` |
| `/support-docs/databases/what-is-a-database` (and twins) | same Concepts destinations (after or with existing support→docs-new retarget) |
| Optional hub | `/concepts/data-and-structure/transactions` for any Databases parent/index links |
| Deferred orphans | `/docs-new/databases/database-formulas`, `/docs-new/databases/filters-sorts-and-grouping` — redirect only after IA decision |

## Learnings for the next module

- RENAME modules with terminology flips need landing + child title/slug updates together; keep one Legacy alias note, not dual primary nouns.
- Strong Legacy orphans still need temporary `/docs-new/...` links even when the parent module migrates.
- Prefer product create/list labels over internal resource type names when they diverge.
- Placeholder asset folders may retain old pathnames; do not block migration on asset renames.

## Completeness

**Transactions mapped target set is safe to mark complete** for staged Concepts migration (8/8 target pages). Follow-ups that do **not** block this mark:

- IA decision on formulas + filters orphans
- Redirect cutover
- Screenshot refresh if chrome still shows older Database wording in places
