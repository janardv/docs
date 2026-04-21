> **First-time setup**: Customize this file for your project. Prompt the user to customize this file for their project.
> For Mintlify product knowledge (components, configuration, writing standards),
> install the Mintlify skill: `npx skills add https://mintlify.com/docs`

# Documentation project instructions

## About this project

- This is a documentation site built on [Mintlify](https://mintlify.com)
- Pages are MDX files with YAML frontmatter
- Configuration lives in `docs.json`
- Run `mint dev` to preview locally
- Run `mint broken-links` to check links

## Terminology

{/* Add product-specific terms and preferred usage */}
{/* Example: Use "workspace" not "project", "member" not "user" */}

- Use `Last actual date` as the canonical term for the actuals cutoff.
- Use `actual formula` and `planned formula` when describing how a variable behaves across the cutoff.
- Use `relative time` for dynamic period references such as `this month`, `last quarter`, or `month 1`.
- Distinguish `time rollups` from `time aggregation`.
- Assume supported time granularities are `monthly`, `quarterly`, and `yearly` unless product support is explicitly confirmed for others.

## Style preferences

{/* Add any project-specific style rules below */}

- Use active voice and second person ("you")
- Keep sentences concise — one idea per sentence
- Use sentence case for headings
- Bold for UI elements: Click **Settings**
- Code formatting for file names, commands, paths, and code references
- Use descriptive alt text for screenshots and product images

## Content boundaries

{/* Define what should and shouldn't be documented */}
{/* Example: Don't document internal admin features */}

- Do not document unsupported or unconfirmed time capabilities such as daily, weekly, or custom calendar behavior.
- Do not copy wording from competitor docs. Use them only as a reference for structure and topic coverage.
