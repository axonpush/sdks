from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_breakdown_dimension import AnalyticsBreakdownDimension
from ...models.breakdown_output_body import BreakdownOutputBody
from ...models.error_model import ErrorModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    dimension: AnalyticsBreakdownDimension | Unset = UNSET,
    tag_key: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    source: str | Unset = UNSET,
    model: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    app: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    environment: str | Unset = UNSET,
    api_key: str | Unset = UNSET,
    user: str | Unset = UNSET,
    filter_tag_key: str | Unset = UNSET,
    filter_tag_value: str | Unset = UNSET,
    service: str | Unset = UNSET,
    operation: str | Unset = UNSET,
    error_type: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["since"] = since

    params["until"] = until

    json_dimension: str | Unset = UNSET
    if not isinstance(dimension, Unset):
        json_dimension = dimension.value

    params["dimension"] = json_dimension

    params["tagKey"] = tag_key

    params["limit"] = limit

    params["source"] = source

    params["model"] = model

    params["provider"] = provider

    params["app"] = app

    params["channel"] = channel

    params["environment"] = environment

    params["apiKey"] = api_key

    params["user"] = user

    params["filterTagKey"] = filter_tag_key

    params["filterTagValue"] = filter_tag_value

    params["service"] = service

    params["operation"] = operation

    params["errorType"] = error_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/breakdown",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BreakdownOutputBody | ErrorModel:
    if response.status_code == 200:
        response_200 = BreakdownOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BreakdownOutputBody | ErrorModel]:
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
    dimension: AnalyticsBreakdownDimension | Unset = UNSET,
    tag_key: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    source: str | Unset = UNSET,
    model: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    app: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    environment: str | Unset = UNSET,
    api_key: str | Unset = UNSET,
    user: str | Unset = UNSET,
    filter_tag_key: str | Unset = UNSET,
    filter_tag_value: str | Unset = UNSET,
    service: str | Unset = UNSET,
    operation: str | Unset = UNSET,
    error_type: str | Unset = UNSET,
) -> Response[BreakdownOutputBody | ErrorModel]:
    """Top-N breakdown by model, provider, status, source, app, key, user, agent, tool, or tag

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now
        dimension (AnalyticsBreakdownDimension | Unset): Breakdown dimension (default model)
        tag_key (str | Unset): Attribute key to group by when dimension=tag
        limit (int | Unset): Top-N entries (default 50, max 500)
        source (str | Unset): Filter by event source (e.g. gateway)
        model (str | Unset): Filter by request/response model
        provider (str | Unset): Filter by model provider
        app (str | Unset): Filter by app id
        channel (str | Unset): Filter by channel id
        environment (str | Unset): Filter by environment id or slug
        api_key (str | Unset): Filter by API key id
        user (str | Unset): Filter by end-user id
        filter_tag_key (str | Unset): Custom-dimension (attribute) key to filter on; pair with
            filterTagValue
        filter_tag_value (str | Unset): Value for filterTagKey
        service (str | Unset): Filter by service (resource service.name)
        operation (str | Unset): Filter by operation / span name
        error_type (str | Unset): Filter by error type

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BreakdownOutputBody | ErrorModel]
    """

    kwargs = _get_kwargs(
        since=since,
        until=until,
        dimension=dimension,
        tag_key=tag_key,
        limit=limit,
        source=source,
        model=model,
        provider=provider,
        app=app,
        channel=channel,
        environment=environment,
        api_key=api_key,
        user=user,
        filter_tag_key=filter_tag_key,
        filter_tag_value=filter_tag_value,
        service=service,
        operation=operation,
        error_type=error_type,
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
    dimension: AnalyticsBreakdownDimension | Unset = UNSET,
    tag_key: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    source: str | Unset = UNSET,
    model: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    app: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    environment: str | Unset = UNSET,
    api_key: str | Unset = UNSET,
    user: str | Unset = UNSET,
    filter_tag_key: str | Unset = UNSET,
    filter_tag_value: str | Unset = UNSET,
    service: str | Unset = UNSET,
    operation: str | Unset = UNSET,
    error_type: str | Unset = UNSET,
) -> BreakdownOutputBody | ErrorModel | None:
    """Top-N breakdown by model, provider, status, source, app, key, user, agent, tool, or tag

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now
        dimension (AnalyticsBreakdownDimension | Unset): Breakdown dimension (default model)
        tag_key (str | Unset): Attribute key to group by when dimension=tag
        limit (int | Unset): Top-N entries (default 50, max 500)
        source (str | Unset): Filter by event source (e.g. gateway)
        model (str | Unset): Filter by request/response model
        provider (str | Unset): Filter by model provider
        app (str | Unset): Filter by app id
        channel (str | Unset): Filter by channel id
        environment (str | Unset): Filter by environment id or slug
        api_key (str | Unset): Filter by API key id
        user (str | Unset): Filter by end-user id
        filter_tag_key (str | Unset): Custom-dimension (attribute) key to filter on; pair with
            filterTagValue
        filter_tag_value (str | Unset): Value for filterTagKey
        service (str | Unset): Filter by service (resource service.name)
        operation (str | Unset): Filter by operation / span name
        error_type (str | Unset): Filter by error type

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BreakdownOutputBody | ErrorModel
    """

    return sync_detailed(
        client=client,
        since=since,
        until=until,
        dimension=dimension,
        tag_key=tag_key,
        limit=limit,
        source=source,
        model=model,
        provider=provider,
        app=app,
        channel=channel,
        environment=environment,
        api_key=api_key,
        user=user,
        filter_tag_key=filter_tag_key,
        filter_tag_value=filter_tag_value,
        service=service,
        operation=operation,
        error_type=error_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    dimension: AnalyticsBreakdownDimension | Unset = UNSET,
    tag_key: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    source: str | Unset = UNSET,
    model: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    app: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    environment: str | Unset = UNSET,
    api_key: str | Unset = UNSET,
    user: str | Unset = UNSET,
    filter_tag_key: str | Unset = UNSET,
    filter_tag_value: str | Unset = UNSET,
    service: str | Unset = UNSET,
    operation: str | Unset = UNSET,
    error_type: str | Unset = UNSET,
) -> Response[BreakdownOutputBody | ErrorModel]:
    """Top-N breakdown by model, provider, status, source, app, key, user, agent, tool, or tag

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now
        dimension (AnalyticsBreakdownDimension | Unset): Breakdown dimension (default model)
        tag_key (str | Unset): Attribute key to group by when dimension=tag
        limit (int | Unset): Top-N entries (default 50, max 500)
        source (str | Unset): Filter by event source (e.g. gateway)
        model (str | Unset): Filter by request/response model
        provider (str | Unset): Filter by model provider
        app (str | Unset): Filter by app id
        channel (str | Unset): Filter by channel id
        environment (str | Unset): Filter by environment id or slug
        api_key (str | Unset): Filter by API key id
        user (str | Unset): Filter by end-user id
        filter_tag_key (str | Unset): Custom-dimension (attribute) key to filter on; pair with
            filterTagValue
        filter_tag_value (str | Unset): Value for filterTagKey
        service (str | Unset): Filter by service (resource service.name)
        operation (str | Unset): Filter by operation / span name
        error_type (str | Unset): Filter by error type

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BreakdownOutputBody | ErrorModel]
    """

    kwargs = _get_kwargs(
        since=since,
        until=until,
        dimension=dimension,
        tag_key=tag_key,
        limit=limit,
        source=source,
        model=model,
        provider=provider,
        app=app,
        channel=channel,
        environment=environment,
        api_key=api_key,
        user=user,
        filter_tag_key=filter_tag_key,
        filter_tag_value=filter_tag_value,
        service=service,
        operation=operation,
        error_type=error_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    dimension: AnalyticsBreakdownDimension | Unset = UNSET,
    tag_key: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    source: str | Unset = UNSET,
    model: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    app: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    environment: str | Unset = UNSET,
    api_key: str | Unset = UNSET,
    user: str | Unset = UNSET,
    filter_tag_key: str | Unset = UNSET,
    filter_tag_value: str | Unset = UNSET,
    service: str | Unset = UNSET,
    operation: str | Unset = UNSET,
    error_type: str | Unset = UNSET,
) -> BreakdownOutputBody | ErrorModel | None:
    """Top-N breakdown by model, provider, status, source, app, key, user, agent, tool, or tag

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now
        dimension (AnalyticsBreakdownDimension | Unset): Breakdown dimension (default model)
        tag_key (str | Unset): Attribute key to group by when dimension=tag
        limit (int | Unset): Top-N entries (default 50, max 500)
        source (str | Unset): Filter by event source (e.g. gateway)
        model (str | Unset): Filter by request/response model
        provider (str | Unset): Filter by model provider
        app (str | Unset): Filter by app id
        channel (str | Unset): Filter by channel id
        environment (str | Unset): Filter by environment id or slug
        api_key (str | Unset): Filter by API key id
        user (str | Unset): Filter by end-user id
        filter_tag_key (str | Unset): Custom-dimension (attribute) key to filter on; pair with
            filterTagValue
        filter_tag_value (str | Unset): Value for filterTagKey
        service (str | Unset): Filter by service (resource service.name)
        operation (str | Unset): Filter by operation / span name
        error_type (str | Unset): Filter by error type

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BreakdownOutputBody | ErrorModel
    """

    return (
        await asyncio_detailed(
            client=client,
            since=since,
            until=until,
            dimension=dimension,
            tag_key=tag_key,
            limit=limit,
            source=source,
            model=model,
            provider=provider,
            app=app,
            channel=channel,
            environment=environment,
            api_key=api_key,
            user=user,
            filter_tag_key=filter_tag_key,
            filter_tag_value=filter_tag_value,
            service=service,
            operation=operation,
            error_type=error_type,
        )
    ).parsed
