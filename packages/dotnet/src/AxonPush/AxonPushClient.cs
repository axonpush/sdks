using AxonPush.Events;
using AxonPush.Gates;
using AxonPush.Internal;
using Microsoft.Extensions.Logging;

namespace AxonPush;

/// <summary>
/// Entry point for the AxonPush HTTP API. Construct one client per application, treat it as a
/// singleton, and dispose at shutdown.
/// </summary>
public sealed class AxonPushClient : IDisposable, IAsyncDisposable
{
    private readonly AxonPushTransport _transport;

    public AxonPushClient(AxonPushOptions options, ILoggerFactory? loggerFactory = null)
        : this(options, null, loggerFactory)
    {
    }

    public AxonPushClient(AxonPushOptions options, HttpClient? httpClient, ILoggerFactory? loggerFactory = null)
    {
        ArgumentNullException.ThrowIfNull(options);
        _transport = new AxonPushTransport(options, httpClient, loggerFactory);
        Events = new EventsResource(_transport);
        Gates = new GatesResource(_transport);
    }

    /// <summary>The events resource (POST /events).</summary>
    public EventsResource Events { get; }

    /// <summary>The release-gate resource (policies and gate-decision history under /v2/gate-*).</summary>
    public GatesResource Gates { get; }

    public void Dispose()
    {
        _transport.Dispose();
    }

    public ValueTask DisposeAsync()
    {
        _transport.Dispose();
        return ValueTask.CompletedTask;
    }
}
