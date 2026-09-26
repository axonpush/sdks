"""Organizations resource — current org, membership, invitations, admin."""

from __future__ import annotations

from typing import TYPE_CHECKING, List

from axonpush._internal.api.api.organization import (
    organization_delete as _delete_op,
    organization_get as _get_op,
    organization_invitations_accept as _accept_invite_op,
    organization_invitations_cancel as _delete_invite_op,
    organization_invitations_create as _invite_op,
    organization_leave as _leave_op,
    organization_members_remove as _remove_member_op,
    organization_transfer_ownership as _transfer_op,
    organization_update as _update_op,
)
from axonpush._internal.api.api.user import (
    user_me_organizations as _list_op,
)
from axonpush._internal.api.models import (
    AcceptInvitationInputBody,
    AcceptInvitationOutputBody,
    CreateInvitationInputBody,
    CreateInvitationInputBodyRole,
    InvitationDTO,
    OkOutputBody,
    TransferOwnershipInputBody,
    UpdateOrganizationInputBody,
    UserOrgsOutputBody,
)
from axonpush._internal.api.types import UNSET
from axonpush.models import Organization, UserOrg

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


def _unwrap(result: UserOrgsOutputBody | None) -> List[UserOrg] | None:
    if result is None:
        return None
    return list(result.organizations or [])


def _build_update_dto(*, name: str | None, description: str | None) -> UpdateOrganizationInputBody:
    return UpdateOrganizationInputBody(
        name=name if name is not None else UNSET,
        description=description if description is not None else UNSET,
    )


def _build_invite_dto(
    *, email: str, role: CreateInvitationInputBodyRole | str
) -> CreateInvitationInputBody:
    desired = (
        role
        if isinstance(role, CreateInvitationInputBodyRole)
        else CreateInvitationInputBodyRole(role)
    )
    return CreateInvitationInputBody(invited_email=email, role=desired)


class Organizations:
    """Synchronous organization management."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def list(self) -> List[UserOrg] | None:
        """List organizations the caller is a member of (envelope unwrapped).

        Backed by ``GET /users/me/organizations``.
        """
        return self._client._invoke(_list_op, _coerce=_unwrap)

    def get(self) -> Organization | None:
        """Fetch the caller's active organization. ``GET /organization``."""
        return self._client._invoke(_get_op)

    def update(
        self,
        *,
        name: str | None = None,
        description: str | None = None,
    ) -> Organization | None:
        """Edit the active organization's name / description. ``PATCH /organization``."""
        return self._client._invoke(
            _update_op, body=_build_update_dto(name=name, description=description)
        )

    def delete(self, org_id: str) -> OkOutputBody | None:
        """Delete an organization. ``DELETE /organizations/{orgId}``."""
        return self._client._invoke(_delete_op, org_id=org_id)

    def invite(
        self,
        org_id: str,
        email: str,
        *,
        role: CreateInvitationInputBodyRole | str = CreateInvitationInputBodyRole.USER,
    ) -> InvitationDTO | None:
        """Invite a user to an organization."""
        return self._client._invoke(
            _invite_op, org_id=org_id, body=_build_invite_dto(email=email, role=role)
        )

    def cancel_invitation(self, org_id: str, invitation_id: str) -> OkOutputBody | None:
        """Cancel a pending invitation."""
        return self._client._invoke(
            _delete_invite_op, org_id=org_id, invitation_id=invitation_id
        )

    def remove_member(self, org_id: str, user_id: str) -> OkOutputBody | None:
        """Remove a member from an organization."""
        return self._client._invoke(_remove_member_op, org_id=org_id, user_id=user_id)

    def transfer_ownership(self, org_id: str, target_user_id: str) -> OkOutputBody | None:
        """Transfer organization ownership to another member."""
        return self._client._invoke(
            _transfer_op,
            org_id=org_id,
            body=TransferOwnershipInputBody(user_id=target_user_id),
        )

    def leave(self, org_id: str) -> OkOutputBody | None:
        """Leave an organization. ``POST /organizations/{orgId}/leave``"""
        return self._client._invoke(_leave_op, org_id=org_id)

    def accept_invitation(
        self, body: AcceptInvitationInputBody
    ) -> AcceptInvitationOutputBody | None:
        """Accept a pending invitation. ``POST /invitations/accept``"""
        return self._client._invoke(_accept_invite_op, body=body)


class AsyncOrganizations:
    """Async sibling of :class:`Organizations`."""

    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def list(self) -> List[UserOrg] | None:
        """See :meth:`Organizations.list`."""
        return await self._client._invoke(_list_op, _coerce=_unwrap)

    async def get(self) -> Organization | None:
        """See :meth:`Organizations.get`."""
        return await self._client._invoke(_get_op)

    async def update(
        self,
        *,
        name: str | None = None,
        description: str | None = None,
    ) -> Organization | None:
        """See :meth:`Organizations.update`."""
        return await self._client._invoke(
            _update_op, body=_build_update_dto(name=name, description=description)
        )

    async def delete(self, org_id: str) -> OkOutputBody | None:
        """See :meth:`Organizations.delete`."""
        return await self._client._invoke(_delete_op, org_id=org_id)

    async def invite(
        self,
        org_id: str,
        email: str,
        *,
        role: CreateInvitationInputBodyRole | str = CreateInvitationInputBodyRole.USER,
    ) -> InvitationDTO | None:
        """See :meth:`Organizations.invite`."""
        return await self._client._invoke(
            _invite_op, org_id=org_id, body=_build_invite_dto(email=email, role=role)
        )

    async def cancel_invitation(self, org_id: str, invitation_id: str) -> OkOutputBody | None:
        """See :meth:`Organizations.cancel_invitation`."""
        return await self._client._invoke(
            _delete_invite_op, org_id=org_id, invitation_id=invitation_id
        )

    async def remove_member(self, org_id: str, user_id: str) -> OkOutputBody | None:
        """See :meth:`Organizations.remove_member`."""
        return await self._client._invoke(_remove_member_op, org_id=org_id, user_id=user_id)

    async def transfer_ownership(self, org_id: str, target_user_id: str) -> OkOutputBody | None:
        """See :meth:`Organizations.transfer_ownership`."""
        return await self._client._invoke(
            _transfer_op,
            org_id=org_id,
            body=TransferOwnershipInputBody(user_id=target_user_id),
        )

    async def leave(self, org_id: str) -> OkOutputBody | None:
        """See :meth:`Organizations.leave`."""
        return await self._client._invoke(_leave_op, org_id=org_id)

    async def accept_invitation(
        self, body: AcceptInvitationInputBody
    ) -> AcceptInvitationOutputBody | None:
        """See :meth:`Organizations.accept_invitation`."""
        return await self._client._invoke(_accept_invite_op, body=body)
