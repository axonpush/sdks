from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_series_bucket import ActivitySeriesBucket
from ...models.activity_series_metric import ActivitySeriesMetric
from ...models.activity_series_window import ActivitySeriesWindow
from ...models.activity_workspace_series import ActivityWorkspaceSeries
from ...models.error_model import ErrorModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: str,
    *,
    environment: str | Unset = UNSET,
    metric: ActivitySeriesMetric | Unset = ActivitySeriesMetric.OUTCOMES,
    window: ActivitySeriesWindow | Unset = ActivitySeriesWindow.VALUE_1,
    bucket: ActivitySeriesBucket | Unset = UNSET,
    entity: str | Unset = UNSET,
    funnel: str | Unset = UNSET,
    side: str | Unset = UNSET,
    client_query: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["environment"] = environment

    json_metric: str | Unset = UNSET
    if not isinstance(metric, Unset):
        json_metric = metric.value

    params["metric"] = json_metric

    json_window: str | Unset = UNSET
    if not isinstance(window, Unset):
        json_window = window.value

    params["window"] = json_window

    json_bucket: str | Unset = UNSET
    if not isinstance(bucket, Unset):
        json_bucket = bucket.value

    params["bucket"] = json_bucket

    params["entity"] = entity

    params["funnel"] = funnel

    params["side"] = side

    params["client"] = client_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspaces/{workspace_id}/series".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActivityWorkspaceSeries | ErrorModel:
    if response.status_code == 200:
        response_200 = ActivityWorkspaceSeries.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ActivityWorkspaceSeries | ErrorModel]:
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
    metric: ActivitySeriesMetric | Unset = ActivitySeriesMetric.OUTCOMES,
    window: ActivitySeriesWindow | Unset = ActivitySeriesWindow.VALUE_1,
    bucket: ActivitySeriesBucket | Unset = UNSET,
    entity: str | Unset = UNSET,
    funnel: str | Unset = UNSET,
    side: str | Unset = UNSET,
    client_query: str | Unset = UNSET,
) -> Response[ActivityWorkspaceSeries | ErrorModel]:
    """Zero-filled time series: observations by the outcome role, distinct funnel entities by furthest
    stage, or source-to-view lag

    Args:
        workspace_id (str):
        environment (str | Unset):
        metric (ActivitySeriesMetric | Unset): outcomes: observations by the outcome role; funnel:
            distinct entities by furthest stage; lag: source-to-view percentiles Default:
            ActivitySeriesMetric.OUTCOMES.
        window (ActivitySeriesWindow | Unset): 90d reads de-identified daily rollups Default:
            ActivitySeriesWindow.VALUE_1.
        bucket (ActivitySeriesBucket | Unset): Defaults per window: 1h→5m, 24h→1h, 7d→1h, 30d→1d,
            90d→1d. Allowed: 1h:5m, 24h:5m|1h, 7d:1h|1d, 30d:1d, 90d:1d
        entity (str | Unset): outcomes: only events that update this entity
        funnel (str | Unset): funnel: funnel name, default the first declared
        side (str | Unset): Filter by the actor_side role
        client_query (str | Unset): Filter by the client role

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivityWorkspaceSeries | ErrorModel]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        environment=environment,
        metric=metric,
        window=window,
        bucket=bucket,
        entity=entity,
        funnel=funnel,
        side=side,
        client_query=client_query,
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
    metric: ActivitySeriesMetric | Unset = ActivitySeriesMetric.OUTCOMES,
    window: ActivitySeriesWindow | Unset = ActivitySeriesWindow.VALUE_1,
    bucket: ActivitySeriesBucket | Unset = UNSET,
    entity: str | Unset = UNSET,
    funnel: str | Unset = UNSET,
    side: str | Unset = UNSET,
    client_query: str | Unset = UNSET,
) -> ActivityWorkspaceSeries | ErrorModel | None:
    """Zero-filled time series: observations by the outcome role, distinct funnel entities by furthest
    stage, or source-to-view lag

    Args:
        workspace_id (str):
        environment (str | Unset):
        metric (ActivitySeriesMetric | Unset): outcomes: observations by the outcome role; funnel:
            distinct entities by furthest stage; lag: source-to-view percentiles Default:
            ActivitySeriesMetric.OUTCOMES.
        window (ActivitySeriesWindow | Unset): 90d reads de-identified daily rollups Default:
            ActivitySeriesWindow.VALUE_1.
        bucket (ActivitySeriesBucket | Unset): Defaults per window: 1h→5m, 24h→1h, 7d→1h, 30d→1d,
            90d→1d. Allowed: 1h:5m, 24h:5m|1h, 7d:1h|1d, 30d:1d, 90d:1d
        entity (str | Unset): outcomes: only events that update this entity
        funnel (str | Unset): funnel: funnel name, default the first declared
        side (str | Unset): Filter by the actor_side role
        client_query (str | Unset): Filter by the client role

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivityWorkspaceSeries | ErrorModel
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        environment=environment,
        metric=metric,
        window=window,
        bucket=bucket,
        entity=entity,
        funnel=funnel,
        side=side,
        client_query=client_query,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
    metric: ActivitySeriesMetric | Unset = ActivitySeriesMetric.OUTCOMES,
    window: ActivitySeriesWindow | Unset = ActivitySeriesWindow.VALUE_1,
    bucket: ActivitySeriesBucket | Unset = UNSET,
    entity: str | Unset = UNSET,
    funnel: str | Unset = UNSET,
    side: str | Unset = UNSET,
    client_query: str | Unset = UNSET,
) -> Response[ActivityWorkspaceSeries | ErrorModel]:
    """Zero-filled time series: observations by the outcome role, distinct funnel entities by furthest
    stage, or source-to-view lag

    Args:
        workspace_id (str):
        environment (str | Unset):
        metric (ActivitySeriesMetric | Unset): outcomes: observations by the outcome role; funnel:
            distinct entities by furthest stage; lag: source-to-view percentiles Default:
            ActivitySeriesMetric.OUTCOMES.
        window (ActivitySeriesWindow | Unset): 90d reads de-identified daily rollups Default:
            ActivitySeriesWindow.VALUE_1.
        bucket (ActivitySeriesBucket | Unset): Defaults per window: 1h→5m, 24h→1h, 7d→1h, 30d→1d,
            90d→1d. Allowed: 1h:5m, 24h:5m|1h, 7d:1h|1d, 30d:1d, 90d:1d
        entity (str | Unset): outcomes: only events that update this entity
        funnel (str | Unset): funnel: funnel name, default the first declared
        side (str | Unset): Filter by the actor_side role
        client_query (str | Unset): Filter by the client role

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivityWorkspaceSeries | ErrorModel]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        environment=environment,
        metric=metric,
        window=window,
        bucket=bucket,
        entity=entity,
        funnel=funnel,
        side=side,
        client_query=client_query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
    metric: ActivitySeriesMetric | Unset = ActivitySeriesMetric.OUTCOMES,
    window: ActivitySeriesWindow | Unset = ActivitySeriesWindow.VALUE_1,
    bucket: ActivitySeriesBucket | Unset = UNSET,
    entity: str | Unset = UNSET,
    funnel: str | Unset = UNSET,
    side: str | Unset = UNSET,
    client_query: str | Unset = UNSET,
) -> ActivityWorkspaceSeries | ErrorModel | None:
    """Zero-filled time series: observations by the outcome role, distinct funnel entities by furthest
    stage, or source-to-view lag

    Args:
        workspace_id (str):
        environment (str | Unset):
        metric (ActivitySeriesMetric | Unset): outcomes: observations by the outcome role; funnel:
            distinct entities by furthest stage; lag: source-to-view percentiles Default:
            ActivitySeriesMetric.OUTCOMES.
        window (ActivitySeriesWindow | Unset): 90d reads de-identified daily rollups Default:
            ActivitySeriesWindow.VALUE_1.
        bucket (ActivitySeriesBucket | Unset): Defaults per window: 1h→5m, 24h→1h, 7d→1h, 30d→1d,
            90d→1d. Allowed: 1h:5m, 24h:5m|1h, 7d:1h|1d, 30d:1d, 90d:1d
        entity (str | Unset): outcomes: only events that update this entity
        funnel (str | Unset): funnel: funnel name, default the first declared
        side (str | Unset): Filter by the actor_side role
        client_query (str | Unset): Filter by the client role

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivityWorkspaceSeries | ErrorModel
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            environment=environment,
            metric=metric,
            window=window,
            bucket=bucket,
            entity=entity,
            funnel=funnel,
            side=side,
            client_query=client_query,
        )
    ).parsed
