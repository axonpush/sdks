"""OTel-native telemetry for AxonPush.

Emits real OTLP over HTTP to the AxonPush ingest endpoint
(``POST {base}/v1/traces``), routed by the ``X-Axonpush-Channel`` header
and authed by ``X-API-Key``. Spans follow the GenAI semantic conventions
so they are portable to any OTLP backend, not just AxonPush.

Unlike :mod:`axonpush.integrations.otel` (which converts spans to
proprietary ``app.span`` events through the events API), this module
reuses the application's own :class:`~opentelemetry.sdk.trace.TracerProvider`
and attaches a :class:`BatchSpanProcessor` that ships OTLP directly. The
``/event`` exporter stays as a fallback for callers who want channel
fan-out on the events plane.

Requires the ``otel`` extra::

    pip install axonpush[otel]

Usage::

    from axonpush.telemetry import configure_telemetry, genai_span, record_genai_response

    handle = configure_telemetry(service_name="my-agent", environment="prod")
    tracer = handle.tracer()

    with genai_span(tracer, operation="chat", request_model="gpt-4o", system="openai") as span:
        ...  # call the model
        record_genai_response(span, response_model="gpt-4o", input_tokens=12, output_tokens=48)

    handle.flush()  # serverless: call per invocation

On AWS Lambda the batch processor's ``atexit`` hook is unreliable because
the container is frozen between invocations. Detect the environment via
``AWS_LAMBDA_FUNCTION_NAME`` and call :meth:`TelemetryHandle.flush` at the
end of each invocation.
"""

from __future__ import annotations

import json
import logging as _stdlib_logging
import os
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Iterator, Optional, Sequence, Set, Tuple

try:
    from opentelemetry import trace as _trace_api
    from opentelemetry.exporter.otlp.proto.http import Compression
    from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
    from opentelemetry.sdk.resources import Resource
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor
except ImportError:
    raise ImportError(
        "axonpush.telemetry requires the 'otel' extra. Install it with: pip install axonpush[otel]"
    ) from None

from axonpush._config import ContentCaptureMode, Settings
from axonpush._redaction import redact_telemetry
from axonpush.integrations._publisher import detect_serverless

if TYPE_CHECKING:
    from opentelemetry.trace import Span, Tracer

__all__ = [
    "TelemetryHandle",
    "configure_telemetry",
    "genai_span",
    "record_genai_content",
    "record_genai_response",
]

_internal_logger = _stdlib_logging.getLogger("axonpush")

#: Guards against attaching our processor to the same (endpoint, channel)
#: twice — e.g. when ``configure_telemetry`` is called from multiple modules
#: that all reuse the global provider.
_INSTALLED: Set[Tuple[str, Optional[str]]] = set()


class TelemetryHandle:
    """Handle over the span processor installed by :func:`configure_telemetry`."""

    def __init__(
        self,
        *,
        provider: TracerProvider,
        processor: BatchSpanProcessor,
        owns_provider: bool,
        settings: Settings,
    ) -> None:
        self._provider = provider
        self._processor = processor
        self._owns_provider = owns_provider
        self._settings = settings

    def flush(self, timeout_ms: int = 2000) -> bool:
        """Block until buffered spans are exported, or until ``timeout_ms``.

        Returns ``True`` if the flush completed within the timeout. Call this
        at the end of each invocation on serverless platforms where the
        container is frozen between calls.
        """
        return bool(self._processor.force_flush(timeout_ms))

    def shutdown(self) -> None:
        """Flush and stop the processor. Idempotent."""
        self._processor.shutdown()  # type: ignore[no-untyped-call]

    def tracer(self, name: str = "axonpush") -> "Tracer":
        """Return a tracer from the underlying provider."""
        return self._provider.get_tracer(name)


def configure_telemetry(
    *,
    base_url: Optional[str] = None,
    api_key: Optional[str] = None,
    channel_id: Optional[str] = None,
    service_name: Optional[str] = None,
    environment: Optional[str] = None,
    service_version: Optional[str] = None,
    tracer_provider: Optional[TracerProvider] = None,
    content_capture: ContentCaptureMode = "metadata_only",
    redact_keys: Optional[Sequence[str]] = None,
) -> TelemetryHandle:
    """Install an OTLP span processor that ships GenAI spans to AxonPush.

    Resolution order for ``base_url`` / ``api_key`` / ``channel_id`` is
    argument, then the matching ``AXONPUSH_*`` environment variable.

    Provider selection:
        * ``tracer_provider`` given — attach to it.
        * global provider is already a real SDK ``TracerProvider`` — attach
          our processor to it (never replace).
        * otherwise — create a new provider with a resource describing the
          service and set it as the global provider.

    The returned :class:`TelemetryHandle` carries the ``content_capture`` and
    ``redact_keys`` policy for use by :func:`record_genai_content`.
    """
    settings_kwargs: dict[str, Any] = {
        "content_capture_mode": content_capture,
        "redact_keys": list(redact_keys) if redact_keys is not None else [],
    }
    if base_url is not None:
        settings_kwargs["base_url"] = base_url
    if api_key is not None:
        settings_kwargs["api_key"] = api_key
    settings = Settings(**settings_kwargs)
    base = str(settings.base_url).rstrip("/")
    resolved_api_key = settings.api_key.get_secret_value() if settings.api_key else None
    resolved_channel = channel_id or os.environ.get("AXONPUSH_CHANNEL_ID")
    endpoint = f"{base}/v1/traces"

    provider, owns_provider = _resolve_provider(
        tracer_provider,
        service_name=service_name,
        environment=environment,
        service_version=service_version,
    )

    processor = _install_processor(
        provider,
        endpoint=endpoint,
        api_key=resolved_api_key,
        channel_id=resolved_channel,
    )

    if detect_serverless() is not None:
        _internal_logger.info(
            "AxonPush telemetry detected a serverless host. The batch "
            "processor's atexit flush is unreliable when the container is "
            "frozen — call handle.flush() at the end of each invocation."
        )

    return TelemetryHandle(
        provider=provider,
        processor=processor,
        owns_provider=owns_provider,
        settings=settings,
    )


def _resolve_provider(
    tracer_provider: Optional[TracerProvider],
    *,
    service_name: Optional[str],
    environment: Optional[str],
    service_version: Optional[str],
) -> Tuple[TracerProvider, bool]:
    if tracer_provider is not None:
        return tracer_provider, False

    current = _trace_api.get_tracer_provider()
    if isinstance(current, TracerProvider):
        return current, False

    attrs: dict[str, Any] = {}
    if service_name is not None:
        attrs["service.name"] = service_name
    if environment is not None:
        attrs["deployment.environment.name"] = environment
    if service_version is not None:
        attrs["service.version"] = service_version
    provider = TracerProvider(resource=Resource.create(attrs))
    _trace_api.set_tracer_provider(provider)
    return provider, True


def _install_processor(
    provider: TracerProvider,
    *,
    endpoint: str,
    api_key: Optional[str],
    channel_id: Optional[str],
) -> BatchSpanProcessor:
    key = (endpoint, channel_id)
    headers: dict[str, str] = {}
    if api_key is not None:
        headers["X-API-Key"] = api_key
    if channel_id is not None:
        headers["X-Axonpush-Channel"] = channel_id

    exporter = OTLPSpanExporter(
        endpoint=endpoint,
        headers=headers,
        compression=Compression.Gzip,
    )
    processor = BatchSpanProcessor(exporter)
    if key not in _INSTALLED:
        provider.add_span_processor(processor)
        _INSTALLED.add(key)
    else:
        _internal_logger.debug(
            "AxonPush telemetry already installed for %s; skipping duplicate processor.",
            key,
        )
    return processor


# --- GenAI semantic-convention helpers ------------------------------------


@contextmanager
def genai_span(
    tracer: "Tracer",
    *,
    operation: str,
    request_model: str,
    system: Optional[str] = None,
    agent_name: Optional[str] = None,
    name: Optional[str] = None,
) -> Iterator["Span"]:
    """Start a CLIENT span for a GenAI operation, named per semconv.

    The span name defaults to ``"{operation} {request_model}"``. Sets
    ``gen_ai.operation.name``, ``gen_ai.request.model`` and, when provided,
    ``gen_ai.system`` / ``gen_ai.provider.name`` and ``gen_ai.agent.name``.
    """
    span_name = name or f"{operation} {request_model}"
    attributes: dict[str, Any] = {
        "gen_ai.operation.name": operation,
        "gen_ai.request.model": request_model,
    }
    if system is not None:
        attributes["gen_ai.system"] = system
        attributes["gen_ai.provider.name"] = system
    if agent_name is not None:
        attributes["gen_ai.agent.name"] = agent_name

    with tracer.start_as_current_span(
        span_name, kind=_trace_api.SpanKind.CLIENT, attributes=attributes
    ) as span:
        yield span


def record_genai_response(
    span: "Span",
    *,
    response_model: Optional[str] = None,
    finish_reasons: Optional[Sequence[str]] = None,
    input_tokens: Optional[int] = None,
    output_tokens: Optional[int] = None,
    reasoning_tokens: Optional[int] = None,
    cache_read_tokens: Optional[int] = None,
    cache_write_tokens: Optional[int] = None,
) -> None:
    """Record GenAI response and usage attributes on ``span``."""
    if response_model is not None:
        span.set_attribute("gen_ai.response.model", response_model)
    if finish_reasons is not None:
        span.set_attribute("gen_ai.response.finish_reasons", list(finish_reasons))
    if input_tokens is not None:
        span.set_attribute("gen_ai.usage.input_tokens", input_tokens)
    if output_tokens is not None:
        span.set_attribute("gen_ai.usage.output_tokens", output_tokens)
    if reasoning_tokens is not None:
        span.set_attribute("gen_ai.usage.reasoning_tokens", reasoning_tokens)
    if cache_read_tokens is not None:
        span.set_attribute("gen_ai.usage.cache_read_input_tokens", cache_read_tokens)
    if cache_write_tokens is not None:
        span.set_attribute("gen_ai.usage.cache_write_input_tokens", cache_write_tokens)


def record_genai_content(
    span: "Span",
    *,
    prompt: Optional[Any] = None,
    completion: Optional[Any] = None,
    handle: Optional[TelemetryHandle] = None,
    content_capture: ContentCaptureMode = "metadata_only",
    redact_keys: Optional[Sequence[str]] = None,
) -> None:
    """Emit prompt / completion as span events, gated by the capture policy.

    Content is emitted as span *events* (``gen_ai.content.prompt`` /
    ``gen_ai.content.completion``) rather than attributes so large payloads
    don't inflate the span's attribute set. Redaction follows
    :func:`axonpush._redaction.redact_telemetry`: ``metadata_only`` drops
    content outright, ``redacted`` keeps short previews, ``full`` keeps it —
    and credential-shaped keys are always stripped regardless of mode.

    The policy is taken from ``handle`` when given, else from the
    ``content_capture`` / ``redact_keys`` arguments.
    """
    settings = _policy_settings(handle, content_capture, redact_keys)
    if settings.content_capture_mode == "metadata_only":
        return

    if prompt is not None:
        redacted = redact_telemetry({"prompt": prompt}, settings)
        span.add_event("gen_ai.content.prompt", attributes=_flatten(redacted))
    if completion is not None:
        redacted = redact_telemetry({"completion": completion}, settings)
        span.add_event("gen_ai.content.completion", attributes=_flatten(redacted))


def _policy_settings(
    handle: Optional[TelemetryHandle],
    content_capture: ContentCaptureMode,
    redact_keys: Optional[Sequence[str]],
) -> Settings:
    if handle is not None:
        return handle._settings
    return Settings(
        content_capture_mode=content_capture,
        redact_keys=list(redact_keys) if redact_keys is not None else [],
    )


def _flatten(value: Any) -> dict[str, Any]:
    """Coerce a redacted value into span-event attributes.

    OTel span-event attributes must be flat primitives (or homogeneous
    sequences). Nested structures are serialised to a string so they survive
    the OTLP boundary without being dropped by the SDK.
    """
    out: dict[str, Any] = {}
    if isinstance(value, dict):
        for key, item in value.items():
            k = str(key)
            if isinstance(item, (str, bool, int, float)):
                out[k] = item
            elif isinstance(item, (list, tuple)) and all(
                isinstance(x, (str, bool, int, float)) for x in item
            ):
                out[k] = list(item)
            else:
                out[k] = json.dumps(item, default=str)
    else:
        out["value"] = value if isinstance(value, (str, bool, int, float)) else str(value)
    return out
