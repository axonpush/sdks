from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.action_record import ActionRecord
from ...models.error_model import ErrorModel
from ...models.proposal import Proposal
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    workspace_id: str,
    case_key: str,
    *,
    body: Proposal,
    environment: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["environment"] = environment

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/workspaces/{workspace_id}/workflows/cases/{case_key}/actions".format(
            workspace_id=quote(str(workspace_id), safe=""),
            case_key=quote(str(case_key), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActionRecord | ErrorModel:
    if response.status_code == 200:
        response_200 = ActionRecord.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ActionRecord | ErrorModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    case_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: Proposal,
    environment: str | Unset = UNSET,
) -> Response[ActionRecord | ErrorModel]:
    """Propose a typed action against the current case state

    Args:
        workspace_id (str):
        case_key (str):
        environment (str | Unset):
        body (Proposal):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionRecord | ErrorModel]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        case_key=case_key,
        body=body,
        environment=environment,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    case_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: Proposal,
    environment: str | Unset = UNSET,
) -> ActionRecord | ErrorModel | None:
    """Propose a typed action against the current case state

    Args:
        workspace_id (str):
        case_key (str):
        environment (str | Unset):
        body (Proposal):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionRecord | ErrorModel
    """

    return sync_detailed(
        workspace_id=workspace_id,
        case_key=case_key,
        client=client,
        body=body,
        environment=environment,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    case_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: Proposal,
    environment: str | Unset = UNSET,
) -> Response[ActionRecord | ErrorModel]:
    """Propose a typed action against the current case state

    Args:
        workspace_id (str):
        case_key (str):
        environment (str | Unset):
        body (Proposal):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionRecord | ErrorModel]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        case_key=case_key,
        body=body,
        environment=environment,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    case_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: Proposal,
    environment: str | Unset = UNSET,
) -> ActionRecord | ErrorModel | None:
    """Propose a typed action against the current case state

    Args:
        workspace_id (str):
        case_key (str):
        environment (str | Unset):
        body (Proposal):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionRecord | ErrorModel
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            case_key=case_key,
            client=client,
            body=body,
            environment=environment,
        )
    ).parsed
