using System.Net;
using System.Text;
using System.Text.Json;
using AxonPush.Gates;
using Xunit;

namespace AxonPush.Tests;

public class GatesResourceTests
{
    private static (AxonPushClient client, JsonHandler handler) Build(HttpStatusCode status, string body)
    {
        var handler = new JsonHandler(status, body);
        var options = new AxonPushOptions { ApiKey = "ak_test", TenantId = "org_test" };
        var http = new HttpClient(handler) { BaseAddress = options.BaseUrl };
        return (new AxonPushClient(options, http), handler);
    }

    [Fact]
    public async Task ListPoliciesAsync_GetsPoliciesPath_AndStampsHeaders()
    {
        var (client, handler) = Build(HttpStatusCode.OK, """{"data":[]}""");
        using (client)
        {
            var result = await client.Gates.ListPoliciesAsync();

            Assert.NotNull(result);
            Assert.Empty(result!.Data);
            Assert.Equal(HttpMethod.Get, handler.Request!.Method);
            Assert.Equal("/v2/gate-policies", handler.Request.RequestUri!.AbsolutePath);
            Assert.Equal("ak_test", handler.Request.Headers.GetValues("X-API-Key").Single());
            Assert.Equal("org_test", handler.Request.Headers.GetValues("x-tenant-id").Single());
        }
    }

    [Fact]
    public async Task SavePolicyAsync_PostsCamelCaseBody_OmittingNulls()
    {
        const string response = """
        {"orgId":"org_test","scopeType":"dataset","scopeId":"ds_1","enabled":true,
         "createdAt":"2026-01-01T00:00:00Z","updatedAt":"2026-01-01T00:00:00Z","minScore":0.9}
        """;
        var (client, handler) = Build(HttpStatusCode.OK, response);
        using (client)
        {
            var result = await client.Gates.SavePolicyAsync(new SaveGatePolicyDto
            {
                ScopeType = GatePolicyScope.Dataset,
                ScopeId = "ds_1",
                MinScore = 0.9,
            });

            Assert.Equal(HttpMethod.Post, handler.Request!.Method);
            Assert.Equal("/v2/gate-policies", handler.Request.RequestUri!.AbsolutePath);
            Assert.Contains("\"scopeType\":\"dataset\"", handler.RequestBody);
            Assert.Contains("\"scopeId\":\"ds_1\"", handler.RequestBody);
            Assert.Contains("\"minScore\":0.9", handler.RequestBody);
            // null optionals are dropped by the client's WhenWritingNull policy
            Assert.DoesNotContain("description", handler.RequestBody);
            Assert.DoesNotContain("name", handler.RequestBody);

            Assert.NotNull(result);
            Assert.Equal("ds_1", result!.ScopeId);
            Assert.True(result.Enabled);
            Assert.Equal(0.9, result.MinScore);
        }
    }

    [Fact]
    public async Task GetPolicyAsync_BuildsScopedPath()
    {
        var (client, handler) = Build(HttpStatusCode.OK, """
        {"orgId":"o","scopeType":"target","scopeId":"tgt_1","enabled":true,
         "createdAt":"2026-01-01T00:00:00Z","updatedAt":"2026-01-01T00:00:00Z"}
        """);
        using (client)
        {
            var result = await client.Gates.GetPolicyAsync(GatePolicyScope.Target, "tgt_1");

            Assert.Equal(HttpMethod.Get, handler.Request!.Method);
            Assert.Equal("/v2/gate-policies/target/tgt_1", handler.Request.RequestUri!.AbsolutePath);
            Assert.Equal("tgt_1", result!.ScopeId);
        }
    }

    [Fact]
    public async Task DeletePolicyAsync_SendsDelete_AndReadsFlag()
    {
        var (client, handler) = Build(HttpStatusCode.OK, """{"deleted":true}""");
        using (client)
        {
            var result = await client.Gates.DeletePolicyAsync(GatePolicyScope.Dataset, "ds_1");

            Assert.Equal(HttpMethod.Delete, handler.Request!.Method);
            Assert.Equal("/v2/gate-policies/dataset/ds_1", handler.Request.RequestUri!.AbsolutePath);
            Assert.True(result!.Deleted);
        }
    }

    [Fact]
    public async Task ListRunsAsync_ComposesQueryFromProvidedParams()
    {
        var (client, handler) = Build(HttpStatusCode.OK, """{"data":[],"cursor":null}""");
        using (client)
        {
            await client.Gates.ListRunsAsync(experimentId: "exp_1", limit: "10");

            Assert.Equal("/v2/gate-runs", handler.Request!.RequestUri!.AbsolutePath);
            var query = handler.Request.RequestUri.Query;
            Assert.Contains("experimentId=exp_1", query);
            Assert.Contains("limit=10", query);
            Assert.DoesNotContain("cursor", query);
        }
    }

    [Fact]
    public async Task ListRunsAsync_NoParams_SendsNoQuery()
    {
        var (client, handler) = Build(HttpStatusCode.OK, """{"data":[]}""");
        using (client)
        {
            await client.Gates.ListRunsAsync();
            Assert.Equal(string.Empty, handler.Request!.RequestUri!.Query);
        }
    }

    [Fact]
    public async Task ListRunsAsync_DeserializesRun_WithMetricsThresholdsAndNullCursor()
    {
        const string response = """
        {"data":[{"orgId":"o","gateRunId":"gr_1","experimentId":"exp_1","passed":true,
          "reasons":["score cleared"],"metrics":{"score":0.91},"thresholds":{"minScore":0.8},
          "source":"cli","createdAt":"2026-01-01T00:00:00Z","gitCommit":"abc123"}],"cursor":null}
        """;
        var (client, handler) = Build(HttpStatusCode.OK, response);
        using (client)
        {
            var result = await client.Gates.ListRunsAsync();

            Assert.NotNull(result);
            Assert.Null(result!.Cursor);
            var run = Assert.Single(result.Data);
            Assert.True(run.Passed);
            Assert.Equal("cli", run.Source);
            Assert.Equal("abc123", run.GitCommit);
            Assert.Equal("score cleared", Assert.Single(run.Reasons));
            Assert.Equal(0.8, run.Thresholds["minScore"]);
            Assert.Equal(0.91, ((JsonElement)run.Metrics["score"]!).GetDouble());
        }
    }

    [Fact]
    public async Task GateCalls_DoNotFailOpen_TheyThrowOnError()
    {
        // FailOpen defaults to true, but gate calls are control-plane and must surface errors.
        var (client, _) = Build(HttpStatusCode.Forbidden, """{"message":"nope"}""");
        using (client)
        {
            var ex = await Assert.ThrowsAsync<AxonPushException>(() => client.Gates.ListPoliciesAsync());
            Assert.Equal(HttpStatusCode.Forbidden, ex.StatusCode);
        }
    }

    private sealed class JsonHandler : HttpMessageHandler
    {
        private readonly HttpStatusCode _status;
        private readonly string _body;

        public JsonHandler(HttpStatusCode status, string body)
        {
            _status = status;
            _body = body;
        }

        public HttpRequestMessage? Request { get; private set; }

        public string? RequestBody { get; private set; }

        protected override async Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
        {
            Request = request;
            if (request.Content is not null)
            {
                RequestBody = await request.Content.ReadAsStringAsync(cancellationToken).ConfigureAwait(false);
            }

            return new HttpResponseMessage(_status)
            {
                Content = new StringContent(_body, Encoding.UTF8, "application/json"),
            };
        }
    }
}
