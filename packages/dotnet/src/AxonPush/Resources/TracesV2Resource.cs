using AxonPush.Internal;
using AxonPush.Internal.Api;

namespace AxonPush.Resources;

/// <summary>Generated from the TypeScript surface. See tools/generate-dotnet-resources.py.</summary>
public sealed class TracesV2Resource : ResourceBase
{
    private readonly TraceV2ControllerClient _traceV2ControllerClient;

    internal TracesV2Resource(AxonPushTransport transport)
        : base(transport)
    {
        _traceV2ControllerClient = new TraceV2ControllerClient(Http);
    }

    /// <summary>List. <c>GET /v2/traces</c></summary>
    public Task<TraceListV2ResponseDto> ListAsync(string? agent = null, string? appId = null, System.Collections.Generic.IDictionary<string, string>? attr = null, System.Collections.Generic.IDictionary<string, double>? attrMax = null, System.Collections.Generic.IDictionary<string, double>? attrMin = null, string? cursor = null, string? environment = null, string? environmentId = null, string? fields = null, string? from = null, double? limit = null, string? maxCostUsd = null, string? maxDurationMs = null, string? maxTokens = null, string? minCostUsd = null, string? minDurationMs = null, string? minTokens = null, string? model = null, string? promptId = null, string? promptVersionId = null, string? provider = null, string? query = null, string? release = null, System.Collections.Generic.IDictionary<string, string>? res = null, string? semanticKind = null, string? service = null, string? sessionId = null, Sort? sort = null, string? spanKind = null, string? spanMinDurationMs = null, string? spanModel = null, string? spanStatus = null, string? spanTool = null, string? status = null, string? to = null, string? tool = null, string? userId = null, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _traceV2ControllerClient.ListAsync(agent, appId, attr, attrMax, attrMin, cursor, environment, environmentId, fields, from, limit, maxCostUsd, maxDurationMs, maxTokens, minCostUsd, minDurationMs, minTokens, model, promptId, promptVersionId, provider, query, release, res, semanticKind, service, sessionId, sort, spanKind, spanMinDurationMs, spanModel, spanStatus, spanTool, status, to, tool, userId, cancellationToken);

    /// <summary>Attribute keys. <c>GET /v2/traces/attribute-keys</c></summary>
    public Task<TraceAttributeKeysV2ResponseDto> AttributeKeysAsync(string? agent = null, string? appId = null, System.Collections.Generic.IDictionary<string, string>? attr = null, System.Collections.Generic.IDictionary<string, double>? attrMax = null, System.Collections.Generic.IDictionary<string, double>? attrMin = null, string? environment = null, string? environmentId = null, string? from = null, string? maxCostUsd = null, string? maxDurationMs = null, string? maxTokens = null, string? minCostUsd = null, string? minDurationMs = null, string? minTokens = null, string? model = null, string? prefix = null, string? promptId = null, string? promptVersionId = null, string? provider = null, string? query = null, string? release = null, System.Collections.Generic.IDictionary<string, string>? res = null, Scope? scope = null, string? semanticKind = null, string? service = null, string? sessionId = null, string? spanKind = null, string? spanMinDurationMs = null, string? spanModel = null, string? spanStatus = null, string? spanTool = null, string? status = null, string? to = null, string? tool = null, string? userId = null, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _traceV2ControllerClient.AttributeKeysAsync(agent, appId, attr, attrMax, attrMin, environment, environmentId, from, maxCostUsd, maxDurationMs, maxTokens, minCostUsd, minDurationMs, minTokens, model, prefix, promptId, promptVersionId, provider, query, release, res, scope, semanticKind, service, sessionId, spanKind, spanMinDurationMs, spanModel, spanStatus, spanTool, status, to, tool, userId, cancellationToken);

    /// <summary>Facets. <c>GET /v2/traces/facets</c></summary>
    public Task<TraceFacetsV2ResponseDto> FacetsAsync(string? agent = null, string? appId = null, System.Collections.Generic.IDictionary<string, string>? attr = null, System.Collections.Generic.IDictionary<string, double>? attrMax = null, System.Collections.Generic.IDictionary<string, double>? attrMin = null, string? environment = null, string? environmentId = null, string? fields = null, string? from = null, string? maxCostUsd = null, string? maxDurationMs = null, string? maxTokens = null, string? minCostUsd = null, string? minDurationMs = null, string? minTokens = null, string? model = null, string? promptId = null, string? promptVersionId = null, string? provider = null, string? query = null, string? release = null, System.Collections.Generic.IDictionary<string, string>? res = null, string? semanticKind = null, string? service = null, string? sessionId = null, string? spanKind = null, string? spanMinDurationMs = null, string? spanModel = null, string? spanStatus = null, string? spanTool = null, string? status = null, string? to = null, string? tool = null, string? userId = null, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _traceV2ControllerClient.FacetsAsync(agent, appId, attr, attrMax, attrMin, environment, environmentId, fields, from, maxCostUsd, maxDurationMs, maxTokens, minCostUsd, minDurationMs, minTokens, model, promptId, promptVersionId, provider, query, release, res, semanticKind, service, sessionId, spanKind, spanMinDurationMs, spanModel, spanStatus, spanTool, status, to, tool, userId, cancellationToken);

    /// <summary>Detail. <c>GET /v2/traces/{traceId}</c></summary>
    public Task<TraceDetailV2ResponseDto> DetailAsync(string traceId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _traceV2ControllerClient.DetailAsync(traceId, cancellationToken);

    /// <summary>Events. <c>GET /v2/traces/{traceId}/events</c></summary>
    public Task<TraceEventsV2ResponseDto> EventsAsync(string traceId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _traceV2ControllerClient.EventsAsync(traceId, cancellationToken);

    /// <summary>Spans. <c>GET /v2/traces/{traceId}/spans</c></summary>
    public Task<TraceSpanSearchV2ResponseDto> SpansAsync(string traceId, double? limit = null, string? q = null, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _traceV2ControllerClient.SpansAsync(traceId, limit, q, cancellationToken);
}
