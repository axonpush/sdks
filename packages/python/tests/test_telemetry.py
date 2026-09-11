"""Tests for the OTel-native ``axonpush.telemetry`` module.

These run without a live backend or the full stack: a tiny stdlib
``http.server`` on a background thread stands in for the AxonPush OTLP
collector, captures the request headers + body, and the exported spans are
decoded (protobuf via ``opentelemetry-proto`` or JSON, whichever the SDK
sends) and asserted against the OTel GenAI semantic conventions.

The whole module skips cleanly until the telemetry runtime API is present, so
it can live in the tree while that module is built in parallel.
"""

from __future__ import annotations

import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any, Dict, List, Optional, Tuple

import pytest

# --- import gate: skip the whole file until the runtime API lands -----------

telemetry = pytest.importorskip("axonpush.telemetry")

for _attr in (
    "configure_telemetry",
    "genai_span",
    "record_genai_response",
    "record_genai_content",
):
    if not hasattr(telemetry, _attr):
        pytest.skip(
            f"axonpush.telemetry.{_attr} not implemented yet",
            allow_module_level=True,
        )

configure_telemetry = telemetry.configure_telemetry
genai_span = telemetry.genai_span
record_genai_response = telemetry.record_genai_response
record_genai_content = telemetry.record_genai_content


@pytest.fixture(autouse=True)
def _reset_installed_registry():
    """Reset the per-endpoint processor dedup set around every test.

    ``configure_telemetry`` dedupes span processors via
    ``telemetry._INSTALLED`` (keyed on endpoint + channel). Clearing it keeps
    the idempotency assertions honest regardless of test ordering. Tests pass an
    explicit ``tracer_provider`` so they never touch the process-wide global.
    """
    installed = getattr(telemetry, "_INSTALLED", None)
    if installed is not None:
        installed.clear()
    try:
        yield
    finally:
        if installed is not None:
            installed.clear()


def _new_provider():
    from opentelemetry.sdk.trace import TracerProvider

    return TracerProvider()


# --- mock OTLP collector ----------------------------------------------------


class _Capture:
    def __init__(self) -> None:
        self.requests: List[Tuple[Dict[str, str], bytes]] = []
        self._lock = threading.Lock()

    def add(self, headers: Dict[str, str], body: bytes) -> None:
        with self._lock:
            self.requests.append((headers, body))

    def snapshot(self) -> List[Tuple[Dict[str, str], bytes]]:
        with self._lock:
            return list(self.requests)


def _make_handler(capture: _Capture) -> type[BaseHTTPRequestHandler]:
    class Handler(BaseHTTPRequestHandler):
        def do_POST(self) -> None:  # noqa: N802
            length = int(self.headers.get("Content-Length", "0"))
            body = self.rfile.read(length) if length else b""
            if self.headers.get("Content-Encoding", "").lower() == "gzip" and body:
                import gzip

                body = gzip.decompress(body)
            headers = {k.lower(): v for k, v in self.headers.items()}
            if self.path.rstrip("/").endswith("/v1/traces"):
                capture.add(headers, body)
                self.send_response(200)
                self.send_header("Content-Type", "application/x-protobuf")
                self.end_headers()
                self.wfile.write(b"")
            else:
                self.send_response(404)
                self.end_headers()

        def log_message(self, *args: Any) -> None:  # silence stderr noise
            return

    return Handler


@pytest.fixture()
def otlp_server():
    capture = _Capture()
    server = ThreadingHTTPServer(("127.0.0.1", 0), _make_handler(capture))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    host, port = server.server_address[0], server.server_address[1]
    base_url = f"http://{host}:{port}"
    try:
        yield base_url, capture
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


# --- OTLP payload decoding (protobuf or JSON) -------------------------------


def _decode_spans(body: bytes) -> List[Dict[str, Any]]:
    """Return a normalized list of spans from an OTLP ExportTraceServiceRequest.

    Each span dict has: ``name``, ``attributes`` (dict), ``events`` (list of
    ``{name, attributes}``). Handles both protobuf and JSON encodings.
    """
    text = body.lstrip()
    if text[:1] in (b"{", b"["):
        return _decode_json(json.loads(body))
    return _decode_protobuf(body)


def _av_to_py(v: Any) -> Any:
    # OTLP AnyValue (proto or JSON dict) -> python
    if isinstance(v, dict):
        for k in ("stringValue", "boolValue", "intValue", "doubleValue"):
            if k in v:
                return v[k]
        if "arrayValue" in v:
            return [_av_to_py(x) for x in v["arrayValue"].get("values", [])]
        return v
    return v


def _decode_json(doc: Dict[str, Any]) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for rs in doc.get("resourceSpans", []):
        for ss in rs.get("scopeSpans", rs.get("instrumentationLibrarySpans", [])):
            for sp in ss.get("spans", []):
                attrs = {
                    a["key"]: _av_to_py(a["value"])
                    for a in sp.get("attributes", [])
                }
                events = [
                    {
                        "name": ev.get("name"),
                        "attributes": {
                            a["key"]: _av_to_py(a["value"])
                            for a in ev.get("attributes", [])
                        },
                    }
                    for ev in sp.get("events", [])
                ]
                out.append(
                    {"name": sp.get("name"), "attributes": attrs, "events": events}
                )
    return out


def _proto_attrs(attributes: Any) -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    for kv in attributes:
        val = kv.value
        if val.HasField("string_value"):
            result[kv.key] = val.string_value
        elif val.HasField("bool_value"):
            result[kv.key] = val.bool_value
        elif val.HasField("int_value"):
            result[kv.key] = val.int_value
        elif val.HasField("double_value"):
            result[kv.key] = val.double_value
        elif val.HasField("array_value"):
            result[kv.key] = [_proto_any(x) for x in val.array_value.values]
        else:
            result[kv.key] = None
    return result


def _proto_any(val: Any) -> Any:
    if val.HasField("string_value"):
        return val.string_value
    if val.HasField("bool_value"):
        return val.bool_value
    if val.HasField("int_value"):
        return val.int_value
    if val.HasField("double_value"):
        return val.double_value
    return None


def _decode_protobuf(body: bytes) -> List[Dict[str, Any]]:
    from opentelemetry.proto.collector.trace.v1.trace_service_pb2 import (
        ExportTraceServiceRequest,
    )

    req = ExportTraceServiceRequest()
    req.ParseFromString(body)
    out: List[Dict[str, Any]] = []
    for rs in req.resource_spans:
        for ss in rs.scope_spans:
            for sp in ss.spans:
                events = [
                    {"name": ev.name, "attributes": _proto_attrs(ev.attributes)}
                    for ev in sp.events
                ]
                out.append(
                    {
                        "name": sp.name,
                        "attributes": _proto_attrs(sp.attributes),
                        "events": events,
                    }
                )
    return out


def _all_spans(capture: _Capture) -> List[Dict[str, Any]]:
    spans: List[Dict[str, Any]] = []
    for _headers, body in capture.snapshot():
        if body:
            spans.extend(_decode_spans(body))
    return spans


def _emit_one_span(
    base_url: str,
    *,
    content_capture: str = "metadata_only",
    prompt: Optional[str] = "secret-ish prompt text",
    completion: Optional[str] = "hi",
    redact_keys: Optional[List[str]] = None,
):
    handle = configure_telemetry(
        base_url=base_url,
        api_key="ak_test",
        channel_id="ch_test",
        service_name="test-svc",
        content_capture=content_capture,
        redact_keys=redact_keys,
        tracer_provider=_new_provider(),
    )
    try:
        tracer = handle.tracer("axonpush-test")
        with genai_span(
            tracer,
            operation="chat",
            request_model="gpt-4o",
            system="openai",
        ) as span:
            record_genai_response(
                span,
                response_model="gpt-4o-2024",
                finish_reasons=["stop"],
                input_tokens=11,
                output_tokens=3,
                reasoning_tokens=2,
                cache_read_tokens=5,
            )
            if prompt is not None or completion is not None:
                # policy comes from the handle (content_capture + redact_keys)
                record_genai_content(
                    span, prompt=prompt, completion=completion, handle=handle
                )
        assert handle.flush(timeout_ms=5000) is True
    finally:
        handle.shutdown()


# --- tests ------------------------------------------------------------------


def test_exports_genai_span_with_semconv_and_auth_headers(otlp_server):
    base_url, capture = otlp_server
    _emit_one_span(base_url)

    reqs = capture.snapshot()
    assert reqs, "collector received no OTLP request"

    # headers: X-API-Key + X-Axonpush-Channel present on every request
    for headers, _body in reqs:
        assert headers.get("x-api-key") == "ak_test"
        assert headers.get("x-axonpush-channel") == "ch_test"

    spans = _all_spans(capture)
    assert len(spans) == 1, f"expected exactly one span, got {len(spans)}"
    attrs = spans[0]["attributes"]

    assert attrs.get("gen_ai.operation.name") == "chat"
    assert attrs.get("gen_ai.request.model") == "gpt-4o"
    assert int(attrs.get("gen_ai.usage.input_tokens")) == 11
    assert int(attrs.get("gen_ai.usage.output_tokens")) == 3


def test_metadata_only_does_not_leak_prompt_text(otlp_server):
    base_url, capture = otlp_server
    _emit_one_span(base_url, content_capture="metadata_only")

    # raw bytes must not carry the sensitive prompt content
    for _headers, body in capture.snapshot():
        assert b"secret-ish prompt text" not in body

    spans = _all_spans(capture)
    for sp in spans:
        for ev in sp["events"]:
            for v in ev["attributes"].values():
                assert "secret-ish prompt text" not in str(v)


def test_full_capture_includes_prompt_text(otlp_server):
    base_url, capture = otlp_server
    _emit_one_span(base_url, content_capture="full")

    joined = b"".join(body for _h, body in capture.snapshot())
    assert b"secret-ish prompt text" in joined, (
        "content_capture='full' should include the raw prompt text"
    )


def test_redacted_capture_previews_and_truncates_long_content(otlp_server):
    """``redacted`` keeps a recognisable preview but drops the long tail."""
    base_url, capture = otlp_server
    tail = "LEAK_TAIL_SENTINEL"
    long_prompt = ("head " * 100) + tail  # well over the 256-char preview bound
    _emit_one_span(base_url, content_capture="redacted", prompt=long_prompt)

    spans = _all_spans(capture)
    content_events = [ev for sp in spans for ev in sp["events"]]
    assert content_events, "redacted mode should still emit content span events"

    # the tail past the preview cutoff must not leak
    for _headers, body in capture.snapshot():
        assert tail.encode() not in body


def test_configure_telemetry_is_idempotent(otlp_server):
    """Configuring twice for the same endpoint/channel must not double-export."""
    base_url, capture = otlp_server
    provider = _new_provider()

    h1 = configure_telemetry(
        base_url=base_url,
        api_key="ak_test",
        channel_id="ch_test",
        service_name="test-svc",
        content_capture="metadata_only",
        tracer_provider=provider,
    )
    h2 = configure_telemetry(
        base_url=base_url,
        api_key="ak_test",
        channel_id="ch_test",
        service_name="test-svc",
        content_capture="metadata_only",
        tracer_provider=provider,
    )
    try:
        tracer = h2.tracer("axonpush-test")
        with genai_span(tracer, operation="chat", request_model="gpt-4o"):
            pass
        assert h2.flush(timeout_ms=5000) is True
        h1.flush(timeout_ms=5000)
    finally:
        h2.shutdown()
        h1.shutdown()

    spans = _all_spans(capture)
    matching = [s for s in spans if s["attributes"].get("gen_ai.request.model") == "gpt-4o"]
    assert len(matching) == 1, (
        f"span exported {len(matching)} times; span processor double-registered"
    )
