using AxonPush.Internal;
using AxonPush.Internal.Api;

namespace AxonPush.Resources;

/// <summary>Generated from the TypeScript surface. See tools/generate-dotnet-resources.py.</summary>
public sealed class OnlineEvaluationsResource : ResourceBase
{
    private readonly OnlineEvaluationControllerClient _onlineEvaluationControllerClient;

    internal OnlineEvaluationsResource(AxonPushTransport transport)
        : base(transport)
    {
        _onlineEvaluationControllerClient = new OnlineEvaluationControllerClient(Http);
    }

    /// <summary>List. <c>GET /v2/online-evaluation-rules</c></summary>
    public Task<System.Collections.Generic.ICollection<OnlineRuleResponseDto>> ListAsync(System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _onlineEvaluationControllerClient.ListAsync(cancellationToken);

    /// <summary>Create. <c>POST /v2/online-evaluation-rules</c></summary>
    public Task<OnlineRuleResponseDto> CreateAsync(CreateOnlineRuleDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _onlineEvaluationControllerClient.CreateAsync(body, cancellationToken);

    /// <summary>Delete. <c>DELETE /v2/online-evaluation-rules/{ruleId}</c></summary>
    public Task<DeleteResultDto> DeleteAsync(string ruleId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _onlineEvaluationControllerClient.RemoveAsync(ruleId, cancellationToken);

    /// <summary>Get. <c>GET /v2/online-evaluation-rules/{ruleId}</c></summary>
    public Task<OnlineRuleResponseDto> GetAsync(string ruleId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _onlineEvaluationControllerClient.GetAsync(ruleId, cancellationToken);

    /// <summary>Update. <c>PATCH /v2/online-evaluation-rules/{ruleId}</c></summary>
    public Task<OnlineRuleResponseDto> UpdateAsync(string ruleId, UpdateOnlineRuleDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _onlineEvaluationControllerClient.UpdateAsync(ruleId, body, cancellationToken);

    /// <summary>Backfill. <c>POST /v2/online-evaluation-rules/{ruleId}/backfill</c></summary>
    public Task<System.Collections.Generic.ICollection<OnlineRuleRunResponseDto>> BackfillAsync(string ruleId, BackfillOnlineRuleDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _onlineEvaluationControllerClient.BackfillAsync(ruleId, body, cancellationToken);

    /// <summary>Runs. <c>GET /v2/online-evaluation-rules/{ruleId}/runs</c></summary>
    public Task<System.Collections.Generic.ICollection<OnlineRuleRunResponseDto>> RunsAsync(string ruleId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _onlineEvaluationControllerClient.RunsAsync(ruleId, cancellationToken);
}
