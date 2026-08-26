"""The systems an experiment can run against."""

from __future__ import annotations

from typing import TYPE_CHECKING

from axonpush._internal.api.api.evaluation_targets import (
    evaluation_target_controller_create as _create_op,
    evaluation_target_controller_get as _get_op,
    evaluation_target_controller_list as _list_op,
    evaluation_target_controller_remove as _remove_op,
    evaluation_target_controller_update as _update_op,
)
from axonpush._internal.api.models import (
    CreateEvaluationTargetDto,
    EvaluationTargetDeleteDto,
    EvaluationTargetDto,
    EvaluationTargetListDto,
    UpdateEvaluationTargetDto,
)

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


class EvaluationTargets:
    """The systems an experiment can run against."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def list(self) -> EvaluationTargetListDto | None:
        """List them all. `GET /v2/evaluation-targets`"""
        return self._client._invoke(_list_op)

    def create(self, body: CreateEvaluationTargetDto) -> EvaluationTargetDto | None:
        """Create one. `POST /v2/evaluation-targets`"""
        return self._client._invoke(_create_op, body=body)

    def delete(self, target_id: str) -> EvaluationTargetDeleteDto | None:
        """Delete one. `DELETE /v2/evaluation-targets/{targetId}`"""
        return self._client._invoke(_remove_op, target_id=target_id)

    def get(self, target_id: str) -> EvaluationTargetDto | None:
        """Fetch one by id. `GET /v2/evaluation-targets/{targetId}`"""
        return self._client._invoke(_get_op, target_id=target_id)

    def update(self, target_id: str, body: UpdateEvaluationTargetDto) -> EvaluationTargetDto | None:
        """Update one. `PATCH /v2/evaluation-targets/{targetId}`"""
        return self._client._invoke(_update_op, target_id=target_id, body=body)


class AsyncEvaluationTargets:
    """Async sibling of :class:`EvaluationTargets`."""

    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def list(self) -> EvaluationTargetListDto | None:
        """See :meth:`EvaluationTargets.list`."""
        return await self._client._invoke(_list_op)

    async def create(self, body: CreateEvaluationTargetDto) -> EvaluationTargetDto | None:
        """See :meth:`EvaluationTargets.create`."""
        return await self._client._invoke(_create_op, body=body)

    async def delete(self, target_id: str) -> EvaluationTargetDeleteDto | None:
        """See :meth:`EvaluationTargets.delete`."""
        return await self._client._invoke(_remove_op, target_id=target_id)

    async def get(self, target_id: str) -> EvaluationTargetDto | None:
        """See :meth:`EvaluationTargets.get`."""
        return await self._client._invoke(_get_op, target_id=target_id)

    async def update(
        self, target_id: str, body: UpdateEvaluationTargetDto
    ) -> EvaluationTargetDto | None:
        """See :meth:`EvaluationTargets.update`."""
        return await self._client._invoke(_update_op, target_id=target_id, body=body)
