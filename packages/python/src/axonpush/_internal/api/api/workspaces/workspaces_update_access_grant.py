from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_grant import ActivityGrant
from ...models.error_model import ErrorModel
from ...models.grant_update_input_body import GrantUpdateInputBody
from ...types import UNSET, Response


def _get_kwargs(
    workspace_id: str,
    grant_id: str,
    *,
    body: GrantUpdateInputBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/workspaces/{workspace_id}/access-grants/{grant_id}".format(
            workspace_id=quote(str(workspace_id), safe=""),
            grant_id=quote(str(grant_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActivityGrant | ErrorModel:
    if response.status_code == 200:
        response_200 = ActivityGrant.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ActivityGrant | ErrorModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    grant_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GrantUpdateInputBody,
) -> Response[ActivityGrant | ErrorModel]:
    """Replace a grant's allowed values

    Args:
        workspace_id (str):
        grant_id (str):
        body (GrantUpdateInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivityGrant | ErrorModel]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        grant_id=grant_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    grant_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GrantUpdateInputBody,
) -> ActivityGrant | ErrorModel | None:
    """Replace a grant's allowed values

    Args:
        workspace_id (str):
        grant_id (str):
        body (GrantUpdateInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivityGrant | ErrorModel
    """

    return sync_detailed(
        workspace_id=workspace_id,
        grant_id=grant_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    grant_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GrantUpdateInputBody,
) -> Response[ActivityGrant | ErrorModel]:
    """Replace a grant's allowed values

    Args:
        workspace_id (str):
        grant_id (str):
        body (GrantUpdateInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivityGrant | ErrorModel]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        grant_id=grant_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    grant_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GrantUpdateInputBody,
) -> ActivityGrant | ErrorModel | None:
    """Replace a grant's allowed values

    Args:
        workspace_id (str):
        grant_id (str):
        body (GrantUpdateInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivityGrant | ErrorModel
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            grant_id=grant_id,
            client=client,
            body=body,
        )
    ).parsed
