#!/usr/bin/env python3
"""Check that plugin.json points to existing, correctly named skills."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / ".claude-plugin" / "plugin.json"


def main() -> int:
    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"Invalid plugin manifest: {exc}", file=sys.stderr)
        return 1

    skills = manifest.get("skills")
    if not isinstance(skills, list) or not skills:
        print("plugin.json must define a non-empty skills array.", file=sys.stderr)
        return 1

    errors: list[str] = []
    if len(skills) != len(set(skills)):
        errors.append("plugin.json contains duplicate skill paths.")

    for entry in skills:
        if not isinstance(entry, str) or not entry.startswith("./skills/"):
            errors.append(f"Invalid skill path: {entry!r}")
            continue
        skill_dir = ROOT / entry[2:]
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{entry}: SKILL.md is missing.")
            continue
        content = skill_file.read_text(encoding="utf-8")
        if not content.startswith("---\n"):
            errors.append(f"{entry}: frontmatter must start at line 1.")
            continue
        end = content.find("\n---", 4)
        if end < 0:
            errors.append(f"{entry}: frontmatter closing delimiter is missing.")
            continue
        frontmatter = content[4:end]
        name = re.search(r"^name:\s*(.+)$", frontmatter, re.MULTILINE)
        description = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
        expected = skill_dir.name
        if not name or name.group(1).strip() != expected:
            errors.append(f"{entry}: frontmatter name must equal {expected!r}.")
        if not description or not description.group(1).strip():
            errors.append(f"{entry}: frontmatter description is missing.")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    print(f"Validated plugin manifest and {len(skills)} skill entrypoints.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
