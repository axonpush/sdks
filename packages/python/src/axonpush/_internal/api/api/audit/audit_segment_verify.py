from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.verify_output_body import VerifyOutputBody
from ...types import UNSET, Response


def _get_kwargs(
    segment_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/audit/segments/{segment_id}/verify".format(
            segment_id=quote(str(segment_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | VerifyOutputBody:
    if response.status_code == 200:
        response_200 = VerifyOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | VerifyOutputBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    segment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorModel | VerifyOutputBody]:
    """Verify immutable archive bytes

    Args:
        segment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | VerifyOutputBody]
    """

    kwargs = _get_kwargs(
        segment_id=segment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    segment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorModel | VerifyOutputBody | None:
    """Verify immutable archive bytes

    Args:
        segment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | VerifyOutputBody
    """

    return sync_detailed(
        segment_id=segment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    segment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorModel | VerifyOutputBody]:
    """Verify immutable archive bytes

    Args:
        segment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | VerifyOutputBody]
    """

    kwargs = _get_kwargs(
        segment_id=segment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    segment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorModel | VerifyOutputBody | None:
    """Verify immutable archive bytes

    Args:
        segment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | VerifyOutputBody
    """

    return (
        await asyncio_detailed(
            segment_id=segment_id,
            client=client,
        )
    ).parsed
