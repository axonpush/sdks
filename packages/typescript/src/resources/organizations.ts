import {
  organizationDelete,
  organizationGet,
  organizationInvitationsCancel,
  organizationInvitationsCreate,
  organizationMembersRemove,
  organizationTransferOwnership,
  organizationUpdate,
  userMeOrganizations,
} from "../_internal/api/sdk.gen.js";
import type {
  CreateInvitationInputBodyWritable,
  InvitationDto,
  OkOutputBody,
  UpdateOrganizationInputBodyWritable,
} from "../_internal/api/types.gen.js";
import type { Organization, UserOrg } from "../models.js";
import type { ResourceClient } from "./_client.js";

/** Mutable organization fields accepted by {@link OrganizationsResource.update}. */
export type OrganizationUpdateFields = UpdateOrganizationInputBodyWritable;

/** Invitation roles accepted by {@link OrganizationsResource.invite}. */
export type InvitationRole = CreateInvitationInputBodyWritable["role"];

/**
 * Read and manage organizations, invitations, and ownership transfers.
 *
 * Organization creation is owned by the auth service and is no longer part
 * of this SDK. `get`/`update` operate on the caller's active organization.
 */
export class OrganizationsResource {
  constructor(private readonly client: ResourceClient) {}

  /**
   * The active organization. `GET /organization`
   *
   * @returns The organization, or `null` on fail-open error.
   */
  async get(): Promise<Organization | null> {
    return this.client.invoke(organizationGet, {});
  }

  /**
   * List organizations the caller is a member of. `GET /users/me/organizations`
   *
   * @returns Membership records (org + role), or `null` on fail-open error.
   */
  async list(): Promise<UserOrg[] | null> {
    const res = await this.client.invoke(userMeOrganizations, {});
    return res?.organizations ?? null;
  }

  /**
   * Update the active organization. `PATCH /organization`
   *
   * @param fields - Patch object.
   * @returns The updated organization, or `null` on fail-open error.
   */
  async update(fields: OrganizationUpdateFields): Promise<Organization | null> {
    return this.client.invoke(organizationUpdate, { body: fields });
  }

  /**
   * Delete an organization. `DELETE /organizations/{orgId}`
   *
   * @param orgId - Organization id.
   * @returns Server ack, or `null` on fail-open error.
   */
  async delete(orgId: string): Promise<OkOutputBody | null> {
    return this.client.invoke(organizationDelete, { path: { orgId } });
  }

  /**
   * Invite a user to an organization. `POST /organizations/{orgId}/invitations`
   *
   * @param orgId - Organization id.
   * @param email - Invitee email.
   * @param role - Invitation role; defaults to `"user"`.
   * @returns The created invitation, or `null` on fail-open error.
   */
  async invite(
    orgId: string,
    email: string,
    role: InvitationRole = "user",
  ): Promise<InvitationDto | null> {
    return this.client.invoke(organizationInvitationsCreate, {
      path: { orgId },
      body: { invitedEmail: email, role },
    });
  }

  /**
   * Cancel a pending invitation.
   * `DELETE /organizations/{orgId}/invitations/{invitationId}`
   *
   * @param orgId - Organization id.
   * @param invitationId - Invitation id to cancel.
   * @returns Server ack, or `null` on fail-open error.
   */
  async cancelInvitation(orgId: string, invitationId: string): Promise<OkOutputBody | null> {
    return this.client.invoke(organizationInvitationsCancel, {
      path: { orgId, invitationId },
    });
  }

  /**
   * Remove a member from an organization.
   * `DELETE /organizations/{orgId}/members/{userId}`
   *
   * @param orgId - Organization id.
   * @param userId - User id to remove.
   * @returns Server ack, or `null` on fail-open error.
   */
  async removeMember(orgId: string, userId: string): Promise<OkOutputBody | null> {
    return this.client.invoke(organizationMembersRemove, {
      path: { orgId, userId },
    });
  }

  /**
   * Transfer ownership of an organization to another member.
   * `POST /organizations/{orgId}/transfer-ownership`
   *
   * @param orgId - Organization id.
   * @param targetUserId - User id to promote.
   * @returns Server ack, or `null` on fail-open error.
   */
  async transferOwnership(orgId: string, targetUserId: string): Promise<OkOutputBody | null> {
    return this.client.invoke(organizationTransferOwnership, {
      path: { orgId },
      body: { userId: targetUserId },
    });
  }
}
