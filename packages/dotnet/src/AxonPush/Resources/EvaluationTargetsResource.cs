using AxonPush.Internal;
using AxonPush.Internal.Api;

namespace AxonPush.Resources;

/// <summary>Generated from the TypeScript surface. See tools/generate-dotnet-resources.py.</summary>
public sealed class EvaluationTargetsResource : ResourceBase
{
    private readonly EvaluationTargetControllerClient _evaluationTargetControllerClient;

    internal EvaluationTargetsResource(AxonPushTransport transport)
        : base(transport)
    {
        _evaluationTargetControllerClient = new EvaluationTargetControllerClient(Http);
    }

    /// <summary>List. <c>GET /v2/evaluation-targets</c></summary>
    public Task<EvaluationTargetListDto> ListAsync(System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _evaluationTargetControllerClient.ListAsync(cancellationToken);

    /// <summary>Create. <c>POST /v2/evaluation-targets</c></summary>
    public Task<EvaluationTargetDto> CreateAsync(CreateEvaluationTargetDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _evaluationTargetControllerClient.CreateAsync(body, cancellationToken);

    /// <summary>Delete. <c>DELETE /v2/evaluation-targets/{targetId}</c></summary>
    public Task<EvaluationTargetDeleteDto> DeleteAsync(string targetId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _evaluationTargetControllerClient.RemoveAsync(targetId, cancellationToken);

    /// <summary>Get. <c>GET /v2/evaluation-targets/{targetId}</c></summary>
    public Task<EvaluationTargetDto> GetAsync(string targetId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _evaluationTargetControllerClient.GetAsync(targetId, cancellationToken);

    /// <summary>Update. <c>PATCH /v2/evaluation-targets/{targetId}</c></summary>
    public Task<EvaluationTargetDto> UpdateAsync(string targetId, UpdateEvaluationTargetDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _evaluationTargetControllerClient.UpdateAsync(targetId, body, cancellationToken);
}
