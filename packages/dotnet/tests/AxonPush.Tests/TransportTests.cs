using System.Net;
using AxonPush.Events;
using Xunit;

namespace AxonPush.Tests;

public class TransportTests
{
    [Fact]
    public async Task PublishAsync_StampsAuthHeaders()
    {
        var captured = new List<HttpRequestMessage>();
        var handler = new CapturingHandler(HttpStatusCode.OK, captured);
        var options = new AxonPushOptions
        {
            ApiKey = "ak_test",
            TenantId = "tenant",
            Environment = "production",
        };

        using var http = new HttpClient(handler) { BaseAddress = options.BaseUrl };
        using var client = new AxonPushClient(options, http);

        await client.Events.PublishAsync(new PublishRequest
        {
            Identifier = "id",
            Payload = new Dictionary<string, object?>(),
            ChannelId = "ch",
        });

        var request = captured.Single();
        Assert.Equal("ak_test", request.Headers.GetValues("X-API-Key").Single());
        Assert.Equal("tenant", request.Headers.GetValues("x-tenant-id").Single());
        Assert.Equal("production", request.Headers.GetValues("X-Axonpush-Environment").Single());
    }

    [Fact]
    public async Task PublishAsync_RetriesOn500_ThenSucceeds()
    {
        var statuses = new Queue<HttpStatusCode>(new[]
        {
            HttpStatusCode.InternalServerError,
            HttpStatusCode.InternalServerError,
            HttpStatusCode.OK,
        });
        var handler = new SequenceHandler(statuses);
        var options = new AxonPushOptions { ApiKey = "k", TenantId = "t", MaxRetries = 3 };

        using var http = new HttpClient(handler) { BaseAddress = options.BaseUrl };
        using var client = new AxonPushClient(options, http);

        var result = await client.Events.PublishAsync(new PublishRequest
        {
            Identifier = "id",
            Payload = new Dictionary<string, object?>(),
            ChannelId = "ch",
        });

        Assert.True(result.Success);
        Assert.Equal(3, result.Attempts);
    }

    [Fact]
    public async Task PublishAsync_FailOpen_SwallowsTerminalFailure()
    {
        var handler = new SequenceHandler(new Queue<HttpStatusCode>(new[] { HttpStatusCode.Forbidden }));
        var options = new AxonPushOptions { ApiKey = "k", TenantId = "t", FailOpen = true };

        using var http = new HttpClient(handler) { BaseAddress = options.BaseUrl };
        using var client = new AxonPushClient(options, http);

        var result = await client.Events.PublishAsync(new PublishRequest
        {
            Identifier = "id",
            Payload = new Dictionary<string, object?>(),
            ChannelId = "ch",
        });

        Assert.False(result.Success);
        Assert.Equal(HttpStatusCode.Forbidden, result.StatusCode);
    }

    [Fact]
    public async Task PublishAsync_FailClosed_Throws()
    {
        var handler = new SequenceHandler(new Queue<HttpStatusCode>(new[] { HttpStatusCode.Forbidden }));
        var options = new AxonPushOptions { ApiKey = "k", TenantId = "t", FailOpen = false };

        using var http = new HttpClient(handler) { BaseAddress = options.BaseUrl };
        using var client = new AxonPushClient(options, http);

        await Assert.ThrowsAsync<AxonPushException>(() => client.Events.PublishAsync(new PublishRequest
        {
            Identifier = "id",
            Payload = new Dictionary<string, object?>(),
            ChannelId = "ch",
        }));
    }

    private sealed class CapturingHandler : HttpMessageHandler
    {
        private readonly HttpStatusCode _status;
        private readonly List<HttpRequestMessage> _captured;

        public CapturingHandler(HttpStatusCode status, List<HttpRequestMessage> captured)
        {
            _status = status;
            _captured = captured;
        }

        protected override Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
        {
            _captured.Add(request);
            return Task.FromResult(new HttpResponseMessage(_status));
        }
    }

    private sealed class SequenceHandler : HttpMessageHandler
    {
        private readonly Queue<HttpStatusCode> _statuses;

        public SequenceHandler(Queue<HttpStatusCode> statuses)
        {
            _statuses = statuses;
        }

        protected override Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
        {
            var status = _statuses.Count > 0 ? _statuses.Dequeue() : HttpStatusCode.InternalServerError;
            return Task.FromResult(new HttpResponseMessage(status));
        }
    }
}
