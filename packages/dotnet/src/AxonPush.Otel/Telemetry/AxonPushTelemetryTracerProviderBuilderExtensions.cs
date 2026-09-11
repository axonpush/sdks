using Microsoft.Extensions.Configuration;
using OpenTelemetry.Trace;

namespace AxonPush.Otel.Telemetry;

/// <summary>
/// Wires OTLP export to AxonPush onto an application's own <see cref="TracerProviderBuilder"/>,
/// so the app keeps ownership of its provider and other instrumentation.
/// </summary>
public static class AxonPushTelemetryTracerProviderBuilderExtensions
{
    /// <summary>
    /// Add the AxonPush OTLP exporter (batched, <c>HttpProtobuf</c>) and a matching resource to
    /// an existing <see cref="TracerProviderBuilder"/>, and subscribe it to the configured
    /// ActivitySources. Options unset here fall back to <c>AXONPUSH_*</c> environment variables.
    /// </summary>
    /// <returns>
    /// The builder, plus (via <paramref name="handle"/>) the content-capture policy for
    /// <see cref="GenAi.RecordContent"/>. The returned <see cref="TelemetryHandle"/> does not own
    /// the provider — the app is responsible for disposing its own <c>TracerProvider</c>.
    /// </returns>
    public static TracerProviderBuilder AddAxonPushTelemetry(
        this TracerProviderBuilder builder,
        out TelemetryHandle handle,
        Action<AxonPushTelemetryOptions>? configure = null,
        IConfiguration? configuration = null)
    {
        ArgumentNullException.ThrowIfNull(builder);

        var options = new AxonPushTelemetryOptions();
        configure?.Invoke(options);
        var resolved = ResolvedTelemetryConfig.Resolve(options, configuration);

        builder
            .AddSource(resolved.SourceNames.ToArray())
            .SetResourceBuilder(AxonPushTelemetry.BuildResource(resolved))
            .AddAxonPushOtlpExporter(resolved);

        handle = new TelemetryHandle(provider: null, ownsProvider: false, resolved);
        return builder;
    }

    /// <summary>
    /// Overload without the policy handle, for callers that use only metadata-only capture or
    /// pass an explicit policy to <see cref="GenAi.RecordContent"/>.
    /// </summary>
    public static TracerProviderBuilder AddAxonPushTelemetry(
        this TracerProviderBuilder builder,
        Action<AxonPushTelemetryOptions>? configure = null,
        IConfiguration? configuration = null)
        => builder.AddAxonPushTelemetry(out _, configure, configuration);
}
