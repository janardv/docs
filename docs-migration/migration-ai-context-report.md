# Context and connections / MCP migration report

Scope: Context and connections landing + MCP. Distinguishes Library Integrations from Connectors & MCP. Legacy untouched. App read-only.

## Pages created

| Target path | Action | Legacy | support-docs | App |
|---|---|---|---|---|
| `concepts/ai-and-agents/context-and-connections` | REPLACE | `docs-new/ai/connectors` | twin | Settings → **Connectors & MCP**; Workspace AI → Tools & Connectors |
| `concepts/ai-and-agents/context-and-connections/mcp` | MOVE | `docs-new/ai/mcp` | twin | `/authorize/mcp`; MCP env config |

## Feature flag / availability

MCP connection config may depend on `NEXT_PUBLIC_MCP_*` environment setup. Documented as supported Concepts topic with governance-first framing; not presented as automatic access to all workspace data. Library Integrations remain out of scope for this AI module (pointed at Transactions for planning data).

## Content

### Preserved
- MCP as structured, permission-aware tool bridge
- Governance / least-privilege tone from Legacy MCP docs

### Rewritten
- Connectors landing rewritten to separate Integrations vs Connectors & MCP
- Avoid implying AI auto-ingests every resource

### Added
- Explicit dual-surface explanation (AI connectors vs Library Integrations)
- Link to Workspace AI Tools & Connectors policy

### Omitted
- Engineer-only MCP env var setup as customer procedure
- Inferred automatic permissions from code paths
- Full Integrations catalog (belongs with data/integrations IA)

## Terminology decisions

| Term | Choice |
|---|---|
| AI settings label | **Connectors & MCP** (also MCP & Connectors) |
| Data ingest | **Integrations** (Library) — not conflated |
| Protocol | **MCP** / Model Context Protocol |

## IA gaps

| Item | Recommendation |
|---|---|
| Integrations under Data vs Settings | Separate from AI Context; track as broader IA gap |
| Authorize/MCP deep how-to | Prefer How-to Guides later |

## Validation

Both paths in nav. No Artifacts expansion. Internal links to Workspace AI / agent connections valid.

## Unresolved questions

1. Whether Integrations should get a dedicated Concepts home outside AI.
2. How much MCP authorize UI detail belongs in Concepts vs How-to.
