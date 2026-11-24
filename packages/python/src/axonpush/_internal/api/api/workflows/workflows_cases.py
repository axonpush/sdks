from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cases_output_body import CasesOutputBody
from ...models.error_model import ErrorModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: str,
    *,
    environment: str | Unset = UNSET,
    workflow: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["environment"] = environment

    params["workflow"] = workflow

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspaces/{workspace_id}/workflows/cases".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CasesOutputBody | ErrorModel:
    if response.status_code == 200:
        response_200 = CasesOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CasesOutputBody | ErrorModel]:
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
    environment: str | Unset = UNSET,
    workflow: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[CasesOutputBody | ErrorModel]:
    """List business cases; cursor pagination is scoped to workspace and environment

    Args:
        workspace_id (str):
        environment (str | Unset):
        workflow (str | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CasesOutputBody | ErrorModel]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        environment=environment,
        workflow=workflow,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
    workflow: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> CasesOutputBody | ErrorModel | None:
    """List business cases; cursor pagination is scoped to workspace and environment

    Args:
        workspace_id (str):
        environment (str | Unset):
        workflow (str | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CasesOutputBody | ErrorModel
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        environment=environment,
        workflow=workflow,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
    workflow: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[CasesOutputBody | ErrorModel]:
    """List business cases; cursor pagination is scoped to workspace and environment

    Args:
        workspace_id (str):
        environment (str | Unset):
        workflow (str | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CasesOutputBody | ErrorModel]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        environment=environment,
        workflow=workflow,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
    workflow: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> CasesOutputBody | ErrorModel | None:
    """List business cases; cursor pagination is scoped to workspace and environment

    Args:
        workspace_id (str):
        environment (str | Unset):
        workflow (str | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CasesOutputBody | ErrorModel
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            environment=environment,
            workflow=workflow,
            cursor=cursor,
        )
    ).parsed
