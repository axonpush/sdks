from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_receipt import ActivityReceipt
from ...models.error_model import ErrorModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: str,
    source_event_id: str,
    *,
    environment: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["environment"] = environment

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspaces/{workspace_id}/observations/{source_event_id}".format(
            workspace_id=quote(str(workspace_id), safe=""),
            source_event_id=quote(str(source_event_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActivityReceipt | ErrorModel:
    if response.status_code == 200:
        response_200 = ActivityReceipt.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ActivityReceipt | ErrorModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    source_event_id: str,
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
) -> Response[ActivityReceipt | ErrorModel]:
    """Check storage and projection separately

    Args:
        workspace_id (str):
        source_event_id (str):
        environment (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivityReceipt | ErrorModel]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        source_event_id=source_event_id,
        environment=environment,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    source_event_id: str,
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
) -> ActivityReceipt | ErrorModel | None:
    """Check storage and projection separately

    Args:
        workspace_id (str):
        source_event_id (str):
        environment (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivityReceipt | ErrorModel
    """

    return sync_detailed(
        workspace_id=workspace_id,
        source_event_id=source_event_id,
        client=client,
        environment=environment,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    source_event_id: str,
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
) -> Response[ActivityReceipt | ErrorModel]:
    """Check storage and projection separately

    Args:
        workspace_id (str):
        source_event_id (str):
        environment (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivityReceipt | ErrorModel]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        source_event_id=source_event_id,
        environment=environment,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    source_event_id: str,
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
) -> ActivityReceipt | ErrorModel | None:
    """Check storage and projection separately

    Args:
        workspace_id (str):
        source_event_id (str):
        environment (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivityReceipt | ErrorModel
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            source_event_id=source_event_id,
            client=client,
            environment=environment,
        )
    ).parsed
