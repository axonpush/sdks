from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_overview_bucket import AnalyticsOverviewBucket
from ...models.analytics_overview_output_body import AnalyticsOverviewOutputBody
from ...models.error_model import ErrorModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    bucket: AnalyticsOverviewBucket | Unset = UNSET,
    dimensions: str | Unset = UNSET,
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

    json_bucket: str | Unset = UNSET
    if not isinstance(bucket, Unset):
        json_bucket = bucket.value

    params["bucket"] = json_bucket

    params["dimensions"] = dimensions

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
        "url": "/analytics/overview",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalyticsOverviewOutputBody | ErrorModel:
    if response.status_code == 200:
        response_200 = AnalyticsOverviewOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AnalyticsOverviewOutputBody | ErrorModel]:
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
    bucket: AnalyticsOverviewBucket | Unset = UNSET,
    dimensions: str | Unset = UNSET,
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
) -> Response[AnalyticsOverviewOutputBody | ErrorModel]:
    """Aggregate observability view (timeseries + latency + per-dimension breakdowns) in one call

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now
        bucket (AnalyticsOverviewBucket | Unset): Time bucket granularity (default hour)
        dimensions (str | Unset): Comma-separated breakdown dimensions (default
            model,provider,status); each must be a supported breakdown dimension
        tag_key (str | Unset): Attribute key to group by for a tag dimension
        limit (int | Unset): Top-N entries per breakdown (default 50, max 500)
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
        Response[AnalyticsOverviewOutputBody | ErrorModel]
    """

    kwargs = _get_kwargs(
        since=since,
        until=until,
        bucket=bucket,
        dimensions=dimensions,
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
    bucket: AnalyticsOverviewBucket | Unset = UNSET,
    dimensions: str | Unset = UNSET,
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
) -> AnalyticsOverviewOutputBody | ErrorModel | None:
    """Aggregate observability view (timeseries + latency + per-dimension breakdowns) in one call

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now
        bucket (AnalyticsOverviewBucket | Unset): Time bucket granularity (default hour)
        dimensions (str | Unset): Comma-separated breakdown dimensions (default
            model,provider,status); each must be a supported breakdown dimension
        tag_key (str | Unset): Attribute key to group by for a tag dimension
        limit (int | Unset): Top-N entries per breakdown (default 50, max 500)
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
        AnalyticsOverviewOutputBody | ErrorModel
    """

    return sync_detailed(
        client=client,
        since=since,
        until=until,
        bucket=bucket,
        dimensions=dimensions,
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
    bucket: AnalyticsOverviewBucket | Unset = UNSET,
    dimensions: str | Unset = UNSET,
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
) -> Response[AnalyticsOverviewOutputBody | ErrorModel]:
    """Aggregate observability view (timeseries + latency + per-dimension breakdowns) in one call

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now
        bucket (AnalyticsOverviewBucket | Unset): Time bucket granularity (default hour)
        dimensions (str | Unset): Comma-separated breakdown dimensions (default
            model,provider,status); each must be a supported breakdown dimension
        tag_key (str | Unset): Attribute key to group by for a tag dimension
        limit (int | Unset): Top-N entries per breakdown (default 50, max 500)
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
        Response[AnalyticsOverviewOutputBody | ErrorModel]
    """

    kwargs = _get_kwargs(
        since=since,
        until=until,
        bucket=bucket,
        dimensions=dimensions,
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
    bucket: AnalyticsOverviewBucket | Unset = UNSET,
    dimensions: str | Unset = UNSET,
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
) -> AnalyticsOverviewOutputBody | ErrorModel | None:
    """Aggregate observability view (timeseries + latency + per-dimension breakdowns) in one call

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now
        bucket (AnalyticsOverviewBucket | Unset): Time bucket granularity (default hour)
        dimensions (str | Unset): Comma-separated breakdown dimensions (default
            model,provider,status); each must be a supported breakdown dimension
        tag_key (str | Unset): Attribute key to group by for a tag dimension
        limit (int | Unset): Top-N entries per breakdown (default 50, max 500)
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
        AnalyticsOverviewOutputBody | ErrorModel
    """

    return (
        await asyncio_detailed(
            client=client,
            since=since,
            until=until,
            bucket=bucket,
            dimensions=dimensions,
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
