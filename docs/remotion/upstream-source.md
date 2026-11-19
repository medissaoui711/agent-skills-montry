# Remotion Upstream Source and Import Policy

**Inspection date:** 2026-11-19

## Sources inspected

- Owner-supplied archive: `remotion-best-practices.zip`
- Upstream repository: https://github.com/remotion-dev/skills
- Upstream package metadata: `@remotion/skills`
- Upstream documentation: https://www.remotion.dev/docs/ai/skills

## Version comparison

| Source | Version |
|---|---|
| Supplied archive router | 4.0.536 |
| Upstream repository package and router at inspection | 4.0.545 |

The archive is behind the inspected upstream source. It contains duplicated directory trees and nested map references; it is a knowledge/reference bundle, not a complete Remotion project with package manifest and lockfile.

## License and redistribution finding

The inspected GitHub repository metadata reports no declared repository license, and the inspected default-branch tree contains no root `LICENSE` file. Public visibility is not a redistribution license.

Therefore this repository does **not** copy the upstream Router, reference files, code examples, icons, or map assets verbatim. Instead, the local Remotion Engine contains independently written operational summaries and links to official Remotion documentation. If a later decision requires verbatim import, obtain and record explicit permission or a verifiable license first.

## Integration scope

The local references cover:
- project scaffolding and composition metadata;
- frame-based timing and deterministic motion;
- Arabic/RTL shaping and mixed-direction content;
- media inventory and caption timing;
- Studio preview and explicit rendering;
- map-provider stability and secret handling;
- Studio-editable values;
- version pinning and license checks.

Specialized techniques such as Cesium, Mapbox, MapLibre, MapTiler, and advanced media workflows remain optional. They should be introduced only for a real task, after their provider licenses, data attribution, API keys, and runtime requirements are verified.

## Safety corrections

- Do not reuse unrestricted provider keys from examples.
- Do not treat an archive version as the current Remotion version.
- Do not claim a render succeeded without output evidence.
- Do not render final output unless explicitly requested.
- Do not assume Remotion licensing is free or paid without evaluating the actual headcount and usage model.

## Official references

- [Remotion Agent Skills](https://www.remotion.dev/docs/ai/skills)
- [Remotion License and Pricing](https://www.remotion.dev/docs/license/pricing)
- [Remotion License FAQ](https://www.remotion.dev/docs/license/faq)
- [Remotion Terms](https://www.remotion.dev/docs/terms)
- [Remotion CLI](https://www.remotion.dev/docs/cli)
