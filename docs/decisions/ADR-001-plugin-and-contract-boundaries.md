# ADR-001: Single Plugin, Independent Skills, Versioned Contracts

**Status:** Accepted  
**Date:** 2026-11-19

## Decision

Keep one plugin with independent specialist skills. Use versioned JSON artifacts as the interface between skills. Montry owns workflow coordination; each specialist owns its output artifact.

## Consequences

- Skills remain independently discoverable and maintainable.
- Artifact schemas can be validated independently of prompt wording.
- A skill cannot claim that another skill's work occurred without a referenced artifact.
- Runtime enforcement remains a separate concern and is not implied by this decision.
