# Arabic and Mixed RTL/LTR Text

## Direction and language

Set both language and base direction on the smallest container that owns the Arabic text. For Arabic, use the appropriate Arabic language tag and RTL direction. Do not set the entire composition to RTL if it also contains English, URLs, code, or numeric sequences that require LTR handling.

Keep mixed Arabic/English phrases, product names, handles, dates, and numeric runs grouped so that the browser's bidirectional algorithm can lay them out correctly.

## Shaping

Arabic characters are shaped according to their neighboring characters. Do not split Arabic words into isolated per-letter spans for ordinary kinetic typography. Prefer line-level or word-level animation while keeping each Arabic word intact.

If per-character animation is a genuine requirement, treat it as a specialized typography task: preserve combining marks, ligatures, joining behavior, and mixed-direction runs, then verify the result in the exact browser used for rendering. Do not assume that a technique that works in headless Chromium will render identically in Safari or mobile browsers.

## Fonts

Use only a font that is approved by the Brand Contract when producing DigitalNawa-branded work. Otherwise ask the user to select or supply a font. Verify glyph coverage, shaping, fallback behavior, and font licensing. Do not assume that a font installed on the developer's machine exists on the render machine.

## Required QA

- Inspect Arabic words at full output resolution.
- Check joined letters, diacritics, punctuation, and line breaks.
- Check Arabic text adjacent to English words and digits.
- Verify RTL alignment and safe areas.
- Mark typography NOT_VERIFIED if the actual rendered preview is unavailable.

## Official documentation

- [Remotion text and fonts](https://www.remotion.dev/docs)
- [CSS direction](https://developer.mozilla.org/en-US/docs/Web/CSS/direction)
- [Unicode Bidirectional Algorithm](https://www.unicode.org/reports/tr9/)
