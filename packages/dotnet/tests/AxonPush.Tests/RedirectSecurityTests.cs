using System.Net;
using System.Net.Sockets;
using AxonPush.Events;
using Xunit;

namespace AxonPush.Tests;

public class RedirectSecurityTests
{
    [Theory]
    [InlineData("ak_synthetic", 302)]
    [InlineData("pt_synthetic", 307)]
    public async Task OwnedClient_DoesNotForwardCredentialsToRedirectTarget(string key, int status)
    {
        using var destination = new LoopbackServer(context =>
        {
            context.Response.StatusCode = 200;
            context.Response.Close();
        });
        using var origin = new LoopbackServer(context =>
        {
            context.Response.StatusCode = status;
            context.Response.RedirectLocation = destination.Url.ToString();
            context.Response.Close();
        });
        using var client = new AxonPushClient(new AxonPushOptions
        {
            BaseUrl = origin.Url, ApiKey = key, TenantId = "synthetic", MaxRetries = 2,
        });
        var result = await client.Events.PublishAsync(new PublishRequest
        {
            Identifier = "synthetic", Payload = new Dictionary<string, object?>(), ChannelId = "synthetic",
        });
        Assert.False(result.Success);
        Assert.Equal((HttpStatusCode)status, result.StatusCode);
        Assert.Equal(1, origin.RequestCount);
        Assert.Equal(0, destination.RequestCount);
    }

    private sealed class LoopbackServer : IDisposable
    {
        private readonly HttpListener _listener = new();
        private readonly Task _serving;
        private int _requests;
        public Uri Url { get; }
        public int RequestCount => Volatile.Read(ref _requests);
        public LoopbackServer(Action<HttpListenerContext> respond)
        {
            using var port = new TcpListener(IPAddress.Loopback, 0);
            port.Start();
            Url = new Uri($"http://127.0.0.1:{((IPEndPoint)port.LocalEndpoint).Port}/");
            port.Stop();
            _listener.Prefixes.Add(Url.ToString());
            _listener.Start();
            _serving = Task.Run(async () =>
            {
                try
                {
                    while (_listener.IsListening)
                    {
                        var context = await _listener.GetContextAsync();
                        Interlocked.Increment(ref _requests);
                        respond(context);
                    }
                }
                catch (HttpListenerException) when (!_listener.IsListening) { }
                catch (ObjectDisposedException) { }
            });
        }
        public void Dispose()
        {
            _listener.Close();
            _serving.GetAwaiter().GetResult();
        }
    }
}
