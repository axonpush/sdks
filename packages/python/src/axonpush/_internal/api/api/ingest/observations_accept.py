from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.workspace_ingest_input_body import WorkspaceIngestInputBody
from ...models.workspace_ingest_output_body import WorkspaceIngestOutputBody
from ...types import UNSET, Response


def _get_kwargs(
    workspace_id: str,
    *,
    body: WorkspaceIngestInputBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/workspaces/{workspace_id}/observations".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | WorkspaceIngestOutputBody:
    if response.status_code == 200:
        response_200 = WorkspaceIngestOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | WorkspaceIngestOutputBody]:
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
    body: WorkspaceIngestInputBody,
) -> Response[ErrorModel | WorkspaceIngestOutputBody]:
    """Store an idempotent metadata-only batch; projection occurs independently

    Args:
        workspace_id (str):
        body (WorkspaceIngestInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | WorkspaceIngestOutputBody]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: WorkspaceIngestInputBody,
) -> ErrorModel | WorkspaceIngestOutputBody | None:
    """Store an idempotent metadata-only batch; projection occurs independently

    Args:
        workspace_id (str):
        body (WorkspaceIngestInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | WorkspaceIngestOutputBody
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: WorkspaceIngestInputBody,
) -> Response[ErrorModel | WorkspaceIngestOutputBody]:
    """Store an idempotent metadata-only batch; projection occurs independently

    Args:
        workspace_id (str):
        body (WorkspaceIngestInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | WorkspaceIngestOutputBody]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: WorkspaceIngestInputBody,
) -> ErrorModel | WorkspaceIngestOutputBody | None:
    """Store an idempotent metadata-only batch; projection occurs independently

    Args:
        workspace_id (str):
        body (WorkspaceIngestInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | WorkspaceIngestOutputBody
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            body=body,
        )
    ).parsed
