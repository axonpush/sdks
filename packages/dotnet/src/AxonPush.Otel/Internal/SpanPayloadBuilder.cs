using System.Diagnostics;
using System.Globalization;

namespace AxonPush.Otel.Internal;

/// <summary>
/// Maps a <see cref="Activity"/> to the JSON-shaped dictionary the AxonPush events API expects.
/// Field names match the axonpush-python OTel exporter exactly so that traces from any client
/// land in the AxonPush UI with the same schema.
/// </summary>
internal static class SpanPayloadBuilder
{
    public static Dictionary<string, object?> Build(Activity activity, IReadOnlyDictionary<string, object?> resource)
    {
        ArgumentNullException.ThrowIfNull(activity);
        ArgumentNullException.ThrowIfNull(resource);

        var startNanos = ToUnixNanos(activity.StartTimeUtc);
        var endNanos = ToUnixNanos(activity.StartTimeUtc + activity.Duration);

        var payload = new Dictionary<string, object?>(StringComparer.Ordinal)
        {
            ["traceId"] = activity.TraceId.ToHexString(),
            ["spanId"] = activity.SpanId.ToHexString(),
            ["name"] = activity.DisplayName,
            ["kind"] = ActivityKindMapper.ToProtoInt(activity.Kind),
            ["startTimeUnixNano"] = startNanos.ToString(CultureInfo.InvariantCulture),
            ["endTimeUnixNano"] = endNanos.ToString(CultureInfo.InvariantCulture),
            ["status"] = BuildStatus(activity),
            ["attributes"] = BuildAttributes(activity),
            ["events"] = BuildEvents(activity),
            ["links"] = BuildLinks(activity),
            ["resource"] = new Dictionary<string, object?>(resource, StringComparer.Ordinal),
            ["scope"] = new Dictionary<string, object?>(StringComparer.Ordinal)
            {
                ["name"] = activity.Source.Name,
                ["version"] = string.IsNullOrEmpty(activity.Source.Version) ? null : activity.Source.Version,
            },
        };

        if (activity.ParentSpanId != default)
        {
            payload["parentSpanId"] = activity.ParentSpanId.ToHexString();
        }

        return payload;
    }

    private static Dictionary<string, object?> BuildStatus(Activity activity)
    {
        int code = activity.Status switch
        {
            ActivityStatusCode.Ok => 1,
            ActivityStatusCode.Error => 2,
            _ => 0,
        };

        return new Dictionary<string, object?>(StringComparer.Ordinal)
        {
            ["code"] = code,
            ["message"] = activity.StatusDescription,
        };
    }

    private static Dictionary<string, object?> BuildAttributes(Activity activity)
    {
        var attributes = new Dictionary<string, object?>(StringComparer.Ordinal);
        foreach (var tag in activity.TagObjects)
        {
            attributes[tag.Key] = AttributeValueCoercer.Coerce(tag.Value);
        }
        return attributes;
    }

    private static List<Dictionary<string, object?>> BuildEvents(Activity activity)
    {
        var events = new List<Dictionary<string, object?>>();
        foreach (var ev in activity.Events)
        {
            var attrs = new Dictionary<string, object?>(StringComparer.Ordinal);
            foreach (var tag in ev.Tags)
            {
                attrs[tag.Key] = AttributeValueCoercer.Coerce(tag.Value);
            }

            events.Add(new Dictionary<string, object?>(StringComparer.Ordinal)
            {
                ["timeUnixNano"] = ToUnixNanos(ev.Timestamp.UtcDateTime).ToString(CultureInfo.InvariantCulture),
                ["name"] = ev.Name,
                ["attributes"] = attrs,
            });
        }
        return events;
    }

    private static List<Dictionary<string, object?>> BuildLinks(Activity activity)
    {
        var links = new List<Dictionary<string, object?>>();
        foreach (var link in activity.Links)
        {
            var attrs = new Dictionary<string, object?>(StringComparer.Ordinal);
            foreach (var tag in link.Tags ?? [])
            {
                attrs[tag.Key] = AttributeValueCoercer.Coerce(tag.Value);
            }

            links.Add(new Dictionary<string, object?>(StringComparer.Ordinal)
            {
                ["traceId"] = link.Context.TraceId.ToHexString(),
                ["spanId"] = link.Context.SpanId.ToHexString(),
                ["attributes"] = attrs,
            });
        }
        return links;
    }

    private static long ToUnixNanos(DateTime utc)
    {
        var unixTicks = utc.Ticks - DateTime.UnixEpoch.Ticks;
        return unixTicks * 100;
    }
}
