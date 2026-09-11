using System.Diagnostics;
using AxonPush.Otel.Internal;

namespace AxonPush.Otel.Telemetry;

/// <summary>
/// GenAI semantic-convention helpers over <see cref="Activity"/>, mirroring the
/// Python SDK's <c>genai_span</c> / <c>record_genai_response</c> / <c>record_genai_content</c>.
/// </summary>
public static class GenAi
{
    /// <summary>
    /// Start a CLIENT activity for a GenAI operation, named <c>"{operation} {requestModel}"</c>
    /// unless <paramref name="name"/> overrides it. Sets <c>gen_ai.operation.name</c>,
    /// <c>gen_ai.request.model</c> and, when provided, <c>gen_ai.system</c> /
    /// <c>gen_ai.provider.name</c> and <c>gen_ai.agent.name</c>.
    /// </summary>
    /// <returns>The started activity, or <see langword="null"/> if no listener is sampling the source.</returns>
    public static Activity? StartSpan(
        ActivitySource source,
        string operation,
        string requestModel,
        string? system = null,
        string? agentName = null,
        string? name = null)
    {
        ArgumentNullException.ThrowIfNull(source);
        ArgumentException.ThrowIfNullOrEmpty(operation);
        ArgumentException.ThrowIfNullOrEmpty(requestModel);

        var spanName = name ?? $"{operation} {requestModel}";
        var tags = new ActivityTagsCollection
        {
            ["gen_ai.operation.name"] = operation,
            ["gen_ai.request.model"] = requestModel,
        };
        if (system is not null)
        {
            tags["gen_ai.system"] = system;
            tags["gen_ai.provider.name"] = system;
        }
        if (agentName is not null)
        {
            tags["gen_ai.agent.name"] = agentName;
        }

        return source.StartActivity(spanName, ActivityKind.Client, default(ActivityContext), tags);
    }

    /// <summary>Record GenAI response and usage attributes on <paramref name="activity"/>.</summary>
    public static void RecordResponse(
        Activity? activity,
        string? responseModel = null,
        IReadOnlyList<string>? finishReasons = null,
        int? inputTokens = null,
        int? outputTokens = null,
        int? reasoningTokens = null,
        int? cacheReadTokens = null,
        int? cacheWriteTokens = null)
    {
        if (activity is null)
        {
            return;
        }
        if (responseModel is not null)
        {
            activity.SetTag("gen_ai.response.model", responseModel);
        }
        if (finishReasons is not null)
        {
            activity.SetTag("gen_ai.response.finish_reasons", finishReasons.ToArray());
        }
        if (inputTokens is not null)
        {
            activity.SetTag("gen_ai.usage.input_tokens", inputTokens);
        }
        if (outputTokens is not null)
        {
            activity.SetTag("gen_ai.usage.output_tokens", outputTokens);
        }
        if (reasoningTokens is not null)
        {
            activity.SetTag("gen_ai.usage.reasoning_tokens", reasoningTokens);
        }
        if (cacheReadTokens is not null)
        {
            activity.SetTag("gen_ai.usage.cache_read_input_tokens", cacheReadTokens);
        }
        if (cacheWriteTokens is not null)
        {
            activity.SetTag("gen_ai.usage.cache_write_input_tokens", cacheWriteTokens);
        }
    }

    /// <summary>
    /// Emit prompt / completion as span events (<c>gen_ai.content.prompt</c> /
    /// <c>gen_ai.content.completion</c>), gated by the capture policy. Content is
    /// emitted as events rather than attributes so large payloads don't inflate the
    /// span. Redaction follows <see cref="TelemetryRedactor"/>: metadata-only drops
    /// content, redacted keeps previews, full keeps it; secret-shaped keys are always
    /// stripped. The policy is taken from <paramref name="handle"/> when given,
    /// else from the explicit arguments.
    /// </summary>
    public static void RecordContent(
        Activity? activity,
        object? prompt = null,
        object? completion = null,
        TelemetryHandle? handle = null,
        ContentCaptureMode contentCapture = ContentCaptureMode.MetadataOnly,
        IReadOnlyList<string>? redactKeys = null,
        int maxContentLength = 4096)
    {
        if (activity is null)
        {
            return;
        }

        var mode = handle?.ContentCapture ?? contentCapture;
        var keys = handle?.RedactKeys ?? redactKeys ?? Array.Empty<string>();
        var maxLen = handle?.MaxContentLength ?? maxContentLength;

        if (mode == ContentCaptureMode.MetadataOnly)
        {
            return;
        }

        if (prompt is not null)
        {
            AddContentEvent(activity, "gen_ai.content.prompt", "prompt", prompt, mode, keys, maxLen);
        }
        if (completion is not null)
        {
            AddContentEvent(activity, "gen_ai.content.completion", "completion", completion, mode, keys, maxLen);
        }
    }

    private static void AddContentEvent(
        Activity activity,
        string eventName,
        string key,
        object value,
        ContentCaptureMode mode,
        IReadOnlyList<string> redactKeys,
        int maxContentLength)
    {
        var wrapper = new Dictionary<string, object?>(StringComparer.Ordinal) { [key] = value };
        var redacted = TelemetryRedactor.Redact(wrapper, mode, redactKeys, maxContentLength);
        var flat = TelemetryRedactor.Flatten(redacted);

        var tags = new ActivityTagsCollection();
        foreach (var (k, v) in flat)
        {
            tags[k] = v;
        }
        activity.AddEvent(new ActivityEvent(eventName, tags: tags));
    }
}
