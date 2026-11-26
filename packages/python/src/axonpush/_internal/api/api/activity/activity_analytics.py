from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_analytics import ActivityAnalytics
from ...models.activity_analytics_window import ActivityAnalyticsWindow
from ...models.error_model import ErrorModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: str,
    *,
    fresh: bool | Unset = UNSET,
    environment: str | Unset = UNSET,
    window: ActivityAnalyticsWindow | Unset = ActivityAnalyticsWindow.VALUE_0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["fresh"] = fresh

    params["environment"] = environment

    json_window: str | Unset = UNSET
    if not isinstance(window, Unset):
        json_window = window.value

    params["window"] = json_window

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspaces/{workspace_id}/analytics".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActivityAnalytics | ErrorModel:
    if response.status_code == 200:
        response_200 = ActivityAnalytics.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ActivityAnalytics | ErrorModel]:
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
    fresh: bool | Unset = UNSET,
    environment: str | Unset = UNSET,
    window: ActivityAnalyticsWindow | Unset = ActivityAnalyticsWindow.VALUE_0,
) -> Response[ActivityAnalytics | ErrorModel]:
    """Distinct funnel milestones, funnel splits and client breakdowns; snapshots never count

    Args:
        workspace_id (str):
        fresh (bool | Unset): Bypass the 15-second summary cache
        environment (str | Unset):
        window (ActivityAnalyticsWindow | Unset): 90d reads de-identified daily rollups and is
            refused for scoped access Default: ActivityAnalyticsWindow.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivityAnalytics | ErrorModel]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        fresh=fresh,
        environment=environment,
        window=window,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    fresh: bool | Unset = UNSET,
    environment: str | Unset = UNSET,
    window: ActivityAnalyticsWindow | Unset = ActivityAnalyticsWindow.VALUE_0,
) -> ActivityAnalytics | ErrorModel | None:
    """Distinct funnel milestones, funnel splits and client breakdowns; snapshots never count

    Args:
        workspace_id (str):
        fresh (bool | Unset): Bypass the 15-second summary cache
        environment (str | Unset):
        window (ActivityAnalyticsWindow | Unset): 90d reads de-identified daily rollups and is
            refused for scoped access Default: ActivityAnalyticsWindow.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivityAnalytics | ErrorModel
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        fresh=fresh,
        environment=environment,
        window=window,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    fresh: bool | Unset = UNSET,
    environment: str | Unset = UNSET,
    window: ActivityAnalyticsWindow | Unset = ActivityAnalyticsWindow.VALUE_0,
) -> Response[ActivityAnalytics | ErrorModel]:
    """Distinct funnel milestones, funnel splits and client breakdowns; snapshots never count

    Args:
        workspace_id (str):
        fresh (bool | Unset): Bypass the 15-second summary cache
        environment (str | Unset):
        window (ActivityAnalyticsWindow | Unset): 90d reads de-identified daily rollups and is
            refused for scoped access Default: ActivityAnalyticsWindow.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivityAnalytics | ErrorModel]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        fresh=fresh,
        environment=environment,
        window=window,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    fresh: bool | Unset = UNSET,
    environment: str | Unset = UNSET,
    window: ActivityAnalyticsWindow | Unset = ActivityAnalyticsWindow.VALUE_0,
) -> ActivityAnalytics | ErrorModel | None:
    """Distinct funnel milestones, funnel splits and client breakdowns; snapshots never count

    Args:
        workspace_id (str):
        fresh (bool | Unset): Bypass the 15-second summary cache
        environment (str | Unset):
        window (ActivityAnalyticsWindow | Unset): 90d reads de-identified daily rollups and is
            refused for scoped access Default: ActivityAnalyticsWindow.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivityAnalytics | ErrorModel
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            fresh=fresh,
            environment=environment,
            window=window,
        )
    ).parsed
