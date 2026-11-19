---
name: motion-builder
description: Convert an approved Story Plan and optional Edit Decision List into a structured Remotion Production Plan. Does not own brand identity or final QC.
---

# Motion Builder — Production Planner

## Responsibility

Translate approved creative and editorial artifacts into a deterministic Production Plan. Remotion Engine performs execution. This skill does not independently select a rendering framework or claim that a render exists.

## Required inputs

- Valid Story Plan.
- Valid Edit Decision List when supplied footage requires editing.
- Approved Brand Contract when DigitalNawa identity is requested.
- Asset inventory with source paths and usage-rights status.
- Target dimensions, frame rate, and delivery format from the Creative Brief or user.

If required inputs are missing, stop and identify them.

## Planning workflow

1. Resolve the composition dimensions, frame rate, and duration in frames.
2. Map each Story Plan scene to a composition scene and frame interval.
3. Reference assets by stable IDs; do not embed secrets or invent missing media.
4. Define transitions, animation timing, typography, and audio decisions.
5. Consume brand tokens from the approved Brand Contract only. Do not hardcode palette or font values.
6. Record unknown assets, fonts, rights, and technical assumptions as UNVERIFIED.
7. Produce data compatible with `contracts/production-plan.schema.json`.

## Remotion conventions

- Remotion is the primary execution engine.
- Keep project dependencies pinned to a compatible version set.
- Use frame-based timing and deterministic composition inputs.
- Prefer reusable components and data-driven scene definitions.
- Prepare preview before final rendering.
- Final render requires an explicit export request from the user.

## Handoff

Pass the Production Plan and referenced artifacts to `remotion-engine`. Do not self-certify render success or QC status.
