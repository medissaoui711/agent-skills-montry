# Media and Captions

## Asset inventory

Every image, video, audio file, font, and external media reference must have a stable asset ID and a known source. Record usage rights and any attribution requirement before adding it to a production composition.

Prefer project-managed local assets for repeatable renders. If an asset is remote, verify that it is stable, reachable in the render environment, and permitted for the intended use. Do not depend on a transient URL or an authenticated browser session.

## Video and audio

Use the correct Remotion media components and wait for asynchronous media readiness when the composition requires it. Check duration, dimensions, audio presence, and any trim boundaries before constructing the timeline.

Audio checks include synchronization, clipping, abrupt cuts, and level consistency. If the audio cannot be inspected, QC must say NOT_VERIFIED.

## Captions

Keep caption content in structured data rather than embedding subtitle timing in unrelated JSX. Each caption entry should identify its text and start/end time, with a documented timebase. Validate that times are non-negative, ordered, and within the media duration.

For Arabic captions, apply the RTL guidance in [Arabic and RTL](arabic-rtl.md). Do not split Arabic letters for karaoke effects without a dedicated shaping test.

## Official documentation

- [Images](https://www.remotion.dev/docs/img)
- [Video](https://www.remotion.dev/docs/video)
- [Audio](https://www.remotion.dev/docs/audio)
- [Captions](https://www.remotion.dev/docs/captions)
- [Static files](https://www.remotion.dev/docs/staticfile)
