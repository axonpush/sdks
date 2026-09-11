using System.Collections;
using System.Globalization;
using System.Text.Json;
using System.Text.RegularExpressions;
using AxonPush.Otel.Telemetry;

namespace AxonPush.Otel.Internal;

/// <summary>
/// Client-side content redaction, mirroring the Python SDK's <c>_redaction.py</c>.
/// Credential-shaped keys are always stripped; content-shaped keys follow the
/// <see cref="ContentCaptureMode"/> ladder (drop / preview / keep).
/// </summary>
internal static partial class TelemetryRedactor
{
    /// <summary>How much of a content value <see cref="ContentCaptureMode.Redacted"/> keeps.</summary>
    internal const int ContentPreviewLength = 256;

    [GeneratedRegex(
        "^(authorization|proxy-authorization|cookie|set-cookie|password|passwd|secret|" +
        "client_secret|api[-_.]?key|access[-_.]?token|refresh[-_.]?token|private[-_.]?key)$",
        RegexOptions.IgnoreCase | RegexOptions.CultureInvariant)]
    private static partial Regex SecretKey();

    [GeneratedRegex(
        "^(prompt|prompts|messages?|completion|completions|input|output|response|" +
        "tool[-_.]?(arguments?|result|output)|retrieval[-_.]?(documents?|content))$",
        RegexOptions.IgnoreCase | RegexOptions.CultureInvariant)]
    private static partial Regex ContentKey();

    /// <summary>Return a recursively copied value safe for telemetry transport.</summary>
    public static object? Redact(
        object? value,
        ContentCaptureMode mode,
        IReadOnlyCollection<string> redactKeys,
        int maxContentLength)
    {
        var configured = new HashSet<string>(
            redactKeys.Select(k => k.ToLowerInvariant()),
            StringComparer.Ordinal);
        var previewing = mode == ContentCaptureMode.Redacted;
        return Visit(value, inContent: false, mode, configured, previewing, maxContentLength);
    }

    private static object? Visit(
        object? current,
        bool inContent,
        ContentCaptureMode mode,
        HashSet<string> configured,
        bool previewing,
        int maxContentLength)
    {
        switch (current)
        {
            case string text:
                {
                    var limit = inContent
                        ? Math.Min(ContentPreviewLength, maxContentLength)
                        : maxContentLength;
                    if (text.Length > limit)
                    {
                        var previewBound = inContent && ContentPreviewLength < maxContentLength;
                        var marker = previewBound ? "[REDACTED_PREVIEW]" : "[TRUNCATED]";
                        return $"{text[..limit]}…{marker}";
                    }
                    return text;
                }
            case IDictionary<string, object?> map:
                {
                    var output = new Dictionary<string, object?>(map.Count, StringComparer.Ordinal);
                    foreach (var (key, child) in map)
                    {
                        var isContent = ContentKey().IsMatch(key);
                        var shouldRedact =
                            SecretKey().IsMatch(key)
                            || configured.Contains(key.ToLowerInvariant())
                            || (mode == ContentCaptureMode.MetadataOnly && isContent);
                        output[key] = shouldRedact
                            ? "[REDACTED]"
                            : Visit(child, inContent || (previewing && isContent), mode, configured, previewing, maxContentLength);
                    }
                    return output;
                }
            case IEnumerable enumerable when current is not string:
                {
                    var list = new List<object?>();
                    foreach (var item in enumerable)
                    {
                        list.Add(Visit(item, inContent, mode, configured, previewing, maxContentLength));
                    }
                    return list;
                }
            default:
                return current;
        }
    }

    /// <summary>
    /// Coerce a redacted value into flat span-event attributes. Nested structures are
    /// JSON-serialised so they survive the OTLP boundary without being dropped.
    /// Mirrors the Python <c>_flatten</c>.
    /// </summary>
    public static Dictionary<string, object?> Flatten(object? value)
    {
        var output = new Dictionary<string, object?>(StringComparer.Ordinal);
        if (value is IDictionary<string, object?> map)
        {
            foreach (var (key, item) in map)
            {
                output[key] = CoerceLeaf(item);
            }
        }
        else
        {
            output["value"] = IsPrimitive(value) ? value : Stringify(value);
        }
        return output;
    }

    private static object? CoerceLeaf(object? item)
    {
        if (IsPrimitive(item))
        {
            return item;
        }
        if (item is IEnumerable enumerable && item is not string)
        {
            var all = new List<object?>();
            var homogeneous = true;
            foreach (var element in enumerable)
            {
                if (!IsPrimitive(element))
                {
                    homogeneous = false;
                    break;
                }
                all.Add(element);
            }
            if (homogeneous)
            {
                return all;
            }
        }
        return Stringify(item);
    }

    private static bool IsPrimitive(object? value) =>
        value is string or bool
            or byte or sbyte or short or ushort or int or uint or long or ulong
            or float or double or decimal;

    private static string Stringify(object? value)
    {
        if (value is null)
        {
            return "null";
        }
        try
        {
            return JsonSerializer.Serialize(value);
        }
        catch (NotSupportedException)
        {
            return Convert.ToString(value, CultureInfo.InvariantCulture) ?? value.ToString() ?? string.Empty;
        }
    }
}
