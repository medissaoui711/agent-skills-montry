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

## Reference routing

Read only the references relevant to the task:

- New project or composition: [Project and Composition](references/project-and-composition.md).
- Scene timing, animation, and frame math: [Timeline and Motion](references/timeline-and-motion.md).
- Arabic or mixed RTL/LTR text: [Arabic and RTL](references/arabic-rtl.md).
- Audio, video, images, and subtitles: [Media and Captions](references/media-and-captions.md).
- Interactive preview and export: [Studio and Rendering](references/studio-and-render.md).
- Maps or external map providers: [Maps and Secrets](references/maps-and-secrets.md).
- Studio-editable parameters: [Interactive Editing](references/interactive-editing.md).
- Version and licensing checks: [Version and License](references/version-and-license.md).

## Execution policy

1. Validate the Production Plan and all referenced artifact IDs.
2. Confirm that asset paths resolve and that external assets have appropriate usage rights.
3. Confirm that the installed Remotion packages form a compatible, pinned version set.
4. Build or update the Remotion composition from the plan; do not invent brand tokens.
5. Start Remotion Studio as soon as the project can run. Open the exact URL printed by the process and verify that the composition preview loads.
6. Keep preview as the default review surface while changes are being made.
7. Run final rendering only when the user explicitly requests export.
8. Record the actual renderer version, composition ID, dimensions, frame rate, duration, and output file metadata.
9. Hand the preview or rendered artifact to QC Checker. Do not self-issue a QC PASS.

## Safety and secrets

- Never place API keys, provider tokens, or credentials in source files or committed configuration.
- Use least-privilege, scoped provider keys supplied through environment variables.
- Do not use a provider key described as unrestricted; verify scopes, domains, quotas, and rotation.
- Do not describe an untested preview or render as successful.
- Do not bypass licensing checks for commercial or automated rendering.
- Do not accept user-uploaded arbitrary Remotion projects for a hosted rendering service without confirming that the current Remotion terms permit the exact model.

## Knowledge provenance

The owner-supplied archive is used as a research input, not copied verbatim. See [Remotion upstream source and import policy](../../docs/remotion/upstream-source.md). Local references are original summaries and implementation rules; consult official Remotion documentation for current API details.
