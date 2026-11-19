# DigitalNawa Studio — Architecture Specification

**Status:** Approved architecture baseline; implementation details remain subject to the open gates.  
**Version:** 1.0.0

## System boundary

DigitalNawa Studio is a single Claude Code plugin containing independent specialist skills. The skills exchange versioned artifacts through JSON contracts. Montry coordinates workflow; it does not claim that prose instructions alone provide runtime enforcement.

## Layers

1. **Orchestration:** Montry receives the request, selects the applicable workflow, checks prerequisites, and records blocked transitions.
2. **Creative:** Brand DigitalNawa resolves approved identity data; Hook Analyzer develops an opening when the narrative needs one.
3. **Editorial:** Cut Editor creates an Edit Decision List when source footage requires trimming.
4. **Production:** Motion Builder translates the approved Story Plan and Edit Decision List into a Production Plan. Remotion Engine is the primary execution adapter.
5. **Quality:** QC Checker evaluates artifacts and rendered outputs using evidence-backed checks.
6. **Delivery:** Delivery Manifest records actual files and their verifiable metadata.

## Ownership rules

- Every artifact has one producer and a stable artifact ID.
- Consumers must not silently mutate upstream artifacts.
- A change creates a new artifact version and invalidates dependent approvals where relevant.
- Missing evidence is NOT_VERIFIED, never PASS.
- A failed prerequisite blocks downstream execution.
- Final rendering is performed only when the user requests export.
- Brand values are read from the approved Brand Contract; this repository must not invent them.

## Primary engine

Remotion is the primary video execution engine. Hyperframes is not part of the default production path. Retaining or reintroducing it requires a documented technical decision and a bounded use case.

## Open gates

- **Brand gate:** verify the original DigitalNawa assets, colors, fonts, and their sources before approving a Brand Contract.
- **License gate:** verify Remotion license applicability for the owner's team size, business model, and automated rendering use before commercial operation.
- **Runtime gate:** JSON contracts and skill instructions do not themselves guarantee orchestration enforcement. Any runtime automation must be separately designed, tested, and documented.

## Repository layout

See the root tree and `contracts/README.md`. The intended separation is skills, contracts, shared brand data, validation scripts, tests, and documentation.
