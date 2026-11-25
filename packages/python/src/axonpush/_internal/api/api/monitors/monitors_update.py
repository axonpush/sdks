from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_model import ErrorModel
from ...models.monitor_dto import MonitorDTO
from ...models.update_monitor_input_body import UpdateMonitorInputBody
from typing import cast


def _get_kwargs(
    monitor_id: str,
    *,
    body: UpdateMonitorInputBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/monitors/{monitor_id}".format(
            monitor_id=quote(str(monitor_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | MonitorDTO:
    if response.status_code == 200:
        response_200 = MonitorDTO.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | MonitorDTO]:
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
    body: UpdateMonitorInputBody,
) -> Response[ErrorModel | MonitorDTO]:
    """Mute or unmute a cron monitor

    Args:
        monitor_id (str):
        body (UpdateMonitorInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | MonitorDTO]
    """

    kwargs = _get_kwargs(
        monitor_id=monitor_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    monitor_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateMonitorInputBody,
) -> ErrorModel | MonitorDTO | None:
    """Mute or unmute a cron monitor

    Args:
        monitor_id (str):
        body (UpdateMonitorInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | MonitorDTO
    """

    return sync_detailed(
        monitor_id=monitor_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    monitor_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateMonitorInputBody,
) -> Response[ErrorModel | MonitorDTO]:
    """Mute or unmute a cron monitor

    Args:
        monitor_id (str):
        body (UpdateMonitorInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | MonitorDTO]
    """

    kwargs = _get_kwargs(
        monitor_id=monitor_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    monitor_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateMonitorInputBody,
) -> ErrorModel | MonitorDTO | None:
    """Mute or unmute a cron monitor

    Args:
        monitor_id (str):
        body (UpdateMonitorInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | MonitorDTO
    """

    return (
        await asyncio_detailed(
            monitor_id=monitor_id,
            client=client,
            body=body,
        )
    ).parsed
