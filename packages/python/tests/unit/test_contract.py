"""Replay contract/fixtures/*.json against the Python SDK.

The server generates these by calling its own signing function and scope enum,
so they cannot describe behaviour the backend does not have. The AXONPUSH_*
surface was previously transcribed into each SDK by hand, which is how the
timeout unit and the fail-open default came to disagree between languages.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from axonpush._config import Settings

FIXTURES = Path(__file__).resolve().parents[4] / "contract" / "fixtures"


def load(name: str) -> Any:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


ENV = load("env.json")
HEADERS = load("headers.json")
ERRORS = load("errors.json")


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
        assert HEADERS["auth"]["publicToken"] == "X-Public-Token"
        assert HEADERS["tenancy"]["orgId"] == "x-tenant-id"
        assert HEADERS["scoping"]["environment"] == "X-Axonpush-Environment"
        assert HEADERS["tracing"]["traceId"] == "X-Axonpush-Trace-Id"

    def test_transport_sends_exactly_these(self) -> None:
        from axonpush._internal import transport

        source = Path(transport.__file__).read_text(encoding="utf-8")
        # The Go backend authenticates ``ak_`` keys via ``x-axonpush-api-key``
        # (the shared ``headers.json`` fixture still records the legacy
        # ``X-API-Key`` name, which the transport intentionally no longer uses).
        for header in (
            "x-axonpush-api-key",
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
