from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

from jsonschema import Draft202012Validator, FormatChecker
from semantic_validation import (
    validate_edit_decision_list,
    validate_production_plan,
    validate_qc_report,
)


class ContractSchemaTests(unittest.TestCase):
    def setUp(self):
        self.contracts = ROOT / "contracts"
        self.schemas = {
            path.stem.replace(".schema", ""): json.loads(path.read_text(encoding="utf-8"))
            for path in self.contracts.glob("*.schema.json")
        }

    def test_all_seven_schemas_are_draft_2020_12(self):
        self.assertEqual(len(self.schemas), 7)
        for schema in self.schemas.values():
            self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
            Draft202012Validator.check_schema(schema)

    def test_brand_contract_instance_is_valid(self):
        schema = self.schemas["brand"]
        instance = json.loads((ROOT / "shared/brand/brand-contract.json").read_text(encoding="utf-8"))
        errors = list(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(instance))
        self.assertEqual(errors, [])

    def test_brand_contract_keeps_unapproved_identity_gates_explicit(self):
        instance = json.loads((ROOT / "shared/brand/brand-contract.json").read_text(encoding="utf-8"))
        self.assertEqual(instance["approval_status"], "PENDING")
        self.assertTrue(all(item["approval_status"] == "APPROVED" for item in instance["color_palette"]))
        self.assertTrue(all(item["approval_status"] == "PROVISIONAL" for item in instance["typography"]))

    def test_brand_schema_rejects_invalid_hex(self):
        schema = self.schemas["brand"]
        instance = json.loads((ROOT / "shared/brand/brand-contract.json").read_text(encoding="utf-8"))
        instance["color_palette"][0]["value"] = "warm-yellow"
        errors = list(Draft202012Validator(schema).iter_errors(instance))
        self.assertTrue(any("warm-yellow" in error.message for error in errors))

    def test_brand_schema_rejects_unknown_top_level_property(self):
        schema = self.schemas["brand"]
        instance = json.loads((ROOT / "shared/brand/brand-contract.json").read_text(encoding="utf-8"))
        instance["unreviewed_override"] = True
        errors = list(Draft202012Validator(schema).iter_errors(instance))
        self.assertTrue(errors)


class SemanticValidationTests(unittest.TestCase):
    def test_qc_pass_requires_evidence(self):
        report = {
            "overall_status": "PASS",
            "checks": [{"check_id": "logo", "status": "PASS", "evidence": []}],
        }
        self.assertTrue(validate_qc_report(report))

    def test_qc_overall_pass_requires_all_checks_to_pass(self):
        report = {
            "overall_status": "PASS",
            "checks": [
                {"check_id": "logo", "status": "PASS", "evidence": ["https://example.com/logo.png"]},
                {"check_id": "audio", "status": "NOT_VERIFIED", "evidence": None},
            ],
        }
        self.assertTrue(validate_qc_report(report))

    def test_edl_rejects_missing_media_and_out_of_range_cut(self):
        edl = {
            "source_media": [{"media_id": "source-1", "duration_frames": 100}],
            "segments": [
                {"segment_id": "a", "media_id": "missing", "in_frame": 0, "out_frame": 10},
                {"segment_id": "b", "media_id": "source-1", "in_frame": 20, "out_frame": 101},
                {"segment_id": "c", "media_id": "source-1", "in_frame": 30, "out_frame": 30},
            ],
        }
        self.assertEqual(len(validate_edit_decision_list(edl)), 3)

    def test_production_scene_must_fit_composition_duration(self):
        plan = {
            "video": {"duration_frames": 100},
            "scenes": [{"scene_id": "scene-1", "from": 80, "duration_frames": 30}],
        }
        self.assertTrue(validate_production_plan(plan))


if __name__ == "__main__":
    unittest.main()
