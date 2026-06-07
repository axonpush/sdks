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

    /// <summary>Channel the event belongs to.</summary>
    public required string ChannelId { get; init; }

    /// <summary>Event-type discriminator. Defaults to <see cref="EventType.AppSpan"/>.</summary>
    public string EventType { get; init; } = AxonPush.EventType.AppSpan;

    /// <summary>OTel trace identifier (32 lowercase hex characters).</summary>
    public string? TraceId { get; init; }

    /// <summary>OTel span identifier (16 lowercase hex characters).</summary>
    public string? SpanId { get; init; }

    /// <summary>Parent event identifier, when this event continues a chain.</summary>
    public string? ParentEventId { get; init; }

    /// <summary>Environment tag (e.g. "production").</summary>
    public string? Environment { get; init; }

    /// <summary>Free-form metadata keyed by string.</summary>
    public IReadOnlyDictionary<string, object?>? Metadata { get; init; }
}
