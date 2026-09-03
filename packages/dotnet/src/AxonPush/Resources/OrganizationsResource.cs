using AxonPush.Internal;
using AxonPush.Internal.Api;

namespace AxonPush.Resources;

/// <summary>Generated from the TypeScript surface. See tools/generate-dotnet-resources.py.</summary>
public sealed class OrganizationsResource : ResourceBase
{
    private readonly OrganizationControllerClient _organizationControllerClient;

    internal OrganizationsResource(AxonPushTransport transport)
        : base(transport)
    {
        _organizationControllerClient = new OrganizationControllerClient(Http);
    }

    /// <summary>Create. <c>POST /organizations</c></summary>
    public Task<OrganizationCreateResponseDto> CreateAsync(CreateOrganizationDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _organizationControllerClient.CreateOrganizationAsync(body, cancellationToken);

    /// <summary>Get. <c>GET /organizations/{id}</c></summary>
    public Task<OrganizationResponseDto> GetAsync(string id, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _organizationControllerClient.GetOrganizationAsync(id, cancellationToken);

    /// <summary>List. <c>GET /organizations</c></summary>
    public Task<System.Collections.Generic.ICollection<OrganizationResponseDto>> ListAsync(System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _organizationControllerClient.GetAllOrganizationsAsync(cancellationToken);

    /// <summary>Update. <c>PATCH /organizations/{id}</c></summary>
    public Task<OkResponseDto> UpdateAsync(string id, CreateOrganizationDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _organizationControllerClient.EditOrganizationAsync(id, body, cancellationToken);

    /// <summary>Delete. <c>DELETE /organizations/{id}</c></summary>
    public Task<OkResponseDto> DeleteAsync(string id, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _organizationControllerClient.DeleteOrganizationAsync(id, cancellationToken);

    /// <summary>Invite. <c>POST /organizations/{id}/invitations</c></summary>
    public Task<InvitationResponseDto> InviteAsync(string id, CreateInvitationDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _organizationControllerClient.CreateInvitationAsync(id, body, cancellationToken);

    /// <summary>Cancel invitation. <c>DELETE /organizations/{id}/invitations/{invitationId}</c></summary>
    public Task<SuccessResponseDto> CancelInvitationAsync(string id, string invitationId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _organizationControllerClient.DeleteInvitationAsync(id, invitationId, cancellationToken);

    /// <summary>Remove member. <c>DELETE /organizations/{id}/members/{userId}</c></summary>
    public Task<SuccessResponseDto> RemoveMemberAsync(string id, string userId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _organizationControllerClient.RemoveMemberAsync(id, userId, cancellationToken);

    /// <summary>Transfer ownership. <c>POST /organizations/{id}/transfer-ownership</c></summary>
    public Task<SuccessResponseDto> TransferOwnershipAsync(string id, TransferOwnershipDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _organizationControllerClient.TransferOwnershipAsync(id, body, cancellationToken);
}
