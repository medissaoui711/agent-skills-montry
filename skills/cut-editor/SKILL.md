---
name: cut-editor
description: Prepare evidence-based edit decisions for supplied footage, including trimming, clip extraction, and loop planning. Produces an Edit Decision List; does not claim to execute edits.
---

# Cut Editor

## Scope

Use only when the user supplies raw footage, a transcript, timestamps, or a media inventory that needs editing. This skill plans edits and produces an Edit Decision List (EDL). It does not render.

## Required source data

Record the source media identifier, URI or path, duration, and timebase (FPS). Use transcript timestamps or inspected media evidence. Never invent timestamps.

## Trim decisions

Identify false starts, repeated introductions, off-topic sections, redundant explanations, and filler only when removal preserves meaning.

For every proposed cut record:
- source media ID
- exact in-frame and out-frame
- preceding and following spoken words when a transcript exists
- reason for the cut
- cover-shot requirement
- expected time saved
- confidence or evidence limitation

Keep pauses that support comprehension, tone, or humour. Warn when a cut could strengthen or distort a claim.

## Clip extraction

Extract candidate clips only when each can stand alone with a clear idea and adequate context. Record exact frame ranges and explain any context that must be added.

## Loop planning

Propose visual and/or audio loop points only when the source supports them. Do not sacrifice the story's conclusion merely to create a loop.

## Output

Produce `contracts/edit-decision-list.schema.json` compatible data. Validate that:
- each segment references an existing source media ID;
- `out_frame` is greater than `in_frame`;
- the range does not exceed the known source duration;
- timeline positions are non-negative;
- the timebase is explicit.

If a condition cannot be verified, mark it NOT_VERIFIED and do not claim the EDL is ready for execution.
