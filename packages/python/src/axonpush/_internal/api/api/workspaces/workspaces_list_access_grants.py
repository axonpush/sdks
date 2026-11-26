from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.grant_list_output_body import GrantListOutputBody
from ...types import UNSET, Response


def _get_kwargs(
    workspace_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspaces/{workspace_id}/access-grants".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | GrantListOutputBody:
    if response.status_code == 200:
        response_200 = GrantListOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | GrantListOutputBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorModel | GrantListOutputBody]:
    """List scoped data-access grants for members and API keys

     A member or API key with any grant sees only records carrying a granted value of a scoping
    attribute, on every read: activity, timeline, catalog, views, series, analytics, summary, health,
    incidents, traces and MCP. Organization-wide telemetry reads are refused for them. Owners and admins
    are never scoped.

    Args:
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | GrantListOutputBody]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorModel | GrantListOutputBody | None:
    """List scoped data-access grants for members and API keys

     A member or API key with any grant sees only records carrying a granted value of a scoping
    attribute, on every read: activity, timeline, catalog, views, series, analytics, summary, health,
    incidents, traces and MCP. Organization-wide telemetry reads are refused for them. Owners and admins
    are never scoped.

    Args:
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | GrantListOutputBody
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorModel | GrantListOutputBody]:
    """List scoped data-access grants for members and API keys

     A member or API key with any grant sees only records carrying a granted value of a scoping
    attribute, on every read: activity, timeline, catalog, views, series, analytics, summary, health,
    incidents, traces and MCP. Organization-wide telemetry reads are refused for them. Owners and admins
    are never scoped.

    Args:
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | GrantListOutputBody]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorModel | GrantListOutputBody | None:
    """List scoped data-access grants for members and API keys

     A member or API key with any grant sees only records carrying a granted value of a scoping
    attribute, on every read: activity, timeline, catalog, views, series, analytics, summary, health,
    incidents, traces and MCP. Organization-wide telemetry reads are refused for them. Owners and admins
    are never scoped.

    Args:
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | GrantListOutputBody
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
        )
    ).parsed
