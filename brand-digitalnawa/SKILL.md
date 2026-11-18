---
name: brand-digitalnawa
description: DigitalNawa brand source of truth. Use FIRST for any DigitalNawa video. Loads logo, colors, fonts, and motion identity from GitHub repo. Never guess brand assets.
---

# Brand - DigitalNawa

## 1. Source of Truth (Do Not Guess)

- Repo: https://github.com/medissaoui711/DigitalNawa-Brand-Project
- Logo source ONLY: DigitalNawa/03-Logo-Assets
- If logo file is not found in repo, STOP and ask user to upload logo PNG/SVG. Do NOT generate a similar logo with AI.

## 2. Visual Identity

- Background: #050810 (dark blue-black)
- Grid: Subtle dot grid, opacity 8%
- Danger / Problem: #FF3B3B
- Solution / Success: #00FF9D
- Info: #00D4FF
- Warning / CTA: #FFC800
- Text Primary: #FFFFFF
- Text Secondary: #A8B0C0
- Font English: Space Grotesk Bold / Inter ExtraBold
- Font Arabic: Cairo Black / Tajawal ExtraBold
- On-screen text: Max 5 words per screen, kinetic typography, word by word.

## 3. Motion Identity - MANDATORY

- Easing for ALL animations: cubic-bezier(0.22, 1, 0.36, 1)
- Max scene duration: 3.5 seconds. Cut, zoom 105%, or new element every 3.5s.
- No Linear easing. No Bounce easing.

Sequence for EVERY video:
1. START: Rising Pixels - 24 pixels rise from bottom, Stagger 0.04s, Opacity 0 -> 100%
2. ASSEMBLY: Pixels assemble into original logo
3. REVEAL: ديجيتال نوى -> morph to DigitalNawa (same weight, smooth)
4. END: Slogan lockup Build. -> Innovate. -> Teach. word by word, Scale 95% -> 100% each word, Hold 0.8s, Fade Out

## 4. Logo Video Spec (Pilot 9s)

- Duration: 9.0 seconds, 60fps
- Exports: 1080x1920 (Reels), 1080x1080 (Post), 1920x1080 (YouTube)
- Timeline:
  - 0.0-2.0s Rising Pixels
  - 2.0-3.5s Assembly to Logo
  - 3.5-5.5s Name Reveal Arabic -> English
  - 5.5-8.0s Slogan Build. Innovate. Teach.
  - 8.0-9.0s Hold + Fade Out
- Audio: Light whoosh + ding only. No loud music.

## 5. Failure Rules

- If Arabic text ديجيتال نوى is distorted, REJECT and fix font. Arabic letters must be perfect.
- If logo differs from repo file by even 1%, REJECT.
- If colors differ, REJECT and re-read repo.
