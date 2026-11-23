# Time migration report

Scope: Time module only (target children). Legacy `docs-new/time/**` and `support-docs/time/**` left untouched. App repo read-only. Redirects not applied.

## Pages created

| Target path | Migration action | Legacy sources used | App sources used |
|---|---|---|---|
| `concepts/data-and-structure/time` | MOVE (landing) | `docs-new/time/time-in-oculon` + target children | Model settings time controls; Last actual date |
| `concepts/data-and-structure/time/time-in-oculon` | MOVE | Prefer richer `docs-new/time/time-in-oculon` over short support twin | `ModelSettings`; `time_params` |
| `concepts/data-and-structure/time/time-granularity` | MOVE | `docs-new/time/time-granularity` | Granularity options in model settings |
| `concepts/data-and-structure/time/relative-time` | MOVE | `docs-new/time/relative-time` | Relative time helpers; formula context |
| `concepts/data-and-structure/time/time-aggregation` | MOVE | `docs-new/time/time-aggregation` | Summary review patterns |
| `concepts/data-and-structure/time/time-best-practices` | MOVE | `docs-new/time/time-best-practices` | Close workflow around Last actual date |

Also updated: `docs.json` Concepts → Data and structure → Time; `concepts/index.mdx`.

**Not created (target omission / open IA):** dedicated Concepts pages for `last-actual-date` or `time-rollups`, even though strong Legacy pages exist. Temporary links point to Concepts Legacy.

## Content merge decisions

### Preserved

- Full docs-new Time conceptual set (settings, granularity, relative time, aggregation, best practices)
- Rollups vs aggregation distinction
- Monthly / quarterly / yearly guidance
- Close checklist and failure modes
- Screenshots (`model-settings.png`, `fr-relative-time.png`)

### Rewritten

- Image markup → Frame/alt where images present
- Internal links to other migrated Time/Variables/Formulas Concepts paths
- Links to Last actual date and Time rollups kept on Legacy paths
- Granularity intro wording lightly tightened (“supported … for planning docs”)

### Added

- Landing Cards + explicit Last actual date callout
- Related links to Variable behavior and Legacy orphans

### Omitted

- Creating Concepts children for Last actual date / Time rollups (not in target list; flagged)
- Documenting **daily** / **weekly** granularity even though model settings UI lists them — follows `AGENTS.md` content boundary (monthly/quarterly/yearly only) and migration-map partial flag note
- `NEXT_PUBLIC_MODEL_TIME_GRANULARITY_ENABLED` customer instructions
- FISCAL_ROLLUP internal QA detail

## Terminology decisions

| Legacy / target | Product UI | Choice |
|---|---|---|
| Last actual date | Model settings **Last actual date** | Canonical (`AGENTS.md`) |
| Actual formula / planned formula | Actual / planned formula | Keep |
| Relative time | Relative time helpers / patterns | Keep |
| Time aggregation vs time rollups | Aggregation vs rollup concepts | Keep distinction; rollups page remains Legacy |
| Planning horizon / fiscal year | Model time params / admin Planning | Describe model settings; do not collapse with AI Plan mode |
| Monthly / quarterly / yearly | Granularity control (also shows daily/weekly in UI) | Document only monthly/quarterly/yearly per docs policy |

## Validation

| Check | Result |
|---|---|
| Files exist | Pass (6 pages) |
| docs.json paths valid | Pass |
| Internal links valid | Pass (orphans → Legacy) |
| Referenced images exist | Pass |
| Unrelated legacy unchanged | Pass |
| Mintlify validate | Pre-existing 5 Legacy orphans only |
| Mintlify broken-links | Pre-existing only; none in Concepts Time |

## Unresolved questions

1. Add **Last actual date** as an official Concepts Time child? Strongly recommended; currently Legacy-linked everywhere.
2. Add **Time rollups** as Concepts child, or fold permanently into aggregation?
3. Confirm whether daily/weekly granularity is GA enough to document later (currently excluded by project docs policy).
4. Admin **Planning** defaults vs per-model time settings: how much cross-linking belongs here vs Settings module?

## Planned redirects (later cutover)

| Source | Destination |
|---|---|
| `/docs-new/time/time-in-oculon` (and twins) | `/concepts/data-and-structure/time/time-in-oculon` |
| `/docs-new/time/time-granularity` | `/concepts/data-and-structure/time/time-granularity` |
| `/docs-new/time/relative-time` | `/concepts/data-and-structure/time/relative-time` |
| `/docs-new/time/time-aggregation` | `/concepts/data-and-structure/time/time-aggregation` |
| `/docs-new/time/time-best-practices` | `/concepts/data-and-structure/time/time-best-practices` |
| `/docs-new/time/last-actual-date` | TBD Concepts path if IA adds child |
| `/docs-new/time/time-rollups` | TBD |

## Learnings

- Prefer richer docs-new Time pages over short support twins.
- Target IA gaps (Last actual date, rollups) force temporary Legacy links; flag them rather than inventing pages outside the map.
