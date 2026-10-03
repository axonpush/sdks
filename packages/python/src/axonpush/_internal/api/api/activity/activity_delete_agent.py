from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.workspace_status_output_body import WorkspaceStatusOutputBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: str,
    agent_id: str,
    *,
    environment: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["environment"] = environment

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/workspaces/{workspace_id}/agents/{agent_id}".format(
            workspace_id=quote(str(workspace_id), safe=""),
            agent_id=quote(str(agent_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | WorkspaceStatusOutputBody:
    if response.status_code == 200:
        response_200 = WorkspaceStatusOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | WorkspaceStatusOutputBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
) -> Response[ErrorModel | WorkspaceStatusOutputBody]:
    """Delete agent evidence and install a replay tombstone

    Args:
        workspace_id (str):
        agent_id (str):
        environment (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | WorkspaceStatusOutputBody]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        agent_id=agent_id,
        environment=environment,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
) -> ErrorModel | WorkspaceStatusOutputBody | None:
    """Delete agent evidence and install a replay tombstone

    Args:
        workspace_id (str):
        agent_id (str):
        environment (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | WorkspaceStatusOutputBody
    """

    return sync_detailed(
        workspace_id=workspace_id,
        agent_id=agent_id,
        client=client,
        environment=environment,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
) -> Response[ErrorModel | WorkspaceStatusOutputBody]:
    """Delete agent evidence and install a replay tombstone

    Args:
        workspace_id (str):
        agent_id (str):
        environment (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | WorkspaceStatusOutputBody]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        agent_id=agent_id,
        environment=environment,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
) -> ErrorModel | WorkspaceStatusOutputBody | None:
    """Delete agent evidence and install a replay tombstone

    Args:
        workspace_id (str):
        agent_id (str):
        environment (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | WorkspaceStatusOutputBody
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            agent_id=agent_id,
            client=client,
            environment=environment,
        )
    ).parsed
