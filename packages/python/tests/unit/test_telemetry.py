"""Unit tests for the OTel-native ``axonpush.telemetry`` module."""

from __future__ import annotations

import pytest

pytest.importorskip("opentelemetry.sdk.trace")
pytest.importorskip("opentelemetry.exporter.otlp.proto.http.trace_exporter")

from opentelemetry.sdk.trace import TracerProvider  # noqa: E402
from opentelemetry.sdk.trace.export import SimpleSpanProcessor  # noqa: E402
from opentelemetry.sdk.trace.export.in_memory_span_exporter import (  # noqa: E402
    InMemorySpanExporter,
)

import axonpush.telemetry.core as telemetry  # noqa: E402
from axonpush.telemetry import (  # noqa: E402
    configure_telemetry,
    genai_span,
    record_genai_content,
    record_genai_response,
)


@pytest.fixture(autouse=True)
def _reset_installed():
    telemetry._INSTALLED.clear()
    yield
    telemetry._INSTALLED.clear()


@pytest.fixture()
def recording_provider():
    """A provider + in-memory exporter to read spans back out."""
    provider = TracerProvider()
    exporter = InMemorySpanExporter()
    provider.add_span_processor(SimpleSpanProcessor(exporter))
    return provider, exporter


def test_configure_uses_supplied_provider():
    provider = TracerProvider()
    handle = configure_telemetry(
        base_url="https://api.example.com",
        api_key="ak_test",
        channel_id="ch_1",
        tracer_provider=provider,
    )
    assert handle._provider is provider
    assert handle._owns_provider is False
    assert handle.tracer("x") is not None


def test_endpoint_and_headers_from_args():
    provider = TracerProvider()
    handle = configure_telemetry(
        base_url="https://api.example.com/",
        api_key="ak_secret",
        channel_id="ch_42",
        tracer_provider=provider,
    )
    exporter = handle._processor.span_exporter
    assert exporter._endpoint == "https://api.example.com/v1/traces"
    headers = exporter._session.headers
    assert headers["X-API-Key"] == "ak_secret"
    assert headers["X-Axonpush-Channel"] == "ch_42"


def test_env_resolution(monkeypatch):
    monkeypatch.setenv("AXONPUSH_BASE_URL", "https://env.example.com")
    monkeypatch.setenv("AXONPUSH_API_KEY", "ak_env")
    monkeypatch.setenv("AXONPUSH_CHANNEL_ID", "ch_env")
    provider = TracerProvider()
    handle = configure_telemetry(tracer_provider=provider)
    exporter = handle._processor.span_exporter
    assert exporter._endpoint == "https://env.example.com/v1/traces"
    headers = exporter._session.headers
    assert headers["X-API-Key"] == "ak_env"
    assert headers["X-Axonpush-Channel"] == "ch_env"


def test_idempotent_processor_install():
    provider = TracerProvider()
    before = len(provider._active_span_processor._span_processors)
    configure_telemetry(
        base_url="https://api.example.com",
        api_key="ak",
        channel_id="ch",
        tracer_provider=provider,
    )
    configure_telemetry(
        base_url="https://api.example.com",
        api_key="ak",
        channel_id="ch",
        tracer_provider=provider,
    )
    after = len(provider._active_span_processor._span_processors)
    assert after == before + 1


def test_attaches_to_existing_global_provider(monkeypatch):
    from opentelemetry import trace as trace_api

    real = TracerProvider()
    monkeypatch.setattr(trace_api, "get_tracer_provider", lambda: real)
    handle = configure_telemetry(base_url="https://a.co", api_key="ak", channel_id="ch")
    assert handle._provider is real
    assert handle._owns_provider is False


def test_genai_span_attributes(recording_provider):
    provider, exporter = recording_provider
    tracer = provider.get_tracer("t")
    with genai_span(
        tracer, operation="chat", request_model="gpt-4o", system="openai"
    ) as span:
        record_genai_response(
            span,
            response_model="gpt-4o-2024",
            finish_reasons=["stop"],
            input_tokens=10,
            output_tokens=20,
            reasoning_tokens=5,
            cache_read_tokens=3,
        )
    spans = exporter.get_finished_spans()
    assert len(spans) == 1
    s = spans[0]
    assert s.name == "chat gpt-4o"
    attrs = dict(s.attributes)
    assert attrs["gen_ai.operation.name"] == "chat"
    assert attrs["gen_ai.request.model"] == "gpt-4o"
    assert attrs["gen_ai.system"] == "openai"
    assert attrs["gen_ai.provider.name"] == "openai"
    assert attrs["gen_ai.response.model"] == "gpt-4o-2024"
    assert attrs["gen_ai.response.finish_reasons"] == ("stop",)
    assert attrs["gen_ai.usage.input_tokens"] == 10
    assert attrs["gen_ai.usage.output_tokens"] == 20
    assert attrs["gen_ai.usage.reasoning_tokens"] == 5
    assert attrs["gen_ai.usage.cache_read_input_tokens"] == 3


def test_custom_span_name(recording_provider):
    provider, exporter = recording_provider
    tracer = provider.get_tracer("t")
    with genai_span(tracer, operation="chat", request_model="m", name="custom"):
        pass
    assert exporter.get_finished_spans()[0].name == "custom"


def test_content_metadata_only_drops_content(recording_provider):
    provider, exporter = recording_provider
    tracer = provider.get_tracer("t")
    with genai_span(tracer, operation="chat", request_model="m") as span:
        record_genai_content(
            span, prompt="hello", completion="world", content_capture="metadata_only"
        )
    events = exporter.get_finished_spans()[0].events
    assert len(events) == 0


def test_content_full_keeps_content(recording_provider):
    provider, exporter = recording_provider
    tracer = provider.get_tracer("t")
    with genai_span(tracer, operation="chat", request_model="m") as span:
        record_genai_content(
            span, prompt="hello", completion="world", content_capture="full"
        )
    events = exporter.get_finished_spans()[0].events
    names = {e.name for e in events}
    assert names == {"gen_ai.content.prompt", "gen_ai.content.completion"}
    prompt_ev = next(e for e in events if e.name == "gen_ai.content.prompt")
    assert prompt_ev.attributes["prompt"] == "hello"


def test_content_strips_secret_keys(recording_provider):
    provider, exporter = recording_provider
    tracer = provider.get_tracer("t")
    with genai_span(tracer, operation="chat", request_model="m") as span:
        record_genai_content(
            span,
            prompt={"text": "hi", "api_key": "leak"},
            content_capture="full",
        )
    ev = exporter.get_finished_spans()[0].events[0]
    # nested dict is JSON-serialised into the "prompt" attribute
    assert "leak" not in ev.attributes["prompt"]
    assert "[REDACTED]" in ev.attributes["prompt"]


def test_content_policy_from_handle(recording_provider):
    provider, exporter = recording_provider
    handle = configure_telemetry(
        base_url="https://a.co",
        api_key="ak",
        channel_id="ch",
        tracer_provider=provider,
        content_capture="full",
    )
    tracer = provider.get_tracer("t")
    with genai_span(tracer, operation="chat", request_model="m") as span:
        record_genai_content(span, prompt="kept", handle=handle)
    events = exporter.get_finished_spans()[0].events
    assert events[0].attributes["prompt"] == "kept"


def test_flush_and_shutdown():
    provider = TracerProvider()
    handle = configure_telemetry(
        base_url="https://a.co", api_key="ak", channel_id="ch", tracer_provider=provider
    )
    assert handle.flush(100) in (True, False)
    handle.shutdown()
