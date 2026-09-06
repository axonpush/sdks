using AxonPush.Internal;

namespace AxonPush.Gates;

/// <summary>
/// Release-gate policies and the history of gate decisions. Mirrors the
/// <c>gates</c> resource in the Python and TypeScript SDKs.
/// </summary>
public sealed class GatesResource
{
    private const string PoliciesPath = "v2/gate-policies";
    private const string RunsPath = "v2/gate-runs";

    private readonly AxonPushTransport _transport;

    internal GatesResource(AxonPushTransport transport)
    {
        _transport = transport;
    }

    /// <summary>Lists the release-gate policies. <c>GET /v2/gate-policies</c>.</summary>
    public Task<GatePolicyListDto?> ListPoliciesAsync(CancellationToken cancellationToken = default) =>
        _transport.SendAsync<GatePolicyListDto>(HttpMethod.Get, PoliciesPath, null, cancellationToken);

    /// <summary>Creates or updates a release-gate policy. <c>POST /v2/gate-policies</c>.</summary>
    public Task<GatePolicyDto?> SavePolicyAsync(SaveGatePolicyDto body, CancellationToken cancellationToken = default)
    {
        ArgumentNullException.ThrowIfNull(body);
        return _transport.SendAsync<GatePolicyDto>(HttpMethod.Post, PoliciesPath, body, cancellationToken);
    }

    /// <summary>Reads the policy for a scope. <c>GET /v2/gate-policies/{scopeType}/{scopeId}</c>.</summary>
    public Task<GatePolicyDto?> GetPolicyAsync(string scopeType, string scopeId, CancellationToken cancellationToken = default) =>
        _transport.SendAsync<GatePolicyDto>(HttpMethod.Get, PolicyPath(scopeType, scopeId), null, cancellationToken);

    /// <summary>Deletes the policy for a scope. <c>DELETE /v2/gate-policies/{scopeType}/{scopeId}</c>.</summary>
    public Task<GatePolicyDeleteDto?> DeletePolicyAsync(string scopeType, string scopeId, CancellationToken cancellationToken = default) =>
        _transport.SendAsync<GatePolicyDeleteDto>(HttpMethod.Delete, PolicyPath(scopeType, scopeId), null, cancellationToken);

    /// <summary>Lists recorded gate decisions. <c>GET /v2/gate-runs</c>.</summary>
    public Task<GateRunListDto?> ListRunsAsync(
        string? cursor = null,
        string? experimentId = null,
        string? limit = null,
        CancellationToken cancellationToken = default) =>
        _transport.SendAsync<GateRunListDto>(HttpMethod.Get, RunsPath + Query(cursor, experimentId, limit), null, cancellationToken);

    private static string PolicyPath(string scopeType, string scopeId)
    {
        ArgumentException.ThrowIfNullOrWhiteSpace(scopeType);
        ArgumentException.ThrowIfNullOrWhiteSpace(scopeId);
        return $"{PoliciesPath}/{Uri.EscapeDataString(scopeType)}/{Uri.EscapeDataString(scopeId)}";
    }

    private static string Query(string? cursor, string? experimentId, string? limit)
    {
        var parts = new List<string>(3);
        if (!string.IsNullOrEmpty(cursor)) parts.Add($"cursor={Uri.EscapeDataString(cursor)}");
        if (!string.IsNullOrEmpty(experimentId)) parts.Add($"experimentId={Uri.EscapeDataString(experimentId)}");
        if (!string.IsNullOrEmpty(limit)) parts.Add($"limit={Uri.EscapeDataString(limit)}");
        return parts.Count == 0 ? string.Empty : "?" + string.Join("&", parts);
    }
}
