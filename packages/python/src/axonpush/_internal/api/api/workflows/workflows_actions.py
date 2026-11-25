from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.actions_page import ActionsPage
from ...models.error_model import ErrorModel
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    workspace_id: str,
    *,
    environment: str | Unset = UNSET,
    case_key: str | Unset = UNSET,
    attention: bool | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["environment"] = environment

    params["case_key"] = case_key

    params["attention"] = attention

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspaces/{workspace_id}/workflows/actions".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActionsPage | ErrorModel:
    if response.status_code == 200:
        response_200 = ActionsPage.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ActionsPage | ErrorModel]:
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
    case_key: str | Unset = UNSET,
    attention: bool | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[ActionsPage | ErrorModel]:
    """Discover typed actions available on a case or list review and recovery tasks

    Args:
        workspace_id (str):
        environment (str | Unset):
        case_key (str | Unset):
        attention (bool | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionsPage | ErrorModel]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        environment=environment,
        case_key=case_key,
        attention=attention,
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
    case_key: str | Unset = UNSET,
    attention: bool | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> ActionsPage | ErrorModel | None:
    """Discover typed actions available on a case or list review and recovery tasks

    Args:
        workspace_id (str):
        environment (str | Unset):
        case_key (str | Unset):
        attention (bool | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionsPage | ErrorModel
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        environment=environment,
        case_key=case_key,
        attention=attention,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
    case_key: str | Unset = UNSET,
    attention: bool | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[ActionsPage | ErrorModel]:
    """Discover typed actions available on a case or list review and recovery tasks

    Args:
        workspace_id (str):
        environment (str | Unset):
        case_key (str | Unset):
        attention (bool | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionsPage | ErrorModel]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        environment=environment,
        case_key=case_key,
        attention=attention,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
    case_key: str | Unset = UNSET,
    attention: bool | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> ActionsPage | ErrorModel | None:
    """Discover typed actions available on a case or list review and recovery tasks

    Args:
        workspace_id (str):
        environment (str | Unset):
        case_key (str | Unset):
        attention (bool | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionsPage | ErrorModel
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            environment=environment,
            case_key=case_key,
            attention=attention,
            cursor=cursor,
        )
    ).parsed
