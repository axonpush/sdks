from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.trace_intelligence_cluster_list_response_dto import (
    TraceIntelligenceClusterListResponseDto,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    app_id: str,
    cursor: str | Unset = UNSET,
    environment_id: str,
    from_: str | Unset = UNSET,
    limit: float | Unset = UNSET,
    search: str | Unset = UNSET,
    signal_kind: str | Unset = UNSET,
    to: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["appId"] = app_id

    params["cursor"] = cursor

    params["environmentId"] = environment_id

    params["from"] = from_

    params["limit"] = limit

    params["search"] = search

    params["signalKind"] = signal_kind

    params["to"] = to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/trace-intelligence/clusters",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TraceIntelligenceClusterListResponseDto | None:
    if response.status_code == 200:
        response_200 = TraceIntelligenceClusterListResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TraceIntelligenceClusterListResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    app_id: str,
    cursor: str | Unset = UNSET,
    environment_id: str,
    from_: str | Unset = UNSET,
    limit: float | Unset = UNSET,
    search: str | Unset = UNSET,
    signal_kind: str | Unset = UNSET,
    to: str | Unset = UNSET,
) -> Response[TraceIntelligenceClusterListResponseDto]:
    """
    Args:
        app_id (str):
        cursor (str | Unset):
        environment_id (str):
        from_ (str | Unset):
        limit (float | Unset):
        search (str | Unset):
        signal_kind (str | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TraceIntelligenceClusterListResponseDto]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        cursor=cursor,
        environment_id=environment_id,
        from_=from_,
        limit=limit,
        search=search,
        signal_kind=signal_kind,
        to=to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    app_id: str,
    cursor: str | Unset = UNSET,
    environment_id: str,
    from_: str | Unset = UNSET,
    limit: float | Unset = UNSET,
    search: str | Unset = UNSET,
    signal_kind: str | Unset = UNSET,
    to: str | Unset = UNSET,
) -> TraceIntelligenceClusterListResponseDto | None:
    """
    Args:
        app_id (str):
        cursor (str | Unset):
        environment_id (str):
        from_ (str | Unset):
        limit (float | Unset):
        search (str | Unset):
        signal_kind (str | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TraceIntelligenceClusterListResponseDto
    """

    return sync_detailed(
        client=client,
        app_id=app_id,
        cursor=cursor,
        environment_id=environment_id,
        from_=from_,
        limit=limit,
        search=search,
        signal_kind=signal_kind,
        to=to,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    app_id: str,
    cursor: str | Unset = UNSET,
    environment_id: str,
    from_: str | Unset = UNSET,
    limit: float | Unset = UNSET,
    search: str | Unset = UNSET,
    signal_kind: str | Unset = UNSET,
    to: str | Unset = UNSET,
) -> Response[TraceIntelligenceClusterListResponseDto]:
    """
    Args:
        app_id (str):
        cursor (str | Unset):
        environment_id (str):
        from_ (str | Unset):
        limit (float | Unset):
        search (str | Unset):
        signal_kind (str | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TraceIntelligenceClusterListResponseDto]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        cursor=cursor,
        environment_id=environment_id,
        from_=from_,
        limit=limit,
        search=search,
        signal_kind=signal_kind,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    app_id: str,
    cursor: str | Unset = UNSET,
    environment_id: str,
    from_: str | Unset = UNSET,
    limit: float | Unset = UNSET,
    search: str | Unset = UNSET,
    signal_kind: str | Unset = UNSET,
    to: str | Unset = UNSET,
) -> TraceIntelligenceClusterListResponseDto | None:
    """
    Args:
        app_id (str):
        cursor (str | Unset):
        environment_id (str):
        from_ (str | Unset):
        limit (float | Unset):
        search (str | Unset):
        signal_kind (str | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TraceIntelligenceClusterListResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            app_id=app_id,
            cursor=cursor,
            environment_id=environment_id,
            from_=from_,
            limit=limit,
            search=search,
            signal_kind=signal_kind,
            to=to,
        )
    ).parsed
