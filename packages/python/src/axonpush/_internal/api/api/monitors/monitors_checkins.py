from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_model import ErrorModel
from ...models.list_monitor_check_ins_output_body import ListMonitorCheckInsOutputBody
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    monitor_id: str,
    *,
    before: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["before"] = before

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/monitors/{monitor_id}/checkins".format(
            monitor_id=quote(str(monitor_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | ListMonitorCheckInsOutputBody:
    if response.status_code == 200:
        response_200 = ListMonitorCheckInsOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | ListMonitorCheckInsOutputBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    monitor_id: str,
    *,
    client: AuthenticatedClient | Client,
    before: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ErrorModel | ListMonitorCheckInsOutputBody]:
    """List a cron monitor's check-ins, newest first (older paging)

    Args:
        monitor_id (str):
        before (str | Unset): Keyset upper bound (RFC3339, exclusive) on startedAt for older
            check-ins
        limit (int | Unset): Max check-ins (default 50, max 500)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ListMonitorCheckInsOutputBody]
    """

    kwargs = _get_kwargs(
        monitor_id=monitor_id,
        before=before,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    monitor_id: str,
    *,
    client: AuthenticatedClient | Client,
    before: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ErrorModel | ListMonitorCheckInsOutputBody | None:
    """List a cron monitor's check-ins, newest first (older paging)

    Args:
        monitor_id (str):
        before (str | Unset): Keyset upper bound (RFC3339, exclusive) on startedAt for older
            check-ins
        limit (int | Unset): Max check-ins (default 50, max 500)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ListMonitorCheckInsOutputBody
    """

    return sync_detailed(
        monitor_id=monitor_id,
        client=client,
        before=before,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    monitor_id: str,
    *,
    client: AuthenticatedClient | Client,
    before: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ErrorModel | ListMonitorCheckInsOutputBody]:
    """List a cron monitor's check-ins, newest first (older paging)

    Args:
        monitor_id (str):
        before (str | Unset): Keyset upper bound (RFC3339, exclusive) on startedAt for older
            check-ins
        limit (int | Unset): Max check-ins (default 50, max 500)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ListMonitorCheckInsOutputBody]
    """

    kwargs = _get_kwargs(
        monitor_id=monitor_id,
        before=before,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    monitor_id: str,
    *,
    client: AuthenticatedClient | Client,
    before: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ErrorModel | ListMonitorCheckInsOutputBody | None:
    """List a cron monitor's check-ins, newest first (older paging)

    Args:
        monitor_id (str):
        before (str | Unset): Keyset upper bound (RFC3339, exclusive) on startedAt for older
            check-ins
        limit (int | Unset): Max check-ins (default 50, max 500)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ListMonitorCheckInsOutputBody
    """

    return (
        await asyncio_detailed(
            monitor_id=monitor_id,
            client=client,
            before=before,
            limit=limit,
        )
    ).parsed
