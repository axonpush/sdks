from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.efficacy_output_body import EfficacyOutputBody
from ...models.error_model import ErrorModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["since"] = since

    params["until"] = until

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/moderation/efficacy",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EfficacyOutputBody | ErrorModel:
    if response.status_code == 200:
        response_200 = EfficacyOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EfficacyOutputBody | ErrorModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
) -> Response[EfficacyOutputBody | ErrorModel]:
    """Guardrail efficacy + latency

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EfficacyOutputBody | ErrorModel]
    """

    kwargs = _get_kwargs(
        since=since,
        until=until,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
) -> EfficacyOutputBody | ErrorModel | None:
    """Guardrail efficacy + latency

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EfficacyOutputBody | ErrorModel
    """

    return sync_detailed(
        client=client,
        since=since,
        until=until,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
) -> Response[EfficacyOutputBody | ErrorModel]:
    """Guardrail efficacy + latency

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EfficacyOutputBody | ErrorModel]
    """

    kwargs = _get_kwargs(
        since=since,
        until=until,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
) -> EfficacyOutputBody | ErrorModel | None:
    """Guardrail efficacy + latency

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EfficacyOutputBody | ErrorModel
    """

    return (
        await asyncio_detailed(
            client=client,
            since=since,
            until=until,
        )
    ).parsed
