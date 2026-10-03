using AxonPush.Events;
using AxonPush.Operations;
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
        Workspaces = new WorkspacesResource(_transport);
        Templates = new TemplatesResource(_transport);
        Observations = new ObservationsResource(_transport);
        Activity = new ActivityResource(_transport);

    }

    /// <summary>The events resource (POST /events).</summary>
    public EventsResource Events { get; }
    public WorkspacesResource Workspaces { get; }
    public TemplatesResource Templates { get; }
    public ObservationsResource Observations { get; }
    public ActivityResource Activity { get; }


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
