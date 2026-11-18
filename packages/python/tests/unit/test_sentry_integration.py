"""Unit tests for ``install_sentry`` — verifies DSN construction, env-var
fallbacks, precedence of the environment detector, and the Sentry SDK
contract (single ``sentry_sdk.init`` call with the right kwargs).

These tests do NOT require ``sentry-sdk`` to be installed. A stub module is
injected via ``sys.modules`` so the integration's ``import sentry_sdk`` call
binds to the stub."""

from __future__ import annotations

import sys
import types

import pytest

from axonpush.integrations.sentry import build_dsn, install_sentry, sentry_project_id


@pytest.fixture()
def sentry_stub(monkeypatch):
    """Install a fake ``sentry_sdk`` module that records ``init()`` calls.

    Without this, ``install_sentry`` raises ImportError on systems that don't
    have sentry-sdk installed — these tests must work either way."""
    stub = types.ModuleType("sentry_sdk")
    calls: list[dict] = []

    def fake_init(**kwargs):
        calls.append(kwargs)

    stub.init = fake_init  # type: ignore[attr-defined]
    monkeypatch.setitem(sys.modules, "sentry_sdk", stub)
    return calls


@pytest.fixture(autouse=True)
def _clear_env(monkeypatch):
    """Prevent the host's real env vars from leaking into the env detector."""
    for k in (
        "AXONPUSH_PUBLIC_TOKEN",
        "AXONPUSH_CHANNEL_ID",
        "AXONPUSH_HOST",
        "AXONPUSH_ENVIRONMENT",
        "SENTRY_ENVIRONMENT",
        "APP_ENV",
        "ENV",
    ):
        monkeypatch.delenv(k, raising=False)


class TestBuildDsn:
    def test_https_for_production_host(self):
        assert build_dsn("pt_abc", 42, "api.axonpush.xyz") == "https://pt_abc@api.axonpush.xyz/66"

    def test_http_for_localhost(self):
        assert build_dsn("pt_abc", 42, "localhost:3000") == "http://pt_abc@localhost:3000/66"

    def test_http_for_127_loopback(self):
        assert build_dsn("pt_abc", 42, "127.0.0.1:3000") == "http://pt_abc@127.0.0.1:3000/66"

    def test_rejects_api_keys(self):
        with pytest.raises(ValueError, match="public ingest token"):
            build_dsn("ak_abc", 42, "api.axonpush.xyz")


class TestSentryProjectId:
    def test_uuid_channel_matches_dashboard_derivation(self):
        assert sentry_project_id("0a1b2c3d-4e5f-6789-abcd-ef0123456789") == 0x0A1B2C3D

    def test_prefixed_id_parses_leading_hex_like_parse_int(self):
        assert sentry_project_id("ch_123") == 0xC

    def test_falls_back_to_one(self):
        assert sentry_project_id(None) == 1
        assert sentry_project_id("zzz") == 1
        assert sentry_project_id("00000000-0000") == 1


class TestInstallSentry:
    def test_builds_dsn_from_kwargs(self, sentry_stub):
        install_sentry(public_token="pt_abc", channel_id="0a1b2c3d-0000")
        assert len(sentry_stub) == 1
        assert sentry_stub[0]["dsn"] == f"https://pt_abc@api.axonpush.xyz/{0x0A1B2C3D}"

    def test_channel_is_optional(self, sentry_stub):
        install_sentry(public_token="pt_abc")
        assert sentry_stub[0]["dsn"] == "https://pt_abc@api.axonpush.xyz/1"

    def test_explicit_dsn_bypasses_builder(self, sentry_stub):
        install_sentry(dsn="https://custom@sentry.io/1")
        assert sentry_stub[0]["dsn"] == "https://custom@sentry.io/1"

    def test_env_vars_fill_in_missing_kwargs(self, sentry_stub, monkeypatch):
        monkeypatch.setenv("AXONPUSH_PUBLIC_TOKEN", "pt_from_env")
        monkeypatch.setenv("AXONPUSH_CHANNEL_ID", "7")
        install_sentry()
        assert sentry_stub[0]["dsn"] == "https://pt_from_env@api.axonpush.xyz/7"

    def test_custom_host_env_var(self, sentry_stub, monkeypatch):
        monkeypatch.setenv("AXONPUSH_PUBLIC_TOKEN", "pt_x")
        monkeypatch.setenv("AXONPUSH_HOST", "localhost:3000")
        install_sentry()
        assert sentry_stub[0]["dsn"] == "http://pt_x@localhost:3000/1"

    def test_missing_credentials_raises(self, sentry_stub):
        with pytest.raises(ValueError, match="public_token"):
            install_sentry()

    def test_api_key_is_refused(self, sentry_stub):
        with pytest.raises(ValueError, match="api_key"):
            install_sentry(api_key="ak_x", channel_id=1)
        with pytest.raises(ValueError, match="public ingest token"):
            install_sentry(public_token="ak_x")
        assert sentry_stub == []
    def test_environment_and_release_forwarded(self, sentry_stub):
        install_sentry(
            public_token="pt_x",
            channel_id=1,
            environment="production",
            release="my-app@1.2.3",
        )
        assert sentry_stub[0]["environment"] == "production"
        assert sentry_stub[0]["release"] == "my-app@1.2.3"

    def test_environment_auto_detected_from_env_vars(self, sentry_stub, monkeypatch):
        """Same precedence as the AxonPush client:
        AXONPUSH_ENVIRONMENT > SENTRY_ENVIRONMENT > APP_ENV > ENV."""
        monkeypatch.setenv("ENV", "env-val")
        monkeypatch.setenv("APP_ENV", "app-env-val")
        monkeypatch.setenv("SENTRY_ENVIRONMENT", "sentry-val")
        monkeypatch.setenv("AXONPUSH_ENVIRONMENT", "axonpush-val")
        install_sentry(public_token="pt_x", channel_id=1)
        assert sentry_stub[0]["environment"] == "axonpush-val"

    def test_environment_not_set_when_nothing_detected(self, sentry_stub):
        install_sentry(public_token="pt_x", channel_id=1)
        assert "environment" not in sentry_stub[0]

    def test_extra_kwargs_passed_through_to_sentry_init(self, sentry_stub):
        """``**sentry_init_kwargs`` catches everything not explicitly named —
        these are the knobs users will want to tune (sample rates, integrations,
        transport options)."""
        install_sentry(
            public_token="pt_x",
            channel_id=1,
            traces_sample_rate=0.25,
            send_default_pii=False,
            max_breadcrumbs=50,
        )
        call = sentry_stub[0]
        assert call["traces_sample_rate"] == 0.25
        assert call["send_default_pii"] is False
        assert call["max_breadcrumbs"] == 50

    def test_explicit_environment_beats_env_var(self, sentry_stub, monkeypatch):
        monkeypatch.setenv("AXONPUSH_ENVIRONMENT", "from-env")
        install_sentry(public_token="pt_x", channel_id=1, environment="explicit")
        assert sentry_stub[0]["environment"] == "explicit"


class TestMissingSentrySdk:
    def test_import_error_has_actionable_message(self, monkeypatch):
        """If sentry-sdk isn't installed, install_sentry must raise an
        ImportError with install instructions — not a cryptic ModuleNotFoundError."""
        monkeypatch.setitem(sys.modules, "sentry_sdk", None)  # poison the import
        with pytest.raises(ImportError, match="pip install sentry-sdk"):
            install_sentry(public_token="pt_x", channel_id=1)
