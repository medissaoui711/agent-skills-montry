#!/usr/bin/env python3
"""Validate Draft 2020-12 contract schemas and the checked-in Brand Contract."""
from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError:
    print("Missing dependency. Install with: python -m pip install -r requirements-dev.txt", file=sys.stderr)
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = ROOT / "contracts"
SCHEMAS = sorted(CONTRACTS.glob("*.schema.json"))


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    if not SCHEMAS:
        print("No contract schemas found.", file=sys.stderr)
        return 1

    errors: list[str] = []
    loaded: dict[str, dict] = {}

    for path in SCHEMAS:
        try:
            schema = load_json(path)
            Draft202012Validator.check_schema(schema)
            if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
                errors.append(f"{path.relative_to(ROOT)}: unexpected or missing $schema declaration")
            loaded[path.name] = schema
        except Exception as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")

    brand_path = ROOT / "shared" / "brand" / "brand-contract.json"
    brand_schema = loaded.get("brand.schema.json")
    if brand_schema is None:
        errors.append("contracts/brand.schema.json: schema unavailable for Brand Contract validation")
    elif not brand_path.is_file():
        errors.append("shared/brand/brand-contract.json: required Brand Contract is missing")
    else:
        try:
            instance = load_json(brand_path)
            validator = Draft202012Validator(brand_schema, format_checker=FormatChecker())
            for error in validator.iter_errors(instance):
                location = ".".join(str(part) for part in error.absolute_path) or "<root>"
                errors.append(f"shared/brand/brand-contract.json:{location}: {error.message}")
        except Exception as exc:
            errors.append(f"shared/brand/brand-contract.json: {exc}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    print(f"Validated {len(SCHEMAS)} JSON Schema documents (Draft 2020-12).")
    print("Validated shared/brand/brand-contract.json against brand.schema.json.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
