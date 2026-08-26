from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_trace_intelligence_backfill_dto import CreateTraceIntelligenceBackfillDto
from ...models.trace_intelligence_backfill_response_dto import TraceIntelligenceBackfillResponseDto
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: CreateTraceIntelligenceBackfillDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/trace-intelligence/backfills",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TraceIntelligenceBackfillResponseDto | None:
    if response.status_code == 201:
        response_201 = TraceIntelligenceBackfillResponseDto.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TraceIntelligenceBackfillResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateTraceIntelligenceBackfillDto,
) -> Response[TraceIntelligenceBackfillResponseDto]:
    """
    Args:
        body (CreateTraceIntelligenceBackfillDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TraceIntelligenceBackfillResponseDto]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateTraceIntelligenceBackfillDto,
) -> TraceIntelligenceBackfillResponseDto | None:
    """
    Args:
        body (CreateTraceIntelligenceBackfillDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TraceIntelligenceBackfillResponseDto
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateTraceIntelligenceBackfillDto,
) -> Response[TraceIntelligenceBackfillResponseDto]:
    """
    Args:
        body (CreateTraceIntelligenceBackfillDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TraceIntelligenceBackfillResponseDto]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateTraceIntelligenceBackfillDto,
) -> TraceIntelligenceBackfillResponseDto | None:
    """
    Args:
        body (CreateTraceIntelligenceBackfillDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TraceIntelligenceBackfillResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
