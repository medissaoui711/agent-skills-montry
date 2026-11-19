from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

from jsonschema import Draft202012Validator, FormatChecker
from semantic_validation import validate_artifact_chain

FIXTURES = ROOT / "tests" / "fixtures" / "workflow"
SCHEMA_DIR = ROOT / "contracts"


def load_chain():
    entries = []
    for path in sorted(FIXTURES.glob("*.json")):
        contract = path.stem
        artifact = json.loads(path.read_text(encoding="utf-8"))
        schema = json.loads((SCHEMA_DIR / f"{contract}.schema.json").read_text(encoding="utf-8"))
        errors = list(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(artifact))
        if errors:
            raise AssertionError(f"{path.name} fixture is schema-invalid: {errors}")
        entries.append({"contract": contract, "artifact": artifact})
    return entries


class WorkflowIntegrationTests(unittest.TestCase):
    def test_synthetic_end_to_end_artifact_chain_is_valid(self):
        self.assertEqual(validate_artifact_chain(load_chain()), [])

    def test_missing_source_artifact_blocks_chain(self):
        entries = load_chain()
        entries[1]["artifact"]["source_artifacts"][0]["artifact_id"] = "missing-brief"
        self.assertTrue(any("does not exist" in error for error in validate_artifact_chain(entries)))

    def test_source_contract_version_mismatch_is_rejected(self):
        entries = load_chain()
        entries[1]["artifact"]["source_artifacts"][0]["version"] = "9.9.9"
        self.assertTrue(any("contract or version mismatch" in error for error in validate_artifact_chain(entries)))

    def test_cycle_in_artifact_graph_is_rejected(self):
        entries = load_chain()
        entries[0]["artifact"]["source_artifacts"] = [
            {"artifact_id": "story-001", "contract": "story-plan", "version": "1.0.0"}
        ]
        self.assertTrue(any("cycle" in error for error in validate_artifact_chain(entries)))

    def test_ready_delivery_requires_qc_pass(self):
        entries = load_chain()
        qc = next(item["artifact"] for item in entries if item["contract"] == "qc-report")
        qc["overall_status"] = "NOT_VERIFIED"
        self.assertTrue(any("READY delivery requires" in error for error in validate_artifact_chain(entries)))

    def test_production_plan_must_consume_edl_when_present(self):
        entries = load_chain()
        plan = next(item["artifact"] for item in entries if item["contract"] == "production-plan")
        plan["source_artifacts"] = [ref for ref in plan["source_artifacts"] if ref["contract"] != "edit-decision-list"]
        self.assertTrue(any("Edit Decision List exists" in error for error in validate_artifact_chain(entries)))

    def test_pending_brand_contract_blocks_branded_production(self):
        entries = load_chain()
        brand = copy.deepcopy(json.loads((ROOT / "shared" / "brand" / "brand-contract.json").read_text(encoding="utf-8")))
        brand.update({
            "artifact_id": "brand-pending-test", "project_id": "integration-fixture-project",
            "contract_version": "1.0.0", "created_at": "2026-11-19T07:59:00Z",
            "producer": "brand-digitalnawa", "status": "approved",
            "validation": {"status": "PASS", "issues": []}
        })
        entries.append({"contract": "brand", "artifact": brand})
        plan = next(item["artifact"] for item in entries if item["contract"] == "production-plan")
        plan["source_artifacts"].append({
            "artifact_id": "brand-pending-test", "contract": "brand", "version": "1.0.0"
        })
        self.assertTrue(any("Brand Contract is not approved" in error for error in validate_artifact_chain(entries)))


if __name__ == "__main__":
    unittest.main()
