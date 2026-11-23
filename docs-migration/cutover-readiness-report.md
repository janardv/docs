# Cutover readiness report

Batch F structural cutover prep. Legacy MDX files remain on disk. App repo untouched. No production publish in this step.

## Redirect summary

Source map: `docs-migration/redirect-map.md`

| Category | Count |
|---|---:|
| DIRECT (docs-new → Concepts) | 81 |
| RENAMED | 18 |
| MERGED | 35 |
| ARCHIVE / NO REDIRECT | 0 |
| REVIEW | 0 |
| **Mapped Legacy Concepts URLs** | **134** |

Applied in `docs.json`:

| Redirect set | Count |
|---|---:|
| Root `/` | 1 |
| `/docs-new/**` → `/concepts/**` | 134 |
| `/support-docs/**` retargeted one-hop to Concepts (was Legacy hop) | 109 |
| **Total redirects in docs.json** | **244** |

Important mappings included:

- Databases → Transactions
- Scenarios Compare → Analysis → Scenario compare
- Versioning / cloning orphans → Model History (or Models landing)
- Core / Settings / Resources Legacy → new Concepts paths
- Strong orphan and missing-nav paths → canonical Concepts destinations

Validation: **0 redirect loops**, **0 multi-hop chains**, **0 destinations still pointing at `/docs-new/**`**.

## Legacy cleanup

| Item | Action |
|---|---|
| Concepts Legacy tab | `hidden: true` (files retained in git) |
| Missing nav orphans (5) | Removed from Legacy nav; redirects added |
| How to guides | Unchanged / visible |
| Integrations | Unchanged / visible |
| Old docs | Remains `hidden: true` |
| Legacy MDX under `docs-new/**` | Untouched on disk |

Orphans fixed:

1. `docs-new/time/actuals-and-forecast-boundary` → Last actual date
2. `docs-new/models/cloning-and-versioning` → Model History
3. `docs-new/models/model-organization` → Models landing
4. `docs-new/views/private-vs-shared-views` → Sharing views
5. `docs-new/views/view-behavior` → What is a view

Intentionally retained:

- Legacy MDX content for rollback during cutover
- Pre-existing broken links in hidden Legacy / Old docs / essentials sample pages (not Concepts)

## Root route

| | |
|---|---|
| Old destination | `/docs-new/getting-started/what-is-oculon` |
| New destination | `/concepts` |

Decision: `/concepts` (the Concepts landing/`concepts/index.mdx`) is the better default because it is the canonical section hub for the new IA—modules, availability notes, and Resources—rather than a single core page. `/concepts/core-concepts/what-is-oculon` remains reachable from the landing and via Legacy redirect.

## Internal link cleanup

| Metric | Count |
|---|---:|
| Concepts files updated | 24 |
| `/docs-new/**` links replaced with Concepts URLs | 32 |
| Intentionally retained Legacy links in Concepts | 0 |

## Validation

| Check | Result |
|---|---|
| Mintlify validate | **Pass** (`success build validation passed`) |
| Broken links | Same pre-existing **10** in **7** non-Concepts files (Legacy images, essentials samples, support-docs indexes). **0** new Concepts breaks |
| Concepts internal links | **788** checked, **0** broken |
| Concepts nav paths | All resolve |
| Legacy nav missing files | **0** (orphans removed) |
| Redirect destination files | All resolve |
| Redirect loops / multi-hop | **0** |
| Concepts Legacy files deleted | **No** |

## Remaining risks

1. **Deploy/publish still required** — redirects and Legacy hide take effect only when this `docs.json` is deployed.
2. **Hidden Legacy remains URL-reachable until redirects fire** — expected Mintlify behavior; redirects cover mapped paths.
3. **Pre-existing essentials/support-docs broken links** remain outside Concepts cutover scope.
4. **Plan mode / Skills / sensitive-data** Legacy URLs merge to parent Concepts pages (no dedicated pages)—acceptable; deeper pages can follow later.
5. **Rollback window** depends on keeping `docs-new/**` until post-cutover confidence; do not delete yet.

## Cutover recommendation

**READY WITH KNOWN NON-BLOCKING ISSUES**

Concepts is the canonical public surface. Redirects and Legacy hide are configured. Remaining issues are pre-existing non-Concepts link noise and deferred non-blocking content depth—not blockers for cutover publish of this structural change.
