using AxonPush.Internal;
using AxonPush.Internal.Api;

namespace AxonPush.Resources;

/// <summary>Generated from the TypeScript surface. See tools/generate-dotnet-resources.py.</summary>
public sealed class AppsResource : ResourceBase
{
    private readonly AppsControllerClient _appsControllerClient;

    internal AppsResource(AxonPushTransport transport)
        : base(transport)
    {
        _appsControllerClient = new AppsControllerClient(Http);
    }

    /// <summary>List. <c>GET /apps</c></summary>
    public Task<System.Collections.Generic.ICollection<AppResponseDto>> ListAsync(System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _appsControllerClient.GetAllAppsAsync(cancellationToken);

    /// <summary>Get. <c>GET /apps/{id}</c></summary>
    public Task<AppResponseDto> GetAsync(string id, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _appsControllerClient.GetAppAsync(id, cancellationToken);

    /// <summary>Create. <c>POST /apps</c></summary>
    public Task<AppResponseDto> CreateAsync(CreateAppDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _appsControllerClient.CreateAppAsync(body, cancellationToken);

    /// <summary>Update. <c>PATCH /apps/{id}</c></summary>
    public Task<OkResponseDto> UpdateAsync(string id, CreateAppDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _appsControllerClient.EditAppAsync(id, body, cancellationToken);

    /// <summary>Delete. <c>DELETE /apps/{id}</c></summary>
    public Task<OkResponseDto> DeleteAsync(string id, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _appsControllerClient.DeleteAppAsync(id, cancellationToken);
}
