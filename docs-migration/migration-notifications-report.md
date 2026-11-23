# Notifications migration report

Scope: Notifications Concepts page under Personal settings. Legacy untouched. support-docs notifications page is outdated (“coming soon”).

## Pages created

| Target path | Action | Legacy | support-docs | App |
|---|---|---|---|---|
| `concepts/settings-and-administration/personal-settings` | RENAME | `profile-and-preferences` (light conceptual parent) | twin | My Account |
| `.../personal-settings/notifications` | CREATE | — | `support-docs/account/notifications` (outdated; not authoritative) | Inbox types; My Account → Notifications |

## Notification coverage

Documented Inbox categories from app types:

comment, mention, assignment, status_change, access_request, access_granted, access_revoked, workspace_invite, role_changed

Documented distinction:

- Inbox = review/act on alerts
- My Account → Notifications = personal preferences
- Do not duplicate full preference UI as Concepts procedure

## Content omitted
- Exhaustive preference toggles without product copy confirmation
- Treating support-docs “coming soon” as current truth

## IA gaps
| Item | Recommendation |
|---|---|
| Inbox as chrome | add Resources/How-to or Personal settings child later |
| Full preference matrix | document when UI labels are confirmed |

## Validation
Pass; no new Concepts Mintlify errors.

## Unresolved
1. Map each Inbox type to preference toggles precisely.
2. Whether Inbox deserves its own Concepts page.
