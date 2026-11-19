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
