from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activate_draft_input_body import ActivateDraftInputBody
from ...models.activate_draft_output_body import ActivateDraftOutputBody
from ...models.error_model import ErrorModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: str,
    *,
    body: ActivateDraftInputBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/workspaces/{workspace_id}/draft/activate".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActivateDraftOutputBody | ErrorModel:
    if response.status_code == 200:
        response_200 = ActivateDraftOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ActivateDraftOutputBody | ErrorModel]:
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
    body: ActivateDraftInputBody | Unset = UNSET,
) -> Response[ActivateDraftOutputBody | ErrorModel]:
    """Save the draft as a revision and rebuild projections with it; the draft is then cleared

     Fails with 422 listing the issues when the draft has validation errors. Projections rebuild in the
    background; the workspace's requestedRevision shows progress until it becomes the activeRevision.

    Args:
        workspace_id (str):
        body (ActivateDraftInputBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivateDraftOutputBody | ErrorModel]
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
    body: ActivateDraftInputBody | Unset = UNSET,
) -> ActivateDraftOutputBody | ErrorModel | None:
    """Save the draft as a revision and rebuild projections with it; the draft is then cleared

     Fails with 422 listing the issues when the draft has validation errors. Projections rebuild in the
    background; the workspace's requestedRevision shows progress until it becomes the activeRevision.

    Args:
        workspace_id (str):
        body (ActivateDraftInputBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivateDraftOutputBody | ErrorModel
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
    body: ActivateDraftInputBody | Unset = UNSET,
) -> Response[ActivateDraftOutputBody | ErrorModel]:
    """Save the draft as a revision and rebuild projections with it; the draft is then cleared

     Fails with 422 listing the issues when the draft has validation errors. Projections rebuild in the
    background; the workspace's requestedRevision shows progress until it becomes the activeRevision.

    Args:
        workspace_id (str):
        body (ActivateDraftInputBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivateDraftOutputBody | ErrorModel]
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
    body: ActivateDraftInputBody | Unset = UNSET,
) -> ActivateDraftOutputBody | ErrorModel | None:
    """Save the draft as a revision and rebuild projections with it; the draft is then cleared

     Fails with 422 listing the issues when the draft has validation errors. Projections rebuild in the
    background; the workspace's requestedRevision shows progress until it becomes the activeRevision.

    Args:
        workspace_id (str):
        body (ActivateDraftInputBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivateDraftOutputBody | ErrorModel
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            body=body,
        )
    ).parsed
