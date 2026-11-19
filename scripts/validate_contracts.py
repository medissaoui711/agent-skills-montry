#!/usr/bin/env python3
"""Validate JSON Schema files in contracts/ against Draft 2020-12."""
from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError:
    print("Missing dependency. Install with: python -m pip install -r requirements-dev.txt", file=sys.stderr)
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = ROOT / "contracts"
SCHEMAS = sorted(CONTRACTS.glob("*.schema.json"))

def main() -> int:
    if not SCHEMAS:
        print("No contract schemas found.", file=sys.stderr)
        return 1

    errors: list[str] = []
    for path in SCHEMAS:
        try:
            schema = json.loads(path.read_text(encoding="utf-8"))
            Draft202012Validator.check_schema(schema)
            if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
                errors.append(f"{path.relative_to(ROOT)}: unexpected or missing $schema declaration")
        except (json.JSONDecodeError, OSError, Exception) as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    print(f"Validated {len(SCHEMAS)} JSON Schema documents (Draft 2020-12).")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
