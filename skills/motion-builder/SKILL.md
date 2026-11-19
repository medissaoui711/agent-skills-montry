---
name: motion-builder
description: Use for building and rendering DigitalNawa motion graphics with code. Uses Remotion / Hyperframes / motion-copy. Must be used after brand-digitalnawa. Never generate logo with AI.
---

# Motion Builder - Code-Based Studio

## Stack

- Primary: Hyperframes (npx hyperframes) + HTML/CSS/JS - For logo, Reels, infographics.
- Alternative: Remotion (React) - For complex data visualizations.
- Reference: motion-copy skill - For copying reference video frame by frame (inspiration only, never copy voice / name / brand of others).

## Setup Check (Run First)

Run in terminal:
node --version
npx hyperframes --help
ffmpeg -version

If any command fails, install it first and confirm with --help. Do NOT proceed to build without passing setup check.

## Build Workflow

1. Read brand-digitalnawa SKILL.md - Get exact colors, fonts, easing, motion sequence.
2. Read reference video if provided - Cut it every 0.1s, list every movement / zoom.
3. Build in code - Use ONLY brand tokens. No hardcoded colors outside brand.
4. Render test at low res - 540x960, 30fps, check Arabic text and logo.
5. Compare - Put render next to reference / original logo, fix any difference. Report differences with timestamps.
6. Final render - 1080x1920, 1080x1080, 1920x1080, 60fps for publishing, 30fps if file too large.

## Code Rules

- Easing: cubic-bezier(0.22, 1, 0.36, 1) everywhere.
- Kinetic Typography: Word by word, not whole sentence at once.
- Highlight box: Red #FF3B3B for problem, Green #00FF9D for solution, Blue #00D4FF for info, Yellow #FFC800 for CTA.
- Text must not cover face / important element. Safe area: Top 15% for headline, Bottom 18% reserved for HUD if used.
- Arabic text: Use Cairo Black, test rendering. If letters disconnect, stop and fix font loading.

## Common Errors - Fix Before Asking User

- Arabic letters disconnected -> Font not loaded. Add @font-face with Cairo Black.
- Logo blurry -> Use SVG / high-res PNG from repo, not AI-generated.
- Colors look off -> Re-read brand-digitalnawa, check hex codes.
- Animation too fast / jittery -> Check easing, must be cubic-bezier above, duration min 0.4s.

## Delivery

Provide: Rendered file paths for 3 sizes, Timeline used, Any deviation from brand and why.
