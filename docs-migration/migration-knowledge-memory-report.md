# Knowledge and memory migration report

Scope: Minimal CREATE page for product-visible personal and agent knowledge. Legacy fragments only. App read-only.

## Pages created

| Target path | Action | Legacy | support-docs | App |
|---|---|---|---|---|
| `concepts/ai-and-agents/knowledge-and-memory` | CREATE | Fragments only (no unified docs-new page) | — | My Account AI / personal memories; custom agent knowledge; `server/memory` (not customer-documented) |

## Feature flag / availability

No dedicated knowledge/memory GA flag documented. Page published with conservative claims only where UI exposes controls.

## Content

### Preserved
- Agent knowledge scoping tone from Custom agents docs (linked, not duplicated wholesale)

### Rewritten
- N/A (new page)

### Added
- Personal memories as My Account–scoped
- Pointer to agent context/knowledge
- Explicit non-claims (no automatic chat memory, no inferred workspace-wide memory, no project memory without Projects docs)

### Omitted
- Persistence implementation details
- Project memory (Projects not migrated)
- Internal memory API / storage behavior

## Terminology decisions

| Term | Choice |
|---|---|
| Page title | **Knowledge and memory** (target IA) |
| Personal scope | **Personal memories** |
| Agent scope | **Agent knowledge** via Custom agents |

## IA gaps

| Item | Status |
|---|---|
| Project memories | Deferred with Projects/Tasks |
| Memory precedence (personal vs workspace instructions) | Unconfirmed — flagged |

## Validation

Page in nav. Links to assistant / custom agents / Workspace AI / personal settings.

## Unresolved questions

1. Whether personal memories are always visible across environments.
2. Scope and retention rules for memories once product confirms them.
