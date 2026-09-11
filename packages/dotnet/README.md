# axonpush for .NET

[axonpush](https://axonpush.xyz) ships three NuGet packages for .NET:

| Package | What it does |
| --- | --- |
| `AxonPush` | HTTP client for the AxonPush events API. |
| `AxonPush.Otel` | OpenTelemetry span exporter that maps `Activity` events to AxonPush. Reusable for any .NET OpenTelemetry workload. |
| `AxonPush.SemanticKernel` | One-call telemetry layer for Microsoft Semantic Kernel. Flips the GenAI diagnostic switch and wires the exporter for you. |

Targets `net8.0` and above.

## Install

For a Semantic Kernel project:

```bash
dotnet add package AxonPush.SemanticKernel
```

For a generic OpenTelemetry project:

```bash
dotnet add package AxonPush.Otel
```

For raw publish access:

```bash
dotnet add package AxonPush
```

## Quickstart: Semantic Kernel

```csharp
using Microsoft.SemanticKernel;
using AxonPush.SemanticKernel;

var builder = Kernel.CreateBuilder();
builder.AddAzureOpenAIChatCompletion("gpt-4o-mini", endpoint, apiKey);

builder.AddAxonPushTelemetry(
    client => { client.ApiKey = "ak_..."; client.TenantId = "..."; },
    exporter => { exporter.ChannelId = "..."; exporter.Environment = "production"; });

var kernel = builder.Build();
```

That single `AddAxonPushTelemetry` call:

1. Flips Semantic Kernel's GenAI diagnostic switch so the kernel emits OpenTelemetry spans for chat completions, function calls, and prompt rendering.
2. Subscribes a `TracerProvider` to every `Microsoft.SemanticKernel.*` activity source.
3. Attaches the axonpush span exporter, batched in the background.

Call `AddAxonPushTelemetry(..., enableSensitiveData: true)` to also forward prompts and completions as span events. The default is off so PII does not leave the process without an explicit opt-in.

## Standalone OpenTelemetry use

```csharp
using OpenTelemetry;
using OpenTelemetry.Trace;
using AxonPush.Otel;

using var tracerProvider = Sdk.CreateTracerProviderBuilder()
    .AddSource("MyApp")
    .AddAxonPushExporter(
        client => { client.ApiKey = "ak_..."; client.TenantId = "..."; },
        exporter => { exporter.ChannelId = "..."; })
    .Build();
```

The exporter is a plain `BaseExporter<Activity>`. `AddAxonPushExporter` wraps it in a `BatchActivityExportProcessor` with sensible defaults.

## OpenTelemetry-native telemetry

`AxonPush.Otel.Telemetry` ships GenAI spans as real OTLP over HTTP to `{BaseUrl}/v1/traces`, routed by the `X-Axonpush-Channel` header and authed by `X-API-Key`. Spans follow the OpenTelemetry GenAI semantic conventions (`gen_ai.*`), so they are portable to any OTLP backend, not just AxonPush. This is the recommended way to send traces. It uses the standard `OpenTelemetry.Exporter.OpenTelemetryProtocol` exporter, batched and non-blocking.

Config resolves from the options callback, then the matching `AXONPUSH_BASE_URL` / `AXONPUSH_API_KEY` / `AXONPUSH_CHANNEL_ID` environment variable (or `IConfiguration` when you pass one).

When the app already owns a `TracerProvider`, reuse it with `AddAxonPushTelemetry` on the builder so the app keeps its own instrumentation and only gains the AxonPush exporter:

```csharp
using OpenTelemetry;
using OpenTelemetry.Trace;
using AxonPush.Otel.Telemetry;

using var provider = Sdk.CreateTracerProviderBuilder()
    .AddSource("axonpush")
    .AddAxonPushTelemetry(out var handle, o =>
    {
        o.ServiceName = "my-agent";
        o.Environment = "prod";
        o.ServiceVersion = "1.4.0";
        o.ContentCapture = ContentCaptureMode.MetadataOnly; // or Redacted / Full
    })
    .Build();
```

When the app does not already own a provider, `ConfigureTelemetry` builds a self-owned one and returns a `TelemetryHandle` for flushing and disposal:

```csharp
using var handle = AxonPushTelemetry.ConfigureTelemetry(o =>
{
    o.ServiceName = "my-agent";
    o.Environment = "prod";
});
```

Wrap a model call in a GenAI span with the `GenAi` helpers. `StartSpan` opens a CLIENT activity on your `ActivitySource` (default source name `"axonpush"`):

```csharp
using System.Diagnostics;
using AxonPush.Otel.Telemetry;

var source = new ActivitySource("axonpush");

using (var span = GenAi.StartSpan(source, operation: "chat", requestModel: "gpt-4o", system: "openai"))
{
    // ... call the model ...
    GenAi.RecordResponse(span,
        responseModel: "gpt-4o",
        inputTokens: 12,
        outputTokens: 48,
        cacheWriteTokens: 0);
    GenAi.RecordContent(span, prompt: "…", completion: "…", handle: handle);
}
```

Prompt and completion land as span events (`gen_ai.content.prompt` / `gen_ai.content.completion`), gated by `ContentCaptureMode`: `MetadataOnly` drops content, `Redacted` keeps previews, `Full` keeps it. Secret-shaped keys are always stripped regardless of mode.

On serverless hosts (AWS Lambda and friends) the batch processor's exit flush is unreliable because the container is frozen between invocations. Call `handle.Flush(timeoutMs)` at the end of each invocation; `handle.Dispose()` flushes and tears down the provider when the handle owns it (it is a no-op when the app owns the provider via `AddAxonPushTelemetry`).

### Which should I use

The OTel-native path above is the recommended way to send traces. The legacy per-framework event-model exporter (`AxonPushSpanExporter` / `AddAxonPushExporter`, which maps `Activity` events to `/event` payloads) still works and is kept for compatibility, but it is being superseded by OTel-native. Frame it as the compatibility path: keep it if you already depend on channel fan-out on the events plane, otherwise reach for `AxonPush.Otel.Telemetry`. Traces from both land in the same dashboard (`/v2/traces`); the server reconciles them through the OTLP normalizer, so you can migrate call sites incrementally without a gap in your traces.

## Environment variables

`AxonPushOptions.FromEnvironment` (called internally) reads:

| Variable | Default | Notes |
| --- | --- | --- |
| `AXONPUSH_API_KEY` | required | API key. |
| `AXONPUSH_TENANT_ID` | required | Tenant identifier. |
| `AXONPUSH_BASE_URL` | `https://api.axonpush.xyz` | Override for self-hosted deployments. |
| `AXONPUSH_ENVIRONMENT` | (none) | Stamped on every event for filtering. |
| `AXONPUSH_TIMEOUT` | `30` | Per-request timeout in seconds. |
| `AXONPUSH_MAX_RETRIES` | `3` | Maximum retry attempts. |
| `AXONPUSH_FAIL_OPEN` | `true` | When true, publish failures are logged and swallowed. |

## What spans you get from Semantic Kernel

With the GenAI switch enabled, Semantic Kernel emits spans on these activity sources:

- `Microsoft.SemanticKernel` for kernel function invocations.
- `Microsoft.SemanticKernel.Connectors.OpenAI` and `Microsoft.SemanticKernel.Connectors.AzureOpenAI` for chat completion calls.
- Connector-specific sources for embeddings, image generation, and other AI services as they ship.

Spans carry the OpenTelemetry GenAI semantic-convention attributes: `gen_ai.system`, `gen_ai.request.model`, `gen_ai.usage.input_tokens`, `gen_ai.usage.output_tokens`, `gen_ai.response.finish_reasons`, and others. AxonPush stores them verbatim, so the same dashboards you build for Python LangChain or TypeScript LangGraph runs apply to your Semantic Kernel runs without changes.

## Sample app

See [`samples/SemanticKernelChat`](samples/SemanticKernelChat) for an end-to-end console REPL with Azure OpenAI as the default backend and an inline `GetTime` kernel function for function-call spans.

## Fail-open behaviour

By default the client treats AxonPush as a soft dependency. If a publish fails after retries, the exception is logged at warning level and the call returns a failed `PublishResult` without throwing. Set `AxonPushOptions.FailOpen = false` (or env `AXONPUSH_FAIL_OPEN=false`) to surface errors to the caller.

The OpenTelemetry exporter follows the same setting. When fail-open is on, `Export` returns `ExportResult.Success` even when individual spans could not be delivered, so the OpenTelemetry SDK never propagates the failure into user code.

## Release gates

`client.Gates` reads and writes release-gate policies and the history of gate
decisions, matching the `gates` resource in the Python and TypeScript SDKs.
Unlike telemetry publishing these are control-plane calls, so they throw
`AxonPushException` on failure rather than failing open.

```csharp
using AxonPush;
using AxonPush.Gates;

using var client = new AxonPushClient(AxonPushOptions.FromEnvironment());

await client.Gates.SavePolicyAsync(new SaveGatePolicyDto
{
    ScopeType = GatePolicyScope.Dataset,
    ScopeId = "ds_123",
    MinScore = 0.8,
    MaxFailureRate = 0.05,
});

var policies = await client.Gates.ListPoliciesAsync();
var runs = await client.Gates.ListRunsAsync(experimentId: "exp_123");
```

## Cross-source correlation

Span payloads emitted by `AxonPush.Otel` use the same JSON shape as the Python (`axonpush`) and TypeScript (`@axonpush/sdk`) exporters. A Semantic Kernel chat completion span shows up in the AxonPush UI with the same schema as a LangChain run from Python or a Vercel AI middleware trace from Node. Trace and span identifiers are preserved, so spans emitted by multiple SDKs against the same workflow correlate naturally.

## License

MIT. See [LICENSE](LICENSE).
