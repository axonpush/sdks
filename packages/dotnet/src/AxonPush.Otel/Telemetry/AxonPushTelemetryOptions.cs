namespace AxonPush.Otel.Telemetry;

/// <summary>
/// Options for <see cref="AxonPushTelemetry.ConfigureTelemetry"/> and
/// <c>AddAxonPushTelemetry</c>. Values left null are resolved from the matching
/// <c>AXONPUSH_*</c> environment variable.
/// </summary>
public sealed class AxonPushTelemetryOptions
{
    /// <summary>Backend base URL (<c>AXONPUSH_BASE_URL</c>). Traces post to <c>{BaseUrl}/v1/traces</c>.</summary>
    public string? BaseUrl { get; set; }

    /// <summary>API key sent as the <c>X-API-Key</c> header (<c>AXONPUSH_API_KEY</c>).</summary>
    public string? ApiKey { get; set; }

    /// <summary>Channel routed to via the <c>X-Axonpush-Channel</c> header (<c>AXONPUSH_CHANNEL_ID</c>).</summary>
    public string? ChannelId { get; set; }

    /// <summary>Resource <c>service.name</c>. Defaults to the entry assembly name.</summary>
    public string? ServiceName { get; set; }

    /// <summary>Resource <c>deployment.environment.name</c>.</summary>
    public string? Environment { get; set; }

    /// <summary>Resource <c>service.version</c>.</summary>
    public string? ServiceVersion { get; set; }

    /// <summary>Content capture policy for <see cref="GenAi.RecordContent"/>. Defaults to metadata only.</summary>
    public ContentCaptureMode ContentCapture { get; set; } = ContentCaptureMode.MetadataOnly;

    /// <summary>Additional attribute keys to always redact, case-insensitive.</summary>
    public IReadOnlyList<string> RedactKeys { get; set; } = Array.Empty<string>();

    /// <summary>Max length of any single content string before truncation. Defaults to 4096.</summary>
    public int MaxContentLength { get; set; } = 4096;

    /// <summary>ActivitySource names to subscribe the TracerProvider to. Defaults to <c>"axonpush"</c>.</summary>
    public IReadOnlyList<string> SourceNames { get; set; } = new[] { "axonpush" };
}
