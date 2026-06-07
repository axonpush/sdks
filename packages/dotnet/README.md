# AxonPush for .NET

[AxonPush](https://axonpush.xyz) ships three NuGet packages for .NET:

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
3. Attaches the AxonPush span exporter, batched in the background.

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

## Cross-source correlation

Span payloads emitted by `AxonPush.Otel` use the same JSON shape as the Python (`axonpush`) and TypeScript (`@axonpush/sdk`) exporters. A Semantic Kernel chat completion span shows up in the AxonPush UI with the same schema as a LangChain run from Python or a Vercel AI middleware trace from Node. Trace and span identifiers are preserved, so spans emitted by multiple SDKs against the same workflow correlate naturally.

## License

MIT. See [LICENSE](LICENSE).
