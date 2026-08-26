namespace AxonPush.Otel;

/// <summary>
/// Configuration for the <see cref="AxonPushSpanExporter"/>.
/// </summary>
public sealed class AxonPushSpanExporterOptions
{
    /// <summary>AxonPush channel that should receive the exported spans. Required.</summary>
    public required string ChannelId { get; set; }

    /// <summary>Service name (OTel <c>service.name</c>). Defaults to the entry assembly name.</summary>
    public string? ServiceName { get; set; }

    /// <summary>Service version (OTel <c>service.version</c>).</summary>
    public string? ServiceVersion { get; set; }

    /// <summary>Environment tag (OTel <c>deployment.environment</c>).</summary>
    public string? Environment { get; set; }
}
