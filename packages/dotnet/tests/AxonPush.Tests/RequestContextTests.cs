using System.Collections.Concurrent;
using System.Net;
using System.Text.Json;
using AxonPush.Events;
using AxonPush.Operations;
using Xunit;
namespace AxonPush.Tests;

public sealed class RequestContextTests
{
    private sealed class Capture : HttpMessageHandler
    {
        internal readonly ConcurrentQueue<JsonElement> Bodies = new();
        protected override async Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken token)
        {
            Bodies.Enqueue(JsonDocument.Parse(await request.Content!.ReadAsStringAsync(token)).RootElement.Clone());
            return new(HttpStatusCode.OK) { Content = new StringContent("{}") };
        }
    }
    private static RequestContext Context(string user) => new() { WorkspaceId = "ws", Environment = "dev", Subjects = new Dictionary<string, string> { { "user", user }, { "company", "acme" } } };
    [Fact]
    public async Task ConcurrentCustomersNeverLeakAcrossClientsOrAfterTheRequest()
    {
        var handler = new Capture(); using var http = new HttpClient(handler); using var client = new AxonPushClient(new() { ApiKey = "test", TenantId = "org" }, http); using var other = new AxonPushClient(new() { ApiKey = "test", TenantId = "org" }, new HttpClient(new Capture()));
        await Task.WhenAll(new[] { "alice", "bob" }.Select(async id =>
        {
            using var scope = client.BeginContext(Context(id)); await Task.Yield();
            Assert.Null(RequestContextScope.Read(other.ContextOwner));
            await client.Events.PublishAsync(new() { Identifier = "request", ChannelId = "channel", Payload = new { } });
        }));
        Assert.Null(RequestContextScope.Read(client.ContextOwner));
        Assert.Equal(new[] { "alice", "bob" }, handler.Bodies.Select(b => b.GetProperty("metadata").GetProperty("user.id").GetString()).OrderBy(x => x));
    }
    [Fact]
    public async Task NestedScopeRestoresParentAndConflictingCaseSubjectsAreRejected()
    {
        var handler = new Capture(); using var http = new HttpClient(handler); using var client = new AxonPushClient(new() { ApiKey = "test", TenantId = "org" }, http);
        using var scope = client.BeginContext(Context("alice"));
        using (client.BeginContext(Context("bob"))) Assert.Equal("bob", RequestContextScope.Read(client.ContextOwner)!.Subjects["user"]);
        Assert.Equal("alice", RequestContextScope.Read(client.ContextOwner)!.Subjects["user"]);
        await scope.PublishFactsAsync("booking", new() { CaseId = "b1", Facts = Array.Empty<Fact>(), Coverage = Array.Empty<Coverage>() });
        Assert.True(handler.Bodies.TryDequeue(out var body)); Assert.Equal("alice", body.GetProperty("input").GetProperty("subjects").GetProperty("user").GetString());
        await Assert.ThrowsAsync<ArgumentException>(() => scope.PublishFactsAsync("booking", new() { CaseId = "b1", Subjects = new Dictionary<string, string> { { "user", "someone-else" } } }));
    }
}
