using System.Diagnostics;
using AxonPush.Otel.Internal;
using Xunit;

namespace AxonPush.Otel.Tests;

public class SpanPayloadBuilderTests
{
    private const string SourceName = "AxonPush.Otel.Tests";
    private static readonly ActivityListener Listener = new()
    {
        ShouldListenTo = s => s.Name == SourceName,
        Sample = (ref ActivityCreationOptions<ActivityContext> _) => ActivitySamplingResult.AllDataAndRecorded,
    };
    private static readonly bool ListenerRegistered = RegisterListener();
    private static readonly ActivitySource Source = new(SourceName, "0.1.0");

    private static bool RegisterListener()
    {
        ActivitySource.AddActivityListener(Listener);
        return true;
    }

    public SpanPayloadBuilderTests()
    {
        _ = ListenerRegistered;
    }

    [Fact]
    public void Build_MapsCoreFields()
    {
        using var activity = Source.StartActivity("ExampleSpan", ActivityKind.Client)!;
        activity.SetTag("gen_ai.request.model", "gpt-4o-mini");
        activity.SetTag("gen_ai.usage.input_tokens", 17);
        activity.SetStatus(ActivityStatusCode.Error, "boom");
        activity.Stop();

        var resource = new Dictionary<string, object?>
        {
            ["service.name"] = "test-svc",
            ["service.version"] = "0.0.1",
        };

        var payload = SpanPayloadBuilder.Build(activity, resource);

        Assert.Equal(activity.TraceId.ToHexString(), payload["traceId"]);
        Assert.Equal(activity.SpanId.ToHexString(), payload["spanId"]);
        Assert.Equal("ExampleSpan", payload["name"]);
        Assert.Equal(3, payload["kind"]);

        var attributes = Assert.IsType<Dictionary<string, object?>>(payload["attributes"]);
        Assert.Equal("gpt-4o-mini", attributes["gen_ai.request.model"]);
        Assert.Equal(17, attributes["gen_ai.usage.input_tokens"]);

        var status = Assert.IsType<Dictionary<string, object?>>(payload["status"]);
        Assert.Equal(2, status["code"]);
        Assert.Equal("boom", status["message"]);

        var scope = Assert.IsType<Dictionary<string, object?>>(payload["scope"]);
        Assert.Equal("AxonPush.Otel.Tests", scope["name"]);
        Assert.Equal("0.1.0", scope["version"]);

        var emittedResource = Assert.IsType<Dictionary<string, object?>>(payload["resource"]);
        Assert.Equal("test-svc", emittedResource["service.name"]);
        Assert.Equal("0.0.1", emittedResource["service.version"]);

        var startNanos = Assert.IsType<string>(payload["startTimeUnixNano"]);
        var endNanos = Assert.IsType<string>(payload["endTimeUnixNano"]);
        Assert.True(long.Parse(endNanos) >= long.Parse(startNanos));
    }

    [Fact]
    public void Build_OmitsParentSpan_WhenRoot()
    {
        using var activity = Source.StartActivity("Root")!;
        activity.Stop();

        var payload = SpanPayloadBuilder.Build(activity, new Dictionary<string, object?>());

        Assert.False(payload.ContainsKey("parentSpanId"));
    }

    [Fact]
    public void Build_IncludesParentSpan_ForChild()
    {
        using var parent = Source.StartActivity("Parent")!;
        using var child = Source.StartActivity("Child", ActivityKind.Internal, parent.Context)!;
        child.Stop();

        var payload = SpanPayloadBuilder.Build(child, new Dictionary<string, object?>());

        Assert.Equal(parent.SpanId.ToHexString(), payload["parentSpanId"]);
    }

    [Fact]
    public void Build_CoercesAttributeValues()
    {
        using var activity = Source.StartActivity("WithFancyTags")!;
        activity.SetTag("list", new[] { 1, 2, 3 });
        activity.SetTag("guid", Guid.NewGuid());
        activity.Stop();

        var payload = SpanPayloadBuilder.Build(activity, new Dictionary<string, object?>());
        var attributes = Assert.IsType<Dictionary<string, object?>>(payload["attributes"]);

        var list = Assert.IsType<List<object?>>(attributes["list"]);
        Assert.Equal(3, list.Count);

        var guidString = Assert.IsType<string>(attributes["guid"]);
        Assert.False(string.IsNullOrEmpty(guidString));
    }
}
