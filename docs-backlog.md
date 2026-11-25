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
