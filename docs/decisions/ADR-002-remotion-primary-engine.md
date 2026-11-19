# ADR-002: Remotion as the Primary Production Engine

**Status:** Accepted as architecture direction; production use remains gated  
**Date:** 2026-11-19

## Decision

Remotion is the primary execution engine for DigitalNawa Studio. Hyperframes is not used as the default path. Any future exception requires a documented technical case and explicit scope.

## Constraints

- Preview precedes final render.
- Final render requires an explicit user export request.
- Remotion package versions must be pinned as a compatible set.
- License applicability must be checked against the actual entity, involved-party headcount, code ownership, and rendering model. Do not assume a paid license is always required; the official Free License may apply to eligible individuals and teams of up to three people.
- Hosted automation or rendering services must be checked against the current terms, especially rules about user-supplied Remotion projects.
- Secrets and map-provider keys must be supplied through secure environment configuration, never committed to the repository.
- The attached Remotion reference archive is not copied verbatim. The inspected upstream repository has no declared license in its GitHub metadata and no root LICENSE file in the tree. Local reference notes are independently written and link to official documentation.
