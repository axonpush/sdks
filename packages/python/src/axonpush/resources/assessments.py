"""Human and automated judgements attached to a trace."""

from __future__ import annotations

from typing import TYPE_CHECKING

from axonpush._internal.api.api.assessments import (
    assessment_controller_create as _create_op,
    assessment_controller_list as _list_op,
    assessment_controller_remove as _remove_op,
    assessment_controller_remove_by_query as _remove_by_query_op,
)
from axonpush._internal.api.models import (
    AssessmentDeleteResponseDto,
    AssessmentDto,
    AssessmentListResponseDto,
    CreateAssessmentDto,
)

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


class Assessments:
    """Human and automated judgements attached to a trace."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def remove_by_query(
        self, trace_id: str, assessment_id: str
    ) -> AssessmentDeleteResponseDto | None:
        """Remove by query. `DELETE /v2/traces/{traceId}/assessments`"""
        return self._client._invoke(
            _remove_by_query_op, trace_id=trace_id, assessment_id=assessment_id
        )

    def list(self, trace_id: str) -> AssessmentListResponseDto | None:
        """List them all. `GET /v2/traces/{traceId}/assessments`"""
        return self._client._invoke(_list_op, trace_id=trace_id)

    def create(self, trace_id: str, body: CreateAssessmentDto) -> AssessmentDto | None:
        """Create one. `POST /v2/traces/{traceId}/assessments`"""
        return self._client._invoke(_create_op, trace_id=trace_id, body=body)

    def delete(self, trace_id: str, assessment_id: str) -> AssessmentDeleteResponseDto | None:
        """Delete one. `DELETE /v2/traces/{traceId}/assessments/{assessmentId}`"""
        return self._client._invoke(_remove_op, trace_id=trace_id, assessment_id=assessment_id)


class AsyncAssessments:
    """Async sibling of :class:`Assessments`."""

    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def remove_by_query(
        self, trace_id: str, assessment_id: str
    ) -> AssessmentDeleteResponseDto | None:
        """See :meth:`Assessments.remove_by_query`."""
        return await self._client._invoke(
            _remove_by_query_op, trace_id=trace_id, assessment_id=assessment_id
        )

    async def list(self, trace_id: str) -> AssessmentListResponseDto | None:
        """See :meth:`Assessments.list`."""
        return await self._client._invoke(_list_op, trace_id=trace_id)

    async def create(self, trace_id: str, body: CreateAssessmentDto) -> AssessmentDto | None:
        """See :meth:`Assessments.create`."""
        return await self._client._invoke(_create_op, trace_id=trace_id, body=body)

    async def delete(self, trace_id: str, assessment_id: str) -> AssessmentDeleteResponseDto | None:
        """See :meth:`Assessments.delete`."""
        return await self._client._invoke(
            _remove_op, trace_id=trace_id, assessment_id=assessment_id
        )
