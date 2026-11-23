# Agent teams migration report

Scope: Agent teams held from public Concepts. No page created. No nav entry.

## Map decision

| Target | Map action | Outcome this batch |
|---|---|---|
| `concepts/ai-and-agents/agent-teams` | CREATE (experimental) | **HOLD** — not created; not in nav |

## Sources reviewed

| Kind | Evidence |
|---|---|
| App | `/team` gated by `agent-teams-enabled` |
| Flags | Default **false** in local, sandbox, development, staging, and production (`registry.environment.test.ts`) |
| Inventory / rules | Migration rules §8 Hold list includes Agent teams |

## Feature flag / availability

`agent-teams-enabled` off everywhere by default. Do not publish as GA. Do not imply Custom agents equals Agent teams.

## Content decisions

- No Concepts MDX
- Custom agents pages explicitly distinguish Agent teams as separate / unpublished
- AI overview does not list Agent teams as a customer surface

## Artifacts note (related AI overlap)

Broader `concepts/artifacts/*` IA is **out of scope** for this AI batch. Board code-block already notes artifacts gating. Artifacts section remains a gap / later module, not expanded here.

## Validation

No Agent teams path in `docs.json`. No orphan Concepts Agent teams file.

## Unresolved questions

1. Conditions for promoting Agent teams to public Concepts.
2. Naming clarity between Custom agents and Agent teams in product chrome.
