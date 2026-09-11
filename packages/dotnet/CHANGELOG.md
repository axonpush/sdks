# Changelog

All notable changes to the axonpush .NET SDKs are documented here. The
format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versioning is [SemVer](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **OTel-native telemetry (`AxonPush.Otel.Telemetry`).**
  `AxonPushTelemetry.ConfigureTelemetry(...)` builds a self-owned
  `TracerProvider` that exports GenAI spans as real OTLP over HTTP to
  `{BaseUrl}/v1/traces` with the `X-API-Key` and `X-Axonpush-Channel` headers,
  returning a `TelemetryHandle` with `Flush(timeoutMs)` and `Dispose()`. Apps
  that already own a provider reuse it with
  `TracerProviderBuilder.AddAxonPushTelemetry(...)`, which attaches the exporter
  and resource without taking ownership. `GenAi.StartSpan` / `RecordResponse` /
  `RecordContent` emit spans under the OpenTelemetry GenAI semantic conventions
  (`gen_ai.*`), with prompt and completion carried as span events gated by
  `ContentCaptureMode` (`MetadataOnly` / `Redacted` / `Full`, secret-shaped keys
  always stripped). This is now the recommended way to send traces. Depends on
  `OpenTelemetry.Exporter.OpenTelemetryProtocol`.
- Config resolves from the options callback, then `AXONPUSH_BASE_URL` /
  `AXONPUSH_API_KEY` / `AXONPUSH_CHANNEL_ID` (or `IConfiguration`). Spans carry a
  Resource with `service.name`, `deployment.environment.name`, and
  `service.version`. On serverless hosts, where the batch processor's exit flush
  is unreliable, call `TelemetryHandle.Flush(...)` at the end of each
  invocation.

### Changed
- The legacy per-framework event-model exporter (`AxonPushSpanExporter` /
  `AddAxonPushExporter`, which maps `Activity` events to `/event` payloads) is
  now a compatibility path, superseded by OTel-native telemetry. It still works
  and is not removed. Traces from both paths land in the same dashboard
  (`/v2/traces`), reconciled server-side through the OTLP normalizer, so call
  sites can migrate incrementally.
