# Interactive Editing in Remotion Studio

## Purpose

Use Studio interactivity when the owner or editor needs to adjust exposed values without changing source code. Keep the interactive surface intentional and limited to parameters that are safe to change.

## Rules

- Expose stable, serializable values such as titles, colors, positions, and selected assets when the project design supports them.
- Keep editable values in explicit component props or the supported inline metadata expected by the installed Remotion version.
- Avoid hidden computed state when the user expects Studio to write an edit back to source.
- Validate user-edited values before they reach composition logic.
- Do not expose secrets, internal file paths, or unrestricted external URLs as editable controls.

## Official documentation

- [Remotion Studio interactivity](https://www.remotion.dev/docs/studio/interactivity)
