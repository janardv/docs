# Docs backlog: hidden pages and deferred features

Pages and topics held back from the published docs until the feature ships or is confirmed. This file is listed in `.mintignore`, so it isn't published.

To bring a page back:

1. Remove its line from `.mintignore`.
2. Add the page path back to its group in `docs.json`.
3. Restore the links listed under **Links removed**.
4. Point any redirects back to the page.
5. Run `mint broken-links` and `python3 .claude/skills/oculon-docs-writing/scripts/check_icons.py`.

## Hidden pages

| Page | Hidden on | Reason | Links removed | Redirects changed |
| :--- | :--- | :--- | :--- | :--- |
| `concepts/data-and-structure/transactions/refresh-and-sync-behavior` | 2026-11-24 | Refresh and sync is a feature for later | Card on `transactions.mdx`; sentence and Related link on `transactions/transaction-types.mdx`; Related links on `transactions/working-with-data.mdx` and `transactions/transaction-best-practices.mdx` | `/docs-new/databases/refresh-and-sync-behavior` and `/support-docs/databases/refresh-and-sync-behavior` now go to `/concepts/data-and-structure/transactions` |
| `concepts/modeling/scenarios/versioning-and-snapshots` | 2026-11-25 | Versioning is hidden and deferred under Scenarios | Versioning card on `scenarios.mdx` | `/docs-new/scenarios/versioning-and-snapshots` and `/support-docs/scenarios/versioning-and-snapshots` now go to `/concepts/modeling/scenarios` |
| `concepts/analysis-and-reporting/views/sharing-views` | 2026-11-25 | Dedicated Share View is not generally available yet | Card on `views.mdx`; Related links on `what-is-a-view.mdx` and `creating-and-configuring-views.mdx`; sharing sentence on `view-best-practices.mdx`; Related link on `sharing-and-permissions.mdx`; sentence on `roles-and-permissions.mdx` | `/docs-new/views/sharing-views`, `/docs-new/views/private-vs-shared-views`, `/support-docs/views/private-vs-shared-views`, and `/concepts/analysis-and-reporting/views/sharing-views` now go to `/concepts/analysis-and-reporting/views` |
| `concepts/workspace-and-collaboration/projects-and-tasks` (section + all child pages) | 2026-11-26 | Projects and tasks will be implemented later | Projects link on `sidebar-and-search.mdx`; Projects mentions on `index.mdx`, `how-oculon-is-organized.mdx`, and `model-history.mdx` | All `/concepts/workspace-and-collaboration/projects-and-tasks*` paths, plus `/docs-new/projects`, `/docs-new/projects-and-tasks`, and `/support-docs/projects-and-tasks`, now go to `/concepts/workspace-and-collaboration/workspaces` |
| `concepts/settings-and-administration/security` (section + login-methods, audit-logs) | 2026-11-26 | Security docs held for a future release | Links on `workspace-settings.mdx`, `personal-settings.mdx`, `roles-and-access.mdx`, and `troubleshooting.mdx` | `/concepts/settings-and-administration/security*`, plus `/docs-new/admin-guide/{security,login-methods,audit-logs}` and `/support-docs/admin-guide/{security,login-methods,audit-logs}`, now go to `/concepts/settings-and-administration/workspace-settings` |

## Deferred or unconfirmed features (not documented)

Features that exist in the app code but are intentionally left out of the docs.

| Feature | Why it's left out |
| :--- | :--- |
| Daily and weekly time granularity | Docs policy: only monthly, quarterly, and yearly |
| Custom rollups | Counts as custom calendar behavior |
| Lookup columns on dimensions | Not enabled on Library dimension pages |
| App switcher (Revenue, Close, Cash, and others) | Looks like a prototype |
| Workspace AI admin settings | Saved only in the browser, not persisted |
| Planning **Default Scenario** setting | Not saved |
| Workspace Planning currency defaults | Saved only in the browser, not persisted |
| Space **+** → **Database** (dimension-backed page) | Behind a workspace setting with no UI to turn it on |
| Full-screen variable page | Entry point unconfirmed |
| Currency exchange-rate conversion | No conversion logic found; values are display-only |
| Dedicated **Share View** / Shared view tab | Shown as coming soon on models; hidden on Transactions until it ships |
| **Projects** and **Tasks** | Feature for later; docs section hidden until it ships |
| **Security** docs group (login methods, audit logs) | Held for a future release; Settings UI may still show Security for users |
