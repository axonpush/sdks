using System.Net;
using System.Text.Json;
using AxonPush.Events;
using AxonPush.Evidence;
using Xunit;

namespace AxonPush.Tests;

public sealed class EvidenceTests
{
    private sealed class Capture : HttpMessageHandler
    {
        internal readonly List<JsonElement> Bodies = [];
        protected override async Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken token)
        {
            Bodies.Add(JsonDocument.Parse(await request.Content!.ReadAsStringAsync(token)).RootElement.Clone());
            return new(HttpStatusCode.OK) { Content = new StringContent("{}") };
        }
    }

    [Fact]
    public async Task NestedTasksPropagateToOrdinaryPublishesAndRestoreTheirParent()
    {
        var handler = new Capture();
        using var http = new HttpClient(handler);
        using var client = new AxonPushClient(new AxonPushOptions { ApiKey = "test", TenantId = "test" }, http);
        var evidence = new EvidenceRecorder(client.Events, "channel", "agent");
        await evidence.TaskAsync("Review a case", async (parent, token) => {
            return await evidence.TaskAsync("Check a reference", async (child, inner) => {
                await client.Events.PublishAsync(new PublishRequest { Identifier = "ordinary", ChannelId = "channel", Payload = new Dictionary<string, object?>() }, inner);
                var metadata = handler.Bodies.Last().GetProperty("metadata");
                Assert.Equal(child, metadata.GetProperty("axonpush.task_id").GetString());
                Assert.Equal(parent, metadata.GetProperty("axonpush.parent_task_id").GetString());
                return true;
            }, token);
        });
        Assert.Null(EvidenceContext.Current.Value);
    }
}
