using System.Net;
using System.Text.Json;
using AxonPush.Events;
using AxonPush.Internal;
using Xunit;

namespace AxonPush.Tests;

public sealed class InfrastructureTests
{
    [Fact]
    public async Task PublishRetriesPreserveGeneratedIdentity()
    {
        var identities = new List<string?>();
        using var http = new HttpClient(new ProbeHandler(async (request, token) =>
        {
            using var body = JsonDocument.Parse(await request.Content!.ReadAsStringAsync(token));
            identities.Add(body.RootElement.GetProperty("dedupKey").GetString());
            return new HttpResponseMessage(identities.Count == 1 ? HttpStatusCode.ServiceUnavailable : HttpStatusCode.OK);
        }));
        using var client = new AxonPushClient(new AxonPushOptions { ApiKey = "synthetic", TenantId = "synthetic", MaxRetries = 1 }, http);
        await client.Events.PublishAsync(new PublishRequest { Identifier = "synthetic", ChannelId = "synthetic", Payload = new Dictionary<string, object?>() });
        Assert.Equal(2, identities.Count);
        Assert.False(string.IsNullOrWhiteSpace(identities[0]));
        Assert.Equal(identities[0], identities[1]);
    }

    [Fact]
    public async Task InvocationBudgetAppliesToInjectedClient()
    {
        using var http = new HttpClient(new ProbeHandler(async (_, token) => { await Task.Delay(5000, token); return new HttpResponseMessage(HttpStatusCode.OK); }));
        using var client = new AxonPushClient(new AxonPushOptions { ApiKey = "synthetic", TenantId = "synthetic", Timeout = TimeSpan.FromMilliseconds(25), FailOpen = false }, http);
        await Assert.ThrowsAsync<AxonPushException>(() => client.Events.PublishAsync(new PublishRequest { Identifier = "synthetic", ChannelId = "synthetic", Payload = new Dictionary<string, object?>() }));
    }

    [Fact]
    public async Task NonIdempotentCreationDoesNotRetry()
    {
        var calls = 0;
        using var http = new HttpClient(new ProbeHandler((_, _) => { calls++; throw new HttpRequestException("synthetic lost response"); }));
        using var transport = new AxonPushTransport(new AxonPushOptions { ApiKey = "synthetic", TenantId = "synthetic", MaxRetries = 3 }, http, null);
        await Assert.ThrowsAsync<AxonPushException>(() => transport.SendAsync<object>(HttpMethod.Post, "apps", new { name = "synthetic" }, CancellationToken.None));
        Assert.Equal(1, calls);
    }

    private sealed class ProbeHandler(Func<HttpRequestMessage, CancellationToken, Task<HttpResponseMessage>> send) : HttpMessageHandler
    {
        protected override Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken) => send(request, cancellationToken);
    }
}
