"""Helpers that point an OpenAI or Anthropic client at the AxonPush gateway.

The gateway is a passthrough proxy: keep your provider key where it already
lives and add the AxonPush key in a header. These helpers assemble the base URL
and headers so you do not hand-build them.

    from openai import OpenAI
    from axonpush import gateway

    client = OpenAI(api_key="sk-...", **gateway.openai_kwargs(api_key="ak_...", target="openrouter"))
"""

from __future__ import annotations

from axonpush._config import Settings

_DEFAULT_BASE_URL = str(Settings.model_fields["base_url"].default)


def _root(base_url: str | None) -> str:
    return (base_url or _DEFAULT_BASE_URL).rstrip("/") + "/gw"


def headers(api_key: str, *, target: str | None = None, app: str | None = None) -> dict[str, str]:
    result = {"x-axonpush-api-key": api_key}
    if target:
        result["x-axonpush-target"] = target
    if app:
        result["x-axonpush-app"] = app
    return result


def openai_base_url(base_url: str | None = None) -> str:
    return _root(base_url) + "/openai/v1"


def anthropic_base_url(base_url: str | None = None) -> str:
    return _root(base_url) + "/anthropic"


def openai_kwargs(
    *,
    api_key: str,
    target: str = "openai",
    app: str | None = None,
    base_url: str | None = None,
) -> dict[str, object]:
    return {
        "base_url": openai_base_url(base_url),
        "default_headers": headers(api_key, target=target, app=app),
    }


def anthropic_kwargs(
    *,
    api_key: str,
    app: str | None = None,
    base_url: str | None = None,
) -> dict[str, object]:
    return {
        "base_url": anthropic_base_url(base_url),
        "default_headers": headers(api_key, app=app),
    }
