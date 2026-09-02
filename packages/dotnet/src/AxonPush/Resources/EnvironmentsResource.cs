using AxonPush.Internal;
using AxonPush.Internal.Api;

namespace AxonPush.Resources;

/// <summary>Generated from the TypeScript surface. See tools/generate-dotnet-resources.py.</summary>
public sealed class EnvironmentsResource : ResourceBase
{
    private readonly EnvironmentControllerClient _environmentControllerClient;

    internal EnvironmentsResource(AxonPushTransport transport)
        : base(transport)
    {
        _environmentControllerClient = new EnvironmentControllerClient(Http);
    }

    /// <summary>List. <c>GET /environments</c></summary>
    public Task<System.Collections.Generic.ICollection<EnvironmentResponseDto>> ListAsync(System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _environmentControllerClient.ListAsync(cancellationToken);

    /// <summary>Create. <c>POST /environments</c></summary>
    public Task<EnvironmentResponseDto> CreateAsync(CreateEnvironmentDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _environmentControllerClient.CreateAsync(body, cancellationToken);

    /// <summary>Update. <c>PATCH /environments/{id}</c></summary>
    public Task<EnvironmentResponseDto> UpdateAsync(string id, UpdateEnvironmentDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _environmentControllerClient.UpdateAsync(id, body, cancellationToken);

    /// <summary>Delete. <c>DELETE /environments/{id}</c></summary>
    public Task<OkResponseDto> DeleteAsync(string id, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _environmentControllerClient.RemoveAsync(id, cancellationToken);

    /// <summary>Promote to default. <c>POST /environments/{id}/promote-to-default</c></summary>
    public Task<EnvironmentResponseDto> PromoteToDefaultAsync(string id, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _environmentControllerClient.PromoteAsync(id, cancellationToken);
}
