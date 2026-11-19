# Workflow State Model

**Version:** 1.0.0

## Workflow states

- `PENDING`: prerequisites have not yet been evaluated.
- `IN_PROGRESS`: the current stage is actively being prepared or executed.
- `WAITING_FOR_INPUT`: required user input or an external artifact is missing.
- `BLOCKED`: a prerequisite, policy, validation, or approval gate prevents progress.
- `COMPLETED`: the stage produced its required artifact and passed its exit checks.
- `CANCELLED`: the user cancelled the workflow.

Workflow state and QC state are separate dimensions.

## QC states

- `PASS`: the defined check was executed and supported by evidence.
- `FAIL`: the check was executed and found a violation.
- `NOT_VERIFIED`: the check could not be completed or evidence is absent.
- `BLOCKED`: policy or a prerequisite prevented the check.

## Conditional workflow

1. Request intake and Creative Brief.
2. Brand validation when DigitalNawa identity is in scope.
3. Hook analysis when useful to the requested narrative; no fixed duration threshold.
4. Story Plan.
5. Cut Editor only when source footage needs selection, trimming, or extraction.
6. Production Plan.
7. Remotion preview.
8. QC validation.
9. Final render only after explicit export request and required gates.
10. Delivery Manifest.

## Transition invariants

- A downstream stage cannot consume a missing or invalid required artifact.
- Cut Editor precedes final Motion production when source-footage edits are required.
- Brand-dependent production is blocked when the required identity data is unverified.
- Preview availability does not imply final render completion.
- Delivery readiness requires a QC report and verifiable deliverable metadata.
- A blocked or NOT_VERIFIED check cannot be silently converted to PASS.

## Failure handling

Every blocked transition records: stage, prerequisite, reason, responsible owner, and the action required to resume. Retry creates a new attempt record; it does not erase the prior failure.
