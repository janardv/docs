# Users / Groups / Permissions (access) migration report

Scope: Conceptual access pages mapped under Settings and administration. Deep security/admin controls not migrated.

## Pages created

| Target path | Action | Legacy | support-docs | App |
|---|---|---|---|---|
| `concepts/settings-and-administration/users-guests-and-invitations` | RENAME | `admin-guide/members-and-roles` | twin | Settings **Users & Groups**; Invite Users; Workspace Owner / Member |
| `concepts/settings-and-administration/roles-and-access` | RENAME | `admin-guide/groups` | twin | Create group; share with groups |

## Access boundary decisions

| Concern | Concepts placement |
|---|---|
| Workspace membership + invites | Users, guests and invitations |
| Groups | Roles and access |
| Item View/Edit/Full Access | Sharing and permissions (summary) + Legacy roles page |
| Inheritance / sensitive data | Legacy for now (IA gaps) |
| Security / audit / login | Remain Settings/Admin — not this batch |

## Content merge

### Preserved
- Invite flow; groups create/share; screenshots

### Rewritten
- Workspace Admin → **Workspace Owner**
- Databases → Transactions
- Settings entry labeled **Users & Groups**

### Added
- Guests conceptual note; clear separation from item sharing

### Omitted
- Full guest ACL matrix beyond confirmed concepts
- Merging Users + Roles into one page (target keeps split)

## IA gaps
| Legacy | Recommendation |
|---|---|
| `members-guests-and-groups` | merge into Users + Roles |
| `roles-and-permissions` | add or merge with Sharing / Roles |
| `permission-inheritance` | add under Sharing |
| `sensitive-data-controls` | Sharing or Security later |

## Validation
Pass; no new Concepts Mintlify errors.

## Unresolved
1. Keep Users / Roles split vs single Users & Groups Concepts page?
2. Confirm Guest product labels vs Member in all share surfaces.
