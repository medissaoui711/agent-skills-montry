# Phase 2 — Integration and Runtime Verification

## Scope implemented in this branch

- Validate a synthetic artifact chain across Creative Brief, Story Plan, Edit Decision List, Production Plan, QC Report, and Delivery Manifest.
- Resolve each source-artifact reference by artifact ID, contract slug, and exact contract version.
- Reject duplicate IDs, missing references, version mismatches, cross-project chains, and dependency cycles.
- Enforce workflow edges: Brief → Story, Story → Production, optional EDL → Production, Production → QC, QC → Delivery.
- Require source artifacts to be approved and validation-PASS before downstream consumption.
- Block branded production when its referenced Brand Contract is not approved.
- Prevent a READY delivery from claiming success without QC PASS and non-placeholder deliverable metadata.
- Run the official Claude Code plugin validator in CI and load the plugin to inspect its component inventory.

## Commands

    python -m pip install -r requirements-dev.txt
    python scripts/validate_contracts.py
    python scripts/validate_plugin.py
    python scripts/validate_workflow.py
    python -m unittest discover -s tests -v
    claude plugin validate . --strict
    claude --plugin-dir . plugin details montry

## Synthetic fixture boundary

Files under tests/fixtures/workflow/ are deliberately synthetic. Their example.invalid URLs, checksum, and byte count are placeholders for schema and gate testing only. They are not real media, evidence, or a delivery manifest for a customer.

## Runtime verification status

### Claude Code

The CI workflow installs the official Claude Code CLI, runs the strict plugin validator, and asks Claude Code to load the local plugin and print its component inventory. This checks the native manifest/skill loader without requiring an Anthropic API key.

An authenticated interactive session is still needed to verify real skill invocation, skill-to-skill handoffs, and behavior under a user prompt. The CI job does not claim to have performed those model-driven evaluations.

### Remotion

The repository currently has no Remotion application project, package manifest, lockfile, or approved license decision record. The Remotion Studio preview test is therefore BLOCKED, not passed. Do not scaffold a production project, launch a customer-facing render service, or run a final render until the owner records the applicable license/use model and authorizes the runtime test.

When the gate is closed, the follow-up runtime check should use a minimal isolated composition, pinned compatible Remotion packages, and a preview-only Studio health check. Final rendering remains outside this phase unless separately requested.

## Exit criteria

- All artifact-chain integration tests pass.
- Claude Code native strict plugin validation passes.
- Claude Code loads the plugin and reports all seven registered skills without load errors.
- Remotion preview remains explicitly BLOCKED until licensing and project-environment prerequisites are verified.
