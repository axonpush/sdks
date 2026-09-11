namespace AxonPush.Otel.Telemetry;

/// <summary>
/// How much prompt / completion content is emitted onto GenAI spans.
/// Mirrors the Python SDK's <c>ContentCaptureMode</c>.
/// </summary>
public enum ContentCaptureMode
{
    /// <summary>Drop content outright; only metadata (models, token counts) is kept.</summary>
    MetadataOnly,

    /// <summary>Keep short previews of content, enough to recognise a run but not reconstruct it.</summary>
    Redacted,

    /// <summary>Keep content verbatim (subject to secret-key and configured-key stripping).</summary>
    Full,
}
