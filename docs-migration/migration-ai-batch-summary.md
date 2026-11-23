# AI and agents batch — combined summary

Date: 2026-11-23. Legacy and support-docs untouched. App read-only. Redirects deferred.

## Pages created by module

| Module | Pages | Paths |
|---|---|---|
| Overview + Workspace AI | 2 | `ai-overview`, `workspace-ai` |
| AI assistant | 3 | `ai-assistant`, `modeling-with-ai`, `reporting-with-ai` |
| Custom agents | 9 | landing + 8 children |
| Context and connections | 2 | landing + `mcp` |
| Knowledge and memory | 1 | `knowledge-and-memory` |
| Feed | 1 | `feed` |
| **Published total** | **18** | all under `concepts/ai-and-agents/` |

Held (no MDX / no nav): Plan mode (REVIEW), Skills (REVIEW), Agent teams (HOLD).

## Action counts (published)

| Action | Count |
|---|---|
| REPLACE | 3 |
| CREATE | 3 |
| MOVE | 12 |
| REVIEW (held) | 2 |
| HOLD (held) | 1 |

## Features published as GA

- AI overview
- Workspace AI
- AI assistant (+ modeling / reporting)
- Custom agents (full child set), with discoverability note
- Context and connections + MCP
- Knowledge and memory (conservative product-visible claims only)

## Features held / availability-noted

| Feature | Status |
|---|---|
| Feed | Published with availability note (`feeds-enabled` on local/sandbox; off elsewhere) — **not GA** |
| Skills | REVIEW — not published |
| Plan mode | REVIEW — not published |
| Agent teams | HOLD — flag off all envs; not published |
| Artifacts (section) | Out of scope; gap recorded; board code-block already notes gating |

## Skills placement decision

Keep **REVIEW**. No Concepts Skills page. No Settings Concepts duplicate. Revisit when IA decides Concepts vs Settings vs How-to.

## Knowledge / Memory coverage

Minimal CREATE page: personal memories + agent knowledge links; explicit non-claims for automatic / workspace-wide / project memory.

## Feed / Agent Teams status

- **Feed:** in nav with gated availability copy.
- **Agent teams:** no page, no nav.

## Artifacts scope decision

Only AI-mapped Artifacts content would ship here; none mapped for this batch beyond existing Boards code-block note. Broader `concepts/artifacts/*` remains a later module / IA gap.

## IA gaps

1. Plan mode naming / publication
2. Skills Concepts vs Settings
3. Integrations home outside AI Context
4. Artifacts section
5. Project memories (with Projects)
6. Agent teams promotion criteria

## Validation

| Check | Result |
|---|---|
| Files exist for 18 nav paths | Pass |
| `docs.json` AI group | Added; paths valid |
| Internal links from AI MDX | 0 broken Concepts targets |
| Images | No AI page image refs |
| Legacy / support-docs | Untouched |
| Mintlify validate | **5 pre-existing** Legacy missing-nav-page warnings only; **0 new Concepts** |
| Mintlify broken-links | **10** broken links (all Legacy / essentials / support-docs); **0 under `concepts/ai-and-agents`** — fewer than prior 15 baseline; no new Concepts errors |

## Safe to mark AI batch complete?

**Yes**, for staged Concepts migration of AI/agents **as scoped**: GA surfaces published; Skills / Plan mode / Agent teams correctly held; Feed availability-noted; Artifacts not expanded; reports filed.

Not a claim that every target-IA AI row is customer-complete (REVIEW/HOLD rows remain open).
