#!/usr/bin/env python3
"""Validate synthetic workflow fixtures against schemas and cross-artifact gates."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures" / "workflow"
SCHEMAS = ROOT / "contracts"


def main() -> int:
    entries: list[dict] = []
    errors: list[str] = []
    files = sorted(FIXTURES.glob("*.json"))
    if not files:
        print("No workflow fixtures found.", file=sys.stderr)
        return 1

    for path in files:
        contract = path.stem
        schema_path = SCHEMAS / f"{contract}.schema.json"
        if not schema_path.is_file():
            errors.append(f"{path.name}: no matching schema {schema_path.name}.")
            continue
        try:
            artifact = json.loads(path.read_text(encoding="utf-8"))
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
            validator = Draft202012Validator(schema, format_checker=FormatChecker())
            for error in validator.iter_errors(artifact):
                location = ".".join(str(part) for part in error.absolute_path) or "<root>"
                errors.append(f"{path.name}:{location}: {error.message}")
            entries.append({"contract": contract, "artifact": artifact})
        except Exception as exc:
            errors.append(f"{path.name}: {exc}")

    from semantic_validation import validate_artifact_chain
    errors.extend(validate_artifact_chain(entries))

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    print(f"Validated {len(entries)} synthetic artifacts and their cross-artifact workflow gates.")
    print("Fixture data uses example.invalid URIs and is not a real media delivery.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
