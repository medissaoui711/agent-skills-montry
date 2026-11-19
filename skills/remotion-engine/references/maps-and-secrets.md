# Maps, External Providers, and Secrets

## Choose the map source

Use a static map when the story needs a stable geographic background. Use provider vector data when the required feature is available and its source-layer and attributes support the intended visual claim. Use custom GeoJSON only when the content requires geometry or editorial emphasis that the provider data does not supply.

For routes and boundary claims, verify the source geometry and coordinate reference before animating it. Do not infer a geographic fact from a decorative map.

## Render stability

Interactive map engines can produce unstable frames when camera state is updated continuously during headless capture. For moving map shots, test a short render early. If labels, terrain, satellite texture, or line work flicker, evaluate a pre-rendered or fixed map plate rather than repeatedly retrying tile loads.

## API key handling

- Never commit map keys or place them in a public composition prop.
- Supply credentials through environment variables or the approved secret manager.
- Use keys scoped to the required APIs, allowed origins/domains, and quota.
- Rotate leaked keys and record the affected asset or render.
- Verify provider attribution and data licensing before delivery.

Do not use an unrestricted key merely because a sample technique mentions one.

## Official documentation

- [Remotion maps and examples](https://www.remotion.dev/docs)
- [MapTiler API keys](https://docs.maptiler.com/cloud/api/authentication-key/)
- [MapLibre GL JS](https://maplibre.org/maplibre-gl-js/docs/)
