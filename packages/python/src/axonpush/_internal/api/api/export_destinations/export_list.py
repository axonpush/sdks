from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.list_output_body_4 import ListOutputBody4
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    env_slug: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["envSlug"] = env_slug

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/export-destinations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | ListOutputBody4:
    if response.status_code == 200:
        response_200 = ListOutputBody4.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | ListOutputBody4]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    env_slug: str | Unset = UNSET,
) -> Response[ErrorModel | ListOutputBody4]:
    """List export destinations

    Args:
        env_slug (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ListOutputBody4]
    """

    kwargs = _get_kwargs(
        env_slug=env_slug,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    env_slug: str | Unset = UNSET,
) -> ErrorModel | ListOutputBody4 | None:
    """List export destinations

    Args:
        env_slug (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ListOutputBody4
    """

    return sync_detailed(
        client=client,
        env_slug=env_slug,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    env_slug: str | Unset = UNSET,
) -> Response[ErrorModel | ListOutputBody4]:
    """List export destinations

    Args:
        env_slug (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ListOutputBody4]
    """

    kwargs = _get_kwargs(
        env_slug=env_slug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    env_slug: str | Unset = UNSET,
) -> ErrorModel | ListOutputBody4 | None:
    """List export destinations

    Args:
        env_slug (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ListOutputBody4
    """

    return (
        await asyncio_detailed(
            client=client,
            env_slug=env_slug,
        )
    ).parsed
