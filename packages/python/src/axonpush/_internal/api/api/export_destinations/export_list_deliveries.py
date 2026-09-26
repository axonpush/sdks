from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.list_deliveries_output_body_1 import ListDeliveriesOutputBody1
from ...types import UNSET, Response


def _get_kwargs(
    destination_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/export-destinations/{destination_id}/deliveries".format(
            destination_id=quote(str(destination_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | ListDeliveriesOutputBody1:
    if response.status_code == 200:
        response_200 = ListDeliveriesOutputBody1.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | ListDeliveriesOutputBody1]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    destination_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorModel | ListDeliveriesOutputBody1]:
    """List recent export deliveries

    Args:
        destination_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ListDeliveriesOutputBody1]
    """

    kwargs = _get_kwargs(
        destination_id=destination_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    destination_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorModel | ListDeliveriesOutputBody1 | None:
    """List recent export deliveries

    Args:
        destination_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ListDeliveriesOutputBody1
    """

    return sync_detailed(
        destination_id=destination_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    destination_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorModel | ListDeliveriesOutputBody1]:
    """List recent export deliveries

    Args:
        destination_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ListDeliveriesOutputBody1]
    """

    kwargs = _get_kwargs(
        destination_id=destination_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    destination_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorModel | ListDeliveriesOutputBody1 | None:
    """List recent export deliveries

    Args:
        destination_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ListDeliveriesOutputBody1
    """

    return (
        await asyncio_detailed(
            destination_id=destination_id,
            client=client,
        )
    ).parsed
