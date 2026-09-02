using AxonPush.Internal;
using AxonPush.Internal.Api;

namespace AxonPush.Resources;

/// <summary>Generated from the TypeScript surface. See tools/generate-dotnet-resources.py.</summary>
public sealed class TraceIntelligenceResource : ResourceBase
{
    private readonly TraceIntelligenceControllerClient _traceIntelligenceControllerClient;

    internal TraceIntelligenceResource(AxonPushTransport transport)
        : base(transport)
    {
        _traceIntelligenceControllerClient = new TraceIntelligenceControllerClient(Http);
    }

    /// <summary>List backfills. <c>GET /v2/trace-intelligence/backfills</c></summary>
    public Task<System.Collections.Generic.ICollection<TraceIntelligenceBackfillResponseDto>> ListBackfillsAsync(System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _traceIntelligenceControllerClient.ListBackfillsAsync(cancellationToken);

    /// <summary>Create backfill. <c>POST /v2/trace-intelligence/backfills</c></summary>
    public Task<TraceIntelligenceBackfillResponseDto> CreateBackfillAsync(CreateTraceIntelligenceBackfillDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _traceIntelligenceControllerClient.CreateBackfillAsync(body, cancellationToken);

    /// <summary>Get backfill. <c>GET /v2/trace-intelligence/backfills/{jobId}</c></summary>
    public Task<TraceIntelligenceBackfillResponseDto> GetBackfillAsync(string jobId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _traceIntelligenceControllerClient.GetBackfillAsync(jobId, cancellationToken);

    /// <summary>List clusters. <c>GET /v2/trace-intelligence/clusters</c></summary>
    public Task<TraceIntelligenceClusterListResponseDto> ListClustersAsync(string appId, string environmentId, string? cursor = null, string? from = null, double? limit = null, string? search = null, string? signalKind = null, string? to = null, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _traceIntelligenceControllerClient.ListClustersAsync(appId, environmentId, cursor, from, limit, search, signalKind, to, cancellationToken);

    /// <summary>Get cluster. <c>GET /v2/trace-intelligence/clusters/{clusterId}</c></summary>
    public Task<TraceIntelligenceClusterResponseDto> GetClusterAsync(string clusterId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _traceIntelligenceControllerClient.GetClusterAsync(clusterId, cancellationToken);

    /// <summary>Add to dataset. <c>POST /v2/trace-intelligence/clusters/{clusterId}/actions/add-to-dataset</c></summary>
    public Task<TraceClusterDatasetActionResponseDto> AddToDatasetAsync(string clusterId, AddTraceClusterToDatasetDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _traceIntelligenceControllerClient.AddToDatasetAsync(clusterId, body, cancellationToken);

    /// <summary>Coverage. <c>GET /v2/trace-intelligence/coverage</c></summary>
    public Task<TraceIntelligenceCoverageResponseDto> CoverageAsync(string appId, string environmentId, string? from = null, string? to = null, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _traceIntelligenceControllerClient.CoverageAsync(appId, environmentId, from, to, cancellationToken);

    /// <summary>Flow. <c>GET /v2/trace-intelligence/flow</c></summary>
    public Task<TraceIntelligenceFlowResponseDto> FlowAsync(string appId, string environmentId, string from, string to, bool? includeUnclustered = null, double? minimumVolume = null, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _traceIntelligenceControllerClient.FlowAsync(appId, environmentId, from, to, includeUnclustered, minimumVolume, cancellationToken);

    /// <summary>Get settings. <c>GET /v2/trace-intelligence/settings</c></summary>
    public Task<TraceIntelligenceSettingsResponseDto> GetSettingsAsync(System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _traceIntelligenceControllerClient.GetSettingsAsync(cancellationToken);

    /// <summary>Update settings. <c>PUT /v2/trace-intelligence/settings</c></summary>
    public Task<TraceIntelligenceSettingsResponseDto> UpdateSettingsAsync(UpdateTraceIntelligenceSettingsDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _traceIntelligenceControllerClient.UpdateSettingsAsync(body, cancellationToken);

    /// <summary>Test provider. <c>POST /v2/trace-intelligence/settings/provider/test</c></summary>
    public Task<TraceIntelligenceProviderTestResponseDto> TestProviderAsync(TestTraceIntelligenceProviderDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _traceIntelligenceControllerClient.TestProviderAsync(body, cancellationToken);

    /// <summary>Get signals. <c>GET /v2/trace-intelligence/traces/{traceId}/signals</c></summary>
    public Task<TraceIntelligenceSignalsResponseDto> GetSignalsAsync(string traceId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _traceIntelligenceControllerClient.GetSignalsAsync(traceId, cancellationToken);
}
