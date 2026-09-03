using AxonPush.Internal;
using AxonPush.Internal.Api;

namespace AxonPush.Events;

/// <summary>
/// Publishing and reading events.
///
/// This one resource stays hand-written while the others are generated: only
/// publishing honours the client's fail-open setting, because telemetry must
/// never take the calling application down. Reads behave like every other
/// resource and surface failures.
/// </summary>
public sealed class EventsResource
{
    private readonly AxonPushTransport _transport;
    private readonly EventControllerClient _events;
    private readonly EventsSearchControllerClient _search;

    internal EventsResource(AxonPushTransport transport)
    {
        _transport = transport;
        _events = new EventControllerClient(transport.HttpClient);
        _search = new EventsSearchControllerClient(transport.HttpClient);
    }

    /// <summary>
    /// Publishes a single event to AxonPush. Honours the client's fail-open setting.
    /// </summary>
    public Task<PublishResult> PublishAsync(
        PublishRequest request,
        CancellationToken cancellationToken = default)
    {
        ArgumentNullException.ThrowIfNull(request);
        return _transport.PostEventAsync(request, cancellationToken);
    }

    /// <summary>List events on a channel. <c>GET /events</c></summary>
    public Task<EventListResponseDto> ListAsync(
        string channelId,
        string? agentId = null,
        string? cursor = null,
        string? environment = null,
        IEnumerable<string>? eventType = null,
        double? limit = null,
        string? payloadFilter = null,
        string? since = null,
        string? traceId = null,
        string? until = null,
        CancellationToken cancellationToken = default) =>
        _events.ListEventsAsync(
            channelId, agentId, cursor, environment, eventType, limit,
            payloadFilter, since, traceId, until, cancellationToken);

    /// <summary>Search events across the organisation. <c>GET /events/search</c></summary>
    public Task<EventListResponseDto> SearchAsync(
        string? agentId = null,
        string? appId = null,
        string? channelId = null,
        string? cursor = null,
        string? environment = null,
        IEnumerable<string>? eventType = null,
        double? limit = null,
        string? payloadFilter = null,
        string? query = null,
        string? since = null,
        string? source = null,
        string? traceId = null,
        string? until = null,
        CancellationToken cancellationToken = default) =>
        _search.SearchAsync(
            agentId, appId, channelId, cursor, environment, eventType, limit,
            payloadFilter, query, since, source, traceId, until, cancellationToken);
}
