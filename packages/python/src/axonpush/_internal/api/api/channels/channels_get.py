from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.channel_dto import ChannelDTO
from ...models.error_model import ErrorModel
from ...types import UNSET, Response


def _get_kwargs(
    app_id: str,
    channel_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/apps/{app_id}/channels/{channel_id}".format(
            app_id=quote(str(app_id), safe=""),
            channel_id=quote(str(channel_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ChannelDTO | ErrorModel:
    if response.status_code == 200:
        response_200 = ChannelDTO.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ChannelDTO | ErrorModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ChannelDTO | ErrorModel]:
    """Get a channel

    Args:
        app_id (str):
        channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChannelDTO | ErrorModel]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        channel_id=channel_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ChannelDTO | ErrorModel | None:
    """Get a channel

    Args:
        app_id (str):
        channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChannelDTO | ErrorModel
    """

    return sync_detailed(
        app_id=app_id,
        channel_id=channel_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ChannelDTO | ErrorModel]:
    """Get a channel

    Args:
        app_id (str):
        channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChannelDTO | ErrorModel]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        channel_id=channel_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ChannelDTO | ErrorModel | None:
    """Get a channel

    Args:
        app_id (str):
        channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChannelDTO | ErrorModel
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            channel_id=channel_id,
            client=client,
        )
    ).parsed
