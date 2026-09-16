from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.destination_dto import DestinationDTO
from ...models.error_model import ErrorModel
from ...models.update_input_body_1 import UpdateInputBody1
from ...types import UNSET, Response


def _get_kwargs(
    destination_id: str,
    *,
    body: UpdateInputBody1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/export-destinations/{destination_id}".format(
            destination_id=quote(str(destination_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DestinationDTO | ErrorModel:
    if response.status_code == 200:
        response_200 = DestinationDTO.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DestinationDTO | ErrorModel]:
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
    body: UpdateInputBody1,
) -> Response[DestinationDTO | ErrorModel]:
    """Update an export destination

    Args:
        destination_id (str):
        body (UpdateInputBody1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DestinationDTO | ErrorModel]
    """

    kwargs = _get_kwargs(
        destination_id=destination_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    destination_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateInputBody1,
) -> DestinationDTO | ErrorModel | None:
    """Update an export destination

    Args:
        destination_id (str):
        body (UpdateInputBody1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DestinationDTO | ErrorModel
    """

    return sync_detailed(
        destination_id=destination_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    destination_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateInputBody1,
) -> Response[DestinationDTO | ErrorModel]:
    """Update an export destination

    Args:
        destination_id (str):
        body (UpdateInputBody1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DestinationDTO | ErrorModel]
    """

    kwargs = _get_kwargs(
        destination_id=destination_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    destination_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateInputBody1,
) -> DestinationDTO | ErrorModel | None:
    """Update an export destination

    Args:
        destination_id (str):
        body (UpdateInputBody1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DestinationDTO | ErrorModel
    """

    return (
        await asyncio_detailed(
            destination_id=destination_id,
            client=client,
            body=body,
        )
    ).parsed
