using System.Net;
using System.Text;
using System.Text.Json;
using AxonPush.Internal.Api;
using Xunit;

namespace AxonPush.Cli.Tests;

/// <summary>
/// The gate call against a server older than the provenance fields, whose
/// forbidNonWhitelisted pipe answers an unknown field with a 400.
/// </summary>
public class GateProvenanceTests
{
    private sealed class GateHandler : HttpMessageHandler
    {
        public List<string> Bodies { get; } = [];

        public int RejectFirst { get; init; } = 1;

        protected override async Task<HttpResponseMessage> SendAsync(
            HttpRequestMessage request,
            CancellationToken cancellationToken)
        {
            var body = request.Content is null
                ? string.Empty
                : await request.Content.ReadAsStringAsync(cancellationToken);
            Bodies.Add(body);

            if (Bodies.Count <= RejectFirst)
            {
                return new HttpResponseMessage(HttpStatusCode.BadRequest)
                {
                    Content = new StringContent(
                        """{"message":["property source should not exist"]}""",
                        Encoding.UTF8,
                        "application/json"),
                };
            }

            return new HttpResponseMessage(HttpStatusCode.OK)
            {
                Content = new StringContent(
                    """{"passed":true,"reasons":[],"experimentId":"exp_1","metrics":{}}""",
                    Encoding.UTF8,
                    "application/json"),
            };
        }
    }

    private static (HttpEvaluationApi Api, GateHandler Handler, AxonPushClient Client) Build(
        int rejectFirst = 1)
    {
        var handler = new GateHandler { RejectFirst = rejectFirst };
        var options = new AxonPushOptions { ApiKey = "ak", TenantId = "t", MaxRetries = 0 };
        var http = new HttpClient(handler) { BaseAddress = options.BaseUrl };
        var client = new AxonPushClient(options, http);
        return (new HttpEvaluationApi(client), handler, client);
    }

    private static IReadOnlyDictionary<string, double> Thresholds =>
        new Dictionary<string, double> { ["minScore"] = 0.8 };

    [Fact]
    public async Task RetriesWithoutProvenanceWhenTheServerRejectsIt()
    {
        var (api, handler, client) = Build();
        using var owned = client;

        var verdict = await api.GateExperimentAsync(
            "exp_1",
            Thresholds,
            new GateProvenance("cli", "abc1234", "main"),
            CancellationToken.None);

        Assert.True(verdict.Passed);
        Assert.Equal(2, handler.Bodies.Count);
        Assert.Contains("\"source\"", handler.Bodies[0], StringComparison.Ordinal);

        var retried = JsonDocument.Parse(handler.Bodies[1]).RootElement;
        Assert.False(retried.TryGetProperty("source", out var _unusedSource));
        Assert.False(retried.TryGetProperty("gitCommit", out var _unusedCommit));
        Assert.Equal(0.8, retried.GetProperty("minScore").GetDouble());
    }

    [Fact]
    public async Task ABadRequestWithNoProvenanceToBlameSurfaces()
    {
        var (api, handler, client) = Build();
        using var owned = client;

        await Assert.ThrowsAsync<AxonPushApiException>(() => api.GateExperimentAsync(
            "exp_1",
            Thresholds,
            new GateProvenance(null, null, null),
            CancellationToken.None));

        Assert.Single(handler.Bodies);
    }

    [Fact]
    public async Task AServerThatRejectsBothTimesStillFails()
    {
        var (api, handler, client) = Build(rejectFirst: 2);
        using var owned = client;

        await Assert.ThrowsAsync<AxonPushApiException>(() => api.GateExperimentAsync(
            "exp_1",
            Thresholds,
            new GateProvenance("cli", "abc1234", "main"),
            CancellationToken.None));

        Assert.Equal(2, handler.Bodies.Count);
    }
}
