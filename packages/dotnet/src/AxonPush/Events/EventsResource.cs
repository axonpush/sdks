using AxonPush.Internal;

namespace AxonPush.Events;

/// <summary>
/// Resource surface for publishing AxonPush events.
/// </summary>
public sealed class EventsResource
{
    private readonly AxonPushTransport _transport;

    internal EventsResource(AxonPushTransport transport)
    {
        _transport = transport;
    }

    /// <summary>
    /// Publishes a single event to AxonPush. Honours the client's fail-open setting.
    /// </summary>
    public Task<PublishResult> PublishAsync(PublishRequest request, CancellationToken cancellationToken = default)
    {
        ArgumentNullException.ThrowIfNull(request);
        return _transport.PostEventAsync(request, cancellationToken);
    }
}
