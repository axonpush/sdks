using System.Text.Json.Serialization;

namespace AxonPush.Events;

/// <summary>
/// Payload published to the AxonPush events API. Field names match the Python and TypeScript SDKs
/// so that traces emitted from any client land in the AxonPush UI with an identical schema.
/// </summary>
public sealed record PublishRequest
{
    /// <summary>Stable identifier for the event (often the OTel span id or a UUID).</summary>
    public required string Identifier { get; init; }

    /// <summary>Event payload. Serialised verbatim as JSON.</summary>
    public required object Payload { get; init; }

    /// <summary>
    /// Channel the event belongs to.
    /// </summary>
    /// <remarks>
    /// Serialised as <c>channel_id</c>. The camelCase policy produced
    /// <c>channelId</c>, which the global ValidationPipe rejected because it
    /// runs with <c>forbidNonWhitelisted</c>, so every publish failed.
    /// </remarks>
    [JsonPropertyName("channel_id")]
    public required string ChannelId { get; init; }

    /// <summary>Agent that emitted the event. Every other SDK sends this.</summary>
    public string? AgentId { get; init; }

    /// <summary>Stable source identity across retries.</summary>
    public string? DedupKey { get; init; }

    /// <summary>Original source occurrence time.</summary>
    public DateTimeOffset? OccurredAt { get; init; }

    /// <summary>Event-type discriminator. Defaults to <see cref="EventType.AppSpan"/>.</summary>
    public string EventType { get; init; } = AxonPush.EventType.AppSpan;

    /// <summary>OTel trace identifier (32 lowercase hex characters).</summary>
    public string? TraceId { get; init; }

    /// <summary>OTel span identifier (16 lowercase hex characters).</summary>
    public string? SpanId { get; init; }

    /// <summary>Parent event identifier, when this event continues a chain.</summary>
    [JsonIgnore]
    public string? ParentEventId { get; init; }

    /// <summary>Environment tag (e.g. "production").</summary>
    [JsonIgnore]
    public string? Environment { get; init; }

    /// <summary>Parent span identifier, when this event continues a span.</summary>
    public string? ParentSpanId { get; init; }

    /// <summary>Free-form metadata keyed by string.</summary>
    [JsonIgnore]
    public IReadOnlyDictionary<string, object?>? Metadata { get; init; }

    /// <summary>Metadata serialized with optional parent-event causality.</summary>
    [JsonPropertyName("metadata")]
    public IReadOnlyDictionary<string, object?>? SerializedMetadata
    {
        get
        {
            if (ParentEventId is null) return Metadata;
            var metadata = Metadata is null
                ? new Dictionary<string, object?>()
                : new Dictionary<string, object?>(Metadata);
            metadata["axonpush.parent_event_id"] = ParentEventId;
            return metadata;
        }
    }
}
