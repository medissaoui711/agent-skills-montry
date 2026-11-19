# Studio Preview and Final Rendering

## Preview-first workflow

As soon as the Remotion project can run, start Studio and obtain its exact printed URL. Open that exact URL in the available browser and verify that Studio and the intended composition load. Keep Studio available while the user reviews and steers the work.

A running process is not proof that the preview works. Record whether the browser opened, whether the composition was listed, and whether its preview rendered.

## Final rendering

Do not render by default. Render only after the user explicitly asks to export, render, or provide a final video file.

Before rendering:
- identify the exact composition ID;
- confirm the expected output path;
- validate width, height, FPS, and duration;
- confirm that assets are available to the render process;
- check license applicability;
- confirm that the render profile matches the delivery requirements.

After rendering, verify the output exists and inspect its metadata. Do not invent a path or report success from a command that was not observed to complete.

## Delivery evidence

Record the composition ID, Remotion version, render command/profile, output path, file size, checksum, dimensions, frame rate, duration, and QC report reference in the Delivery Manifest.

## Official documentation

- [Remotion Studio](https://www.remotion.dev/docs/studio)
- [Render CLI](https://www.remotion.dev/docs/cli/render)
- [Still CLI](https://www.remotion.dev/docs/cli/still)
