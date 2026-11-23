# AI assistant migration report

Scope: AI assistant landing plus Modeling with AI and Reporting with AI. Plan mode held as REVIEW. Legacy untouched. App read-only.

## Pages created

| Target path | Action | Legacy | support-docs | App |
|---|---|---|---|---|
| `concepts/ai-and-agents/ai-assistant` | REPLACE | Shared `docs-new/ai/ai-in-oculon` | twin | `/chat`; AIChat |
| `concepts/ai-and-agents/ai-assistant/modeling-with-ai` | MOVE | `docs-new/ai/modeling-with-ai` | twin | AI chat; plan components |
| `concepts/ai-and-agents/ai-assistant/reporting-with-ai` | MOVE | `docs-new/ai/reporting-with-ai` | twin | AI chat; plan components |
| `concepts/ai-and-agents/ai-assistant/plan-mode` | REVIEW | `docs-new/ai/plan-mode` | twin | plan editor | **Not published** |

## Feature flag / availability

Core assistant treated as GA. No dedicated assistant flag. Plan mode left unpublished pending naming / IA REVIEW (Plans vs Planning vs Projects).

## Content

### Preserved
- Task-oriented modeling and reporting guidance from Legacy
- Assistant as day-to-day chat help

### Rewritten
- Assistant landing separated from Workspace AI and Custom agents
- Concise examples; detailed workflows deferred to How-to Guides

### Added
- Clear distinction from Custom agents
- Links into modeling/reporting children only (no Plan mode nav)

### Omitted
- Plan mode page and deep plan-editor internals
- Skills duplication under assistant
- Mentions of unavailable experimental modes as GA

## Terminology decisions

| Term | Choice |
|---|---|
| Chat surface | **AI assistant** |
| Plan mode | Hold REVIEW; do not publish as GA Concepts child |

## IA gaps

| Item | Recommendation |
|---|---|
| Plan mode | Keep REVIEW until product names Plans vs Planning |
| Skills entry from assistant | Do not duplicate; resolve under Skills REVIEW |

## Validation

Published assistant paths exist in nav. Plan mode file not created. Links avoid unpublished targets.

## Unresolved questions

1. Plan mode publication after naming decision.
2. How much plan-editor behavior belongs in Concepts vs How-to.
