"""Unit tests for the resources added in the contract refresh.

Covers retained error, analytics, alert occurrence and organization resources.
Business workspace coverage lives in test_operations.py. No backend required.
"""

from __future__ import annotations

from typing import Any, Awaitable, Callable

import pytest

from axonpush._internal.api.api.alerts import alerts_occurrences as _occurrences_op
from axonpush._internal.api.api.analytics import (
    analytics_diff as _diff_op,
    analytics_heatmap as _heatmap_op,
    analytics_ingestion_status as _ingestion_status_op,
    analytics_overview as _overview_op,
)
from axonpush._internal.api.api.errors import (
    errors_events as _err_events_op,
    errors_get as _err_get_op,
    errors_list as _err_list_op,
    errors_triage as _err_triage_op,
)
from axonpush._internal.api.api.organization import (
    organization_invitations_accept as _accept_op,
    organization_leave as _leave_op,
)
from axonpush._internal.api.models import (
    ListErrorEventsOutputBody,
    ListErrorsOutputBody,
    OccurrencesOutputBody,
)
from axonpush.resources.alerts import Alerts, AsyncAlerts
from axonpush.resources.analytics import Analytics, AsyncAnalytics
from axonpush.resources.errors import AsyncErrors, Errors
from axonpush.resources.organizations import AsyncOrganizations, Organizations

SENTINEL_BODY: Any = object()


class FakeSyncClient:
    def __init__(self, return_value: Any = None) -> None:
        self.calls: list[tuple[Callable[..., Any], dict[str, Any]]] = []
        self.return_value = return_value

    def _invoke(self, op: Callable[..., Any], /, _coerce: Any = None, **kwargs: Any) -> Any:
        self.calls.append((op, kwargs))
        return _coerce(self.return_value) if _coerce else self.return_value


class FakeAsyncClient:
    def __init__(self, return_value: Any = None) -> None:
        self.calls: list[tuple[Callable[..., Awaitable[Any]], dict[str, Any]]] = []
        self.return_value = return_value

    async def _invoke(
        self, op: Callable[..., Awaitable[Any]], /, _coerce: Any = None, **kwargs: Any
    ) -> Any:
        self.calls.append((op, kwargs))
        return _coerce(self.return_value) if _coerce else self.return_value


class TestErrors:
    def test_list_unwraps_issues_and_filters(self) -> None:
        fake = FakeSyncClient(return_value=ListErrorsOutputBody(issues=[]))
        assert Errors(fake).list(status="unresolved", limit=10) == []
        op, kwargs = fake.calls[0]
        assert op is _err_list_op
        assert kwargs == {"status": "unresolved", "limit": 10}

    def test_list_drops_none_query(self) -> None:
        fake = FakeSyncClient(return_value=ListErrorsOutputBody(issues=[]))
        Errors(fake).list()
        assert fake.calls[0][1] == {}

    def test_get_dispatches_with_query(self) -> None:
        fake = FakeSyncClient()
        Errors(fake).get("fp1", since="t0")
        op, kwargs = fake.calls[0]
        assert op is _err_get_op
        assert kwargs == {"fingerprint": "fp1", "since": "t0"}

    def test_events_unwraps(self) -> None:
        fake = FakeSyncClient(return_value=ListErrorEventsOutputBody(events=[]))
        assert Errors(fake).events("fp1", limit=5) == []
        op, kwargs = fake.calls[0]
        assert op is _err_events_op
        assert kwargs == {"fingerprint": "fp1", "limit": 5}

    def test_triage_forwards_body(self) -> None:
        fake = FakeSyncClient()
        Errors(fake).triage("fp1", SENTINEL_BODY)
        op, kwargs = fake.calls[0]
        assert op is _err_triage_op
        assert kwargs["fingerprint"] == "fp1"
        assert kwargs["body"] is SENTINEL_BODY

    @pytest.mark.asyncio
    async def test_async_events_unwraps(self) -> None:
        fake = FakeAsyncClient(return_value=ListErrorEventsOutputBody(events=[]))
        assert await AsyncErrors(fake).events("fp1") == []
        assert fake.calls[0][0] is _err_events_op


class TestAnalyticsAdditions:
    def test_overview_dispatches(self) -> None:
        fake = FakeSyncClient()
        Analytics(fake).overview(since="t0", bucket="hour")
        op, kwargs = fake.calls[0]
        assert op is _overview_op
        assert kwargs["since"] == "t0"
        assert kwargs["bucket"] == "hour"

    def test_heatmap_dispatches(self) -> None:
        fake = FakeSyncClient()
        Analytics(fake).heatmap(buckets=24)
        op, kwargs = fake.calls[0]
        assert op is _heatmap_op
        assert kwargs["buckets"] == 24

    def test_diff_forwards_body(self) -> None:
        fake = FakeSyncClient()
        Analytics(fake).diff(SENTINEL_BODY)
        op, kwargs = fake.calls[0]
        assert op is _diff_op
        assert kwargs["body"] is SENTINEL_BODY

    def test_ingestion_status_dispatches(self) -> None:
        fake = FakeSyncClient()
        Analytics(fake).ingestion_status(environment="prod")
        op, kwargs = fake.calls[0]
        assert op is _ingestion_status_op
        assert kwargs["environment"] == "prod"

    @pytest.mark.asyncio
    async def test_async_overview_dispatches(self) -> None:
        fake = FakeAsyncClient()
        await AsyncAnalytics(fake).overview()
        assert fake.calls[0][0] is _overview_op


class TestAlertsOccurrences:
    def test_occurrences_unwraps_data(self) -> None:
        fake = FakeSyncClient(return_value=OccurrencesOutputBody(data=[]))
        assert Alerts(fake).occurrences("r1", limit=3) == []
        op, kwargs = fake.calls[0]
        assert op is _occurrences_op
        assert kwargs == {"alert_rule_id": "r1", "limit": 3}

    @pytest.mark.asyncio
    async def test_async_occurrences_unwraps(self) -> None:
        fake = FakeAsyncClient(return_value=OccurrencesOutputBody(data=[]))
        assert await AsyncAlerts(fake).occurrences("r1") == []
        assert fake.calls[0][1] == {"alert_rule_id": "r1"}


class TestOrganizationAdditions:
    def test_leave_dispatches(self) -> None:
        fake = FakeSyncClient()
        Organizations(fake).leave("org1")
        assert fake.calls[0] == (_leave_op, {"org_id": "org1"})

    def test_accept_invitation_forwards_body(self) -> None:
        fake = FakeSyncClient()
        Organizations(fake).accept_invitation(SENTINEL_BODY)
        op, kwargs = fake.calls[0]
        assert op is _accept_op
        assert kwargs["body"] is SENTINEL_BODY

    @pytest.mark.asyncio
    async def test_async_leave_dispatches(self) -> None:
        fake = FakeAsyncClient()
        await AsyncOrganizations(fake).leave("org1")
        assert fake.calls[0] == (_leave_op, {"org_id": "org1"})
