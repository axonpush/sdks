using System.Reflection;
using Microsoft.Extensions.Configuration;
using OpenTelemetry;
using OpenTelemetry.Exporter;
using OpenTelemetry.Resources;
using OpenTelemetry.Trace;

namespace AxonPush.Otel.Telemetry;

/// <summary>
/// OTel-native telemetry for AxonPush. Ships GenAI spans as real OTLP over HTTP to
/// <c>{BaseUrl}/v1/traces</c>, routed by the <c>X-Axonpush-Channel</c> header and authed
/// by <c>X-API-Key</c>. Spans follow the GenAI semantic conventions so they are portable
/// to any OTLP backend.
/// </summary>
/// <remarks>
/// This reuses the standard OpenTelemetry .NET OTLP exporter (batched, non-blocking) rather
/// than the proprietary <see cref="AxonPushSpanExporter"/> events path. The app's own
/// <c>TracerProvider</c> / <c>ActivitySource</c> are reused where possible.
/// <para>
/// On serverless hosts (e.g. AWS Lambda) the batch processor's exit flush is unreliable
/// because the container is frozen between invocations. Call <see cref="TelemetryHandle.Flush"/>
/// at the end of each invocation.
/// </para>
/// </remarks>
public static class AxonPushTelemetry
{
    /// <summary>
    /// Build a self-owned <see cref="TracerProvider"/> that exports GenAI spans to AxonPush over
    /// OTLP, and return a <see cref="TelemetryHandle"/> for flushing / disposal. Use this when the
    /// app does not already own a provider; otherwise prefer
    /// <c>AddAxonPushTelemetry</c> on your existing builder.
    /// </summary>
    public static TelemetryHandle ConfigureTelemetry(
        Action<AxonPushTelemetryOptions>? configure = null,
        IConfiguration? configuration = null)
    {
        var options = new AxonPushTelemetryOptions();
        configure?.Invoke(options);
        var resolved = ResolvedTelemetryConfig.Resolve(options, configuration);

        var provider = Sdk.CreateTracerProviderBuilder()
            .AddSource(resolved.SourceNames.ToArray())
            .SetResourceBuilder(BuildResource(resolved))
            .AddAxonPushOtlpExporter(resolved)
            .Build();

        return new TelemetryHandle(provider, ownsProvider: true, resolved);
    }

    internal static TracerProviderBuilder AddAxonPushOtlpExporter(
        this TracerProviderBuilder builder,
        ResolvedTelemetryConfig config)
    {
        return builder.AddOtlpExporter(otlp =>
        {
            otlp.Endpoint = config.TracesEndpoint;
            otlp.Protocol = OtlpExportProtocol.HttpProtobuf;
            otlp.Headers = config.OtlpHeaders();
        });
    }

    internal static ResourceBuilder BuildResource(ResolvedTelemetryConfig config)
    {
        var attributes = new List<KeyValuePair<string, object>>
        {
            new("service.name", config.ServiceName),
        };
        if (!string.IsNullOrWhiteSpace(config.Environment))
        {
            attributes.Add(new("deployment.environment.name", config.Environment!));
        }
        if (!string.IsNullOrWhiteSpace(config.ServiceVersion))
        {
            attributes.Add(new("service.version", config.ServiceVersion!));
        }
        return ResourceBuilder.CreateDefault().AddAttributes(attributes);
    }
}

/// <summary>
/// Resolved telemetry configuration: options merged with <c>AXONPUSH_*</c> environment fallbacks.
/// </summary>
internal sealed class ResolvedTelemetryConfig
{
    public required Uri TracesEndpoint { get; init; }
    public string? ApiKey { get; init; }
    public string? ChannelId { get; init; }
    public required string ServiceName { get; init; }
    public string? Environment { get; init; }
    public string? ServiceVersion { get; init; }
    public required ContentCaptureMode ContentCapture { get; init; }
    public required IReadOnlyList<string> RedactKeys { get; init; }
    public required int MaxContentLength { get; init; }
    public required IReadOnlyList<string> SourceNames { get; init; }

    public static ResolvedTelemetryConfig Resolve(
        AxonPushTelemetryOptions options,
        IConfiguration? configuration)
    {
        configuration ??= new ConfigurationBuilder().AddEnvironmentVariables().Build();

        var baseUrl = FirstNonBlank(options.BaseUrl, configuration["AXONPUSH_BASE_URL"])
            ?? "https://api.axonpush.xyz";
        var normalized = baseUrl.TrimEnd('/');
        var endpoint = new Uri($"{normalized}/v1/traces", UriKind.Absolute);

        var apiKey = FirstNonBlank(options.ApiKey, configuration["AXONPUSH_API_KEY"]);
        var channelId = FirstNonBlank(options.ChannelId, configuration["AXONPUSH_CHANNEL_ID"]);

        var serviceName = FirstNonBlank(options.ServiceName, configuration["OTEL_SERVICE_NAME"])
            ?? Assembly.GetEntryAssembly()?.GetName().Name
            ?? "dotnet-app";
        var environment = FirstNonBlank(options.Environment, configuration["AXONPUSH_ENVIRONMENT"]);

        return new ResolvedTelemetryConfig
        {
            TracesEndpoint = endpoint,
            ApiKey = apiKey,
            ChannelId = channelId,
            ServiceName = serviceName,
            Environment = environment,
            ServiceVersion = options.ServiceVersion,
            ContentCapture = options.ContentCapture,
            RedactKeys = options.RedactKeys,
            MaxContentLength = options.MaxContentLength,
            SourceNames = options.SourceNames.Count > 0 ? options.SourceNames : new[] { "axonpush" },
        };
    }

    /// <summary>Headers in the OTLP exporter's <c>key=value,key=value</c> format.</summary>
    public string? OtlpHeaders()
    {
        var parts = new List<string>(2);
        if (!string.IsNullOrWhiteSpace(ApiKey))
        {
            parts.Add($"X-API-Key={ApiKey}");
        }
        if (!string.IsNullOrWhiteSpace(ChannelId))
        {
            parts.Add($"X-Axonpush-Channel={ChannelId}");
        }
        return parts.Count > 0 ? string.Join(",", parts) : null;
    }

    private static string? FirstNonBlank(params string?[] candidates)
    {
        foreach (var candidate in candidates)
        {
            if (!string.IsNullOrWhiteSpace(candidate))
            {
                return candidate;
            }
        }
        return null;
    }
}

/// <summary>
/// Handle over a telemetry setup. Carries the content-capture policy for
/// <see cref="GenAi.RecordContent"/> and provides explicit flush / dispose for serverless.
/// </summary>
public sealed class TelemetryHandle : IDisposable
{
    private readonly TracerProvider? _provider;
    private readonly bool _ownsProvider;
    private readonly ResolvedTelemetryConfig _config;

    internal TelemetryHandle(TracerProvider? provider, bool ownsProvider, ResolvedTelemetryConfig config)
    {
        _provider = provider;
        _ownsProvider = ownsProvider;
        _config = config;
    }

    /// <summary>Content capture policy applied by <see cref="GenAi.RecordContent"/>.</summary>
    public ContentCaptureMode ContentCapture => _config.ContentCapture;

    /// <summary>Additional attribute keys to always redact.</summary>
    public IReadOnlyList<string> RedactKeys => _config.RedactKeys;

    /// <summary>Max length of any single content string before truncation.</summary>
    public int MaxContentLength => _config.MaxContentLength;

    /// <summary>
    /// Block until buffered spans are exported, or until <paramref name="timeoutMilliseconds"/>.
    /// Call this at the end of each invocation on serverless platforms. Returns <see langword="true"/>
    /// if the flush completed within the timeout.
    /// </summary>
    public bool Flush(int timeoutMilliseconds = 2000) => _provider?.ForceFlush(timeoutMilliseconds) ?? true;

    /// <summary>
    /// Flush and dispose the provider if this handle owns it. When the handle was produced by
    /// <c>AddAxonPushTelemetry</c> the app owns the provider, so this is a no-op. Idempotent.
    /// </summary>
    public void Dispose()
    {
        if (_ownsProvider)
        {
            _provider?.Dispose();
        }
    }
}
