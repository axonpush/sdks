from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.test_output_body import TestOutputBody
from ...types import UNSET, Response


def _get_kwargs(
    destination_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/export-destinations/{destination_id}/test".format(
            destination_id=quote(str(destination_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | TestOutputBody:
    if response.status_code == 202:
        response_202 = TestOutputBody.from_dict(response.json())

        return response_202

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | TestOutputBody]:
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
) -> Response[ErrorModel | TestOutputBody]:
    """Send a synthetic test event to an export destination

    Args:
        destination_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | TestOutputBody]
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
) -> ErrorModel | TestOutputBody | None:
    """Send a synthetic test event to an export destination

    Args:
        destination_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | TestOutputBody
    """

    return sync_detailed(
        destination_id=destination_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    destination_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorModel | TestOutputBody]:
    """Send a synthetic test event to an export destination

    Args:
        destination_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | TestOutputBody]
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
) -> ErrorModel | TestOutputBody | None:
    """Send a synthetic test event to an export destination

    Args:
        destination_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | TestOutputBody
    """

    return (
        await asyncio_detailed(
            destination_id=destination_id,
            client=client,
        )
    ).parsed
