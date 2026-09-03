using AxonPush.Internal;
using AxonPush.Internal.Api;

namespace AxonPush.Resources;

/// <summary>Generated from the TypeScript surface. See tools/generate-dotnet-resources.py.</summary>
public sealed class GatesResource : ResourceBase
{
    private readonly GatePolicyControllerClient _gatePolicyControllerClient;
    private readonly GateRunControllerClient _gateRunControllerClient;

    internal GatesResource(AxonPushTransport transport)
        : base(transport)
    {
        _gatePolicyControllerClient = new GatePolicyControllerClient(Http);
        _gateRunControllerClient = new GateRunControllerClient(Http);
    }

    /// <summary>List policies. <c>GET /v2/gate-policies</c></summary>
    public Task<GatePolicyListDto> ListPoliciesAsync(System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _gatePolicyControllerClient.ListAsync(cancellationToken);

    /// <summary>Save policy. <c>POST /v2/gate-policies</c></summary>
    public Task<GatePolicyDto> SavePolicyAsync(SaveGatePolicyDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _gatePolicyControllerClient.SaveAsync(body, cancellationToken);

    /// <summary>Delete policy. <c>DELETE /v2/gate-policies/{scopeType}/{scopeId}</c></summary>
    public Task<GatePolicyDeleteDto> DeletePolicyAsync(string scopeId, ScopeType scopeType, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _gatePolicyControllerClient.RemoveAsync(scopeId, scopeType, cancellationToken);

    /// <summary>Get policy. <c>GET /v2/gate-policies/{scopeType}/{scopeId}</c></summary>
    public Task<GatePolicyDto> GetPolicyAsync(string scopeId, ScopeType2 scopeType, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _gatePolicyControllerClient.GetAsync(scopeId, scopeType, cancellationToken);

    /// <summary>List runs. <c>GET /v2/gate-runs</c></summary>
    public Task<GateRunListDto> ListRunsAsync(string? cursor = null, string? experimentId = null, double? limit = null, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _gateRunControllerClient.ListAsync(cursor, experimentId, limit, cancellationToken);
}
