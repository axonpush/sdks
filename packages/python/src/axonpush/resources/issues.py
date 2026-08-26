"""Clustered failures, their occurrences and triage actions."""

from __future__ import annotations

from typing import TYPE_CHECKING, List

from axonpush._internal.api.api.issues import (
    issue_controller_add_to_dataset as _add_to_dataset_op,
    issue_controller_get as _get_op,
    issue_controller_list as _list_op,
    issue_controller_merge as _merge_op,
    issue_controller_occurrences as _occurrences_op,
    issue_controller_update as _update_op,
)
from axonpush._internal.api.models import (
    AddIssueToDatasetDto,
    IssueOccurrenceResponseDto,
    IssueResponseDto,
    MergeIssueDto,
    UpdateIssueDto,
)

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


class Issues:
    """Clustered failures, their occurrences and triage actions."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def list(
        self, severity: str | None = None, status: str | None = None
    ) -> List[IssueResponseDto] | None:
        """List them all. `GET /v2/issues`"""
        return self._client._invoke(_list_op, severity=severity, status=status)

    def get(self, issue_id: str) -> IssueResponseDto | None:
        """Fetch one by id. `GET /v2/issues/{issueId}`"""
        return self._client._invoke(_get_op, issue_id=issue_id)

    def update(self, issue_id: str, body: UpdateIssueDto) -> IssueResponseDto | None:
        """Update one. `PATCH /v2/issues/{issueId}`"""
        return self._client._invoke(_update_op, issue_id=issue_id, body=body)

    def add_to_dataset(self, issue_id: str, body: AddIssueToDatasetDto) -> IssueResponseDto | None:
        """Add to dataset. `POST /v2/issues/{issueId}/actions/add-to-dataset`"""
        return self._client._invoke(_add_to_dataset_op, issue_id=issue_id, body=body)

    def merge(self, issue_id: str, body: MergeIssueDto) -> IssueResponseDto | None:
        """Merge. `POST /v2/issues/{issueId}/merge`"""
        return self._client._invoke(_merge_op, issue_id=issue_id, body=body)

    def occurrences(self, issue_id: str) -> List[IssueOccurrenceResponseDto] | None:
        """Occurrences. `GET /v2/issues/{issueId}/occurrences`"""
        return self._client._invoke(_occurrences_op, issue_id=issue_id)


class AsyncIssues:
    """Async sibling of :class:`Issues`."""

    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def list(
        self, severity: str | None = None, status: str | None = None
    ) -> List[IssueResponseDto] | None:
        """See :meth:`Issues.list`."""
        return await self._client._invoke(_list_op, severity=severity, status=status)

    async def get(self, issue_id: str) -> IssueResponseDto | None:
        """See :meth:`Issues.get`."""
        return await self._client._invoke(_get_op, issue_id=issue_id)

    async def update(self, issue_id: str, body: UpdateIssueDto) -> IssueResponseDto | None:
        """See :meth:`Issues.update`."""
        return await self._client._invoke(_update_op, issue_id=issue_id, body=body)

    async def add_to_dataset(
        self, issue_id: str, body: AddIssueToDatasetDto
    ) -> IssueResponseDto | None:
        """See :meth:`Issues.add_to_dataset`."""
        return await self._client._invoke(_add_to_dataset_op, issue_id=issue_id, body=body)

    async def merge(self, issue_id: str, body: MergeIssueDto) -> IssueResponseDto | None:
        """See :meth:`Issues.merge`."""
        return await self._client._invoke(_merge_op, issue_id=issue_id, body=body)

    async def occurrences(self, issue_id: str) -> List[IssueOccurrenceResponseDto] | None:
        """See :meth:`Issues.occurrences`."""
        return await self._client._invoke(_occurrences_op, issue_id=issue_id)
