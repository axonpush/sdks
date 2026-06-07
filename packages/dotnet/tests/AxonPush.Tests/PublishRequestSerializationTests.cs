using System.Text.Json;
using AxonPush.Events;
using AxonPush.Internal;
using Xunit;

namespace AxonPush.Tests;

public class PublishRequestSerializationTests
{
    [Fact]
    public void Serializes_With_CamelCase_Keys_MatchingPython()
    {
        var request = new PublishRequest
        {
            Identifier = "0123456789abcdef",
            Payload = new Dictionary<string, object?>
            {
                ["traceId"] = "abcd",
                ["nested"] = new Dictionary<string, object?> { ["k"] = "v" },
            },
            ChannelId = "ch_1",
            EventType = EventType.AppSpan,
            TraceId = "0123456789abcdef0123456789abcdef",
            SpanId = "fedcba9876543210",
            Environment = "production",
            Metadata = new Dictionary<string, object?> { ["source"] = "test" },
        };

        var json = JsonSerializer.Serialize(request, AxonPushJsonOptions.Default);

        using var doc = JsonDocument.Parse(json);
        var root = doc.RootElement;

        Assert.Equal("0123456789abcdef", root.GetProperty("identifier").GetString());
        Assert.Equal("ch_1", root.GetProperty("channelId").GetString());
        Assert.Equal(EventType.AppSpan, root.GetProperty("eventType").GetString());
        Assert.Equal("0123456789abcdef0123456789abcdef", root.GetProperty("traceId").GetString());
        Assert.Equal("fedcba9876543210", root.GetProperty("spanId").GetString());
        Assert.Equal("production", root.GetProperty("environment").GetString());
        Assert.Equal("test", root.GetProperty("metadata").GetProperty("source").GetString());

        Assert.Equal("abcd", root.GetProperty("payload").GetProperty("traceId").GetString());
        Assert.Equal("v", root.GetProperty("payload").GetProperty("nested").GetProperty("k").GetString());
    }

    [Fact]
    public void Omits_Null_Optional_Fields()
    {
        var request = new PublishRequest
        {
            Identifier = "id",
            Payload = new Dictionary<string, object?>(),
            ChannelId = "ch",
        };

        var json = JsonSerializer.Serialize(request, AxonPushJsonOptions.Default);

        using var doc = JsonDocument.Parse(json);
        var root = doc.RootElement;

        Assert.False(root.TryGetProperty("traceId", out _));
        Assert.False(root.TryGetProperty("spanId", out _));
        Assert.False(root.TryGetProperty("environment", out _));
        Assert.False(root.TryGetProperty("parentEventId", out _));
        Assert.False(root.TryGetProperty("metadata", out _));
    }
}
