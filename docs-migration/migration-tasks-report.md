# Tasks migration report

Scope: Tasks Concepts page under Projects and tasks. Legacy untouched. App read-only.

## Pages created

| Target path | Action | Legacy | support-docs | App |
|---|---|---|---|---|
| `concepts/workspace-and-collaboration/projects-and-tasks/tasks` | CREATE | — | — | Project Tasks; portfolio **All tasks** / **My tasks**; `/tasks/[taskId]`; `ProjectTaskFields`; agent assignee runs |

## Feature availability / flags

Same as Projects: gated by `projects-enabled` (+ env ceiling). Documented under Projects availability — not GA.

## Content

### Preserved
N/A — no Legacy Tasks Concepts page.

### Added
- All tasks / My tasks scope copy from product
- Core fields: Status, Assignee (people or agents), Reviewer, Due date, Priority, Project, Linked file
- Create/update/move and list/board views at concept level
- Agent assignment pointer without deep agent-run internals

### Omitted
- Exhaustive custom-field catalog as standard for every workspace
- Reviewer notification delivery guarantees
- Experimental agent-tool internals
- Loose-task edge cases beyond “move when product allows”

## Terminology decisions

| Term | Choice |
|---|---|
| Portfolio labels | **All tasks**, **My tasks** |
| Owner field | **Assignee** (product label) |
| Priority | None / Low / Medium / High / Urgent |

## IA gaps

| Item | Status |
|---|---|
| Task types deep how-to | Prefer Settings/How-to later |
| Calendar/Kanban depth | Mentioned lightly via views; not separate pages |

## Validation

Path in nav; links to Activity / AI in projects / settings valid.

## Unresolved questions

1. Which custom-field behaviors are universal vs type-specific.
2. Agent assignment GA posture across environments.
