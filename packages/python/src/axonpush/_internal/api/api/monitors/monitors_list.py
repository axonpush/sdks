from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_model import ErrorModel
from ...models.list_monitors_output_body import ListMonitorsOutputBody
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["appId"] = app_id

    params["environmentId"] = environment_id

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/monitors",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | ListMonitorsOutputBody:
    if response.status_code == 200:
        response_200 = ListMonitorsOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | ListMonitorsOutputBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ErrorModel | ListMonitorsOutputBody]:
    """List cron monitors with status, schedule and recent check-ins

    Args:
        app_id (str | Unset): Filter by app
        environment_id (str | Unset): Filter by environment (id or slug)
        limit (int | Unset): Max monitors (default 50, max 500)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ListMonitorsOutputBody]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        environment_id=environment_id,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ErrorModel | ListMonitorsOutputBody | None:
    """List cron monitors with status, schedule and recent check-ins

    Args:
        app_id (str | Unset): Filter by app
        environment_id (str | Unset): Filter by environment (id or slug)
        limit (int | Unset): Max monitors (default 50, max 500)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ListMonitorsOutputBody
    """

    return sync_detailed(
        client=client,
        app_id=app_id,
        environment_id=environment_id,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ErrorModel | ListMonitorsOutputBody]:
    """List cron monitors with status, schedule and recent check-ins

    Args:
        app_id (str | Unset): Filter by app
        environment_id (str | Unset): Filter by environment (id or slug)
        limit (int | Unset): Max monitors (default 50, max 500)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ListMonitorsOutputBody]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        environment_id=environment_id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ErrorModel | ListMonitorsOutputBody | None:
    """List cron monitors with status, schedule and recent check-ins

    Args:
        app_id (str | Unset): Filter by app
        environment_id (str | Unset): Filter by environment (id or slug)
        limit (int | Unset): Max monitors (default 50, max 500)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ListMonitorsOutputBody
    """

    return (
        await asyncio_detailed(
            client=client,
            app_id=app_id,
            environment_id=environment_id,
            limit=limit,
        )
    ).parsed
