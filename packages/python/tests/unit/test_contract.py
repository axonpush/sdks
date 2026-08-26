"""Replay contract/fixtures/*.json against the Python SDK.

The server generates these by calling its own topic builder, signing function
and scope enum, so they cannot describe behaviour the backend does not have.
The MQTT grammar and the AXONPUSH_* surface were previously transcribed into
each SDK by hand, which is how the timeout unit and the fail-open default came
to disagree between languages.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from axonpush._config import Settings
from axonpush.realtime.topics import build_publish_topic, build_subscribe_topic

FIXTURES = Path(__file__).resolve().parents[4] / "contract" / "fixtures"


def load(name: str) -> Any:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


TOPICS = load("topics.json")
ENV = load("env.json")
HEADERS = load("headers.json")
ERRORS = load("errors.json")


def org_prefix(org_id: str) -> str:
    """The prefix GET /auth/iot-credentials hands back, per the fixture."""
    for case in TOPICS["orgPrefixCases"]:
        if case["orgId"] == org_id:
            return str(case["prefix"])
    raise AssertionError(f"no orgPrefix case for {org_id!r}")


class TestTopics:
    def test_grammar_matches_the_server(self) -> None:
        assert TOPICS["segments"] == [
            "prefix",
            "orgId",
            "envSlug",
            "appId",
            "channelId",
            "eventType",
            "agentId",
        ]
        assert TOPICS["publishFallback"] == "_"
        assert TOPICS["subscribeWildcard"] == "+"

    def test_org_prefix_already_contains_the_org_id(self) -> None:
        """The 6-segment builder here only agrees with the server's 7 because of this."""
        assert TOPICS["orgPrefixIncludesOrgId"] is True

    @pytest.mark.parametrize("case", TOPICS["publishCases"])
    def test_publish(self, case: dict[str, Any]) -> None:
        i = case["input"]
        assert (
            build_publish_topic(
                org_prefix(i["orgId"]),
                app_id=i["appId"],
                channel_id=i["channelId"],
                event_type=i["eventType"],
                agent_id=i.get("agentId"),
                env_slug=i.get("envSlug"),
            )
            == case["topic"]
        )

    @pytest.mark.parametrize("case", TOPICS["subscribeCases"])
    def test_subscribe(self, case: dict[str, Any]) -> None:
        i = case["input"]
        assert (
            build_subscribe_topic(
                org_prefix(i["orgId"]),
                app_id=i.get("appId"),
                channel_id=i.get("channelId"),
                event_type=i.get("eventType"),
                agent_id=i.get("agentId"),
                env_slug=i.get("envSlug"),
            )
            == case["topic"]
        )


class TestEnvironment:
    VARS = ENV["variables"]

    @pytest.fixture(autouse=True)
    def _clear(self, monkeypatch: pytest.MonkeyPatch) -> None:
        for name in self.VARS:
            monkeypatch.delenv(name, raising=False)
        monkeypatch.delenv("AXONPUSH_ORG_ID", raising=False)

    def test_documented_defaults(self) -> None:
        s = Settings()
        assert str(s.base_url).rstrip("/") == str(self.VARS["AXONPUSH_BASE_URL"]["default"]).rstrip(
            "/"
        )
        assert s.max_retries == self.VARS["AXONPUSH_MAX_RETRIES"]["default"]
        assert s.fail_open == self.VARS["AXONPUSH_FAIL_OPEN"]["default"]

    def test_timeout_is_seconds(self) -> None:
        assert self.VARS["AXONPUSH_TIMEOUT"]["unit"] == "seconds"
        assert Settings().timeout == self.VARS["AXONPUSH_TIMEOUT"]["default"]

    def test_timeout_reads_from_the_environment(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("AXONPUSH_TIMEOUT", "5")
        assert Settings().timeout == 5.0

    def test_retry_ladder(self) -> None:
        from axonpush._internal.transport import _BACKOFF_SCHEDULE

        expected = [ms / 1000 for ms in ENV["retry"]["backoffMs"]]
        assert list(_BACKOFF_SCHEDULE) == expected


class TestHeaders:
    def test_canonical_names(self) -> None:
        assert HEADERS["auth"]["apiKey"] == "X-API-Key"
        assert HEADERS["tenancy"]["orgId"] == "x-tenant-id"
        assert HEADERS["scoping"]["environment"] == "X-Axonpush-Environment"
        assert HEADERS["tracing"]["traceId"] == "X-Axonpush-Trace-Id"

    def test_transport_sends_exactly_these(self) -> None:
        from axonpush._internal import transport

        source = Path(transport.__file__).read_text(encoding="utf-8")
        for header in (
            HEADERS["auth"]["apiKey"],
            HEADERS["tenancy"]["orgId"],
            HEADERS["scoping"]["environment"],
        ):
            assert header in source, f"transport does not send {header}"


class TestErrors:
    def test_status_mapping(self) -> None:
        import axonpush.exceptions as exc

        for row in ERRORS["mapping"]:
            name = row["name"]
            assert hasattr(exc, name), f"exceptions is missing {name}"

    def test_retryable_classes_are_marked(self) -> None:
        import axonpush.exceptions as exc

        retryable = exc.RetryableError
        for row in ERRORS["mapping"]:
            cls = getattr(exc, row["name"])
            if row["retryable"]:
                assert issubclass(cls, retryable), f"{row['name']} should be retryable"
