"""Cross-field semantic checks not expressible in the current JSON Schemas."""
from __future__ import annotations


def validate_qc_report(report: dict) -> list[str]:
    errors: list[str] = []
    checks = report.get("checks", [])
    overall = report.get("overall_status")

    if overall == "PASS" and not checks:
        errors.append("QC overall_status cannot be PASS without at least one check.")

    for index, check in enumerate(checks):
        status = check.get("status")
        evidence = check.get("evidence")
        if status == "PASS" and not evidence:
            errors.append(f"checks[{index}]: PASS requires at least one evidence reference.")
        if overall == "PASS" and status != "PASS":
            errors.append(f"checks[{index}]: overall PASS requires every check to be PASS.")

    return errors


def validate_edit_decision_list(edl: dict) -> list[str]:
    errors: list[str] = []
    media = {item.get("media_id"): item for item in edl.get("source_media", [])}
    seen_segments: set[str] = set()

    for index, segment in enumerate(edl.get("segments", [])):
        segment_id = segment.get("segment_id")
        media_id = segment.get("media_id")
        source = media.get(media_id)
        in_frame = segment.get("in_frame")
        out_frame = segment.get("out_frame")

        if segment_id in seen_segments:
            errors.append(f"segments[{index}]: duplicate segment_id {segment_id!r}.")
        seen_segments.add(segment_id)

        if source is None:
            errors.append(f"segments[{index}]: media_id {media_id!r} does not reference source_media.")
            continue
        if in_frame is not None and out_frame is not None and out_frame <= in_frame:
            errors.append(f"segments[{index}]: out_frame must be greater than in_frame.")
        if out_frame is not None and out_frame > source.get("duration_frames", 0):
            errors.append(f"segments[{index}]: out_frame exceeds source media duration.")

    return errors


def validate_production_plan(plan: dict) -> list[str]:
    errors: list[str] = []
    video = plan.get("video", {})
    total_frames = video.get("duration_frames")
    seen_scene_ids: set[str] = set()

    for index, scene in enumerate(plan.get("scenes", [])):
        scene_id = scene.get("scene_id")
        start = scene.get("from")
        duration = scene.get("duration_frames")

        if scene_id in seen_scene_ids:
            errors.append(f"scenes[{index}]: duplicate scene_id {scene_id!r}.")
        seen_scene_ids.add(scene_id)

        if start is not None and duration is not None and total_frames is not None:
            if start + duration > total_frames:
                errors.append(f"scenes[{index}]: scene exceeds video.duration_frames.")

    return errors


CONTRACT_TYPES = {
    "brand", "creative-brief", "story-plan", "edit-decision-list",
    "production-plan", "qc-report", "delivery-manifest",
}


def validate_artifact_chain(entries: list[dict]) -> list[str]:
    """Validate cross-artifact references and workflow gates.

    Each entry has the shape {"contract": <contract slug>, "artifact": <validated dict>}.
    Each artifact is assumed to have passed its own JSON Schema.
    """
    errors: list[str] = []
    by_id: dict[str, dict] = {}
    graph: dict[str, list[str]] = {}
    project_ids: set[str] = set()

    for index, entry in enumerate(entries):
        contract = entry.get("contract")
        artifact = entry.get("artifact")
        if contract not in CONTRACT_TYPES or not isinstance(artifact, dict):
            errors.append(f"entries[{index}]: unknown contract or invalid artifact entry.")
            continue
        artifact_id = artifact.get("artifact_id")
        if not isinstance(artifact_id, str) or not artifact_id:
            errors.append(f"entries[{index}]: artifact_id is missing.")
            continue
        if artifact_id in by_id:
            errors.append(f"duplicate artifact_id {artifact_id!r}.")
            continue
        by_id[artifact_id] = {"contract": contract, "artifact": artifact}
        graph[artifact_id] = []
        if artifact.get("project_id"):
            project_ids.add(artifact["project_id"])

    if len(project_ids) > 1:
        errors.append("all artifacts in one workflow chain must share the same project_id.")

    def refs_for(entry: dict, field: str = "source_artifacts") -> list[dict]:
        value = entry["artifact"].get(field, [])
        return value if isinstance(value, list) else []

    for artifact_id, current in by_id.items():
        seen_refs: set[tuple[str, str, str]] = set()
        for reference in refs_for(current):
            ref_id = reference.get("artifact_id")
            key = (str(ref_id), str(reference.get("contract")), str(reference.get("version")))
            if key in seen_refs:
                errors.append(f"{artifact_id}: duplicate source_artifacts reference {ref_id!r}.")
            seen_refs.add(key)
            target = by_id.get(ref_id)
            if target is None:
                errors.append(f"{artifact_id}: source artifact {ref_id!r} does not exist in this chain.")
                continue
            if (reference.get("contract") != target["contract"]
                    or reference.get("version") != target["artifact"].get("contract_version")):
                errors.append(f"{artifact_id}: source reference {ref_id!r} has a contract or version mismatch.")
                continue
            graph[artifact_id].append(ref_id)
            source = target["artifact"]
            if source.get("status") != "approved":
                errors.append(f"{artifact_id}: source artifact {ref_id!r} is not approved.")
            if source.get("validation", {}).get("status") != "PASS":
                errors.append(f"{artifact_id}: source artifact {ref_id!r} has no validation PASS.")

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> None:
        if node in visiting:
            errors.append(f"artifact dependency cycle detected at {node!r}.")
            return
        if node in visited:
            return
        visiting.add(node)
        for dependency in graph.get(node, []):
            visit(dependency)
        visiting.remove(node)
        visited.add(node)

    for node in graph:
        visit(node)

    def find_contract(contract: str) -> list[tuple[str, dict]]:
        return [(artifact_id, item["artifact"]) for artifact_id, item in by_id.items()
                if item["contract"] == contract]

    def has_source(artifact: dict, target_id: str, target_contract: str) -> bool:
        return any(ref.get("artifact_id") == target_id and ref.get("contract") == target_contract
                   for ref in artifact.get("source_artifacts", []))

    briefs = find_contract("creative-brief")
    stories = find_contract("story-plan")
    edls = find_contract("edit-decision-list")
    plans = find_contract("production-plan")
    qcs = find_contract("qc-report")
    deliveries = find_contract("delivery-manifest")

    for story_id, story in stories:
        if not any(has_source(story, brief_id, "creative-brief") for brief_id, _ in briefs):
            errors.append(f"{story_id}: Story Plan must reference a Creative Brief.")

    for plan_id, plan in plans:
        if not any(has_source(plan, story_id, "story-plan") for story_id, _ in stories):
            errors.append(f"{plan_id}: Production Plan must reference a Story Plan.")
        if edls and not any(has_source(plan, edl_id, "edit-decision-list") for edl_id, _ in edls):
            errors.append(f"{plan_id}: an Edit Decision List exists but is not referenced by the Production Plan.")
        for ref in plan.get("source_artifacts", []):
            if ref.get("contract") == "brand":
                brand = by_id.get(ref.get("artifact_id"))
                if brand and brand["artifact"].get("approval_status") != "APPROVED":
                    errors.append(f"{plan_id}: DigitalNawa Brand Contract is not approved; branded production is blocked.")

    for qc_id, qc in qcs:
        reviewed = qc.get("reviewed_artifacts", [])
        if not any(item.get("contract") == "production-plan"
                   and any(item.get("artifact_id") == plan_id
                           and item.get("version") == plan.get("contract_version")
                           for plan_id, plan in plans)
                   for item in reviewed):
            errors.append(f"{qc_id}: QC Report must review the current Production Plan.")

    for delivery_id, delivery in deliveries:
        qc_id = delivery.get("qc_report_reference")
        qc_entry = by_id.get(qc_id)
        if qc_entry is None or qc_entry["contract"] != "qc-report":
            errors.append(f"{delivery_id}: qc_report_reference must resolve to a QC Report artifact.")
            continue
        qc = qc_entry["artifact"]
        if not has_source(delivery, qc_id, "qc-report"):
            errors.append(f"{delivery_id}: Delivery Manifest must include its QC Report in source_artifacts.")
        if delivery.get("delivery_status") == "READY":
            if qc.get("overall_status") != "PASS" or qc.get("validation", {}).get("status") != "PASS":
                errors.append(f"{delivery_id}: READY delivery requires a QC Report with overall and validation PASS.")
            for index, item in enumerate(delivery.get("deliverables", [])):
                if item.get("size_bytes", 0) <= 0:
                    errors.append(f"{delivery_id}: deliverables[{index}] must have a verified non-zero size.")
                digest = item.get("sha256", "")
                if not digest or set(digest.lower()) == {"0"}:
                    errors.append(f"{delivery_id}: deliverables[{index}] must have a non-placeholder SHA-256.")

    return errors
