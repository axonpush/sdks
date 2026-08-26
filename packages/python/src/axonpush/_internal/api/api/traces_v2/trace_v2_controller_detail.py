from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.trace_detail_v2_response_dto import TraceDetailV2ResponseDto
from ...types import UNSET, Response


def _get_kwargs(
    trace_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/traces/{trace_id}".format(
            trace_id=quote(str(trace_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TraceDetailV2ResponseDto | None:
    if response.status_code == 200:
        response_200 = TraceDetailV2ResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TraceDetailV2ResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trace_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[TraceDetailV2ResponseDto]:
    """
    Args:
        trace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TraceDetailV2ResponseDto]
    """

    kwargs = _get_kwargs(
        trace_id=trace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    trace_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> TraceDetailV2ResponseDto | None:
    """
    Args:
        trace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TraceDetailV2ResponseDto
    """

    return sync_detailed(
        trace_id=trace_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    trace_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[TraceDetailV2ResponseDto]:
    """
    Args:
        trace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TraceDetailV2ResponseDto]
    """

    kwargs = _get_kwargs(
        trace_id=trace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    trace_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> TraceDetailV2ResponseDto | None:
    """
    Args:
        trace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TraceDetailV2ResponseDto
    """

    return (
        await asyncio_detailed(
            trace_id=trace_id,
            client=client,
        )
    ).parsed
