# Concepts migration rulebook

Reusable rules derived from the Dimensions pilot and the planning artifacts in `docs-migration/`. Follow this file for every future Concepts module migration.

**Related artifacts**

- `docs-migration/current-docs-inventory.md`
- `docs-migration/target-concepts-structure.md`
- `docs-migration/app-feature-inventory.md`
- `docs-migration/concepts-migration-map.md`
- `docs-migration/pilot-dimensions-report.md`

**Hard constraints (unless a later step explicitly lifts them)**

- App repo is read-only.
- Do not delete or edit Concepts Legacy (`docs-new/**`) or `support-docs/**` during module migration.
- Do not add redirects during staged migration (cutover is a separate step).
- Migrate only the module in scope.
- Change `docs.json` only enough to expose the new module under the Concepts tab.
- Do not invent product behavior. If the app does not confirm a detail, omit it or flag it in the module report.

---

## 1. Source priority

Use sources in this order of authority for **product behavior**. Use them differently for **IA** and **explanatory copy**.

| Priority | Source | Role |
|---:|---|---|
| 1 | Current app implementation (`oculon-app-client`, read-only) | Canonical for UI labels, entry points, flows, availability, and what customers can do |
| 2 | Concepts Legacy (`docs-new/**`) | Primary customer-facing explanations, examples, and screenshots to preserve or adapt |
| 3 | `support-docs/**` twins | Secondary. Prefer when they improve accessibility (Frame/alt) or contain unique accurate content; otherwise do not let shorter twins overwrite richer `docs-new` pages |
| 4 | Notion / `target-concepts-structure.md` | Canonical for placement, page titles, parent/child IA, and planned paths |
| 5 | App-internal specs/docs (`docs/*.md` in the app repo) | Optional depth for understanding. Never paste internal architecture, flags implementation, or engineer-only paths into customer MDX |

### Clarifications

- **Documented product behavior must match the current app for labels, entry points, and flows you choose to publish.** If Legacy copy conflicts with current UI labels or flows, rewrite the copy. Do not keep outdated chrome (“page panel”, old button names) for continuity.
- **Raw UI/code availability does not automatically mean the behavior should be documented.** See §4 Product-content boundary.
- **Useful customer-facing explanations from Legacy should be preserved.** Definitions, why-it-matters, when-to-use, examples, caution notes, and best practices stay when still true.
- **The Notion target defines placement/IA, not product behavior.** Paths, sidebar groups, and page titles come from the target structure and migration map. Do not invent features because the IA lists a page; if the page is `CREATE`, write only what the app supports.
- **Strong Legacy pages missing from the target IA are IA gaps, not silent drops.** See §3 Strong Legacy content omitted from target IA.
- **Unverified Legacy claims** (for example auto-generated placeholder names not visible in client create APIs) must be softened or removed until product confirms them. Record the gap in the module report.

### Practical read order per page

1. Migration-map row (action, sources, flags, open questions)
2. Target IA row (path, title, children)
3. Mapped `docs-new` page(s)
4. Matching `support-docs` twin (diff against docs-new)
5. App inventory row + targeted app UI/source checks for labels and flows
6. Internal specs only if behavior is still unclear

---

## 2. Migration actions

Every target page has exactly one action from `concepts-migration-map.md`. Execute as follows.

| Action | What to do | Legacy source (`docs-new` / `support-docs`) | New Concepts page |
|---|---|---|---|
| **KEEP** | Content is already accurate for Concepts; copy into the planned path with light path/nav wiring and link/image hygiene | Leave in place until cutover | New file under `concepts/**` |
| **MOVE** | Adapt Legacy content into the planned Concepts path; update terminology, links, and image markup as needed | Untouched | New file; preserve useful explanations |
| **RENAME** | Same as MOVE, plus apply the target title and/or plural/singular slug from the map | Untouched (old slug remains for redirects later) | New file at the **new** path only |
| **MERGE** | Combine multiple sources into one page, or split one Legacy page across multiple targets (for example Publishing + Exports from one shared Legacy page) | Untouched | One or more new files; document split/combine in the report |
| **REPLACE** | Keep the topic and planned path; rewrite substantially using app truth + salvageable Legacy | Untouched | New file; do not treat Legacy as authoritative structure |
| **CREATE** | No usable customer docs source; write from app inventory and verified UI only | N/A (may cite fragments in the report) | New file; stay minimal; no speculative depth |
| **REVIEW** | Do **not** publish customer content until terminology, IA, or release is decided | Untouched | Do not create (or leave unpublished/out of nav) until REVIEW clears |
| **ARCHIVE** | Cutover cleanup only: unpublish/remove Legacy after redirects exist | Eligible only after Concepts is canonical and redirects verified | Not an authoring action during staged migration |

### Must / must not for Legacy during staged migration

- **Must not** delete, rename, or edit Legacy files while creating Concepts pages.
- **Must not** remove Legacy pages from Concepts Legacy nav during a module pilot.
- **Must** leave existing `/support-docs → /docs-new` redirects alone until the cutover step.
- **Must** record planned redirect sources (`redirect: yes` in the map) in the module report for later cutover.

---

## 3. Page structure conventions

Based on the Dimensions pilot and target IA.

### Landing / overview page pattern

- When the target lists a parent feature page (for example `concepts/data-and-structure/dimensions`) **and** children, create a landing page even if Legacy only listed children.
- Landing page should:
  - Open with a short definition and where customers find the feature in product
  - Reuse one overview screenshot when available
  - Link to every child via Cards/columns (or equivalent Mintlify pattern already used in Concepts)
  - Avoid duplicating full child content

### Child pages

- Create a child page for each target child listed for that parent.
- Prefer the map’s planned path exactly.
- Typical set for a mature feature: overview (“What is…”) → create/edit → values/structure → interactions with related features → operations → best practices.

### Strong Legacy content omitted from target IA

When a high-quality Legacy page (`docs-new/**` or a unique `support-docs/**` page) exists but the target IA / migration map has **no** matching Concepts page:

1. **Do not silently drop it.** Record it in the module report as an **IA gap**.
2. **Do not automatically create** a new Concepts page just because the Legacy page is good.
3. **Temporarily allow links** from migrated Concepts pages to the Legacy URL (`/docs-new/...`) when readers still need that topic.
4. In the report, **recommend exactly one** next step:
   - **add to target IA** (preferred when the topic is core and widely linked)
   - **merge into an existing target page** (when the orphan is a facet of a child already planned)
   - **keep temporarily in Legacy** (when IA decision is pending but content must stay reachable)
   - **archive later** (only when the topic is obsolete after cutover; not a staged-migration action)

Current examples identified during Variables / Time / Formulas migration:

| Legacy page | Why it matters | Interim handling |
|---|---|---|
| `docs-new/time/last-actual-date` | Core cutoff for actual vs planned behavior; linked across Variables, Time, Formulas | Link Legacy; recommend **add to target IA** under Time |
| `docs-new/time/time-rollups` | Distinct from time aggregation; referenced throughout Time | Link Legacy; recommend **add to target IA** or **merge** into aggregation after product decision |
| `docs-new/formulas/conditional-logic` | Strong, widely linked formula topic not in Formulas target children | Link Legacy; recommend **add to target IA** or keep temporarily in Legacy |

Fold useful orphan facts into an existing REPLACE/MOVE page only when that improves the target page without pretending the orphan was migrated. Still list the orphan as an IA gap.

### Preferred page depth

- Keep modules shallow: `concepts/<sidebar-group>/<feature>/…` (about 3–4 path segments).
- Do not invent deeper nesting than the target structure.
- One idea per page. Do not merge unrelated children to “save nav.”

### Slug naming

- Use kebab-case matching the target planned path.
- Prefer plural feature folders: `dimensions`, `variables`, `models`.
- Procedural pages: verb-led slugs such as `create-and-edit-dimensions`, `using-dimensions-with-variables`.
- On RENAME, use the **target** slug, not the Legacy slug (example: Legacy `create-and-edit-dimension` → Concepts `create-and-edit-dimensions`).

### Singular vs plural

- Feature parents and folders: plural when the product treats them as a collection (**Dimensions**, **Models**).
- “What is a …” pages: singular noun in the title.
- UI actions may stay singular when the product button is singular (**Create Dimension**) even if the doc title is plural.

### Page titles

- Match target IA titles unless a REVIEW terminology decision changes them.
- Use sentence case.
- Set `description` in frontmatter; use `sidebarTitle` (1–3 words) when the full title is long.
- Bold UI chrome in body copy: **Library**, **Create Dimension**, **+ New Value**.

### Sidebar grouping

- Place pages under the target sidebar group (for example **Data and structure** → **Dimensions**).
- For staged migration, only add the groups needed for modules already migrated (plus Concepts Overview/`concepts/index`).
- Expand the active module group (`expanded: true`) during pilot; leave Concepts Legacy intact.
- Do not mass-rebuild the Concepts tab ahead of content.

---

## 4. Content merge rules

### Preserve from Legacy

- Accurate definitions and conceptual framing
- Still-valid workflows and examples
- Caution / impact notes (downstream formulas, views, boards)
- Best-practice guidance that remains true
- Screenshots that still match current product closely enough to teach

### Rewrite when

- UI labels, entry points, or navigation paths have changed
- Headings are not sentence case or conflict with project style (`AGENTS.md`)
- Images use bare `![](...)` without alt text (upgrade to `<Frame>` + descriptive `alt`)
- Copy exposes outdated chrome or unverified defaults
- Internal links must point at new Concepts paths

### Add app-derived behavior when

- The migration map’s “New app-derived coverage to add” calls for it
- The app inventory confirms a customer-visible entry point, label, or flow missing from Legacy
- You can cite a concrete UI string or route (for example Library **Dimensions**, **Add Dimension**)
- The behavior is allowed under the product-content boundary below

Do **not** add depth that Legacy never covered unless the map/action is REPLACE or CREATE and the app clearly ships the behavior **and** docs/product guidance allows publishing it.

### Product-content boundary

Raw UI or code availability does **not** automatically mean the behavior should be documented in Concepts.

- If app implementation exposes options, controls, or paths that **conflict with established documentation or product guidance** (for example `AGENTS.md`, migration map notes, or an explicit product decision), treat the item as **REVIEW**.
- Prefer **explicit product documentation decisions** over inferred behavior from UI/code alone.
- Until REVIEW clears, keep documenting the guided/supported surface only; mention the conflict in the module report rather than expanding customer docs to match every control in the client.

**Example:** Model settings UI may list **daily** and **weekly** granularity, while current docs intentionally document **monthly**, **quarterly**, and **yearly** only. Do not document daily/weekly from UI inference alone; leave as REVIEW against the established content boundary.

### Avoid duplicate explanations

- Landing pages summarize and link; children teach.
- Do not restate the full “what is” essay on every child page.
- Prefer a short Related section with links over copy-paste sections.

### Outdated screenshots / examples

- Reuse existing assets when they still communicate the concept.
- Flag visual QA in the module report when chrome looks stale but content remains useful.
- Replace screenshots only when they mislead (wrong labels, removed UI, wrong product area).
- Do not invent new example data that the product does not support.
- Prefer product-accurate examples already used in Legacy when still valid (`Region`, `Headcount`, and similar).

### Avoid implementation details

Never publish in customer Concepts pages:

- Dual codepaths (for example coreV2 vs legacy internals)
- Env var names as customer instructions (flags belong only as availability notes when required)
- API payloads, server routes, or storage schemas
- Feature-flag admin surfaces (`/settings/feature-flags`)
- Engineer task docs or migration TODOs from the app repo

Litmus test: if a customer using the product UI would never need the detail, omit it.

### Style (project)

- Second person, active voice, one idea per sentence
- Sentence case headings
- Bold UI elements
- No competitor wording
- Follow `AGENTS.md` terminology for time concepts (`Last actual date`, actual/planned formulas, relative time, rollups vs aggregation)

---

## 5. Terminology rules

1. **Current product UI terminology takes priority** for buttons, tabs, menus, and in-product nouns.
2. **Target IA titles** control page titles and nav labels unless the page is marked REVIEW for naming.
3. **Aliases / Legacy names** may appear once when helpful for readers coming from old docs (“sometimes called…”) if the product still recognizes the concept. Do not teach two competing primary names.
4. **Unresolved conflicts remain REVIEW.** Do not pick a winner in MDX unless migration artifacts already record a clear product-backed decision.

### Known conflicts (do not resolve here)

| Conflict | Evidence (from migration artifacts) | Guidance until decided |
|---|---|---|
| **Transactions vs Databases** | Library + Create menu say **Transactions**; routes/docs often say databases | Hold Databases parent naming as REVIEW; do not publish a conflicting rename |
| **Planning vs Plans vs Plan mode** | Admin **Planning**; AI **Plan mode**; no separate Plans product | Keep surfaces distinct in copy; do not collapse names |
| **History vs Activity vs Model History** | Model **History**; Project **Activity**; Artifact History | Use the product label for the surface you document; Model History remains a coverage gap |
| **Spaces vs Teamspaces / Private space** | Sidebar **Spaces**; settings **Teamspace** | Prefer the label shown on the surface being documented; umbrella term still open |
| Personal settings vs **My Account** | Settings section label | Prefer product **My Account** in body when describing that surface |
| Users & Groups vs split Users / Roles pages | Single settings entry vs split target pages | Follow target IA only after REVIEW if conflict blocks clarity |
| **FP&A** vs Models vs Apps | Switcher **FP&A** opens Library models | Mention FP&A as entry framing when documenting Models; do not treat it as an Apps shell |
| Integrations vs Connectors & MCP | Library Integrations; Settings Connectors & MCP | Treat as potentially separate topics until REVIEW |
| Last actual date vs actuals/forecast boundary | App + `AGENTS.md` prefer **Last actual date** | Prefer **Last actual date** in new copy; orphan Legacy boundary page remains a gap |

---

## 6. Images and assets

- **Reuse** valid existing images under `/images/...`. Do not copy binary assets into a second folder for Concepts.
- Prefer root-relative paths already used by Legacy (for example `/images/getting-started/fr-dimensions.png`).
- Upgrade markup to `<Frame caption="...">` + `<img src="..." alt="...">` when touching a page.
- Alt text must describe what the customer sees; captions may add context.
- **Replace** screenshots only when wrong or misleading; note the need in the module report if replacement is deferred.
- Do not commit SVG as page content images unless Mintlify project rules allow it for that asset type.
- Do not reference absolute docs-host URLs for internal images.

---

## 7. Internal links

- New Concepts pages link to **new Concepts paths** when those pages exist: `/concepts/...` (no `.mdx`, no relative `../`).
- Links to modules **not yet migrated** may temporarily point to Concepts Legacy (`/docs-new/...`) so readers still reach content.
- Links to **strong Legacy orphans omitted from target IA** (§3) may also temporarily point to Concepts Legacy. Do not invent Concepts URLs for those orphans.
- Do not leave links to paths that do not exist yet (future Concepts pages). Prefer Legacy URL or omit until that module migrates.
- Do not edit Legacy pages solely to retarget links during staged migration (avoids unrelated Legacy churn). Exception only if a later explicit cutover task requires it.
- **Redirect updates happen later during cutover.** Module reports should list planned redirect sources (`docs-new` + support twins + renamed slugs) but not apply them in the migration step.

---

## 8. Feature flags / unreleased features

Use `app-feature-inventory.md` and the migration map flag columns as evidence.

| Class | How to handle in Concepts |
|---|---|
| **Generally available** (safe list in migration map) | Document normally |
| **Flag-gated but publishable** (“document only if enabled”) | Only migrate when product asks; if published early, include a clear availability note and avoid implying every workspace has it |
| **Experimental** | Prefer hold; if documenting, label experimental and keep depth minimal |
| **Disabled by default / off in real environments** | Hold from public docs (example: Agent teams off everywhere) |
| **Internal-only** | Never document (feature-flag admin, thin stubs, engineer tools) |

### Current map guidance (summary)

- **Safe now:** Models, Variables, Dimensions, Time, Formulas, Scenarios, Views, Compare, Boards (except code block), Workspaces/Spaces sharing basics, Settings, AI Assistant core, Custom Agents (note discoverability), MCP/Connectors, Resources (careful with flagged sidebar items)
- **Only if enabled:** Projects/Tasks, Templates, Feed, Publishing, Exports, Artifacts, board code block
- **Hold:** Agent teams, deep Apps/v2 shells, internal flag admin, unconfirmed thin switcher stubs

Do not document flag names as customer setup steps. Availability notes should be plain language.

---

## 9. Validation checklist

For every migrated module, before calling the work complete:

1. **Files exist** at every planned `concepts/**` path for the module (including landing page).
2. **`docs.json` entries valid** — every new nav path resolves to an MDX file; only minimum Concepts nav was changed.
3. **Internal links valid** — every `/concepts/...` and temporary `/docs-new/...` link from new pages resolves.
4. **Referenced images exist** on disk at the root-relative path used.
5. **No unrelated Legacy changes** — `git status` clean for out-of-scope `docs-new/**` and `support-docs/**` (especially the module’s Legacy twin folders).
6. **No unrelated module MDX** created or edited.
7. **Mintlify validation checked** — run `mint validate` and `mint broken-links` (or `npx mint@latest ...`). New module paths must introduce no new errors. Pre-existing Legacy orphan errors may remain; call them out explicitly.
8. **Migration report created** at `docs-migration/pilot-<module>-report.md` (or `docs-migration/<module>-migration-report.md`) using the template below.
9. App repo unchanged.

---

## 10. Module migration report template

Copy into `docs-migration/<module>-migration-report.md` (or `pilot-<module>-report.md` for early modules):

```markdown
# <Module> migration report

Scope: <module only>. Legacy sources left untouched unless explicitly listed.
App repo: read-only. Redirects: not applied in this step.

## Pages created

| Target path | Migration action | Legacy sources used | App sources used |
|---|---|---|---|
| `concepts/...` | MOVE / RENAME / ... | `docs-new/...`, `support-docs/...` | UI labels, routes, components |

Also updated:
- `docs.json` (describe minimum Concepts nav change)
- `concepts/index.mdx` (only if needed)

## Content merge decisions

### Preserved
- ...

### Rewritten
- ...

### Added
- ...

### Omitted
- ...

## Terminology decisions

| Legacy / target wording | Current product UI | Choice |
|---|---|---|
| ... | ... | ... |

## Validation

| Check | Result |
|---|---|
| Files exist | Pass / Fail |
| docs.json paths valid | Pass / Fail |
| Internal links valid | Pass / Fail |
| Referenced images exist | Pass / Fail |
| Unrelated legacy unchanged | Pass / Fail |
| Mintlify validate | Pass / Fail (list pre-existing vs new) |
| Mintlify broken-links | Pass / Fail (list pre-existing vs new) |

## Unresolved questions
1. ...

## IA gaps (strong Legacy omitted from target)
| Legacy path | Recommendation (add / merge / keep in Legacy / archive later) | Temporary links used? |
|---|---|---|
| `docs-new/...` | ... | yes / no |

## Product-content boundary / REVIEW items
| UI or code signal | Established docs/product guidance | Handling |
|---|---|---|
| ... | ... | REVIEW / omit / document |

## Planned redirects (for later cutover)
| Source | Destination |
|---|---|
| `/docs-new/...` | `/concepts/...` |

## Learnings for the next module
- ...
```

---

## 11. Lessons from Dimensions pilot and Variables / Time / Formulas

**Repeat**

1. Prefer `docs-new` as the primary body; merge `support-docs` only for unique value (Frame/alt) or when it is richer and still accurate.
2. Create a parent landing page when the target IA has a parent + children, even if Legacy omitted the landing file.
3. Execute RENAME by writing only the new path; leave the old Legacy slug in place for future redirects.
4. Verify UI strings in the app before rewriting create/edit flows; drop unverified defaults.
5. Keep Concepts nav minimal: Overview + the migrating sidebar group/module only.
6. Leave Legacy content and redirects alone until cutover.
7. Treat “no new Mintlify errors on Concepts paths” as the quality gate; expect known Legacy orphan noise.
8. Write a module report with preserve/rewrite/add/omit and terminology tables.
9. Record strong Legacy orphans omitted from target IA as gaps; link Legacy temporarily; do not auto-create Concepts pages.
10. Respect product-content boundaries: do not document every UI option the client exposes when docs guidance is narrower.

**Avoid**

- Expanding into adjacent modules “while you are there”
- Publishing REVIEW naming conflicts (Databases/Transactions, Plan/Planning)
- Publishing flag-gated or hold-list features as if generally available
- Deleting or editing Legacy twins during staged migration
- Adding redirects early
- Documenting internal dual implementations or env flags as customer procedure
- Silently dropping high-quality Legacy topics that the target IA omitted
- Inferring publishable coverage from UI/code alone when it conflicts with `AGENTS.md` or other product docs decisions

**Pattern fit**

- Best fit next: Models, Scenarios, Views (MOVE-heavy, GA)
- Needs REVIEW first: Databases/Transactions, AI Plan vs Planning, some Sharing children, daily/weekly granularity docs policy
- Needs flag policy first: Projects, Templates, Feed, Artifacts, Publishing/Exports

---

## Migration execution checklist

Use this before marking any future module migration complete.

1. Confirm module scope from `concepts-migration-map.md` and migration order; refuse out-of-scope pages.
2. Confirm the module is allowed to publish now (GA / flag policy in §8). Clear any REVIEW blockers first.
3. Read target IA paths/titles and every mapped Legacy + support source; diff twins.
4. Scan nearby Legacy pages for **strong orphans omitted from target IA** (§3). Record each as an IA gap with one recommendation (add / merge / keep in Legacy / archive later). Do not auto-create Concepts pages for them.
5. Spot-check app UI labels and entry points for flows you will describe.
6. Apply the **product-content boundary** (§4): if UI/code exposes options that conflict with established docs/product guidance, mark REVIEW and do not expand customer docs from inference alone.
7. Create only `concepts/**` pages for this module (landing + children per target).
8. Apply the mapped action per page (KEEP/MOVE/RENAME/MERGE/REPLACE/CREATE); never ARCHIVE in this stage.
9. Preserve useful Legacy explanations; rewrite outdated UI; add only verified **and publishable** app behavior.
10. Reuse existing images; add Frame/alt; do not duplicate binaries.
11. Link to Concepts paths when present; otherwise temporary Legacy paths (including IA-gap orphans); introduce no broken links.
12. Update `docs.json` with the minimum Concepts nav for this module only; leave Concepts Legacy intact.
13. Do not modify Legacy MDX, support-docs twins, redirects, or app code.
14. Run validation checklist (§9): files, nav, links, images, git cleanliness, Mintlify validate/broken-links.
15. Write the module migration report (§10), including planned redirects, open questions, **IA gaps**, and **product-content boundary / REVIEW** items.
16. Stop. Do not start the next module unless explicitly requested.
