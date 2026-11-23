# Custom agents migration report

Scope: Custom agents landing and eight child pages. Distinct from Agent teams (HOLD). Legacy untouched. App read-only.

## Pages created

| Target path | Action | Legacy | support-docs | App |
|---|---|---|---|---|
| `concepts/ai-and-agents/custom-agents` | MOVE | landing from what-are + section | twins under `support-docs/custom-agents/*` | `/custom-agents` |
| `.../what-are-custom-agents` | MOVE | `docs-new/custom-agents/what-are-custom-agents` | twin | `/custom-agents` |
| `.../create-a-custom-agent` | MOVE | create page | twin | create flow |
| `.../agent-context-and-knowledge` | MOVE | context page | twin | agent config |
| `.../agent-actions` | MOVE | actions page | twin | agent config |
| `.../agent-permissions` | MOVE | permissions page | twin | Workspace AI Agents tab |
| `.../agent-connections` | MOVE | connections page | twin | tools/connectors |
| `.../agent-safety-and-review` | MOVE | safety page | twin | approvals posture |
| `.../agent-best-practices` | MOVE | best practices | twin | product guidance |

## Feature flag / availability

Custom agents documented as GA with discoverability note (`/custom-agents`; settings nav entry historically commented). Not gated by `agent-teams-enabled`. Feed-related agent activity remains under Feed availability.

## Content

### Preserved
- Strong Legacy explanations for purpose, create, context, actions, permissions, connections, safety, best practices

### Rewritten
- Explicit distinction from AI assistant and Agent teams
- Governance pointers to Workspace AI tabs

### Added
- Availability / discoverability caution where settings entry may be hidden
- Cross-links to Workspace AI and Context and connections

### Omitted
- Agent teams multi-agent orchestration
- Unconfirmed automatic permission grants
- Internal CUSTOM_AGENTS_* flag implementation as customer procedure

## Terminology decisions

| Term | Choice |
|---|---|
| Feature name | **Custom agents** |
| vs chat | Distinct from **AI assistant** |
| vs teams | Distinct from **Agent teams** (not published) |

## IA gaps

| Item | Status |
|---|---|
| Agent teams | HOLD / out of nav |
| Settings nav discoverability | Note only; not inventing alternate entry |

## Validation

Nine Custom agents paths in `docs.json`. Legacy `docs-new/custom-agents/*` untouched.

## Unresolved questions

1. Whether Settings should re-expose a Custom agents admin entry for discoverability.
2. Exact production GA posture if product later gates custom agents behind a flag.
