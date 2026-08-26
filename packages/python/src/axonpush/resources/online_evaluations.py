"""Rules that evaluate live traffic as it arrives."""

from __future__ import annotations

from typing import TYPE_CHECKING, List

from axonpush._internal.api.api.online_evaluations import (
    online_evaluation_controller_backfill as _backfill_op,
    online_evaluation_controller_create as _create_op,
    online_evaluation_controller_get as _get_op,
    online_evaluation_controller_list as _list_op,
    online_evaluation_controller_remove as _remove_op,
    online_evaluation_controller_runs as _runs_op,
    online_evaluation_controller_update as _update_op,
)
from axonpush._internal.api.models import (
    BackfillOnlineRuleDto,
    CreateOnlineRuleDto,
    DeleteResultDto,
    OnlineRuleResponseDto,
    OnlineRuleRunResponseDto,
    UpdateOnlineRuleDto,
)

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


class OnlineEvaluations:
    """Rules that evaluate live traffic as it arrives."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def list(self) -> List[OnlineRuleResponseDto] | None:
        """List them all. `GET /v2/online-evaluation-rules`"""
        return self._client._invoke(_list_op)

    def create(self, body: CreateOnlineRuleDto) -> OnlineRuleResponseDto | None:
        """Create one. `POST /v2/online-evaluation-rules`"""
        return self._client._invoke(_create_op, body=body)

    def delete(self, rule_id: str) -> DeleteResultDto | None:
        """Delete one. `DELETE /v2/online-evaluation-rules/{ruleId}`"""
        return self._client._invoke(_remove_op, rule_id=rule_id)

    def get(self, rule_id: str) -> OnlineRuleResponseDto | None:
        """Fetch one by id. `GET /v2/online-evaluation-rules/{ruleId}`"""
        return self._client._invoke(_get_op, rule_id=rule_id)

    def update(self, rule_id: str, body: UpdateOnlineRuleDto) -> OnlineRuleResponseDto | None:
        """Update one. `PATCH /v2/online-evaluation-rules/{ruleId}`"""
        return self._client._invoke(_update_op, rule_id=rule_id, body=body)

    def backfill(
        self, rule_id: str, body: BackfillOnlineRuleDto
    ) -> List[OnlineRuleRunResponseDto] | None:
        """Backfill. `POST /v2/online-evaluation-rules/{ruleId}/backfill`"""
        return self._client._invoke(_backfill_op, rule_id=rule_id, body=body)

    def runs(self, rule_id: str) -> List[OnlineRuleRunResponseDto] | None:
        """Runs. `GET /v2/online-evaluation-rules/{ruleId}/runs`"""
        return self._client._invoke(_runs_op, rule_id=rule_id)


class AsyncOnlineEvaluations:
    """Async sibling of :class:`OnlineEvaluations`."""

    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def list(self) -> List[OnlineRuleResponseDto] | None:
        """See :meth:`OnlineEvaluations.list`."""
        return await self._client._invoke(_list_op)

    async def create(self, body: CreateOnlineRuleDto) -> OnlineRuleResponseDto | None:
        """See :meth:`OnlineEvaluations.create`."""
        return await self._client._invoke(_create_op, body=body)

    async def delete(self, rule_id: str) -> DeleteResultDto | None:
        """See :meth:`OnlineEvaluations.delete`."""
        return await self._client._invoke(_remove_op, rule_id=rule_id)

    async def get(self, rule_id: str) -> OnlineRuleResponseDto | None:
        """See :meth:`OnlineEvaluations.get`."""
        return await self._client._invoke(_get_op, rule_id=rule_id)

    async def update(self, rule_id: str, body: UpdateOnlineRuleDto) -> OnlineRuleResponseDto | None:
        """See :meth:`OnlineEvaluations.update`."""
        return await self._client._invoke(_update_op, rule_id=rule_id, body=body)

    async def backfill(
        self, rule_id: str, body: BackfillOnlineRuleDto
    ) -> List[OnlineRuleRunResponseDto] | None:
        """See :meth:`OnlineEvaluations.backfill`."""
        return await self._client._invoke(_backfill_op, rule_id=rule_id, body=body)

    async def runs(self, rule_id: str) -> List[OnlineRuleRunResponseDto] | None:
        """See :meth:`OnlineEvaluations.runs`."""
        return await self._client._invoke(_runs_op, rule_id=rule_id)
