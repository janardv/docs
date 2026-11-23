# History / Activity migration report

Scope: History/Activity placement for this batch. No generic History parent created.

## Pages created

| Target path | Action | Legacy | support-docs | App |
|---|---|---|---|---|
| `concepts/modeling/models/model-history` | CREATE | Fold useful content from `docs-new/models/versioning` | cloning/versioning twin not used as Clone docs | Model History panel; Previewing version; Restore |

Also updated Models landing Cards + `docs.json` Models nav.

## Placement decisions

| Surface | Decision |
|---|---|
| Model History | Concepts child under Models (per `ia-decisions.md`) |
| Project Activity | Hold — Projects flag-gated; not migrated in this batch |
| Artifact history | Hold — Artifacts flag-gated |
| Generic History parent | **Do not create** — conflicts with product (no single History object) |

## Content merge

### Preserved
- Checkpoint / baseline intent from Legacy Versioning

### Rewritten
- Product labels History / Preview / Restore
- Clear separation from Project Activity and artifact history

### Added
- Comparison table of history-like surfaces

### Omitted
- Clone model documentation
- Project Activity CREATE pages

## IA gaps
| Item | Recommendation |
|---|---|
| Legacy `docs-new/models/versioning` | redirect to Model History at cutover |
| Project Activity | migrate with Projects when enabled |

## Validation
Pass for Model History page; pre-existing Mintlify Legacy errors unchanged.

## Unresolved
1. When Projects GA, add Project Activity under Projects tree.
2. Artifact history documentation timing with Artifacts migration.
