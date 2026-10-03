from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_draft_view import ActivityDraftView
from ...models.error_model import ErrorModel
from ...models.ops_input_body import OpsInputBody
from ...types import UNSET, Response


def _get_kwargs(
    workspace_id: str,
    *,
    body: OpsInputBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/workspaces/{workspace_id}/draft/ops".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActivityDraftView | ErrorModel:
    if response.status_code == 200:
        response_200 = ActivityDraftView.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ActivityDraftView | ErrorModel]:
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
    body: OpsInputBody,
) -> Response[ActivityDraftView | ErrorModel]:
    """Apply typed edits to the shared draft atomically

     Ops apply in order and all-or-nothing. The result is validated and returned with its issues and
    version+1. Ops: workspace.update; attribute.add|update|remove (the data dictionary);
    entity.add|update|remove; entity.field.add|remove and entity.profile.add|remove (key = attribute);
    event.add|update|remove (type = entity, match = rule); funnel.*, alert.* (name) and view.* (name =
    view id). Call workspaces.describe for the full format and examples. On 409, re-read the draft from
    the error body and reapply.

    Args:
        workspace_id (str):
        body (OpsInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivityDraftView | ErrorModel]
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
    body: OpsInputBody,
) -> ActivityDraftView | ErrorModel | None:
    """Apply typed edits to the shared draft atomically

     Ops apply in order and all-or-nothing. The result is validated and returned with its issues and
    version+1. Ops: workspace.update; attribute.add|update|remove (the data dictionary);
    entity.add|update|remove; entity.field.add|remove and entity.profile.add|remove (key = attribute);
    event.add|update|remove (type = entity, match = rule); funnel.*, alert.* (name) and view.* (name =
    view id). Call workspaces.describe for the full format and examples. On 409, re-read the draft from
    the error body and reapply.

    Args:
        workspace_id (str):
        body (OpsInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivityDraftView | ErrorModel
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
    body: OpsInputBody,
) -> Response[ActivityDraftView | ErrorModel]:
    """Apply typed edits to the shared draft atomically

     Ops apply in order and all-or-nothing. The result is validated and returned with its issues and
    version+1. Ops: workspace.update; attribute.add|update|remove (the data dictionary);
    entity.add|update|remove; entity.field.add|remove and entity.profile.add|remove (key = attribute);
    event.add|update|remove (type = entity, match = rule); funnel.*, alert.* (name) and view.* (name =
    view id). Call workspaces.describe for the full format and examples. On 409, re-read the draft from
    the error body and reapply.

    Args:
        workspace_id (str):
        body (OpsInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivityDraftView | ErrorModel]
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
    body: OpsInputBody,
) -> ActivityDraftView | ErrorModel | None:
    """Apply typed edits to the shared draft atomically

     Ops apply in order and all-or-nothing. The result is validated and returned with its issues and
    version+1. Ops: workspace.update; attribute.add|update|remove (the data dictionary);
    entity.add|update|remove; entity.field.add|remove and entity.profile.add|remove (key = attribute);
    event.add|update|remove (type = entity, match = rule); funnel.*, alert.* (name) and view.* (name =
    view id). Call workspaces.describe for the full format and examples. On 409, re-read the draft from
    the error body and reapply.

    Args:
        workspace_id (str):
        body (OpsInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivityDraftView | ErrorModel
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            body=body,
        )
    ).parsed
