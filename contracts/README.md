# Contract Registry

All contracts use JSON Schema Draft 2020-12. The schemas define artifact structure; they do not prove that the artifact's claims are true or that a workflow stage actually ran.

| Contract | Producer | Purpose |
|---|---|---|
| brand | Brand DigitalNawa | Identity tokens, asset references, approval state |
| creative-brief | Montry / Creative | Audience, objective, platform, constraints |
| story-plan | Creative planning | Ordered narrative scenes |
| production-plan | Motion Builder | Remotion composition and scene instructions |
| edit-decision-list | Cut Editor | Frame-based source-footage edit decisions |
| qc-report | QC Checker | Evidence-backed check results |
| delivery-manifest | Delivery | Actual deliverables and integrity metadata |

## Common envelope

Every artifact includes `contract_version`, `project_id`, `artifact_id`, `created_at`, `producer`, `status`, `source_artifacts`, and `validation`.

- Contract versions use semantic version syntax.
- `source_artifacts` records exact upstream artifact IDs and versions.
- `validation.status` is one of PASS, FAIL, NOT_VERIFIED, or BLOCKED.
- `status` describes artifact lifecycle; it is not the QC result.
- Producers must create a new artifact rather than silently mutate an approved artifact.

## Validation

Run `python scripts/validate_contracts.py`. The validator requires the pinned development dependency in `requirements-dev.txt`. Contract schemas are structural contracts; domain-level invariants such as EDL frame ranges and total scene duration also require semantic tests before production use.

## Brand gate

A schema-valid Brand Contract is not automatically approved. Production requiring DigitalNawa branding must stop unless `approval_status` is APPROVED and all referenced assets have been verified against the official source.
