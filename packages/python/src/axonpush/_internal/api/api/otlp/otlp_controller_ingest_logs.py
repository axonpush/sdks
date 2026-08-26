from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    idempotency_key: str | Unset = UNSET,
    x_axonpush_channel: str,
    x_axonpush_environment: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    headers["X-Axonpush-Channel"] = x_axonpush_channel

    if not isinstance(x_axonpush_environment, Unset):
        headers["X-Axonpush-Environment"] = x_axonpush_environment

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/logs",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    idempotency_key: str | Unset = UNSET,
    x_axonpush_channel: str,
    x_axonpush_environment: str | Unset = UNSET,
) -> Response[Any]:
    """OTLP/HTTP logs ingest (protobuf or JSON)

    Args:
        idempotency_key (str | Unset):
        x_axonpush_channel (str):
        x_axonpush_environment (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        idempotency_key=idempotency_key,
        x_axonpush_channel=x_axonpush_channel,
        x_axonpush_environment=x_axonpush_environment,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    idempotency_key: str | Unset = UNSET,
    x_axonpush_channel: str,
    x_axonpush_environment: str | Unset = UNSET,
) -> Response[Any]:
    """OTLP/HTTP logs ingest (protobuf or JSON)

    Args:
        idempotency_key (str | Unset):
        x_axonpush_channel (str):
        x_axonpush_environment (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        idempotency_key=idempotency_key,
        x_axonpush_channel=x_axonpush_channel,
        x_axonpush_environment=x_axonpush_environment,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
