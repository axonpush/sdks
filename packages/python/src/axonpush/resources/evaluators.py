"""Evaluators and their versions."""

from __future__ import annotations

from typing import TYPE_CHECKING

from axonpush._internal.api.api.evaluators import (
    evaluator_controller_create as _create_op,
    evaluator_controller_create_version as _create_version_op,
    evaluator_controller_get as _get_op,
    evaluator_controller_list as _list_op,
    evaluator_controller_remove as _remove_op,
    evaluator_controller_version as _version_op,
    evaluator_controller_versions as _versions_op,
)
from axonpush._internal.api.models import (
    CreateEvaluatorDto,
    CreateEvaluatorVersionDto,
    EvaluatorDeleteDto,
    EvaluatorDto,
    EvaluatorListDto,
    EvaluatorVersionDto,
    EvaluatorVersionListDto,
)

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


class Evaluators:
    """Evaluators and their versions."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def list(self) -> EvaluatorListDto | None:
        """List them all. `GET /v2/evaluators`"""
        return self._client._invoke(_list_op)

    def create(self, body: CreateEvaluatorDto) -> EvaluatorDto | None:
        """Create one. `POST /v2/evaluators`"""
        return self._client._invoke(_create_op, body=body)

    def delete(self, evaluator_id: str) -> EvaluatorDeleteDto | None:
        """Delete one. `DELETE /v2/evaluators/{evaluatorId}`"""
        return self._client._invoke(_remove_op, evaluator_id=evaluator_id)

    def get(self, evaluator_id: str) -> EvaluatorDto | None:
        """Fetch one by id. `GET /v2/evaluators/{evaluatorId}`"""
        return self._client._invoke(_get_op, evaluator_id=evaluator_id)

    def versions(self, evaluator_id: str) -> EvaluatorVersionListDto | None:
        """Versions. `GET /v2/evaluators/{evaluatorId}/versions`"""
        return self._client._invoke(_versions_op, evaluator_id=evaluator_id)

    def create_version(
        self, evaluator_id: str, body: CreateEvaluatorVersionDto
    ) -> EvaluatorVersionDto | None:
        """Create version. `POST /v2/evaluators/{evaluatorId}/versions`"""
        return self._client._invoke(_create_version_op, evaluator_id=evaluator_id, body=body)

    def version(self, evaluator_id: str, version: str) -> EvaluatorVersionDto | None:
        """Version. `GET /v2/evaluators/{evaluatorId}/versions/{version}`"""
        return self._client._invoke(_version_op, evaluator_id=evaluator_id, version=version)


class AsyncEvaluators:
    """Async sibling of :class:`Evaluators`."""

    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def list(self) -> EvaluatorListDto | None:
        """See :meth:`Evaluators.list`."""
        return await self._client._invoke(_list_op)

    async def create(self, body: CreateEvaluatorDto) -> EvaluatorDto | None:
        """See :meth:`Evaluators.create`."""
        return await self._client._invoke(_create_op, body=body)

    async def delete(self, evaluator_id: str) -> EvaluatorDeleteDto | None:
        """See :meth:`Evaluators.delete`."""
        return await self._client._invoke(_remove_op, evaluator_id=evaluator_id)

    async def get(self, evaluator_id: str) -> EvaluatorDto | None:
        """See :meth:`Evaluators.get`."""
        return await self._client._invoke(_get_op, evaluator_id=evaluator_id)

    async def versions(self, evaluator_id: str) -> EvaluatorVersionListDto | None:
        """See :meth:`Evaluators.versions`."""
        return await self._client._invoke(_versions_op, evaluator_id=evaluator_id)

    async def create_version(
        self, evaluator_id: str, body: CreateEvaluatorVersionDto
    ) -> EvaluatorVersionDto | None:
        """See :meth:`Evaluators.create_version`."""
        return await self._client._invoke(_create_version_op, evaluator_id=evaluator_id, body=body)

    async def version(self, evaluator_id: str, version: str) -> EvaluatorVersionDto | None:
        """See :meth:`Evaluators.version`."""
        return await self._client._invoke(_version_op, evaluator_id=evaluator_id, version=version)
