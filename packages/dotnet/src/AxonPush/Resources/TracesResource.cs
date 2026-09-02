using AxonPush.Internal;
using AxonPush.Internal.Api;

namespace AxonPush.Resources;

/// <summary>Generated from the TypeScript surface. See tools/generate-dotnet-resources.py.</summary>
public sealed class TracesResource : ResourceBase
{
    private readonly TraceControllerClient _traceControllerClient;

    internal TracesResource(AxonPushTransport transport)
        : base(transport)
    {
        _traceControllerClient = new TraceControllerClient(Http);
    }

    /// <summary>List. <c>GET /traces</c></summary>
    public Task<Response> ListAsync(string? appId = null, string? environment = null, double? limit = null, double? page = null, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _traceControllerClient.ListTracesAsync(appId, environment, limit, page, cancellationToken);

    /// <summary>Stats. <c>GET /traces/stats</c></summary>
    public Task<Response2> StatsAsync(string? appId = null, string? environment = null, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _traceControllerClient.GetDashboardStatsAsync(appId, environment, cancellationToken);

    /// <summary>Events. <c>GET /traces/{traceId}/events</c></summary>
    public Task<System.Collections.Generic.ICollection<EventResponseDto>> EventsAsync(string traceId, string? appId = null, string? environment = null, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _traceControllerClient.GetTraceEventsAsync(traceId, appId, environment, cancellationToken);

    /// <summary>Summary. <c>GET /traces/{traceId}/summary</c></summary>
    public Task<Response3> SummaryAsync(string traceId, string? appId = null, string? environment = null, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _traceControllerClient.GetTraceSummaryAsync(traceId, appId, environment, cancellationToken);
}
