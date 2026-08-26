---
title: "Shipping an OpenTelemetry exporter for Microsoft Semantic Kernel"
date: 2026-06-08
author: Sayan Biswas
tags: [semantic-kernel, dotnet, opentelemetry, observability]
---

Microsoft Semantic Kernel quietly added GenAI OpenTelemetry diagnostics a while back. Flip a switch, attach a `TracerProvider`, and your kernel starts emitting spans for every chat completion, function call, and prompt render, complete with the OpenTelemetry GenAI semantic-convention attributes for model name, token usage, and finish reason.

Most observability vendors do not have a quickstart for this. So when I added a Semantic Kernel sample to AxonPush this week, the first thing I shipped was the missing exporter.

This post is about what that took, and a couple of design choices that turned out to matter.

## The five-line developer experience

Here is the entire setup, from `using` to working traces:

```csharp
using Microsoft.SemanticKernel;
using AxonPush.SemanticKernel;

var builder = Kernel.CreateBuilder();
builder.AddAzureOpenAIChatCompletion("gpt-4o-mini", endpoint, apiKey);
builder.AddAxonPushTelemetry(
    client => { client.ApiKey = "ak_..."; client.TenantId = "..."; },
    exporter => { exporter.ChannelId = "..."; });

var kernel = builder.Build();
```

`AddAxonPushTelemetry` does three things:

1. Flips two `AppContext` switches that gate Semantic Kernel's GenAI diagnostics.
2. Builds an OpenTelemetry `TracerProvider` that subscribes to every `Microsoft.SemanticKernel.*` activity source.
3. Attaches the AxonPush span exporter, wrapped in a `BatchActivityExportProcessor`.

That is the developer surface. Everything below is how the pieces fit together and why.

## What you actually see in traces

Run the sample REPL, ask for the time, and the kernel will end up calling the inline `GetTime` function. In AxonPush the resulting trace shows three spans:

- `Kernel.InvokeAsync` from the function dispatcher.
- `chat.completions <deployment>` from the Azure OpenAI connector, carrying `gen_ai.system = "az.ai.openai"`, `gen_ai.request.model`, and `gen_ai.usage.input_tokens` plus `output_tokens`.
- `GetTime` from the kernel function itself.

The schema is identical to the one the Python and TypeScript AxonPush SDKs emit, so the existing dashboards built around LangChain or LangGraph traces light up automatically for Semantic Kernel runs.

## Why a `BaseExporter<Activity>` over a custom listener

Semantic Kernel's diagnostics ride on `System.Diagnostics.Activity`. The idiomatic way to receive those activities is to register a `TracerProvider` from the OpenTelemetry SDK, then attach exporters and processors to it. Anything else, like a hand-rolled `ActivityListener` or a wrapper that hooks into kernel filters, would be reinventing scaffolding the SDK already provides.

This also means the AxonPush exporter is reusable outside Semantic Kernel. The same `AxonPush.Otel` package works for ASP.NET Core, worker services, HttpClient instrumentation, or any other OpenTelemetry source. Semantic Kernel just happens to be the headline integration.

## The experimental switch and why sensitive data defaults off

Semantic Kernel caches its GenAI diagnostic flags into `static readonly bool` fields. They are read once, when the relevant types are first JITted, so they must be set before any kernel work happens. Calling `AddAxonPushTelemetry` during DI registration is early enough, and the extension method handles it.

The first switch enables GenAI spans. The second forwards prompts and completions as span events. The second is off by default. Most teams do not want raw model inputs and outputs landing in their observability backend without an explicit decision, and a one-line flag is the right place for that decision:

```csharp
builder.AddAxonPushTelemetry(client => { ... }, exporter => { ... }, enableSensitiveData: true);
```

This mirrors the way Application Insights and OTLP samples in the Semantic Kernel repo handle the same trade-off.

## Fail-open behaviour

A telemetry pipeline that takes down your app is worse than no telemetry. The AxonPush .NET client treats publish failures as soft failures by default. If a span cannot be delivered, the exception is logged at warning level and the export returns success to the OpenTelemetry SDK, so the kernel keeps responding to prompts.

Concretely, that means the exporter:

- Retries transient failures on a small backoff schedule (250 ms, 500 ms, 1 s, 2 s, 4 s).
- Honours `Retry-After` on 429 responses.
- Catches and swallows terminal failures when `AxonPushOptions.FailOpen` is true.
- Surfaces failures to callers only when fail-open is explicitly turned off.

This is the same shape the Python and TypeScript SDKs use. Cross-runtime consistency is intentional.

## Cross-SDK wire compatibility

The .NET exporter serialises spans into the same JSON shape that the Python and TypeScript SDKs do. Field names match: `traceId`, `spanId`, `name`, `kind`, `startTimeUnixNano`, `endTimeUnixNano`, `status`, `attributes`, `parentSpanId`, `events`, `links`, `resource`, `scope`. Times are unix nanoseconds as strings. Kind is the OpenTelemetry proto integer.

A golden-output unit test asserts the envelope serialisation against a hand-written fixture, which is what keeps the .NET emitter from drifting away from the Python reference shape as either side evolves.

## What is next

A few things on the immediate list:

- A sample showing function-calling spans against `Microsoft.SemanticKernel.Agents`.
- An Azure AI Foundry quickstart that wires the exporter into a deployed Foundry agent.
- A small companion blog post measuring per-agent token cost using the spans the kernel already emits.

If you are building on Semantic Kernel and want to try it, the repo is at [github.com/axonpush/sdks](https://github.com/axonpush/sdks) under `packages/dotnet`, and the AxonPush dashboard is at [axonpush.xyz](https://axonpush.xyz).

I am Sayan Biswas. I work on AxonPush, an observability platform for LLM and agent runs. Find me on [LinkedIn](https://www.linkedin.com/in/sayanbiswas64).
