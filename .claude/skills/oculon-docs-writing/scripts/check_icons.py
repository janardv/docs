#!/usr/bin/env python3
"""Check that every page in the visible docs tabs has a valid Lucide icon.

Mintlify renders an invalid or deprecated icon name as a blank space, so a typo
or an old Lucide alias (e.g. `circle-help`, `history`, `gear`) silently drops the
icon from the sidebar and cards. This script checks frontmatter `icon:` values
and `icon="..."` attributes on Cards against the current Lucide icon list.

Usage (from the repo root):
    python3 .claude/skills/oculon-docs-writing/scripts/check_icons.py [files...]

With no arguments it checks every page in the Concepts, How to guides, and
Integrations tabs of docs.json. Exits 1 if anything is missing or invalid.
"""
import json
import re
import sys
import urllib.request
from pathlib import Path

LUCIDE_TAGS = "https://unpkg.com/lucide-static@latest/tags.json"
TABS = {"Concepts", "How to guides", "Integrations"}
# Mintlify bundles an older Lucide release. These names are valid upstream but
# either render blank in Mintlify (too new) or only exist under an older name.
TOO_NEW = {"rotate-ccw-clock": "clock-fading", "triangle-exclamation-point": "triangle-alert"}
OLD_OK = {"triangle-alert"}


def lucide_names():
    with urllib.request.urlopen(LUCIDE_TAGS, timeout=20) as r:
        return set(json.load(r))


def nav_pages():
    nav = json.loads(Path("docs.json").read_text())["navigation"]
    pages = []

    def walk(x):
        if isinstance(x, str):
            pages.append(x)
        elif isinstance(x, dict):
            for k in ("pages", "groups"):
                if k in x:
                    walk(x[k])
        elif isinstance(x, list):
            for i in x:
                walk(i)

    for tab in nav.get("tabs", []):
        if tab.get("tab") in TABS:
            walk(tab)
    return [p + ".mdx" for p in pages]


def check(f, name, valid, kind):
    if name in TOO_NEW:
        return [f"{f}: {kind} '{name}' renders blank in Mintlify; use '{TOO_NEW[name]}'"]
    if name not in valid and name not in OLD_OK:
        return [f"{f}: invalid {kind} '{name}'"]
    return []


def main():
    valid = lucide_names()
    files = sys.argv[1:] or nav_pages()
    problems = []
    for f in files:
        path = Path(f)
        if not path.exists():
            problems.append(f"{f}: file not found")
            continue
        text = path.read_text()
        parts = text.split("---", 2)
        fm = parts[1] if len(parts) == 3 else ""
        m = re.search(r"^icon:\s*[\"']?([\w-]+)", fm, re.M)
        if not m:
            problems.append(f"{f}: no icon in frontmatter")
        else:
            problems += check(f, m.group(1), valid, "icon")
        for ic in re.findall(r'icon="([\w-]+)"', text):
            problems += check(f, ic, valid, "card icon")
    if problems:
        print("\n".join(problems))
        sys.exit(1)
    print(f"All icons valid ({len(files)} files checked).")


if __name__ == "__main__":
    main()
