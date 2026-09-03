using AxonPush.Internal;
using AxonPush.Internal.Api;

namespace AxonPush.Resources;

/// <summary>Generated from the TypeScript surface. See tools/generate-dotnet-resources.py.</summary>
public sealed class EvaluatorsResource : ResourceBase
{
    private readonly EvaluatorControllerClient _evaluatorControllerClient;

    internal EvaluatorsResource(AxonPushTransport transport)
        : base(transport)
    {
        _evaluatorControllerClient = new EvaluatorControllerClient(Http);
    }

    /// <summary>List. <c>GET /v2/evaluators</c></summary>
    public Task<EvaluatorListDto> ListAsync(System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _evaluatorControllerClient.ListAsync(cancellationToken);

    /// <summary>Create. <c>POST /v2/evaluators</c></summary>
    public Task<EvaluatorDto> CreateAsync(CreateEvaluatorDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _evaluatorControllerClient.CreateAsync(body, cancellationToken);

    /// <summary>Delete. <c>DELETE /v2/evaluators/{evaluatorId}</c></summary>
    public Task<EvaluatorDeleteDto> DeleteAsync(string evaluatorId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _evaluatorControllerClient.RemoveAsync(evaluatorId, cancellationToken);

    /// <summary>Get. <c>GET /v2/evaluators/{evaluatorId}</c></summary>
    public Task<EvaluatorDto> GetAsync(string evaluatorId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _evaluatorControllerClient.GetAsync(evaluatorId, cancellationToken);

    /// <summary>Versions. <c>GET /v2/evaluators/{evaluatorId}/versions</c></summary>
    public Task<EvaluatorVersionListDto> VersionsAsync(string evaluatorId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _evaluatorControllerClient.VersionsAsync(evaluatorId, cancellationToken);

    /// <summary>Create version. <c>POST /v2/evaluators/{evaluatorId}/versions</c></summary>
    public Task<EvaluatorVersionDto> CreateVersionAsync(string evaluatorId, CreateEvaluatorVersionDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _evaluatorControllerClient.CreateVersionAsync(evaluatorId, body, cancellationToken);

    /// <summary>Version. <c>GET /v2/evaluators/{evaluatorId}/versions/{version}</c></summary>
    public Task<EvaluatorVersionDto> VersionAsync(string evaluatorId, double version, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _evaluatorControllerClient.VersionAsync(evaluatorId, version, cancellationToken);
}
