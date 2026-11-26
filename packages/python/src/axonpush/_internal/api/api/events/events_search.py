from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.search_events_output_body import SearchEventsOutputBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    app_id: str | Unset = UNSET,
    channel_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    event_type: str | Unset = UNSET,
    source: str | Unset = UNSET,
    status: str | Unset = UNSET,
    trace_id: str | Unset = UNSET,
    agent_id: str | Unset = UNSET,
    agent_name: str | Unset = UNSET,
    tool_name: str | Unset = UNSET,
    semantic_kind: str | Unset = UNSET,
    service_name: str | Unset = UNSET,
    operation_name: str | Unset = UNSET,
    error_type: str | Unset = UNSET,
    q: str | Unset = UNSET,
    attr_key: str | Unset = UNSET,
    attr_value: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["since"] = since

    params["until"] = until

    params["limit"] = limit

    params["appId"] = app_id

    params["channelId"] = channel_id

    params["environmentId"] = environment_id

    params["eventType"] = event_type

    params["source"] = source

    params["status"] = status

    params["traceId"] = trace_id

    params["agentId"] = agent_id

    params["agentName"] = agent_name

    params["toolName"] = tool_name

    params["semanticKind"] = semantic_kind

    params["serviceName"] = service_name

    params["operationName"] = operation_name

    params["errorType"] = error_type

    params["q"] = q

    params["attrKey"] = attr_key

    params["attrValue"] = attr_value

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | SearchEventsOutputBody:
    if response.status_code == 200:
        response_200 = SearchEventsOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | SearchEventsOutputBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    app_id: str | Unset = UNSET,
    channel_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    event_type: str | Unset = UNSET,
    source: str | Unset = UNSET,
    status: str | Unset = UNSET,
    trace_id: str | Unset = UNSET,
    agent_id: str | Unset = UNSET,
    agent_name: str | Unset = UNSET,
    tool_name: str | Unset = UNSET,
    semantic_kind: str | Unset = UNSET,
    service_name: str | Unset = UNSET,
    operation_name: str | Unset = UNSET,
    error_type: str | Unset = UNSET,
    q: str | Unset = UNSET,
    attr_key: str | Unset = UNSET,
    attr_value: str | Unset = UNSET,
) -> Response[ErrorModel | SearchEventsOutputBody]:
    """Search events with filters

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now
        limit (int | Unset): Max events to return (default 50, max 500)
        app_id (str | Unset): Filter by app
        channel_id (str | Unset): Filter by channel
        environment_id (str | Unset): Filter by environment
        event_type (str | Unset): Filter by event type
        source (str | Unset): Filter by source
        status (str | Unset): Filter by status
        trace_id (str | Unset): Filter by trace id
        agent_id (str | Unset): Filter by agent id
        agent_name (str | Unset): Filter by agent name
        tool_name (str | Unset): Filter by tool name
        semantic_kind (str | Unset): Filter by semantic kind (agent, tool, llm, retriever, db,
            http, log)
        service_name (str | Unset): Filter by service (resource service.name)
        operation_name (str | Unset): Filter by operation / span name
        error_type (str | Unset): Filter by error type
        q (str | Unset): Case-insensitive contains match on search text
        attr_key (str | Unset): JSONB attribute key for equality filter (paired with attrValue)
        attr_value (str | Unset): JSONB attribute value for equality filter (paired with attrKey)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | SearchEventsOutputBody]
    """

    kwargs = _get_kwargs(
        since=since,
        until=until,
        limit=limit,
        app_id=app_id,
        channel_id=channel_id,
        environment_id=environment_id,
        event_type=event_type,
        source=source,
        status=status,
        trace_id=trace_id,
        agent_id=agent_id,
        agent_name=agent_name,
        tool_name=tool_name,
        semantic_kind=semantic_kind,
        service_name=service_name,
        operation_name=operation_name,
        error_type=error_type,
        q=q,
        attr_key=attr_key,
        attr_value=attr_value,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    app_id: str | Unset = UNSET,
    channel_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    event_type: str | Unset = UNSET,
    source: str | Unset = UNSET,
    status: str | Unset = UNSET,
    trace_id: str | Unset = UNSET,
    agent_id: str | Unset = UNSET,
    agent_name: str | Unset = UNSET,
    tool_name: str | Unset = UNSET,
    semantic_kind: str | Unset = UNSET,
    service_name: str | Unset = UNSET,
    operation_name: str | Unset = UNSET,
    error_type: str | Unset = UNSET,
    q: str | Unset = UNSET,
    attr_key: str | Unset = UNSET,
    attr_value: str | Unset = UNSET,
) -> ErrorModel | SearchEventsOutputBody | None:
    """Search events with filters

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now
        limit (int | Unset): Max events to return (default 50, max 500)
        app_id (str | Unset): Filter by app
        channel_id (str | Unset): Filter by channel
        environment_id (str | Unset): Filter by environment
        event_type (str | Unset): Filter by event type
        source (str | Unset): Filter by source
        status (str | Unset): Filter by status
        trace_id (str | Unset): Filter by trace id
        agent_id (str | Unset): Filter by agent id
        agent_name (str | Unset): Filter by agent name
        tool_name (str | Unset): Filter by tool name
        semantic_kind (str | Unset): Filter by semantic kind (agent, tool, llm, retriever, db,
            http, log)
        service_name (str | Unset): Filter by service (resource service.name)
        operation_name (str | Unset): Filter by operation / span name
        error_type (str | Unset): Filter by error type
        q (str | Unset): Case-insensitive contains match on search text
        attr_key (str | Unset): JSONB attribute key for equality filter (paired with attrValue)
        attr_value (str | Unset): JSONB attribute value for equality filter (paired with attrKey)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | SearchEventsOutputBody
    """

    return sync_detailed(
        client=client,
        since=since,
        until=until,
        limit=limit,
        app_id=app_id,
        channel_id=channel_id,
        environment_id=environment_id,
        event_type=event_type,
        source=source,
        status=status,
        trace_id=trace_id,
        agent_id=agent_id,
        agent_name=agent_name,
        tool_name=tool_name,
        semantic_kind=semantic_kind,
        service_name=service_name,
        operation_name=operation_name,
        error_type=error_type,
        q=q,
        attr_key=attr_key,
        attr_value=attr_value,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    app_id: str | Unset = UNSET,
    channel_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    event_type: str | Unset = UNSET,
    source: str | Unset = UNSET,
    status: str | Unset = UNSET,
    trace_id: str | Unset = UNSET,
    agent_id: str | Unset = UNSET,
    agent_name: str | Unset = UNSET,
    tool_name: str | Unset = UNSET,
    semantic_kind: str | Unset = UNSET,
    service_name: str | Unset = UNSET,
    operation_name: str | Unset = UNSET,
    error_type: str | Unset = UNSET,
    q: str | Unset = UNSET,
    attr_key: str | Unset = UNSET,
    attr_value: str | Unset = UNSET,
) -> Response[ErrorModel | SearchEventsOutputBody]:
    """Search events with filters

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now
        limit (int | Unset): Max events to return (default 50, max 500)
        app_id (str | Unset): Filter by app
        channel_id (str | Unset): Filter by channel
        environment_id (str | Unset): Filter by environment
        event_type (str | Unset): Filter by event type
        source (str | Unset): Filter by source
        status (str | Unset): Filter by status
        trace_id (str | Unset): Filter by trace id
        agent_id (str | Unset): Filter by agent id
        agent_name (str | Unset): Filter by agent name
        tool_name (str | Unset): Filter by tool name
        semantic_kind (str | Unset): Filter by semantic kind (agent, tool, llm, retriever, db,
            http, log)
        service_name (str | Unset): Filter by service (resource service.name)
        operation_name (str | Unset): Filter by operation / span name
        error_type (str | Unset): Filter by error type
        q (str | Unset): Case-insensitive contains match on search text
        attr_key (str | Unset): JSONB attribute key for equality filter (paired with attrValue)
        attr_value (str | Unset): JSONB attribute value for equality filter (paired with attrKey)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | SearchEventsOutputBody]
    """

    kwargs = _get_kwargs(
        since=since,
        until=until,
        limit=limit,
        app_id=app_id,
        channel_id=channel_id,
        environment_id=environment_id,
        event_type=event_type,
        source=source,
        status=status,
        trace_id=trace_id,
        agent_id=agent_id,
        agent_name=agent_name,
        tool_name=tool_name,
        semantic_kind=semantic_kind,
        service_name=service_name,
        operation_name=operation_name,
        error_type=error_type,
        q=q,
        attr_key=attr_key,
        attr_value=attr_value,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    app_id: str | Unset = UNSET,
    channel_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    event_type: str | Unset = UNSET,
    source: str | Unset = UNSET,
    status: str | Unset = UNSET,
    trace_id: str | Unset = UNSET,
    agent_id: str | Unset = UNSET,
    agent_name: str | Unset = UNSET,
    tool_name: str | Unset = UNSET,
    semantic_kind: str | Unset = UNSET,
    service_name: str | Unset = UNSET,
    operation_name: str | Unset = UNSET,
    error_type: str | Unset = UNSET,
    q: str | Unset = UNSET,
    attr_key: str | Unset = UNSET,
    attr_value: str | Unset = UNSET,
) -> ErrorModel | SearchEventsOutputBody | None:
    """Search events with filters

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now
        limit (int | Unset): Max events to return (default 50, max 500)
        app_id (str | Unset): Filter by app
        channel_id (str | Unset): Filter by channel
        environment_id (str | Unset): Filter by environment
        event_type (str | Unset): Filter by event type
        source (str | Unset): Filter by source
        status (str | Unset): Filter by status
        trace_id (str | Unset): Filter by trace id
        agent_id (str | Unset): Filter by agent id
        agent_name (str | Unset): Filter by agent name
        tool_name (str | Unset): Filter by tool name
        semantic_kind (str | Unset): Filter by semantic kind (agent, tool, llm, retriever, db,
            http, log)
        service_name (str | Unset): Filter by service (resource service.name)
        operation_name (str | Unset): Filter by operation / span name
        error_type (str | Unset): Filter by error type
        q (str | Unset): Case-insensitive contains match on search text
        attr_key (str | Unset): JSONB attribute key for equality filter (paired with attrValue)
        attr_value (str | Unset): JSONB attribute value for equality filter (paired with attrKey)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | SearchEventsOutputBody
    """

    return (
        await asyncio_detailed(
            client=client,
            since=since,
            until=until,
            limit=limit,
            app_id=app_id,
            channel_id=channel_id,
            environment_id=environment_id,
            event_type=event_type,
            source=source,
            status=status,
            trace_id=trace_id,
            agent_id=agent_id,
            agent_name=agent_name,
            tool_name=tool_name,
            semantic_kind=semantic_kind,
            service_name=service_name,
            operation_name=operation_name,
            error_type=error_type,
            q=q,
            attr_key=attr_key,
            attr_value=attr_value,
        )
    ).parsed
