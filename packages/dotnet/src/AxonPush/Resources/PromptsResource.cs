using AxonPush.Internal;
using AxonPush.Internal.Api;

namespace AxonPush.Resources;

/// <summary>Generated from the TypeScript surface. See tools/generate-dotnet-resources.py.</summary>
public sealed class PromptsResource : ResourceBase
{
    private readonly PromptControllerClient _promptControllerClient;

    internal PromptsResource(AxonPushTransport transport)
        : base(transport)
    {
        _promptControllerClient = new PromptControllerClient(Http);
    }

    /// <summary>List. <c>GET /v2/prompts</c></summary>
    public Task<PromptListDto> ListAsync(System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _promptControllerClient.ListAsync(cancellationToken);

    /// <summary>Create. <c>POST /v2/prompts</c></summary>
    public Task<PromptDto> CreateAsync(CreatePromptDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _promptControllerClient.CreateAsync(body, cancellationToken);

    /// <summary>Delete. <c>DELETE /v2/prompts/{promptId}</c></summary>
    public Task<PromptDeleteDto> DeleteAsync(string promptId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _promptControllerClient.RemoveAsync(promptId, cancellationToken);

    /// <summary>Get. <c>GET /v2/prompts/{promptId}</c></summary>
    public Task<PromptDto> GetAsync(string promptId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _promptControllerClient.GetAsync(promptId, cancellationToken);

    /// <summary>Update. <c>PATCH /v2/prompts/{promptId}</c></summary>
    public Task<PromptDto> UpdateAsync(string promptId, UpdatePromptDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _promptControllerClient.UpdateAsync(promptId, body, cancellationToken);

    /// <summary>Compare. <c>GET /v2/prompts/{promptId}/compare</c></summary>
    public Task<PromptComparisonDto> CompareAsync(string promptId, double baseline, double candidate, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _promptControllerClient.CompareAsync(promptId, baseline, candidate, cancellationToken);

    /// <summary>Deployments. <c>GET /v2/prompts/{promptId}/deployments</c></summary>
    public Task<PromptDeploymentListDto> DeploymentsAsync(string promptId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _promptControllerClient.DeploymentsAsync(promptId, cancellationToken);

    /// <summary>Promote. <c>POST /v2/prompts/{promptId}/promote</c></summary>
    public Task<PromptDeploymentDto> PromoteAsync(string promptId, PromotePromptDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _promptControllerClient.PromoteAsync(promptId, body, cancellationToken);

    /// <summary>Rollback. <c>POST /v2/prompts/{promptId}/rollback</c></summary>
    public Task<PromptDeploymentDto> RollbackAsync(string promptId, RollbackPromptDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _promptControllerClient.RollbackAsync(promptId, body, cancellationToken);

    /// <summary>Versions. <c>GET /v2/prompts/{promptId}/versions</c></summary>
    public Task<PromptVersionListDto> VersionsAsync(string promptId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _promptControllerClient.VersionsAsync(promptId, cancellationToken);

    /// <summary>Create version. <c>POST /v2/prompts/{promptId}/versions</c></summary>
    public Task<PromptVersionDto> CreateVersionAsync(string promptId, CreatePromptVersionDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _promptControllerClient.CreateVersionAsync(promptId, body, cancellationToken);

    /// <summary>Version. <c>GET /v2/prompts/{promptId}/versions/{version}</c></summary>
    public Task<PromptVersionDto> VersionAsync(string promptId, double version, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _promptControllerClient.VersionAsync(promptId, version, cancellationToken);
}
