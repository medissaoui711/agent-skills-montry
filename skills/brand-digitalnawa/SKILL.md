---
name: brand-digitalnawa
description: Resolve and verify the official DigitalNawa brand identity from its source repository. Use before any production that claims DigitalNawa branding. Never infer missing assets or tokens.
---

# Brand — DigitalNawa

## Purpose

This skill is the identity resolver. It does not invent or redesign the brand. It reads the owner-designated source and produces a Brand Contract that other skills consume.

## Official source candidate

- Repository: https://github.com/medissaoui711/DigitalNawa-Brand-Project
- Previously designated logo location: `DigitalNawa/03-Logo-Assets`

The repository path and assets must be checked at the current revision. If the repository or expected path cannot be inspected, report WAITING_FOR_INPUT and ask the owner for the authoritative source or files.

## Required verification

1. Record the repository URL, ref/commit, and exact asset paths.
2. Inspect the original logo files and their formats.
3. Locate authoritative color tokens and record exact values and source references.
4. Locate typography declarations and verify font availability and usage rights.
5. Identify motion, intro, outro, and layout rules only when they are explicitly documented.
6. Record conflicting or obsolete instructions as LEGACY or UNVERIFIED; do not silently choose between them.
7. Prepare `contracts/brand.schema.json` output.

## Approval policy

- Initial status is `UNVERIFIED`.
- Use `PENDING` when the source has been inspected but owner confirmation is required.
- Use `APPROVED` only after the authoritative assets and tokens have been verified and the owner has approved the Brand Contract.
- Use `REJECTED` when the owner rejects the proposed identity data.
- A schema-valid Brand Contract is not automatically an approved brand.

## Official naming

- English name: DigitalNawa
- Arabic name: ديجيتال نواة
- The spelling "ديجيتال نوى" is incorrect.

## Legacy conflict handling

Older skill copies contain conflicting palettes, backgrounds, typography, and mandatory motion sequences. Treat all such embedded values as LEGACY / UNVERIFIED until checked against the official source. Do not apply them to production by memory.

## Failure behavior

If the logo, palette, font, source revision, or license evidence is missing, state exactly what is missing and block only the brand-dependent production. Never generate a substitute logo or claim a match that was not inspected.
