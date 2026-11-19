# Project and Composition

## Before scaffolding

Inspect the target directory, including hidden files. Preserve existing source, environment files, Git metadata, and user changes. If the directory is not empty, choose a new project subdirectory rather than overwriting its contents.

Use the official Remotion project creator for a new project. Confirm Node.js availability and let the scaffold establish a compatible dependency set. Do not invent a package template or silently replace an existing build system.

## Composition model

A Remotion composition is defined by a React component and its render metadata:
- stable composition ID;
- width and height in pixels;
- frame rate;
- duration in frames;
- JSON-serializable default props where appropriate.

Treat frame rate and duration as explicit project inputs. Avoid deriving a different duration independently in multiple components.

Use separate authored composition registrations when the Studio user should be able to edit, reorder, or duplicate each composition independently. Use nested sequences for scene timing and keep the scene plan traceable to the Production Plan.

## Data and defaults

Keep composition inputs serializable. Store editable values in explicit defaults rather than hiding them in computed helper objects. Keep secrets and local machine paths out of serialized props.

## Official documentation

- [Create a Remotion project](https://www.remotion.dev/docs)
- [Compositions](https://www.remotion.dev/docs/composition)
- [Passing props](https://www.remotion.dev/docs/passing-props)
- [Calculate metadata](https://www.remotion.dev/docs/calculate-metadata)
