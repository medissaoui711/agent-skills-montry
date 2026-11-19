# ADR-002: Remotion as the Primary Production Engine

**Status:** Accepted as architecture direction; commercial operation is gated  
**Date:** 2026-11-19

## Decision

Remotion is the primary execution engine for DigitalNawa Studio. Hyperframes is not used as the default path. Any future exception requires a documented technical case and explicit scope.

## Constraints

- Preview precedes final render.
- Final render requires an explicit user export request.
- Remotion package versions must be pinned as a compatible set.
- License applicability must be verified before commercial or automated production.
- Secrets and map-provider keys must be supplied through secure environment configuration, never committed to the repository.
- The attached Remotion reference archive is not copied wholesale in this change. Its upstream provenance, version drift, duplicate files, and licensing must be checked before import.
