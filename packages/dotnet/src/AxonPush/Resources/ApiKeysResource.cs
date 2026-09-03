using AxonPush.Internal;
using AxonPush.Internal.Api;

namespace AxonPush.Resources;

/// <summary>Generated from the TypeScript surface. See tools/generate-dotnet-resources.py.</summary>
public sealed class ApiKeysResource : ResourceBase
{
    private readonly ApiKeyControllerClient _apiKeyControllerClient;

    internal ApiKeysResource(AxonPushTransport transport)
        : base(transport)
    {
        _apiKeyControllerClient = new ApiKeyControllerClient(Http);
    }

    /// <summary>Create. <c>POST /api-keys</c></summary>
    public Task<ApiKeyCreateResponseDto> CreateAsync(CreateApiKeyDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _apiKeyControllerClient.CreateApiKeyAsync(body, cancellationToken);

    /// <summary>List. <c>GET /api-keys</c></summary>
    public Task<System.Collections.Generic.ICollection<ApiKeyResponseDto>> ListAsync(System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _apiKeyControllerClient.ListApiKeysAsync(cancellationToken);

    /// <summary>Delete. <c>DELETE /api-keys/{id}</c></summary>
    public Task<MessageResponseDto> DeleteAsync(string id, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _apiKeyControllerClient.RevokeApiKeyAsync(id, cancellationToken);
}
