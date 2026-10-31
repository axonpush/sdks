"""HTTP transport layer for the AxonPush SDK.

Builds the generated ``AuthenticatedClient`` with httpx event hooks that:

1. inject auth, tenant, environment and trace headers on every outgoing
   request, and
2. convert non-2xx responses into the SDK's :mod:`axonpush.exceptions`
   hierarchy.

Also exposes synchronous and asynchronous retry helpers that re-issue calls
on :class:`~axonpush.exceptions.RetryableError` with exponential backoff and
honour ``Retry-After`` for rate-limit responses.

The retry helpers run each request inside an OpenTelemetry context that
sets both ``suppress_instrumentation`` and ``suppress_http_instrumentation``
keys, so an upstream OTel HTTP instrumentor (httpx, urllib3, aiohttp, ...)
never creates a span for the SDK's own publish/list calls. This avoids the
amplification loop where every published span generates another span which
gets published, and so on.
"""

from __future__ import annotations

import asyncio
import contextvars
from tenacity import (
    Retrying,
    AsyncRetrying,
    retry_if_exception,
    stop_after_attempt,
    stop_before_delay,
    wait_exponential_jitter,
)
import time
from typing import Any, Awaitable, Callable, Iterator, Protocol

import httpx

from axonpush._config import Settings
from axonpush._internal.api.client import AuthenticatedClient
from axonpush._tracing import current_trace
from axonpush.exceptions import (
    APIConnectionError,
    AxonPushError,
    RateLimitError,
    RetryableError,
    from_response,
)

_BACKOFF_SCHEDULE: tuple[float, ...] = (0.25, 0.5, 1.0, 2.0, 4.0)

# Both keys exist across opentelemetry versions; setting both is forward-
# and backward-compatible. Different instrumentors check different keys.
_OTEL_SUPPRESS_KEYS: tuple[str, ...] = (
    "suppress_instrumentation",
    "suppress_http_instrumentation",
)


class _OtelSuppression:
    """Context manager that flags the current OTel context to skip instrumentation.

    Soft-imports ``opentelemetry``; if not installed, this is a no-op.
    HTTP-style instrumentations (httpx, urllib3, aiohttp, ...) check these
    keys before creating a span and skip when set.
    """

    __slots__ = ("_tokens",)

    def __init__(self) -> None:
        self._tokens: list[Any] = []

    def __enter__(self) -> "_OtelSuppression":
        try:
            from opentelemetry import context as _otel_context
        except ImportError:
            return self
        for key in _OTEL_SUPPRESS_KEYS:
            self._tokens.append(_otel_context.attach(_otel_context.set_value(key, True)))
        return self

    def __exit__(self, *exc: Any) -> None:
        if not self._tokens:
            return
        try:
            from opentelemetry import context as _otel_context
        except ImportError:
            self._tokens.clear()
            return
        for tok in reversed(self._tokens):
            _otel_context.detach(tok)
        self._tokens.clear()


class _DetailedSyncOp(Protocol):
    def sync_detailed(self, **kwargs: Any) -> Any: ...


class _DetailedAsyncOp(Protocol):
    def asyncio_detailed(self, **kwargs: Any) -> Awaitable[Any]: ...


def _auth_header_name(api_key: str) -> str:
    """Route the credential to its header by prefix.

    ``pt_`` public ingest tokens go on ``X-Public-Token``; everything else
    (``ak_`` API keys) goes on ``x-axonpush-api-key`` (the header the backend
    expects).
    """
    return "X-Public-Token" if api_key.startswith("pt_") else "x-axonpush-api-key"


def _auth_headers(settings: Settings) -> dict[str, str]:
    headers: dict[str, str] = {}
    if settings.api_key is not None:
        key = settings.api_key.get_secret_value()
        headers[_auth_header_name(key)] = key
    if settings.tenant_id is not None:
        headers["x-tenant-id"] = settings.tenant_id
    if settings.environment is not None:
        headers["X-Axonpush-Environment"] = settings.environment
    return headers


def _inject_request_headers(request: httpx.Request) -> None:
    state = _retry_safe.get()
    if state is not None:
        import json

        safe = request.method in ("GET", "HEAD")
        if request.method == "POST":
            try:
                body = json.loads(request.content)
                if request.url.path == "/event":
                    safe = isinstance(body.get("dedupKey"), str) and bool(body["dedupKey"])
                elif request.url.path.startswith("/workspaces/") and request.url.path.endswith(
                    "/observations"
                ):
                    items = body.get("observations")
                    safe = isinstance(items, list) and all(
                        isinstance(item.get("source_event_id"), str) and item["source_event_id"]
                        for item in items
                    )
            except (ValueError, TypeError, AttributeError):
                safe = False
        state[0] = safe
    deadline = _deadline.get()
    if deadline is not None:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise APIConnectionError("AxonPush invocation timed out")
        request.extensions["timeout"] = {
            kind: remaining for kind in ("connect", "read", "write", "pool")
        }
    ctx = current_trace()
    if ctx is not None:
        span_id = ctx.next_span_id()
        request.headers["X-Axonpush-Trace-Id"] = ctx.trace_id
        request.headers["X-Axonpush-Span-Id"] = span_id
        request.headers["traceparent"] = ctx.traceparent(span_id)
    if not request.content:
        request.headers.pop("Content-Type", None)


async def _async_inject_request_headers(request: httpx.Request) -> None:
    _inject_request_headers(request)


class _DeadlineStream(httpx.SyncByteStream):
    def __init__(self, stream: httpx.SyncByteStream, deadline: float) -> None:
        self.stream, self.deadline = stream, deadline

    def __iter__(self) -> Iterator[bytes]:
        try:
            for chunk in self.stream:
                if time.monotonic() >= self.deadline:
                    raise httpx.ReadTimeout("AxonPush invocation timed out")
                yield chunk
        finally:
            self.stream.close()

    def close(self) -> None:
        self.stream.close()


def _raise_for_status(response: httpx.Response) -> None:
    deadline = _deadline.get()
    if deadline is not None and isinstance(response.stream, httpx.SyncByteStream):
        response.stream = _DeadlineStream(response.stream, deadline)
    if response.is_success:
        return
    response.read()
    raise from_response(response)


async def _async_raise_for_status(response: httpx.Response) -> None:
    if response.is_success:
        return
    await response.aread()
    raise from_response(response)


def _base_url_str(settings: Settings) -> str:
    return str(settings.base_url).rstrip("/")


def _make_timeout(settings: Settings) -> httpx.Timeout:
    return httpx.Timeout(settings.timeout, connect=min(5.0, settings.timeout))


def build_sync_client(settings: Settings) -> AuthenticatedClient:
    """Construct an :class:`AuthenticatedClient` for synchronous use.

    Args:
        settings: Effective SDK configuration.

    Returns:
        A generated ``AuthenticatedClient`` whose underlying
        :class:`httpx.Client` has request and response event hooks attached
        for header injection and error mapping.
    """
    headers = _auth_headers(settings)
    base_url = _base_url_str(settings)
    httpx_client = httpx.Client(
        base_url=base_url,
        headers=headers,
        follow_redirects=False,
        timeout=_make_timeout(settings),
        event_hooks={
            "request": [_inject_request_headers],
            "response": [_raise_for_status],
        },
    )
    api_key = settings.api_key.get_secret_value() if settings.api_key is not None else ""
    client = AuthenticatedClient(
        base_url=base_url,
        token=api_key,
        prefix="",
        auth_header_name=_auth_header_name(api_key),
        raise_on_unexpected_status=False,
        timeout=_make_timeout(settings),
        headers=headers,
    )
    client.set_httpx_client(httpx_client)
    return client


def build_async_client(settings: Settings) -> AuthenticatedClient:
    """Construct an :class:`AuthenticatedClient` for asynchronous use.

    Args:
        settings: Effective SDK configuration.

    Returns:
        A generated ``AuthenticatedClient`` whose underlying
        :class:`httpx.AsyncClient` has the same hooks installed as the sync
        variant.
    """
    headers = _auth_headers(settings)
    base_url = _base_url_str(settings)
    httpx_client = httpx.AsyncClient(
        base_url=base_url,
        headers=headers,
        follow_redirects=False,
        timeout=_make_timeout(settings),
        event_hooks={
            "request": [_async_inject_request_headers],
            "response": [_async_raise_for_status],
        },
    )
    api_key = settings.api_key.get_secret_value() if settings.api_key is not None else ""
    client = AuthenticatedClient(
        base_url=base_url,
        token=api_key,
        prefix="",
        auth_header_name=_auth_header_name(api_key),
        raise_on_unexpected_status=False,
        timeout=_make_timeout(settings),
        headers=headers,
    )
    client.set_async_httpx_client(httpx_client)
    return client


def _backoff_for(attempt: int, error: AxonPushError) -> float:
    # Retained for callers/tests inspecting the nominal shared ladder.
    if isinstance(error, RateLimitError) and error.retry_after is not None:
        return max(0.0, float(error.retry_after))
    return _BACKOFF_SCHEDULE[min(attempt, len(_BACKOFF_SCHEDULE) - 1)]


def _wrap_transport_error(exc: BaseException) -> APIConnectionError:
    return APIConnectionError(f"Failed to connect to AxonPush API: {exc}")


_deadline: contextvars.ContextVar[float | None] = contextvars.ContextVar(
    "axonpush_deadline", default=None
)
_retry_safe: contextvars.ContextVar[list[bool] | None] = contextvars.ContextVar(
    "axonpush_retry_safe", default=None
)
_jitter = wait_exponential_jitter(initial=0.25, max=4, jitter=0.25)


def _retry_wait(state: Any) -> float:
    error = state.outcome.exception()
    if isinstance(error, RateLimitError) and error.retry_after is not None:
        return error.retry_after
    return _jitter(state)


def _retry_options(max_retries: int, timeout: float) -> dict[str, Any]:
    if isinstance(max_retries, bool) or not isinstance(max_retries, int) or max_retries < 0:
        raise ValueError("max_retries must be a nonnegative integer")
    return dict(
        retry=retry_if_exception(_should_retry),
        stop=stop_after_attempt(max_retries + 1) | stop_before_delay(timeout),
        wait=_retry_wait,
        reraise=True,
    )


def _should_retry(error: BaseException) -> bool:
    safety = _retry_safe.get()
    return safety is not None and safety[0] and isinstance(error, RetryableError)


def call_with_retries_sync(
    op: Any,
    *,
    max_retries: int,
    timeout: float = 30.0,
    retry_safe: bool = False,
    sleep: Callable[[float], None] = time.sleep,
    **kwargs: Any,
) -> Any:
    safety_token = _retry_safe.set([retry_safe])
    token = _deadline.set(time.monotonic() + timeout)
    try:
        for attempt in Retrying(**_retry_options(max_retries, timeout), sleep=sleep):
            with attempt, _OtelSuppression():
                try:
                    result = op.sync_detailed(**kwargs)
                    if time.monotonic() >= (_deadline.get() or float("inf")):
                        raise APIConnectionError("AxonPush invocation timed out")
                    return result
                except (httpx.TransportError, httpx.RequestError) as exc:
                    raise _wrap_transport_error(exc) from exc
    finally:
        _deadline.reset(token)
        _retry_safe.reset(safety_token)


async def call_with_retries_async(
    op: Any,
    *,
    max_retries: int,
    timeout: float = 30.0,
    retry_safe: bool = False,
    sleep: Callable[[float], Awaitable[None]] = asyncio.sleep,
    **kwargs: Any,
) -> Any:
    async def run() -> Any:
        async for attempt in AsyncRetrying(**_retry_options(max_retries, timeout), sleep=sleep):
            with attempt, _OtelSuppression():
                try:
                    result = await op.asyncio_detailed(**kwargs)
                    if time.monotonic() >= (_deadline.get() or float("inf")):
                        raise APIConnectionError("AxonPush invocation timed out")
                    return result
                except (httpx.TransportError, httpx.RequestError) as exc:
                    raise _wrap_transport_error(exc) from exc

    safety_token = _retry_safe.set([retry_safe])
    token = _deadline.set(time.monotonic() + timeout)
    try:
        return await asyncio.wait_for(run(), timeout)
    except asyncio.TimeoutError as exc:
        raise APIConnectionError("AxonPush invocation timed out") from exc
    finally:
        _deadline.reset(token)
        _retry_safe.reset(safety_token)


__all__ = [
    "build_async_client",
    "build_sync_client",
    "call_with_retries_async",
    "call_with_retries_sync",
]
