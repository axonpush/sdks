"""Prompt registry: versions, deployments, promotion and rollback."""

from __future__ import annotations

from typing import TYPE_CHECKING

from axonpush._internal.api.api.prompts import (
    prompt_controller_compare as _compare_op,
    prompt_controller_create as _create_op,
    prompt_controller_create_version as _create_version_op,
    prompt_controller_deployments as _deployments_op,
    prompt_controller_get as _get_op,
    prompt_controller_list as _list_op,
    prompt_controller_promote as _promote_op,
    prompt_controller_remove as _remove_op,
    prompt_controller_rollback as _rollback_op,
    prompt_controller_update as _update_op,
    prompt_controller_version as _version_op,
    prompt_controller_versions as _versions_op,
)
from axonpush._internal.api.models import (
    CreatePromptDto,
    CreatePromptVersionDto,
    PromotePromptDto,
    PromptComparisonDto,
    PromptDeleteDto,
    PromptDeploymentDto,
    PromptDeploymentListDto,
    PromptDto,
    PromptListDto,
    PromptVersionDto,
    PromptVersionListDto,
    RollbackPromptDto,
    UpdatePromptDto,
)

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


class Prompts:
    """Prompt registry: versions, deployments, promotion and rollback."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def list(self) -> PromptListDto | None:
        """List them all. `GET /v2/prompts`"""
        return self._client._invoke(_list_op)

    def create(self, body: CreatePromptDto) -> PromptDto | None:
        """Create one. `POST /v2/prompts`"""
        return self._client._invoke(_create_op, body=body)

    def delete(self, prompt_id: str) -> PromptDeleteDto | None:
        """Delete one. `DELETE /v2/prompts/{promptId}`"""
        return self._client._invoke(_remove_op, prompt_id=prompt_id)

    def get(self, prompt_id: str) -> PromptDto | None:
        """Fetch one by id. `GET /v2/prompts/{promptId}`"""
        return self._client._invoke(_get_op, prompt_id=prompt_id)

    def update(self, prompt_id: str, body: UpdatePromptDto) -> PromptDto | None:
        """Update one. `PATCH /v2/prompts/{promptId}`"""
        return self._client._invoke(_update_op, prompt_id=prompt_id, body=body)

    def compare(self, prompt_id: str, baseline: str, candidate: str) -> PromptComparisonDto | None:
        """Compare. `GET /v2/prompts/{promptId}/compare`"""
        return self._client._invoke(
            _compare_op, prompt_id=prompt_id, baseline=baseline, candidate=candidate
        )

    def deployments(self, prompt_id: str) -> PromptDeploymentListDto | None:
        """Deployments. `GET /v2/prompts/{promptId}/deployments`"""
        return self._client._invoke(_deployments_op, prompt_id=prompt_id)

    def promote(self, prompt_id: str, body: PromotePromptDto) -> PromptDeploymentDto | None:
        """Promote. `POST /v2/prompts/{promptId}/promote`"""
        return self._client._invoke(_promote_op, prompt_id=prompt_id, body=body)

    def rollback(self, prompt_id: str, body: RollbackPromptDto) -> PromptDeploymentDto | None:
        """Rollback. `POST /v2/prompts/{promptId}/rollback`"""
        return self._client._invoke(_rollback_op, prompt_id=prompt_id, body=body)

    def versions(self, prompt_id: str) -> PromptVersionListDto | None:
        """Versions. `GET /v2/prompts/{promptId}/versions`"""
        return self._client._invoke(_versions_op, prompt_id=prompt_id)

    def create_version(
        self, prompt_id: str, body: CreatePromptVersionDto
    ) -> PromptVersionDto | None:
        """Create version. `POST /v2/prompts/{promptId}/versions`"""
        return self._client._invoke(_create_version_op, prompt_id=prompt_id, body=body)

    def version(self, prompt_id: str, version: str) -> PromptVersionDto | None:
        """Version. `GET /v2/prompts/{promptId}/versions/{version}`"""
        return self._client._invoke(_version_op, prompt_id=prompt_id, version=version)


class AsyncPrompts:
    """Async sibling of :class:`Prompts`."""

    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def list(self) -> PromptListDto | None:
        """See :meth:`Prompts.list`."""
        return await self._client._invoke(_list_op)

    async def create(self, body: CreatePromptDto) -> PromptDto | None:
        """See :meth:`Prompts.create`."""
        return await self._client._invoke(_create_op, body=body)

    async def delete(self, prompt_id: str) -> PromptDeleteDto | None:
        """See :meth:`Prompts.delete`."""
        return await self._client._invoke(_remove_op, prompt_id=prompt_id)

    async def get(self, prompt_id: str) -> PromptDto | None:
        """See :meth:`Prompts.get`."""
        return await self._client._invoke(_get_op, prompt_id=prompt_id)

    async def update(self, prompt_id: str, body: UpdatePromptDto) -> PromptDto | None:
        """See :meth:`Prompts.update`."""
        return await self._client._invoke(_update_op, prompt_id=prompt_id, body=body)

    async def compare(
        self, prompt_id: str, baseline: str, candidate: str
    ) -> PromptComparisonDto | None:
        """See :meth:`Prompts.compare`."""
        return await self._client._invoke(
            _compare_op, prompt_id=prompt_id, baseline=baseline, candidate=candidate
        )

    async def deployments(self, prompt_id: str) -> PromptDeploymentListDto | None:
        """See :meth:`Prompts.deployments`."""
        return await self._client._invoke(_deployments_op, prompt_id=prompt_id)

    async def promote(self, prompt_id: str, body: PromotePromptDto) -> PromptDeploymentDto | None:
        """See :meth:`Prompts.promote`."""
        return await self._client._invoke(_promote_op, prompt_id=prompt_id, body=body)

    async def rollback(self, prompt_id: str, body: RollbackPromptDto) -> PromptDeploymentDto | None:
        """See :meth:`Prompts.rollback`."""
        return await self._client._invoke(_rollback_op, prompt_id=prompt_id, body=body)

    async def versions(self, prompt_id: str) -> PromptVersionListDto | None:
        """See :meth:`Prompts.versions`."""
        return await self._client._invoke(_versions_op, prompt_id=prompt_id)

    async def create_version(
        self, prompt_id: str, body: CreatePromptVersionDto
    ) -> PromptVersionDto | None:
        """See :meth:`Prompts.create_version`."""
        return await self._client._invoke(_create_version_op, prompt_id=prompt_id, body=body)

    async def version(self, prompt_id: str, version: str) -> PromptVersionDto | None:
        """See :meth:`Prompts.version`."""
        return await self._client._invoke(_version_op, prompt_id=prompt_id, version=version)
