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

Run:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_contracts.py
python scripts/validate_plugin.py
python -m unittest discover -s tests -v
```

The contract validator checks all schema documents and validates the checked-in Brand Contract instance. Unit tests cover schema validity, Brand Contract gates, unknown properties, invalid color values, and selected cross-field invariants.

## Semantic invariants

Some constraints span multiple fields or artifacts and cannot be expressed clearly in the current schemas. `scripts/semantic_validation.py` checks:
- QC PASS requires evidence for every passing check and every check must pass.
- EDL segments must reference known source media, have a positive frame range, and remain within source duration.
- Production scenes must fit within the composition duration and have unique IDs.

## Brand gate

A schema-valid Brand Contract is not automatically approved. The current contract preserves the five core palette values recorded as approved, while the overall contract remains PENDING because logo geometry/lockup, typography, licensing, and final asset acceptance remain unresolved. Production requiring DigitalNawa branding must not proceed as if the full identity were approved.
