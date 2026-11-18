"""Sentry SDK integration helper.

Builds a Sentry DSN that points the official ``sentry-sdk`` at the AxonPush
Sentry ingest (``/api/{projectId}/envelope/`` and ``/api/{projectId}/store/``)
and forwards every other ``sentry_sdk.init`` kwarg through.

The DSN key must be a channel-scoped public ingest token (``pt_...``); the
server resolves the org, channel and environment from it and refuses API keys.
Sentry SDKs require an integer project id, so the project segment is a
placeholder derived from the channel id (the same derivation the dashboard
uses) and is not used for routing.

Tested against ``sentry-sdk>=1.40,<3``.

Usage::

    from axonpush.integrations.sentry import install_sentry
    install_sentry(
        public_token="pt_...",
        channel_id="ch_...",
        environment="production",
        release="my-app@1.2.3",
    )

Environment variable fallbacks (when args are omitted):
    - public_token: AXONPUSH_PUBLIC_TOKEN
    - channel_id:   AXONPUSH_CHANNEL_ID
    - host:         AXONPUSH_HOST (default: api.axonpush.xyz)
    - environment:  AXONPUSH_ENVIRONMENT, then SENTRY_ENVIRONMENT, then APP_ENV, then ENV
"""

from __future__ import annotations

import logging
import os
import re
from typing import Any, Optional

logger = logging.getLogger("axonpush.sentry")

_ENV_PRECEDENCE = (
    "AXONPUSH_ENVIRONMENT",
    "SENTRY_ENVIRONMENT",
    "APP_ENV",
    "ENV",
)

_LEADING_HEX = re.compile(r"[0-9a-fA-F]+")


def sentry_project_id(channel_id: int | str | None) -> int:
    """Derive the integer Sentry project id placeholder from a channel id."""
    if channel_id is None:
        return 1
    match = _LEADING_HEX.match(str(channel_id).replace("-", "")[:8])
    return (int(match.group(), 16) if match else 0) or 1


def build_dsn(public_token: str, channel_id: int | str | None, host: str) -> str:
    """Format an AxonPush Sentry DSN from a ``pt_`` public ingest token."""
    _require_public_token(public_token)
    scheme = "http" if host.startswith("localhost") or host.startswith("127.") else "https"
    return f"{scheme}://{public_token}@{host}/{sentry_project_id(channel_id)}"


def _require_public_token(token: str) -> None:
    if not token.startswith("pt_"):
        raise ValueError(
            "Sentry ingest needs a channel-scoped public ingest token (pt_...), "
            "not an API key. Mint one in the dashboard or via /public-ingest-tokens."
        )


def _detect_environment() -> Optional[str]:
    for name in _ENV_PRECEDENCE:
        val = os.getenv(name)
        if val:
            return val
    return None


def install_sentry(
    *,
    public_token: Optional[str] = None,
    channel_id: Optional[int | str] = None,
    host: Optional[str] = None,
    environment: Optional[str] = None,
    release: Optional[str] = None,
    dsn: Optional[str] = None,
    **sentry_init_kwargs: Any,
) -> None:
    """Initialize the Sentry SDK, pointed at AxonPush.

    Args:
        public_token: Channel-scoped public ingest token (``pt_...``). Falls
            back to ``AXONPUSH_PUBLIC_TOKEN``.
        channel_id: Channel the token is scoped to; only used to derive the
            integer project id placeholder. Falls back to ``AXONPUSH_CHANNEL_ID``.
        host: AxonPush host. Falls back to ``AXONPUSH_HOST`` then
            ``api.axonpush.xyz``.
        environment: Deployment environment. Auto-detected from
            ``AXONPUSH_ENVIRONMENT`` / ``SENTRY_ENVIRONMENT`` / ``APP_ENV``
            / ``ENV`` when not provided.
        release: Release tag forwarded to ``sentry_sdk.init``.
        dsn: Fully-formed DSN (as shown in the dashboard). When set, the
            other AxonPush args are ignored.
        **sentry_init_kwargs: Forwarded to ``sentry_sdk.init`` verbatim.

    Raises:
        ImportError: ``sentry-sdk`` is not installed.
        ValueError: No DSN or public token was supplied, or the token is not
            a ``pt_`` public ingest token.
    """
    if "api_key" in sentry_init_kwargs:
        raise ValueError(
            "install_sentry no longer accepts api_key: Sentry ingest refuses API keys. "
            "Pass public_token='pt_...' or the dsn shown in the dashboard."
        )
    try:
        import sentry_sdk
    except ImportError as exc:
        raise ImportError(
            "install_sentry requires sentry-sdk. Install it with `pip install sentry-sdk`.",
        ) from exc

    if dsn is None:
        public_token = public_token or os.getenv("AXONPUSH_PUBLIC_TOKEN")
        if channel_id is None:
            channel_id = os.getenv("AXONPUSH_CHANNEL_ID") or None
        host = host or os.getenv("AXONPUSH_HOST") or "api.axonpush.xyz"
        if not public_token:
            raise ValueError(
                "install_sentry needs a public_token (pt_...) or a fully-formed dsn. "
                "Pass one as an argument or set AXONPUSH_PUBLIC_TOKEN.",
            )
        dsn = build_dsn(public_token, channel_id, host)

    resolved_env = environment if environment is not None else _detect_environment()
    logger.debug(
        "install_sentry: dsn host=%s environment=%s release=%s",
        dsn.rsplit("@", 1)[-1] if "@" in dsn else dsn,
        resolved_env,
        release,
    )

    init_kwargs: dict[str, Any] = {"dsn": dsn, **sentry_init_kwargs}
    if resolved_env is not None:
        init_kwargs.setdefault("environment", resolved_env)
    if release is not None:
        init_kwargs.setdefault("release", release)

    sentry_sdk.init(**init_kwargs)
