from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_timeseries_bucket import AnalyticsTimeseriesBucket
from ...models.error_model import ErrorModel
from ...models.timeseries_output_body import TimeseriesOutputBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    bucket: AnalyticsTimeseriesBucket | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["since"] = since

    params["until"] = until

    json_bucket: str | Unset = UNSET
    if not isinstance(bucket, Unset):
        json_bucket = bucket.value

    params["bucket"] = json_bucket

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/timeseries",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | TimeseriesOutputBody:
    if response.status_code == 200:
        response_200 = TimeseriesOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | TimeseriesOutputBody]:
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
    bucket: AnalyticsTimeseriesBucket | Unset = UNSET,
) -> Response[ErrorModel | TimeseriesOutputBody]:
    """Time-bucketed activity (counts, tokens, cost, latency)

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now
        bucket (AnalyticsTimeseriesBucket | Unset): Time bucket granularity (default hour)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | TimeseriesOutputBody]
    """

    kwargs = _get_kwargs(
        since=since,
        until=until,
        bucket=bucket,
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
    bucket: AnalyticsTimeseriesBucket | Unset = UNSET,
) -> ErrorModel | TimeseriesOutputBody | None:
    """Time-bucketed activity (counts, tokens, cost, latency)

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now
        bucket (AnalyticsTimeseriesBucket | Unset): Time bucket granularity (default hour)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | TimeseriesOutputBody
    """

    return sync_detailed(
        client=client,
        since=since,
        until=until,
        bucket=bucket,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    bucket: AnalyticsTimeseriesBucket | Unset = UNSET,
) -> Response[ErrorModel | TimeseriesOutputBody]:
    """Time-bucketed activity (counts, tokens, cost, latency)

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now
        bucket (AnalyticsTimeseriesBucket | Unset): Time bucket granularity (default hour)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | TimeseriesOutputBody]
    """

    kwargs = _get_kwargs(
        since=since,
        until=until,
        bucket=bucket,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    bucket: AnalyticsTimeseriesBucket | Unset = UNSET,
) -> ErrorModel | TimeseriesOutputBody | None:
    """Time-bucketed activity (counts, tokens, cost, latency)

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now
        bucket (AnalyticsTimeseriesBucket | Unset): Time bucket granularity (default hour)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | TimeseriesOutputBody
    """

    return (
        await asyncio_detailed(
            client=client,
            since=since,
            until=until,
            bucket=bucket,
        )
    ).parsed
