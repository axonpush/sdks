from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.test_trace_intelligence_provider_dto import TestTraceIntelligenceProviderDto
from ...models.trace_intelligence_provider_test_response_dto import (
    TraceIntelligenceProviderTestResponseDto,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: TestTraceIntelligenceProviderDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/trace-intelligence/settings/provider/test",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TraceIntelligenceProviderTestResponseDto | None:
    if response.status_code == 201:
        response_201 = TraceIntelligenceProviderTestResponseDto.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TraceIntelligenceProviderTestResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TestTraceIntelligenceProviderDto,
) -> Response[TraceIntelligenceProviderTestResponseDto]:
    """
    Args:
        body (TestTraceIntelligenceProviderDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TraceIntelligenceProviderTestResponseDto]
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
    body: TestTraceIntelligenceProviderDto,
) -> TraceIntelligenceProviderTestResponseDto | None:
    """
    Args:
        body (TestTraceIntelligenceProviderDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TraceIntelligenceProviderTestResponseDto
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TestTraceIntelligenceProviderDto,
) -> Response[TraceIntelligenceProviderTestResponseDto]:
    """
    Args:
        body (TestTraceIntelligenceProviderDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TraceIntelligenceProviderTestResponseDto]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TestTraceIntelligenceProviderDto,
) -> TraceIntelligenceProviderTestResponseDto | None:
    """
    Args:
        body (TestTraceIntelligenceProviderDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TraceIntelligenceProviderTestResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
