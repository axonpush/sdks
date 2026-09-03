# Changelog

The format is [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this
package follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] – 2026-09-02

First release. Until now the .NET SDK was the only client without a generated
API layer, exposed one of twenty resources, and had never been published — the
NuGet badge in the README pointed at a package that did not exist.

### Added
- **A generated API client.** NSwag emits `Internal/Api/AxonPushApi.g.cs` from
  `contract/openapi.sdk.json`, the same contract the TypeScript and Python
  clients are generated from. `dotnet nswag run nswag.json` regenerates it, and
  CI fails if the checked-in copy drifts.
- **All twenty resources**, matching the TypeScript and Python surfaces method
  for method: alerts, analytics, api keys, apps, assessments, channels,
  datasets, environments, evaluation targets, evaluators, events, experiments,
  gates, issues, online evaluations, organizations, prompts, trace
  intelligence, traces, traces v2 and webhooks. They are generated from the
  TypeScript surface by `tools/generate-dotnet-resources.py`, so parity holds by
  construction and `tools/surface-diff.ts` proves it.
- **`AxonPush.Cli`**, packed as the `axonpush-eval` dotnet tool. It replays a
  dataset revision against a local evaluator command and applies the release
  gate, with the same six exit codes (`0` passed, `1` gate blocked, `2` usage,
  `3` API, `4` evaluation, `130` cancelled), the same stdin/stdout evaluator
  protocol and the same JSON, JUnit and GitHub-summary artifacts as the other
  two CLIs. A pipeline written against one runs against any of them.
- `EventsResource.ListAsync` and `EventsResource.SearchAsync`.

### Changed
- **Headers and retries moved into the HTTP pipeline.** They were inlined in the
  single publish method, so every new resource would have copied the retry loop.
  `AxonPushHeaderHandler` and `AxonPushRetryHandler` now apply to every request,
  including the generated clients'. A caller-supplied `HttpClient` becomes the
  terminal hop rather than replacing the pipeline, so injected clients get the
  same headers and backoff.
- **Fail-open is confined to telemetry.** `Events.PublishAsync` still honours it:
  an observability call must never take the calling application down. Every
  other call surfaces its failure, because a gate that passes because the API
  was unreachable is worse than no gate.
