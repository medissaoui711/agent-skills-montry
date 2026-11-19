# Version and License Controls

## Version pinning

Use one compatible Remotion release across `remotion`, `@remotion/cli`, and any installed `@remotion/*` packages. Pin exact versions in the package manifest and lockfile. Do not mix versions copied from examples or use `latest` in production setup.

When updating, review the official upgrade guidance, update the related packages as a set, and run the composition, preview, and render tests before accepting the change.

## Upstream skill reference version

The owner-supplied archive reports version `4.0.536`. The upstream `remotion-dev/skills` repository inspected on 2026-11-19 reports version `4.0.545`. The archive is therefore stale relative to the inspected upstream revision.

## Licensing gate

The Remotion license is proprietary/source-available, not an OSI open-source license. Eligibility depends on the user or organization and the actual usage model.

As inspected on 2026-11-19, the official FAQ describes a Free License for individuals and organizations/teams up to three people, with additional categories and conditions. For organizations not eligible for the Free License, the official pricing page distinguishes Creator seats and Automator render-based usage. Automation plans and rendering-service restrictions must be assessed against the exact business model.

Before production use, record:
- legal entity and total headcount of involved parties;
- who owns and operates the Remotion codebase;
- whether the workflow is manual creation or programmatic automation;
- whether customers only receive finished media or can submit their own Remotion code;
- applicable plan, terms, and any written permission required.

Do not assume the Free License or a paid plan applies without checking the current terms for the actual situation. This reference is operational guidance, not legal advice.

## Official sources

- [License and Pricing](https://www.remotion.dev/docs/license/pricing)
- [License FAQ](https://www.remotion.dev/docs/license/faq)
- [Terms and Conditions](https://www.remotion.dev/docs/terms)
- [Remotion upgrade guide](https://www.remotion.dev/docs/upgrading)
