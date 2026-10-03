using System.Net;
using System.Text.Json;
using System.Text.Json.Nodes;
using AxonPush.Internal;
using AxonPush.Operations;
using Xunit;

namespace AxonPush.Tests;

public sealed class OperationsTests
{
    private static string FixturePath()
    {
        var directory = new DirectoryInfo(AppContext.BaseDirectory);
        while (directory is not null)
        {
            var path = Path.Combine(directory.FullName, "contract", "fixtures", "activity-observation.json");
            if (File.Exists(path)) return path;
            directory = directory.Parent;
        }
        throw new InvalidOperationException("Cannot locate shared observation fixture");
    }

    [Fact]
    public async Task Acceptance_RetryIdentityAndOriginalOccurrenceArePreserved()
    {
        var fixture = JsonSerializer.Deserialize<ActivityObservation>(File.ReadAllText(FixturePath()), AxonPushJsonOptions.Default)!;
        var captured = new List<string>();
        var handler = new Handler(async (request) =>
        {
            Assert.Equal("/workspaces/synthetic-workspace/observations", request.RequestUri!.AbsolutePath);
            Assert.Equal("dev", request.Headers.GetValues("X-Axonpush-Environment").Single());
            captured.Add(await request.Content!.ReadAsStringAsync());
            return new HttpResponseMessage(HttpStatusCode.OK) { Content = new StringContent("{\"receipts\":[{\"sourceEventId\":\"synthetic-operation-start-1\",\"status\":\"stored\",\"receivedAt\":\"2026-10-03T00:00:01Z\",\"projectedAt\":null}]}") };
        });
        var options = new AxonPushOptions { ApiKey = "ak_synthetic", TenantId = "synthetic-org", Environment = "dev", MaxRetries = 0 };
        using var http = new HttpClient(handler) { BaseAddress = new Uri("http://operations.example.test/") };
        using var sdk = new AxonPushClient(options, http);
        var body = new WorkspaceIngestInputBody { Environment = "dev", Observations = new[] { fixture } };
        var first = await sdk.Observations.AcceptAsync("synthetic-workspace", body);
        await sdk.Observations.AcceptAsync("synthetic-workspace", body);
        Assert.Equal(captured[0], captured[1]);
        Assert.Equal("stored", first!.Receipts![0].Status);
        Assert.Null(first.Receipts[0].ProjectedAt);
        var sent = JsonNode.Parse(captured[0])!["observations"]![0]!;
        Assert.Equal("synthetic-operation-start-1", sent["source_event_id"]!.GetValue<string>());
        Assert.Equal(fixture.OccurredAt, DateTimeOffset.Parse(sent["occurred_at"]!.GetValue<string>()));
        Assert.Equal("self_reported", sent["client"]!["confidence"]!.GetValue<string>());
        Assert.True(sent["client"]!["conflict"]!.GetValue<bool>());
        Assert.Equal(2, sent["client"]!["evidence"]!.AsArray().Count);
        Assert.Equal("mcp_client_info", sent["client"]!["evidence"]![0]!["source"]!.GetValue<string>());
        Assert.Equal("synthetic-company-1", sent["actor"]!["related_agent_ids"]![0]!.GetValue<string>());
        Assert.Equal("synthetic-role-1", sent["correlation"]!["role_id"]!.GetValue<string>());
        Assert.Equal(fixture.Correlation.TraceId, sent["correlation"]!["trace_id"]!.GetValue<string>());
    }

    [Fact]
    public async Task Receipt_EncodesOpaqueIdsAndSeparatesProjection()
    {
        var handler = new Handler((request) =>
        {
            Assert.Contains("synthetic%2Fworkspace/observations/source%3A1", request.RequestUri!.OriginalString);
            Assert.Equal("?environment=dev", request.RequestUri.Query);
            return Task.FromResult(new HttpResponseMessage(HttpStatusCode.OK) { Content = new StringContent("{\"sourceEventId\":\"source:1\",\"status\":\"projected\",\"receivedAt\":\"2026-10-03T00:00:01Z\",\"projectedAt\":\"2026-10-03T00:00:02Z\"}") });
        });
        using var http = new HttpClient(handler) { BaseAddress = new Uri("http://operations.example.test/") };
        using var sdk = new AxonPushClient(new AxonPushOptions { ApiKey = "ak_synthetic", TenantId = "synthetic-org", MaxRetries = 0 }, http);
        var result = await sdk.Observations.ReceiptAsync("synthetic/workspace", "source:1", "dev");
        Assert.Equal("projected", result!.Status);
        Assert.NotNull(result.ProjectedAt);
    }

    [Fact]
    public async Task ObservationConnectionFailure_FailsOpenWhenConfigured()
    {
        var handler = new Handler((_) => throw new HttpRequestException("synthetic connection failure"));
        using var http = new HttpClient(handler) { BaseAddress = new Uri("http://operations.example.test/") };
        using var sdk = new AxonPushClient(new AxonPushOptions { ApiKey = "ak_synthetic", TenantId = "synthetic-org", FailOpen = true, MaxRetries = 0 }, http);
        Assert.Null(await sdk.Observations.AcceptAsync("workspace", new WorkspaceIngestInputBody { Environment = "dev", Observations = Array.Empty<ActivityObservation>() }));
    }

    [Fact]
    public async Task ObservationAuthFailure_IsVisibleEvenWithFailOpen()
    {
        var handler = new Handler((_) => Task.FromResult(new HttpResponseMessage(HttpStatusCode.Unauthorized)));
        using var http = new HttpClient(handler) { BaseAddress = new Uri("http://operations.example.test/") };
        using var sdk = new AxonPushClient(new AxonPushOptions { ApiKey = "ak_synthetic", TenantId = "synthetic-org", FailOpen = true, MaxRetries = 0 }, http);
        var exception = await Assert.ThrowsAsync<AxonPushException>(() => sdk.Observations.AcceptAsync("workspace", new WorkspaceIngestInputBody { Environment = "dev", Observations = Array.Empty<ActivityObservation>() }));
        Assert.Equal(HttpStatusCode.Unauthorized, exception.StatusCode);
    }

    private sealed class Handler(Func<HttpRequestMessage, Task<HttpResponseMessage>> response) : HttpMessageHandler
    {
        protected override Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken) => response(request);
    }
}
