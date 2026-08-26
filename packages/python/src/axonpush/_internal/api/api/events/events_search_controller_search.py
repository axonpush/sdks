from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_list_response_dto import EventListResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    agent_id: str | Unset = UNSET,
    app_id: str | Unset = UNSET,
    channel_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    environment: str | Unset = UNSET,
    event_type: list[str] | Unset = UNSET,
    limit: float | Unset = UNSET,
    payload_filter: str | Unset = UNSET,
    query: str | Unset = UNSET,
    since: str | Unset = UNSET,
    source: str | Unset = UNSET,
    trace_id: str | Unset = UNSET,
    until: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["agentId"] = agent_id

    params["appId"] = app_id

    params["channelId"] = channel_id

    params["cursor"] = cursor

    params["environment"] = environment

    json_event_type: list[str] | Unset = UNSET
    if not isinstance(event_type, Unset):
        json_event_type = event_type

    params["eventType"] = json_event_type

    params["limit"] = limit

    params["payloadFilter"] = payload_filter

    params["query"] = query

    params["since"] = since

    params["source"] = source

    params["traceId"] = trace_id

    params["until"] = until

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/events/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EventListResponseDto | None:
    if response.status_code == 200:
        response_200 = EventListResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EventListResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    agent_id: str | Unset = UNSET,
    app_id: str | Unset = UNSET,
    channel_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    environment: str | Unset = UNSET,
    event_type: list[str] | Unset = UNSET,
    limit: float | Unset = UNSET,
    payload_filter: str | Unset = UNSET,
    query: str | Unset = UNSET,
    since: str | Unset = UNSET,
    source: str | Unset = UNSET,
    trace_id: str | Unset = UNSET,
    until: str | Unset = UNSET,
) -> Response[EventListResponseDto]:
    """
    Args:
        agent_id (str | Unset):
        app_id (str | Unset):
        channel_id (str | Unset):
        cursor (str | Unset):
        environment (str | Unset):
        event_type (list[str] | Unset):
        limit (float | Unset):
        payload_filter (str | Unset):
        query (str | Unset):
        since (str | Unset):
        source (str | Unset):
        trace_id (str | Unset):
        until (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EventListResponseDto]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        app_id=app_id,
        channel_id=channel_id,
        cursor=cursor,
        environment=environment,
        event_type=event_type,
        limit=limit,
        payload_filter=payload_filter,
        query=query,
        since=since,
        source=source,
        trace_id=trace_id,
        until=until,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    agent_id: str | Unset = UNSET,
    app_id: str | Unset = UNSET,
    channel_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    environment: str | Unset = UNSET,
    event_type: list[str] | Unset = UNSET,
    limit: float | Unset = UNSET,
    payload_filter: str | Unset = UNSET,
    query: str | Unset = UNSET,
    since: str | Unset = UNSET,
    source: str | Unset = UNSET,
    trace_id: str | Unset = UNSET,
    until: str | Unset = UNSET,
) -> EventListResponseDto | None:
    """
    Args:
        agent_id (str | Unset):
        app_id (str | Unset):
        channel_id (str | Unset):
        cursor (str | Unset):
        environment (str | Unset):
        event_type (list[str] | Unset):
        limit (float | Unset):
        payload_filter (str | Unset):
        query (str | Unset):
        since (str | Unset):
        source (str | Unset):
        trace_id (str | Unset):
        until (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EventListResponseDto
    """

    return sync_detailed(
        client=client,
        agent_id=agent_id,
        app_id=app_id,
        channel_id=channel_id,
        cursor=cursor,
        environment=environment,
        event_type=event_type,
        limit=limit,
        payload_filter=payload_filter,
        query=query,
        since=since,
        source=source,
        trace_id=trace_id,
        until=until,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    agent_id: str | Unset = UNSET,
    app_id: str | Unset = UNSET,
    channel_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    environment: str | Unset = UNSET,
    event_type: list[str] | Unset = UNSET,
    limit: float | Unset = UNSET,
    payload_filter: str | Unset = UNSET,
    query: str | Unset = UNSET,
    since: str | Unset = UNSET,
    source: str | Unset = UNSET,
    trace_id: str | Unset = UNSET,
    until: str | Unset = UNSET,
) -> Response[EventListResponseDto]:
    """
    Args:
        agent_id (str | Unset):
        app_id (str | Unset):
        channel_id (str | Unset):
        cursor (str | Unset):
        environment (str | Unset):
        event_type (list[str] | Unset):
        limit (float | Unset):
        payload_filter (str | Unset):
        query (str | Unset):
        since (str | Unset):
        source (str | Unset):
        trace_id (str | Unset):
        until (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EventListResponseDto]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        app_id=app_id,
        channel_id=channel_id,
        cursor=cursor,
        environment=environment,
        event_type=event_type,
        limit=limit,
        payload_filter=payload_filter,
        query=query,
        since=since,
        source=source,
        trace_id=trace_id,
        until=until,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    agent_id: str | Unset = UNSET,
    app_id: str | Unset = UNSET,
    channel_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    environment: str | Unset = UNSET,
    event_type: list[str] | Unset = UNSET,
    limit: float | Unset = UNSET,
    payload_filter: str | Unset = UNSET,
    query: str | Unset = UNSET,
    since: str | Unset = UNSET,
    source: str | Unset = UNSET,
    trace_id: str | Unset = UNSET,
    until: str | Unset = UNSET,
) -> EventListResponseDto | None:
    """
    Args:
        agent_id (str | Unset):
        app_id (str | Unset):
        channel_id (str | Unset):
        cursor (str | Unset):
        environment (str | Unset):
        event_type (list[str] | Unset):
        limit (float | Unset):
        payload_filter (str | Unset):
        query (str | Unset):
        since (str | Unset):
        source (str | Unset):
        trace_id (str | Unset):
        until (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EventListResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            agent_id=agent_id,
            app_id=app_id,
            channel_id=channel_id,
            cursor=cursor,
            environment=environment,
            event_type=event_type,
            limit=limit,
            payload_filter=payload_filter,
            query=query,
            since=since,
            source=source,
            trace_id=trace_id,
            until=until,
        )
    ).parsed
