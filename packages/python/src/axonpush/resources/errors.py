"""Errors resource — issue triage and error-event drilldown. ``/errors``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List

from axonpush._internal.api.api.errors import (
    errors_events as _events_op,
    errors_get as _get_op,
    errors_list as _list_op,
    errors_triage as _triage_op,
)
from axonpush._internal.api.models import (
    ErrorIssueDTO,
    ErrorsListStatus,
    EventDTO,
    IssueDetailDTO,
    IssueTriageDTO,
    ListErrorEventsOutputBody,
    ListErrorsOutputBody,
    PatchErrorInputBody,
)

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


def _unwrap_issues(result: ListErrorsOutputBody | None) -> List[ErrorIssueDTO] | None:
    if result is None:
        return None
    return list(result.issues or [])


def _unwrap_events(result: ListErrorEventsOutputBody | None) -> List[EventDTO] | None:
    if result is None:
        return None
    return list(result.events or [])


def _list_kwargs(
    *,
    since: str | None,
    until: str | None,
    status: ErrorsListStatus | str | None,
    service: str | None,
    q: str | None,
    assignee: str | None,
    limit: int | None,
) -> Dict[str, Any]:
    return {
        k: v
        for k, v in {
            "since": since,
            "until": until,
            "status": status,
            "service": service,
            "q": q,
            "assignee": assignee,
            "limit": limit,
        }.items()
        if v is not None
    }


class Errors:
    """Synchronous error-issue triage."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def list(
        self,
        *,
        since: str | None = None,
        until: str | None = None,
        status: ErrorsListStatus | str | None = None,
        service: str | None = None,
        q: str | None = None,
        assignee: str | None = None,
        limit: int | None = None,
    ) -> List[ErrorIssueDTO] | None:
        """List error issues (envelope unwrapped). ``GET /errors``"""
        kwargs = _list_kwargs(
            since=since,
            until=until,
            status=status,
            service=service,
            q=q,
            assignee=assignee,
            limit=limit,
        )
        return self._client._invoke(_list_op, _coerce=_unwrap_issues, **kwargs)

    def get(
        self,
        fingerprint: str,
        *,
        since: str | None = None,
        until: str | None = None,
    ) -> IssueDetailDTO | None:
        """Fetch one issue by fingerprint. ``GET /errors/{fingerprint}``"""
        kwargs = {k: v for k, v in {"since": since, "until": until}.items() if v is not None}
        return self._client._invoke(_get_op, fingerprint=fingerprint, **kwargs)

    def events(
        self,
        fingerprint: str,
        *,
        before: str | None = None,
        after: str | None = None,
        limit: int | None = None,
    ) -> List[EventDTO] | None:
        """List raw events for an issue (envelope unwrapped).

        ``GET /errors/{fingerprint}/events``
        """
        kwargs = {
            k: v
            for k, v in {"before": before, "after": after, "limit": limit}.items()
            if v is not None
        }
        return self._client._invoke(
            _events_op, _coerce=_unwrap_events, fingerprint=fingerprint, **kwargs
        )

    def triage(self, fingerprint: str, body: PatchErrorInputBody) -> IssueTriageDTO | None:
        """Update an issue's triage state. ``PATCH /errors/{fingerprint}``"""
        return self._client._invoke(_triage_op, fingerprint=fingerprint, body=body)


class AsyncErrors:
    """Async sibling of :class:`Errors`."""

    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def list(
        self,
        *,
        since: str | None = None,
        until: str | None = None,
        status: ErrorsListStatus | str | None = None,
        service: str | None = None,
        q: str | None = None,
        assignee: str | None = None,
        limit: int | None = None,
    ) -> List[ErrorIssueDTO] | None:
        """See :meth:`Errors.list`."""
        kwargs = _list_kwargs(
            since=since,
            until=until,
            status=status,
            service=service,
            q=q,
            assignee=assignee,
            limit=limit,
        )
        return await self._client._invoke(_list_op, _coerce=_unwrap_issues, **kwargs)

    async def get(
        self,
        fingerprint: str,
        *,
        since: str | None = None,
        until: str | None = None,
    ) -> IssueDetailDTO | None:
        """See :meth:`Errors.get`."""
        kwargs = {k: v for k, v in {"since": since, "until": until}.items() if v is not None}
        return await self._client._invoke(_get_op, fingerprint=fingerprint, **kwargs)

    async def events(
        self,
        fingerprint: str,
        *,
        before: str | None = None,
        after: str | None = None,
        limit: int | None = None,
    ) -> List[EventDTO] | None:
        """See :meth:`Errors.events`."""
        kwargs = {
            k: v
            for k, v in {"before": before, "after": after, "limit": limit}.items()
            if v is not None
        }
        return await self._client._invoke(
            _events_op, _coerce=_unwrap_events, fingerprint=fingerprint, **kwargs
        )

    async def triage(self, fingerprint: str, body: PatchErrorInputBody) -> IssueTriageDTO | None:
        """See :meth:`Errors.triage`."""
        return await self._client._invoke(_triage_op, fingerprint=fingerprint, body=body)
