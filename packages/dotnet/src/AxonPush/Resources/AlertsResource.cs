using AxonPush.Internal;
using AxonPush.Internal.Api;

namespace AxonPush.Resources;

/// <summary>Generated from the TypeScript surface. See tools/generate-dotnet-resources.py.</summary>
public sealed class AlertsResource : ResourceBase
{
    private readonly AlertControllerClient _alertControllerClient;

    internal AlertsResource(AxonPushTransport transport)
        : base(transport)
    {
        _alertControllerClient = new AlertControllerClient(Http);
    }

    /// <summary>List. <c>GET /v2/alerts</c></summary>
    public Task<AlertRuleListDto> ListAsync(System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _alertControllerClient.ListAsync(cancellationToken);

    /// <summary>Create. <c>POST /v2/alerts</c></summary>
    public Task<AlertRuleDto> CreateAsync(CreateAlertRuleDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _alertControllerClient.CreateAsync(body, cancellationToken);

    /// <summary>Delete. <c>DELETE /v2/alerts/{alertRuleId}</c></summary>
    public Task<AlertDeleteDto> DeleteAsync(string alertRuleId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _alertControllerClient.RemoveAsync(alertRuleId, cancellationToken);

    /// <summary>Update. <c>PATCH /v2/alerts/{alertRuleId}</c></summary>
    public Task<AlertRuleDto> UpdateAsync(string alertRuleId, UpdateAlertRuleDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _alertControllerClient.UpdateAsync(alertRuleId, body, cancellationToken);
}
