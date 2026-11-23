# Scenarios migration report

Scope: Scenarios module only. Legacy `docs-new/scenarios/**` and `support-docs/scenarios/**` left untouched. App repo read-only. Redirects not applied.

## Pages created

| Target path | Migration action | Legacy sources used | support-docs sources used | App sources used |
|---|---|---|---|---|
| `concepts/modeling/scenarios` | MOVE (landing) | overview from what-is-a-scenario | twin | Scenario switcher; **Default Scenario** |
| `concepts/modeling/scenarios/what-is-a-scenario` | MOVE | Prefer richer docs-new | twin | `is_default`; scenario branching |
| `concepts/modeling/scenarios/create-and-manage-scenarios` | MOVE | Prefer docs-new | twin | **New Scenario**; switcher; lock/share |
| `concepts/modeling/scenarios/scenario-sync-behavior` | REPLACE (within mapped MOVE topic) | docs-new sync page (heavily adapted) | twin | Inheritance via overrides; no `auto_sync` field on `Scenario` |
| `concepts/modeling/scenarios/scenario-overrides` | MOVE | Prefer docs-new | twin | Override + **Revert to original**; locked scenarios |
| `concepts/modeling/scenarios/versioning-and-snapshots` | MOVE | Prefer docs-new (speculative section removed) | twin | Lifecycle framing only |
| `concepts/modeling/scenarios/scenario-best-practices` | MOVE | Prefer docs-new | twin | **Allow Changes**; **Merge Changes** |

Also updated: `docs.json` Concepts → Modeling → Scenarios; `concepts/index.mdx`.

### REVIEW not published as Concepts page

| Target map row | Action | Handling |
|---|---|---|
| Compare scenarios | **REVIEW** (overlap with Analysis Compare) | **No Concepts page created.** Temporary Legacy link to `/docs-new/scenarios/compare-scenarios`. Manual review required before publishing under Scenarios vs Compare. |

## Content merge decisions

### Preserved

- Branching mental model, create/manage workflow, override intent, best practices
- Real screenshots (`scenario.png`, `fr-scenario.png`)
- Links to Merge / Governance Legacy orphans

### Rewritten

- **Main Scenario** → **Default Scenario** (product UI / `is_default`)
- Create control → **New Scenario**
- Locking → **Allow Changes** off
- Reset override → include **Revert to original**
- Sync page rewritten around verified inheritance/overrides (not unverified auto-sync toggle)
- Removed speculative “what may come next” from versioning page
- Placeholder SVGs replaced with `<Note>` (screenshot pending)
- Frame/alt for real PNGs
- Cross-links to Models Concepts paths

### Added

- Landing Cards + alias note (Main Scenario → Default Scenario)
- Related Legacy links for Merge, Governance, Compare (REVIEW)

### Omitted

- Concepts page for **Compare scenarios** (REVIEW)
- Auto-creating Concepts pages for **Merge scenarios** and **Scenario governance and access** (IA gaps; strong Legacy)
- Documenting an **auto-sync from main** ON/OFF control (not present on `Scenario` type / UI labels found)
- Internal scenario-cache implementation docs

## Terminology decisions

| Legacy / target | Product UI | Choice |
|---|---|---|
| Main Scenario | **Default Scenario** | Prefer Default Scenario; mention Main as older alias once |
| New scenario / create | **New Scenario** | Prefer product label |
| Allow Changes / locked | **Allow Changes** (`is_locked`) | Prefer product label |
| Allow Merging | **Allow Merging** (`allow_merge`) | Prefer product label |
| Merge Changes | **Merge Changes** | Prefer product label |
| Reset override | **Revert to original** / revert override | Prefer verified revert affordance |
| auto-sync from main | (no matching UI field found) | Do not document as toggle; describe inheritance instead; REVIEW |
| Compare scenarios | Compare surfaces + Legacy page | Hold Concepts publish pending REVIEW vs Analysis Compare |

## IA gaps (strong Legacy omitted from target)

| Legacy path | Recommendation | Temporary links used? |
|---|---|---|
| `docs-new/scenarios/merge-scenarios` | **add to target IA** under Scenarios | yes |
| `docs-new/scenarios/scenario-governance-and-access` | **add to target IA** under Scenarios | yes |
| `docs-new/scenarios/compare-scenarios` | **REVIEW** vs Analysis → Compare; add under one place only after decision | yes (Legacy only; not Concepts) |

## Product-content boundary / REVIEW items

| UI or code signal | Established guidance / evidence | Handling |
|---|---|---|
| Legacy “auto-sync from main” ON/OFF | No `auto_sync` on `Scenario`; UI shows lock/merge/share | REPLACE sync page; do not document toggle |
| Compare scenarios target page | Map marks REVIEW vs Analysis Compare | Do not create Concepts page yet |
| Speculative approval-flow future copy | Product-content boundary | Removed from versioning page |

## Validation

| Check | Result |
|---|---|
| Files exist | Pass (7 Concepts pages; Compare intentionally omitted) |
| docs.json paths valid | Pass (Compare not listed) |
| Internal links valid | Pass |
| Referenced images exist | Pass |
| Unrelated legacy unchanged | Pass |
| Mintlify validate | Pre-existing 5 Legacy orphans only |
| Mintlify broken-links | Pre-existing 15 only; none in Concepts Scenarios |

## Unresolved questions

1. Confirm **Default Scenario** as the permanent customer term (retire Main Scenario everywhere).
2. Resolve **Compare scenarios** placement: Scenarios child vs Analysis Compare (or both with clear split).
3. Promote Merge + Governance into target IA before cutover (currently Legacy-linked).
4. Is there any customer-facing auto-sync control planned, or should inheritance-only docs remain?

## Planned redirects (later cutover)

| Source | Destination |
|---|---|
| `/docs-new/scenarios/what-is-a-scenario` | `/concepts/modeling/scenarios/what-is-a-scenario` |
| `/docs-new/scenarios/create-and-manage-scenarios` | `/concepts/modeling/scenarios/create-and-manage-scenarios` |
| `/docs-new/scenarios/scenario-sync-behavior` | `/concepts/modeling/scenarios/scenario-sync-behavior` |
| `/docs-new/scenarios/scenario-overrides` | `/concepts/modeling/scenarios/scenario-overrides` |
| `/docs-new/scenarios/versioning-and-snapshots` | `/concepts/modeling/scenarios/versioning-and-snapshots` |
| `/docs-new/scenarios/scenario-best-practices` | `/concepts/modeling/scenarios/scenario-best-practices` |
| `/docs-new/scenarios/compare-scenarios` | TBD after REVIEW |
| `/docs-new/scenarios/merge-scenarios` | TBD if added |
| `/docs-new/scenarios/scenario-governance-and-access` | TBD if added |

## Learnings

- Scenario docs required terminology correction (Main → Default) and a product-content rewrite for sync.
- REVIEW rows must stay out of Concepts nav even when Legacy content is strong.

## Cutover blocker completion

Batch A (2026-11-23): Scenario governance and access + Merge scenarios.

### Pages added/updated

| Path | Action |
|---|---|
| `concepts/modeling/scenarios/scenario-governance-and-access` | MOVE (new Concepts page) |
| `concepts/modeling/scenarios/merge-scenarios` | MOVE (new Concepts page) |
| `concepts/modeling/scenarios.mdx` | Updated Cards + Related links |
| Sibling Scenarios Concepts pages | Retargeted governance/merge links to Concepts; Compare → Analysis Scenario compare |
| `docs.json` | Added both pages under Modeling → Scenarios |

Legacy `docs-new/scenarios/**` untouched. No redirects yet.

### Behavior confirmed (app)

| Topic | Evidence |
|---|---|
| **Allow Changes** | Manage Scenario switch; Full access; non-default only; locks editing (`is_locked`) |
| **Allow Merging** | Manage Scenario switch; edit access; non-default; disabled when locked; gates **Merge changes** |
| **Share** | Full access; non-default only; Default hides Share |
| **Copy Link** | Available including Default Scenario |
| **Delete** | Full access; non-default; blocked when locked; Default cannot delete |
| **Merge Changes** | User-facing Manage Scenario → **Merge changes** → modal **Merge Changes to scenario** |
| Merge destination | Current UI filters destinations to **Default Scenario** only |
| Merge source | Non-default with edit + Allow Merging on |

### Content omitted

- Legacy “Who can view” label (product uses **Share**)
- Speculative approval / reviewed state machine (“what comes next” from Legacy)
- Free-form merge to arbitrary non-default destinations (not in current UI)
- Internal merge API / cache implementation details
- Duplicating global roles matrix (linked out instead)

### Unresolved limitations

- Merge destination is **Default Scenario only** until product expands the dialog — documented as a limitation, not REVIEW of the page itself
- Compare scenarios Legacy page remains REVIEW for archive/redirect only; Concepts uses Analysis → Scenario compare
- No formal “approved” scenario status in product

### Validation result

| Check | Result |
|---|---|
| New files exist | Pass (2) |
| docs.json paths | Pass (9 Scenarios children including governance + merge) |
| Internal Concepts links from Scenarios | No remaining `/docs-new/scenarios/*` links |
| Images | No new image refs (placeholders omitted) |
| Legacy untouched | Pass |
| Mintlify broken-links | **10** pre-existing (Legacy/essentials/support); **0** under Concepts Scenarios |
| Mintlify validate | **5** pre-existing Legacy missing-nav warnings; **0** new Concepts errors |

### Cutover status for these blockers

| Blocker | Status |
|---|---|
| Scenario governance and access | **Resolved** (published Concepts) |
| Merge scenarios | **Resolved** (published Concepts; destination limitation noted) |
| Either remains REVIEW? | **No** for these two pages. Compare scenarios Legacy redirect target remains a separate cutover item (Analysis Scenario compare already exists). |
| Scenarios module cutover-ready? | **Yes for mapped Scenarios Concepts content**, pending overall cutover redirects. Not blocked on governance/merge anymore. |
