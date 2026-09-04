from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.gate_run_list_dto import GateRunListDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cursor: str | Unset = UNSET,
    experiment_id: str | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["experimentId"] = experiment_id

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/gate-runs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GateRunListDto | None:
    if response.status_code == 200:
        response_200 = GateRunListDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GateRunListDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    experiment_id: str | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GateRunListDto]:
    """
    Args:
        cursor (str | Unset):
        experiment_id (str | Unset):
        limit (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GateRunListDto]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        experiment_id=experiment_id,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    experiment_id: str | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GateRunListDto | None:
    """
    Args:
        cursor (str | Unset):
        experiment_id (str | Unset):
        limit (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GateRunListDto
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        experiment_id=experiment_id,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    experiment_id: str | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GateRunListDto]:
    """
    Args:
        cursor (str | Unset):
        experiment_id (str | Unset):
        limit (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GateRunListDto]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        experiment_id=experiment_id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    experiment_id: str | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GateRunListDto | None:
    """
    Args:
        cursor (str | Unset):
        experiment_id (str | Unset):
        limit (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GateRunListDto
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            experiment_id=experiment_id,
            limit=limit,
        )
    ).parsed
