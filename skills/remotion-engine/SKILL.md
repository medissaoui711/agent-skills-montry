---
name: remotion-engine
description: Primary execution adapter for DigitalNawa Studio video projects built with Remotion. Use when translating an approved Production Plan into a Remotion preview or an explicitly requested final render.
---

# Remotion Engine

## Responsibility

Execute an approved Production Plan with Remotion. This skill is an implementation adapter, not the creative director, brand authority, or QC authority.

## Required inputs

- A valid Production Plan artifact.
- Its referenced Story Plan and, when applicable, Edit Decision List.
- An approved Brand Contract when the video uses DigitalNawa identity.
- Available media assets with known paths and usage rights.
- A project environment with a pinned, compatible Remotion toolchain.

If a required input is missing, invalid, or blocked, stop and report the exact prerequisite.

## Execution policy

1. Validate the Production Plan and all referenced artifact IDs.
2. Confirm that asset paths resolve and that external assets have appropriate usage rights.
3. Build or update the Remotion composition from the plan; do not invent brand tokens.
4. Prepare a preview first and report its location and technical properties.
5. Run final rendering only when the user explicitly requests export.
6. Record the actual renderer version, composition ID, dimensions, frame rate, duration, and output file metadata.
7. Hand the preview or rendered artifact to QC Checker. Do not self-issue a QC PASS.

## Safety and secrets

- Never place API keys, provider tokens, or credentials in source files or committed configuration.
- Use least-privilege, scoped provider keys supplied through environment variables.
- Do not describe an untested render as successful.
- Do not bypass licensing checks for commercial or automated rendering.

## Knowledge references

The Remotion best-practices archive supplied by the repository owner is a candidate reference source. It is not treated as an executable project or as 11 independently installable skills. Import and update its reference material only after provenance, license, duplication, and version checks.
