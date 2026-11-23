# Concepts IA and terminology decisions

Decision-making only. Derived from migration artifacts, module reports, and current app UI evidence. No MDX, `docs.json`, or app changes in this step.

**Sources consulted**

- `docs-migration/target-concepts-structure.md`
- `docs-migration/concepts-migration-map.md`
- `docs-migration/app-feature-inventory.md`
- `docs-migration/migration-rules.md`
- `docs-migration/migration-models-report.md`
- `docs-migration/migration-scenarios-report.md`
- App (read-only): Library nav, Create menu, model History, scenario controls, board slash menu, Compare docs

---

## 1. Scenario Compare

### Recommendation evaluated

- Scenario documentation explains scenario-specific behavior.
- Detailed comparison functionality belongs under **Analysis and reporting → Compare**.
- Scenario pages link to Compare rather than maintaining a duplicate **Compare scenarios** page.

### Classification: **ACCEPT recommendation**

### Why

- The target IA already has a full Compare module: `concepts/analysis-and-reporting/compare` with **What is a compare**, **Time compare**, and **Scenario compare**.
- It also still lists **Compare scenarios** under Scenarios, which duplicates the Analysis Compare surface.
- App inventory and Compare Legacy (`docs-new/compare/scenario-compare`) describe one product Compare workflow (scenario vs scenario columns/variance in models and boards), not a second scenario-only compare product.
- The Scenarios migration map already marked **Compare scenarios** as REVIEW for this overlap; Concepts did not publish that page.
- Keeping scenario “why/when to compare” blurbs on Scenarios pages, with deep links to Analysis → Compare → Scenario compare, avoids two competing homes for the same UI.

### Implications

- Remove **Compare scenarios** from the Scenarios target children.
- Keep / migrate **Scenario compare** under Analysis → Compare.
- Scenarios landing and best practices should link to `/concepts/analysis-and-reporting/compare/scenario-compare` once Compare is migrated (Legacy path until then).

---

## 2. Model History

### Classification: **add as a Models child page**

Prefer Models because the behavior is model-scoped.

| Field | Finding |
|---|---|
| Current app terminology | Toolbar **History** (`aria-label` / tooltip). Preview banner: **Previewing version …**, **Restore**. Internal: checkpoints / Model History panel |
| App source paths | `app/(app)/model/components/history/**`, `ModelDetailsHeader` History toggle, `server/modelHistory`, `hooks/useModelHistory` |
| Legacy / support docs | `docs-new/models/versioning.mdx` (checkpoint framing, no dedicated “History” page). No solid support-docs twin for History UI. Concepts Legacy nav still points at missing `cloning-and-versioning` / `model-organization` |
| Recommended target page | Title: **Model History**; path: `concepts/modeling/models/model-history`; `sidebarTitle`: History |
| Add to target IA? | **Yes** |

### Notes

- Do **not** invent a shared cross-product “History” Concepts parent. Project **Activity** and Artifact History remain separate surfaces.
- Fold useful Legacy **Versioning** explanations into Model History where they match checkpoint/preview/restore. Retire standalone Models **Versioning** as a separate Concepts child once History exists (see §3).

---

## 3. Model versioning / cloning / organization

| Topic | Implemented? | User-facing terminology | Existing docs | Recommended placement | Action |
|---|---|---|---|---|---|
| **Model History / versioning** | **Yes** — History sidebar, checkpoint preview, restore | **History**; “version” in preview/restore copy | `docs-new/models/versioning`; thin support cloning/versioning page | Models → **Model History** | **add** History; **merge** Legacy versioning content into it; **archive** standalone Versioning Concepts target if any |
| **Model cloning** | **No dedicated “Clone model” UX found.** Library resource menu exposes **Copy to** (destination copy). Scenario **Duplicate** is scenario-scoped, not model clone | **Copy to** (Library), not Clone | `support-docs/models/cloning-and-versioning` (and broken Legacy nav to missing `docs-new` path) | Not a Models Concepts child. Optional mention under Library / Sharing later | **hold** / later **archive** cloning docs; do not create a Clone Concepts page |
| **Model organization** | Partial — Library Spaces, folders, Recents/Favorites/Shared, naming | Spaces / Library organization, not a Models settings page | `support-docs/models/model-organization` (broken Legacy nav twin) | Workspace / Resources / Library (future), not Models children | **hold** for Library/Workspace IA; **archive** from Models track |

### Rule applied

Do not create Concepts pages for unsupported or misnamed functionality. **Copy to** is not the same as Legacy “clone a model for a new structure”; document Copy to only when Library/destination docs are in scope.

---

## 4. Scenario governance and access

### Recommendation: **dedicated child page**

Controls are substantial enough for their own page:

- **Allow Changes** (lock / unlock; Default Scenario special-cased)
- **Allow Merging** (`allow_merge`)
- Scenario **Share** / visibility expectations
- Delete safeguards (Default Scenario cannot be deleted)
- Distinct from create/manage and from override mechanics

### Placement

- Title: **Scenario governance and access**
- Path: `concepts/modeling/scenarios/scenario-governance-and-access`
- Source: MOVE from `docs-new/scenarios/scenario-governance-and-access` (rewrite Main → Default Scenario; drop speculative future copy)

### Related (also recommend adding, separate from this decision)

- **Merge scenarios** (`docs-new/scenarios/merge-scenarios`) should become a Scenarios child as well. Governance can summarize and link; Merge should not stay Legacy-only.

Including all of governance inside Create and manage would overcrowd that page and bury lock/merge/visibility rules.

---

## 5. Databases vs Transactions

### Choice: **A. Transactions everywhere publicly; old Database terminology only as alias / redirect**

### Evidence

| Surface | Label |
|---|---|
| Library tab | **Transactions** |
| Create menu | **Create Transactions** |
| Board slash insert | **Transactions** |
| Internal routes / types | `/library/databases`, `/databases/[id]`, resource type `database` |
| Legacy docs | Almost entirely “Databases” / `docs-new/databases/**` |
| Target IA today | Parent **Databases** |

### Why not B, C, or a hybrid object model

- **B (Databases everywhere)** contradicts the primary customer UI and Create/Library labels.
- **C (Transactions module / Database object)** invents a dual conceptual model the product does not teach users. Internal “database” is an implementation/route name, not a second customer noun.
- Public docs should match what users click. Routes need not appear in Concepts prose.

### Evaluation against criteria

| Criterion | Assessment for A |
|---|---|
| What users see | Matches Library, Create, Boards |
| Conceptual clarity | One public noun for the source-data grid |
| Migration impact | High rename cost (paths, titles, links, glossary) but one-time and map already flagged REVIEW |
| Search / discoverability | Keep “database” as search alias / glossary cross-reference for Legacy readers |
| Existing links | Redirect `/docs-new/databases/*` and support twins → `/concepts/data-and-structure/transactions/*` at cutover |
| Future consistency | Aligns with product; reduces ongoing doc/UI drift |

### Public docs recommendations

| Item | Decision |
|---|---|
| Target sidebar label | **Transactions** |
| Landing page title | **Transactions** |
| Overview child title | **What is a transaction** (or **What are Transactions** if plural voice preferred; recommend singular “What is a transaction” for consistency with Variables/Dimensions) |
| Preferred Concepts slug root | `concepts/data-and-structure/transactions` |
| Child slug pattern | Replace `database-*` with `transaction-*` or neutral verbs where clearer (`working-with-data`, `linked-data`, `refresh-and-sync-behavior` can keep verb slugs) |
| Old docs `/docs-new/databases/*` URLs | Redirect to new Concepts Transactions paths at cutover |
| Product `/databases` app routes | Do not present as customer terminology; optional advanced note only if needed |
| Should “database” appear in copy? | Yes, sparingly: glossary alias and one-line “older docs called these Databases” where helpful. Not the primary heading/noun |

### Board block

- Target child previously framed as “Transactions block” is already aligned; keep **Transactions** naming when Boards migrate.

---

## 6. Final decisions table

| Topic | Decision | Target location | Migration action | Blocking? | Notes |
|---|---|---|---|---|---|
| Scenario Compare | **ACCEPT** — deep compare under Analysis → Compare; Scenarios link out | Remove Scenarios → Compare scenarios; keep Analysis → Compare → Scenario compare | UPDATE map/IA; no Scenarios Concepts page | **Yes** before Scenarios polish / Compare migration | Avoid duplicate homes |
| Model History | **Add** Models child | `concepts/modeling/models/model-history` | CREATE (app + fold Legacy versioning) | **Yes** before claiming Models complete | UI label History |
| Model versioning (Legacy page) | **Merge into Model History** | Same as History | MERGE then ARCHIVE Legacy Versioning as standalone Concepts target | No (with History) | |
| Model cloning | **Hold / do not document as Clone** | None under Models | HOLD; archive cloning Legacy later | No | Use **Copy to** only when Library docs exist |
| Model organization | **Hold** outside Models | Future Library / Workspace / Resources | HOLD | No | Broken Legacy nav orphan |
| Scenario governance | **Dedicated Scenarios child** | `concepts/modeling/scenarios/scenario-governance-and-access` | MOVE from Legacy | **Yes** before Scenarios cutover completeness | Allow Changes / Allow Merging / visibility |
| Merge scenarios | **Add** Scenarios child (companion) | `concepts/modeling/scenarios/merge-scenarios` | MOVE from Legacy | Recommended with governance | Directional Merge Changes |
| Databases vs Transactions | **A — Transactions publicly** | Rename Databases → Transactions under Data and structure | RENAME all Databases map/IA rows; UPDATE glossary | **Yes** before Databases/Transactions migration | Alias database for search/Legacy |

---

## Changes required in target IA

Exact updates for `target-concepts-structure.md` (do not apply in this step):

### Modeling → Models

- **Add** child: **Model History** → `concepts/modeling/models/model-history`
- **Do not add** Cloning and versioning or Model organization as Models children
- If Versioning appears as a planned Models child anywhere, **remove** it in favor of Model History

### Modeling → Scenarios

- **Remove** child: **Compare scenarios** (`concepts/modeling/scenarios/compare-scenarios`)
- **Add** child: **Scenario governance and access** → `concepts/modeling/scenarios/scenario-governance-and-access`
- **Add** child: **Merge scenarios** → `concepts/modeling/scenarios/merge-scenarios`
- Keep Analysis → Compare → **Scenario compare** unchanged
- Note on Scenarios parent: link to Analysis Compare for comparison workflows

### Data and structure → Databases (rename)

- **Rename** parent **Databases** → **Transactions**
- **Rename** path root `concepts/data-and-structure/databases` → `concepts/data-and-structure/transactions`
- **Rename** child titles from Database… → Transaction… where the noun is the feature (What is a transaction, Transaction types, Transaction structure, Transaction best practices, etc.)
- Keep operational children where the title is verb-led if still accurate (Working with data, Linked data, Refresh and sync behavior)
- Update notes: Library **Transactions**, **Create Transactions**, routes remain `/databases` internally

### Analysis → Boards (when reached)

- Confirm Transactions block naming (already intended); no Databases block label

### Glossary / Core concepts (when reached)

- Add Transactions primary term; Database as alias

---

## Changes required in migration map

Exact updates for `concepts-migration-map.md` (do not apply in this step):

1. **Scenarios → Compare scenarios**  
   - Change from REVIEW/publish candidate to **ARCHIVE from Scenarios target** / redirect intent toward Analysis → Scenario compare.  
   - Reason: accepted dedupe decision.

2. **Analysis → Scenario compare**  
   - Confirm MOVE when Compare module migrates; note Scenarios pages should cross-link here.

3. **Models**  
   - **Add** row: Model History → `concepts/modeling/models/model-history` → **CREATE** (sources: app History UI; fold `docs-new/models/versioning`).  
   - Open question “Include cloning orphans?” → resolve as **no Concepts clone page**; cloning support page → HOLD/ARCHIVE.  
   - Flag Model History gap as closed once page is mapped.

4. **Scenarios**  
   - **Add** MOVE rows for `scenario-governance-and-access` and `merge-scenarios`.  
   - Sync-behavior notes: inheritance documented; auto-sync toggle remains non-documented unless product ships a control.

5. **Databases parent and all children**  
   - Clear REVIEW naming block.  
   - Set action **RENAME** (Databases → Transactions) for parent + noun-based children.  
   - Update planned paths to `concepts/data-and-structure/transactions/**`.  
   - Update Preserve/Add columns to use Transactions UI labels.  
   - Redirect column: yes from `/docs-new/databases/*` and support twins.

6. **Global terminology table**  
   - Mark Transactions vs Databases as **decided: public term Transactions**.  
   - Mark Scenario Compare overlap as **decided: Analysis Compare owns deep compare**.  
   - Mark Model History as **decided: Models child**.

7. **Missing target coverage table**  
   - Update Model History recommendation from “add” wish to mapped child.  
   - Update Transactions/Databases row to decided rename.

8. **Migration order**  
   - Unblock Databases/Transactions migration after map/IA rename applied.  
   - Optional: insert Scenarios governance + merge pages as a small follow-up before Views/Compare.  
   - Compare module should absorb scenario comparison; no Scenarios compare page.

---

## Still open (out of this decision set)

Not resolved here; remain tracked elsewhere:

- Last actual date / Time rollups as official Time children
- Conditional logic as Formulas child
- Daily/weekly granularity docs policy
- Planning vs Plan mode naming
- Spaces vs Teamspaces umbrella term

---

_End of IA decisions. Apply target IA + migration map updates only when explicitly requested; then resume content migration._
