# Timeline and Motion

## Timebase

Use frames as the authoritative time unit inside the composition. Convert seconds to frames through the composition FPS and preserve the conversion in the Production Plan. Avoid mixing milliseconds, seconds, and frame numbers without an explicit conversion.

For each scene, record its start frame and duration. Confirm that the final frame range remains within the composition duration. Keep scene IDs stable across revisions.

## Animation

Drive animation from the current Remotion frame. Use Remotion's interpolation and easing APIs for deterministic motion. Clamp values when the intended animation must remain within a bounded range.

Do not use browser timers, wall-clock time, or CSS transitions as the source of animation timing. They can make output depend on render speed or browser state.

Prefer reusable motion components and data-driven keyframes. Do not impose a universal scene-length limit or a single easing curve on every video; the approved Story Plan and content purpose determine the rhythm.

## Transitions

Use explicit transition intent from the Story Plan. Check that adjacent scenes do not produce unintended blank frames, abrupt audio gaps, or overlapping elements. If a transition requires overlap, model that overlap deliberately in the frame ranges.

## Official documentation

- [Using interpolate](https://www.remotion.dev/docs/interpolate)
- [Easing](https://www.remotion.dev/docs/easing)
- [Sequence](https://www.remotion.dev/docs/sequence)
- [Timing](https://www.remotion.dev/docs/timing)
