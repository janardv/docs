# AI overview + Workspace AI migration report

Scope: AI overview landing and Workspace AI admin policy. Legacy untouched. App read-only. Redirects deferred.

## Pages created

| Target path | Action | Legacy | support-docs | App |
|---|---|---|---|---|
| `concepts/ai-and-agents/ai-overview` | REPLACE | `docs-new/ai/ai-in-oculon` | twin | AIChat; Settings → Workspace AI |
| `concepts/ai-and-agents/workspace-ai` | CREATE | Shared blurbs only in `ai-in-oculon` | — | `SettingsWorkspaceAiDrawer` (Defaults / Agents / Approvals / Tools & Connectors; Lite/Pro/Max) |

## Feature flag / availability

No product feature flag gates these surfaces. Documented as GA Concepts pages.

## Content

### Preserved
- Purpose of AI in planning context
- Built-in vs configurable help framing
- Grounded, permission-aware behavior expectations

### Rewritten
- Split shared Legacy `ai-in-oculon` into overview vs Workspace AI vs assistant
- Admin chrome labels aligned to Workspace AI tabs

### Added
- Surface map table (assistant, Workspace AI, custom agents, connections, knowledge)
- Workspace AI tab table and model tier note
- Separation of Workspace AI vs My Account personal AI

### Omitted
- Plan mode (REVIEW)
- Skills (REVIEW)
- Agent teams (HOLD)
- Internal chat/tool implementation details

## Terminology decisions

| Term | Choice |
|---|---|
| Landing title | **AI overview** (not “AI in Oculon”) |
| Admin surface | **Workspace AI** |
| Settings connectors label | **Connectors & MCP** / **Tools & Connectors** |

## IA gaps

| Item | Status |
|---|---|
| Plan mode under AI assistant | REVIEW — not published |
| Skills Concepts vs Settings | REVIEW — not published under Concepts |
| Broader Artifacts IA | Deferred; not part of this batch |

## Validation

Files exist; `docs.json` paths added under AI and agents. Internal links point to published Concepts peers. Mintlify validate / broken-links: no new Concepts errors expected (pre-existing Legacy noise unchanged).

## Unresolved questions

1. Whether Plan mode should remain a Concepts child after naming REVIEW.
2. Whether Workspace AI instructions copy should deepen once product confirms shared instruction precedence.
