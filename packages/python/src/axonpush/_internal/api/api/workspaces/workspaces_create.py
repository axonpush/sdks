from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_workspace import ActivityWorkspace
from ...models.create_input_body import CreateInputBody
from ...models.error_model import ErrorModel
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: CreateInputBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/workspaces",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActivityWorkspace | ErrorModel:
    if response.status_code == 201:
        response_201 = ActivityWorkspace.from_dict(response.json())

        return response_201

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ActivityWorkspace | ErrorModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateInputBody,
) -> Response[ActivityWorkspace | ErrorModel]:
    """Create a workspace for an application, from a full or blank spec

    Args:
        body (CreateInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivityWorkspace | ErrorModel]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateInputBody,
) -> ActivityWorkspace | ErrorModel | None:
    """Create a workspace for an application, from a full or blank spec

    Args:
        body (CreateInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivityWorkspace | ErrorModel
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateInputBody,
) -> Response[ActivityWorkspace | ErrorModel]:
    """Create a workspace for an application, from a full or blank spec

    Args:
        body (CreateInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivityWorkspace | ErrorModel]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateInputBody,
) -> ActivityWorkspace | ErrorModel | None:
    """Create a workspace for an application, from a full or blank spec

    Args:
        body (CreateInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivityWorkspace | ErrorModel
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
