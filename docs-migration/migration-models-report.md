# Models migration report

Scope: Models module only. Legacy `docs-new/models/**` and `support-docs/models/**` left untouched. App repo read-only. Redirects not applied.

## Pages created

| Target path | Migration action | Legacy sources used | support-docs sources used | App sources used |
|---|---|---|---|---|
| `concepts/modeling/models` | MOVE (landing) | `docs-new/models/what-is-a-model` | twin (shorter; not primary) | Library / **FP&A**; **Create Model** |
| `concepts/modeling/models/what-is-a-model` | MOVE | Prefer richer `docs-new/models/what-is-a-model` | twin for comparison | CreateEntityMenu **Create Model**; Library models |
| `concepts/modeling/models/model-structure` | MOVE | `docs-new/models/model-structure` | twin | Model sections / variables grid |
| `concepts/modeling/models/model-settings` | MOVE | `docs-new/models/model-settings` | twin | `ModelSettings`; `time_params`; **Last actual date**; **History** |
| `concepts/modeling/models/linked-models` | MOVE | `docs-new/models/linked-models` | twin | Linked items panel |
| `concepts/modeling/models/model-best-practices` | MOVE | `docs-new/models/model-best-practices` | twin | — |

Also updated: `docs.json` Concepts → Modeling → Models; `concepts/index.mdx`.

**Not created as Concepts children (IA gaps):** Model History, `docs-new/models/versioning`, support-only `cloning-and-versioning` / `model-organization`.

## Content merge decisions

### Preserved

- Model definition, contents, structure pattern, settings hub, linked-model guidance, best practices
- Screenshots (`fr-model-details`, `fr-model-breakdown`, `fr-last-actual`, `fr-linked-items`)
- Links to Versioning Legacy where Legacy Models pages already pointed there

### Rewritten

- Frame/alt image markup
- Cross-links to migrated Variables / Time / Formulas / Scenarios Concepts paths
- Database phrasing → **Transactions** with Legacy Databases path retained
- Entry framing: Library / **FP&A** / **Create Model**

### Added

- Landing Cards
- Model settings note pointing to **History** and scenarios (History remains an IA gap)
- Related links on landing to Versioning Legacy orphan

### Omitted

- Auto-creating Concepts pages for Versioning, Cloning and versioning, Model organization, Model History
- Internal FORMULA/PLUGIN architecture docs
- Documenting daily/weekly granularity (content boundary; see Time report)

## Terminology decisions

| Legacy / target | Product UI | Choice |
|---|---|---|
| Model / models | Library Models; **Create Model** | Keep |
| FP&A | App switcher **FP&A** | Mention as entry framing |
| database | Library **Transactions** | Prefer Transactions; Legacy Databases link temporary |
| Last actual date | Model settings **Last actual date** | Keep |
| History / versioning | Model **History**; Legacy Versioning page | Mention History; Versioning stays Legacy IA gap |
| Cloning and versioning | — | IA gap (support-docs only; Legacy nav orphan) |

## IA gaps (strong Legacy omitted from target)

| Legacy path | Recommendation | Temporary links used? |
|---|---|---|
| `docs-new/models/versioning` | **add to target IA** under Models (or fold with Model History decision) | yes |
| `support-docs/models/cloning-and-versioning` | **keep temporarily in Legacy** / fix broken Concepts Legacy nav path; decide clone vs History vs Versioning | no (broken in Legacy nav already) |
| `support-docs/models/model-organization` | **merge** into Models best practices / Library later, or keep Legacy | no (broken in Legacy nav already) |
| Model **History** (app-implemented; no dedicated Legacy Concepts page) | **add to target IA** under Models | mentioned in settings; no dedicated page |

## Product-content boundary / REVIEW items

| UI or code signal | Established guidance | Handling |
|---|---|---|
| Daily/weekly granularity in model settings | Docs document monthly/quarterly/yearly | Omit; REVIEW (Time module) |
| Model History checkpoints | Missing from target IA | Mention only; recommend IA add |

## Validation

| Check | Result |
|---|---|
| Files exist | Pass (6) |
| docs.json paths valid | Pass |
| Internal links valid | Pass |
| Referenced images exist | Pass |
| Unrelated legacy unchanged | Pass |
| Mintlify validate | Same 5 pre-existing Legacy orphans only (includes `docs-new/models/cloning-and-versioning` and `model-organization` missing files) |
| Mintlify broken-links | Same 15 pre-existing; none in Concepts Models |

## Unresolved questions

1. Should Model **History** and Legacy **Versioning** be one Concepts child or two?
2. Is cloning still a first-class customer workflow distinct from scenarios + History?
3. When Databases/Transactions naming is decided, retarget the Transactions Legacy link.

## Planned redirects (later cutover)

| Source | Destination |
|---|---|
| `/docs-new/models/what-is-a-model` | `/concepts/modeling/models/what-is-a-model` |
| `/docs-new/models/model-structure` | `/concepts/modeling/models/model-structure` |
| `/docs-new/models/model-settings` | `/concepts/modeling/models/model-settings` |
| `/docs-new/models/linked-models` | `/concepts/modeling/models/linked-models` |
| `/docs-new/models/model-best-practices` | `/concepts/modeling/models/model-best-practices` |
| `/docs-new/models/versioning` | TBD if added to Concepts |

## Learnings

- Prefer docs-new over shorter support twins for Models.
- Strong orphans (Versioning / History / cloning) need IA decisions before more MOVE pages.
