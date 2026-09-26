from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dashboard_body import DashboardBody
from ...models.dashboard_view import DashboardView
from ...models.error_model import ErrorModel
from ...types import UNSET, Response


def _get_kwargs(
    dashboard_id: str,
    *,
    body: DashboardBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/dashboards/{dashboard_id}".format(
            dashboard_id=quote(str(dashboard_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DashboardView | ErrorModel:
    if response.status_code == 200:
        response_200 = DashboardView.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DashboardView | ErrorModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dashboard_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DashboardBody,
) -> Response[DashboardView | ErrorModel]:
    """Update a saved dashboard

    Args:
        dashboard_id (str):
        body (DashboardBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DashboardView | ErrorModel]
    """

    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dashboard_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DashboardBody,
) -> DashboardView | ErrorModel | None:
    """Update a saved dashboard

    Args:
        dashboard_id (str):
        body (DashboardBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DashboardView | ErrorModel
    """

    return sync_detailed(
        dashboard_id=dashboard_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dashboard_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DashboardBody,
) -> Response[DashboardView | ErrorModel]:
    """Update a saved dashboard

    Args:
        dashboard_id (str):
        body (DashboardBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DashboardView | ErrorModel]
    """

    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dashboard_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DashboardBody,
) -> DashboardView | ErrorModel | None:
    """Update a saved dashboard

    Args:
        dashboard_id (str):
        body (DashboardBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DashboardView | ErrorModel
    """

    return (
        await asyncio_detailed(
            dashboard_id=dashboard_id,
            client=client,
            body=body,
        )
    ).parsed
