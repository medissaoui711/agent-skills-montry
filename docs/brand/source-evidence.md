# DigitalNawa Brand Source Evidence

**Inspected repository:** [DigitalNawa-Brand-Project](https://github.com/medissaoui711/DigitalNawa-Brand-Project)  
**Inspected ref:** `main`  
**Commit:** `bf2d22c54048a72ce87579e29d1fc4e6c50fab05`

## Verified from repository content

### Core palette

The local decision record `docs/governance/DN-GOV-001-Central-Decision-Register-v1.0.0.md`, section DN-DEC-006, records the exact core palette as APPROVED:

| Token | Value |
|---|---|
| Warm Ivory | `#FEF3C7` |
| Warm Gray | `#78716C` |
| Muted Teal | `#0EA5A4` |
| Dark Brown | `#1C1917` |
| Warm Orange | `#EA5808` |

The continuation owner-decision register at `work/DN-BRAND-001-FINAL-QA-CONTINUATION-003/OWNER-DECISION-REGISTER.md` states that the core palette was explicitly approved in the WP02 owner brief and must be preserved. It also cautions that the central DN-GOV-001 document itself remains draft/pending. Therefore this contract marks the five core color tokens APPROVED while retaining an overall Brand Contract status of PENDING.

### Typography

DN-DEC-007 and the visual-system foundation identify Inter, Cairo / IBM Plex Sans Arabic, and JetBrains Mono as candidates, not final approved selections. The repository tree contains no WOFF, WOFF2, TTF, or OTF font files. Font licensing, embedding, and deployment remain unverified.

### Logo assets

The repository contains master SVGs and light/dark/monochrome variants. However:
- The visual-system foundation says the symbol SVG is a geometric reconstruction from the written concept, not an exact trace of the original reference.
- DN-DEC-004 approves the symbol direction only, not the final Master SVG or final logo lockup.
- DN-DEC-005 records exact fidelity to the original reference as NOT VERIFIED.
- The asset manifest status is `draft`, and final package acceptance is NOT VERIFIED.

The Brand Contract therefore references candidate masters as UNVERIFIED and does not represent them as approved production artwork.

### Motion and tagline

DN-DEC-002 records the official tagline `Build. Innovate. Teach.` as approved. This does not establish a mandatory opening/closing sequence for every video. The symbol concept includes rising pixels, but the inspected evidence does not approve the old fixed 24-pixel intro sequence, 3.5-second scene cap, or specific easing/timing rules as universal video requirements.

### Contrast

The visual-system foundation reports these ratios:
- Dark Brown on Warm Ivory: 15.71:1.
- Warm Gray on Warm Ivory: 4.31:1.
- Muted Teal on Warm Ivory: 2.7:1.
- Warm Orange on Warm Ivory: 3.20:1.

The same source notes that teal and orange are accents, not normal-sized text on Warm Ivory. Actual combinations still require per-use validation.

## Current contract status

The file `shared/brand/brand-contract.json` is a traceable, partially resolved contract:
- Core palette tokens: APPROVED within the recorded decision scope.
- Logo master files: UNVERIFIED.
- Typography: PROVISIONAL.
- Mandatory intro: none established.
- Official tagline: approved, but not mandatory for every video.
- Overall Brand Contract: PENDING.
- Validation: NOT_VERIFIED.

Brand-dependent production must not treat the overall identity as fully approved until the remaining owner decisions and source acceptance gates are closed.
