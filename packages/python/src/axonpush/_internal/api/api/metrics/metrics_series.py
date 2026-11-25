from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_model import ErrorModel
from ...models.metric_series_result_dto import MetricSeriesResultDTO
from ...models.metrics_series_agg import MetricsSeriesAgg
from ...models.metrics_series_interval import MetricsSeriesInterval
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    name: str,
    agg: MetricsSeriesAgg | Unset = UNSET,
    interval: MetricsSeriesInterval | Unset = UNSET,
    group_by: str | Unset = UNSET,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["name"] = name

    json_agg: str | Unset = UNSET
    if not isinstance(agg, Unset):
        json_agg = agg.value

    params["agg"] = json_agg

    json_interval: str | Unset = UNSET
    if not isinstance(interval, Unset):
        json_interval = interval.value

    params["interval"] = json_interval

    params["groupBy"] = group_by

    params["appId"] = app_id

    params["environmentId"] = environment_id

    params["since"] = since

    params["until"] = until

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/metrics/series",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | MetricSeriesResultDTO:
    if response.status_code == 200:
        response_200 = MetricSeriesResultDTO.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | MetricSeriesResultDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str,
    agg: MetricsSeriesAgg | Unset = UNSET,
    interval: MetricsSeriesInterval | Unset = UNSET,
    group_by: str | Unset = UNSET,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
) -> Response[ErrorModel | MetricSeriesResultDTO]:
    """Aggregate one trace metric over time, optionally grouped by an attribute (top 10 groups)

    Args:
        name (str):
        agg (MetricsSeriesAgg | Unset): Aggregation (default sum)
        interval (MetricsSeriesInterval | Unset): Bucket size (default 1h)
        group_by (str | Unset): Attribute key to split by; top 10 groups
        app_id (str | Unset):
        environment_id (str | Unset): Environment slug or id
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | MetricSeriesResultDTO]
    """

    kwargs = _get_kwargs(
        name=name,
        agg=agg,
        interval=interval,
        group_by=group_by,
        app_id=app_id,
        environment_id=environment_id,
        since=since,
        until=until,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    name: str,
    agg: MetricsSeriesAgg | Unset = UNSET,
    interval: MetricsSeriesInterval | Unset = UNSET,
    group_by: str | Unset = UNSET,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
) -> ErrorModel | MetricSeriesResultDTO | None:
    """Aggregate one trace metric over time, optionally grouped by an attribute (top 10 groups)

    Args:
        name (str):
        agg (MetricsSeriesAgg | Unset): Aggregation (default sum)
        interval (MetricsSeriesInterval | Unset): Bucket size (default 1h)
        group_by (str | Unset): Attribute key to split by; top 10 groups
        app_id (str | Unset):
        environment_id (str | Unset): Environment slug or id
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | MetricSeriesResultDTO
    """

    return sync_detailed(
        client=client,
        name=name,
        agg=agg,
        interval=interval,
        group_by=group_by,
        app_id=app_id,
        environment_id=environment_id,
        since=since,
        until=until,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str,
    agg: MetricsSeriesAgg | Unset = UNSET,
    interval: MetricsSeriesInterval | Unset = UNSET,
    group_by: str | Unset = UNSET,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
) -> Response[ErrorModel | MetricSeriesResultDTO]:
    """Aggregate one trace metric over time, optionally grouped by an attribute (top 10 groups)

    Args:
        name (str):
        agg (MetricsSeriesAgg | Unset): Aggregation (default sum)
        interval (MetricsSeriesInterval | Unset): Bucket size (default 1h)
        group_by (str | Unset): Attribute key to split by; top 10 groups
        app_id (str | Unset):
        environment_id (str | Unset): Environment slug or id
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | MetricSeriesResultDTO]
    """

    kwargs = _get_kwargs(
        name=name,
        agg=agg,
        interval=interval,
        group_by=group_by,
        app_id=app_id,
        environment_id=environment_id,
        since=since,
        until=until,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    name: str,
    agg: MetricsSeriesAgg | Unset = UNSET,
    interval: MetricsSeriesInterval | Unset = UNSET,
    group_by: str | Unset = UNSET,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
) -> ErrorModel | MetricSeriesResultDTO | None:
    """Aggregate one trace metric over time, optionally grouped by an attribute (top 10 groups)

    Args:
        name (str):
        agg (MetricsSeriesAgg | Unset): Aggregation (default sum)
        interval (MetricsSeriesInterval | Unset): Bucket size (default 1h)
        group_by (str | Unset): Attribute key to split by; top 10 groups
        app_id (str | Unset):
        environment_id (str | Unset): Environment slug or id
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | MetricSeriesResultDTO
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            agg=agg,
            interval=interval,
            group_by=group_by,
            app_id=app_id,
            environment_id=environment_id,
            since=since,
            until=until,
        )
    ).parsed
