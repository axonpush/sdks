using System.Text.Json;
using System.Text.Json.Nodes;
using AxonPush.Events;
using AxonPush.Internal;
using Xunit;

namespace AxonPush.Tests.Contract;

/// <summary>
/// Asserts the client against contract/openapi.sdk.json and contract/fixtures.
///
/// This SDK was the only one without a generated client, and the only one that
/// did not work: it posted to <c>events</c>, where the sole route is
/// <c>GET /events/search</c>, and it sent <c>channelId</c> where the DTO
/// declares <c>channel_id</c>. Nothing compared it to the contract, so nothing
/// noticed. These tests are that comparison.
/// </summary>
public sealed class ContractTests
{
    private static readonly JsonNode Spec = LoadContract("openapi.sdk.json");
    private static readonly JsonNode Topics = LoadContract("fixtures/topics.json");
    private static readonly JsonNode Headers = LoadContract("fixtures/headers.json");
    private static readonly JsonNode Env = LoadContract("fixtures/env.json");

    private static JsonNode LoadContract(string relative)
    {
        // probe for the file, not a directory named "contract": this test project
        // has a Contract/ folder of its own, and Windows paths are case-insensitive
        var suffix = Path.Combine("contract", relative.Replace('/', Path.DirectorySeparatorChar));
        var dir = new DirectoryInfo(AppContext.BaseDirectory);
        while (dir is not null && !File.Exists(Path.Combine(dir.FullName, suffix)))
        {
            dir = dir.Parent;
        }

        if (dir is null)
        {
            throw new InvalidOperationException($"could not locate contract/{relative} above the test output");
        }

        var path = Path.Combine(dir.FullName, suffix);
        return JsonNode.Parse(File.ReadAllText(path))
               ?? throw new InvalidOperationException($"{relative} was empty");
    }

    private static JsonObject PublishSchema()
    {
        var op = Spec["paths"]!["/event"]!["post"]!;
        var reference = op["requestBody"]!["content"]!["application/json"]!["schema"]!["$ref"]!
            .GetValue<string>();
        var name = reference.Split('/')[^1];
        return Spec["components"]!["schemas"]![name]!.AsObject();
    }

    [Fact]
    public void PublishRouteMatchesTheContract()
    {
        // the bug: "events" resolved to the search path, which has no POST
        Assert.NotNull(Spec["paths"]!["/event"]?["post"]);
        Assert.Null(Spec["paths"]!["/events"]?["post"]);
        Assert.Equal("event", AxonPushTransport.EventsPath);
    }

    [Fact]
    public void PublishBodyUsesTheFieldNamesTheContractDeclares()
    {
        var request = new PublishRequest
        {
            Identifier = "id",
            Payload = new { ok = true },
            ChannelId = "chan_1",
            AgentId = "agent_1",
        };

        var json = JsonSerializer.Serialize(request, AxonPushJsonOptions.Default);
        var sent = JsonNode.Parse(json)!.AsObject();
        var declared = PublishSchema()["properties"]!.AsObject()
            .Select(p => p.Key)
            .ToHashSet(StringComparer.Ordinal);

        // forbidNonWhitelisted is on server-side, so an undeclared field is a 400
        foreach (var field in sent.Select(p => p.Key))
        {
            Assert.True(declared.Contains(field), $"'{field}' is not declared by CreateEventDto");
        }
    }

    [Fact]
    public void PublishBodyCarriesEveryRequiredField()
    {
        var required = PublishSchema()["required"]!.AsArray()
            .Select(n => n!.GetValue<string>())
            .ToArray();

        var json = JsonSerializer.Serialize(
            new PublishRequest { Identifier = "id", Payload = new { }, ChannelId = "chan_1" },
            AxonPushJsonOptions.Default);
        var sent = JsonNode.Parse(json)!.AsObject();

        foreach (var field in required)
        {
            Assert.True(sent.ContainsKey(field), $"required field '{field}' was not serialised");
        }
    }

    [Fact]
    public void AgentIdIsSupported()
    {
        // every Python and TypeScript integration sends one; this SDK had no field for it
        Assert.Contains("agentId", PublishSchema()["properties"]!.AsObject().Select(p => p.Key));

        var json = JsonSerializer.Serialize(
            new PublishRequest
            {
                Identifier = "id",
                Payload = new { },
                ChannelId = "c",
                AgentId = "agent_1",
            },
            AxonPushJsonOptions.Default);
        Assert.Contains("\"agentId\":\"agent_1\"", json);
    }

    [Fact]
    public void HeaderNamesMatchTheFixture()
    {
        Assert.Equal("X-API-Key", Headers["auth"]!["apiKey"]!.GetValue<string>());
        Assert.Equal("x-tenant-id", Headers["tenancy"]!["orgId"]!.GetValue<string>());
        Assert.Equal(
            "X-Axonpush-Environment",
            Headers["scoping"]!["environment"]!.GetValue<string>());
        Assert.Equal("X-Axonpush-Trace-Id", Headers["tracing"]!["traceId"]!.GetValue<string>());
    }

    [Fact]
    public void DefaultsMatchTheContract()
    {
        var vars = Env["variables"]!;
        var options = new AxonPushOptions();

        Assert.Equal(
            vars["AXONPUSH_BASE_URL"]!["default"]!.GetValue<string>().TrimEnd('/'),
            options.BaseUrl.ToString().TrimEnd('/'));
        Assert.Equal(vars["AXONPUSH_MAX_RETRIES"]!["default"]!.GetValue<int>(), options.MaxRetries);
        Assert.Equal(vars["AXONPUSH_FAIL_OPEN"]!["default"]!.GetValue<bool>(), options.FailOpen);
        Assert.Equal("seconds", vars["AXONPUSH_TIMEOUT"]!["unit"]!.GetValue<string>());
        Assert.Equal(
            vars["AXONPUSH_TIMEOUT"]!["default"]!.GetValue<double>(),
            options.Timeout.TotalSeconds);
    }

    [Fact]
    public void RetryLadderMatchesTheContract()
    {
        var expected = Env["retry"]!["backoffMs"]!.AsArray()
            .Select(n => TimeSpan.FromMilliseconds(n!.GetValue<int>()))
            .ToArray();

        Assert.Equal(expected, RetryPolicy.BackoffSchedule.ToArray());
    }

    [Fact]
    public void TopicGrammarIsRecorded()
    {
        // .NET does not build topics yet; assert the shape it must follow when it does
        Assert.Equal(
            new[] { "prefix", "orgId", "envSlug", "appId", "channelId", "eventType", "agentId" },
            Topics["segments"]!.AsArray().Select(n => n!.GetValue<string>()).ToArray());
        Assert.Equal("_", Topics["publishFallback"]!.GetValue<string>());
        Assert.Equal("+", Topics["subscribeWildcard"]!.GetValue<string>());
    }
}
