from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.trace_intelligence_coverage_response_dto import TraceIntelligenceCoverageResponseDto
from ...types import UNSET, Response


def _get_kwargs(
    *,
    app_id: str,
    environment_id: str,
    from_: str,
    to: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["appId"] = app_id

    params["environmentId"] = environment_id

    params["from"] = from_

    params["to"] = to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/trace-intelligence/coverage",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TraceIntelligenceCoverageResponseDto | None:
    if response.status_code == 200:
        response_200 = TraceIntelligenceCoverageResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TraceIntelligenceCoverageResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    app_id: str,
    environment_id: str,
    from_: str,
    to: str,
) -> Response[TraceIntelligenceCoverageResponseDto]:
    """
    Args:
        app_id (str):
        environment_id (str):
        from_ (str):
        to (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TraceIntelligenceCoverageResponseDto]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        environment_id=environment_id,
        from_=from_,
        to=to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    app_id: str,
    environment_id: str,
    from_: str,
    to: str,
) -> TraceIntelligenceCoverageResponseDto | None:
    """
    Args:
        app_id (str):
        environment_id (str):
        from_ (str):
        to (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TraceIntelligenceCoverageResponseDto
    """

    return sync_detailed(
        client=client,
        app_id=app_id,
        environment_id=environment_id,
        from_=from_,
        to=to,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    app_id: str,
    environment_id: str,
    from_: str,
    to: str,
) -> Response[TraceIntelligenceCoverageResponseDto]:
    """
    Args:
        app_id (str):
        environment_id (str):
        from_ (str):
        to (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TraceIntelligenceCoverageResponseDto]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        environment_id=environment_id,
        from_=from_,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    app_id: str,
    environment_id: str,
    from_: str,
    to: str,
) -> TraceIntelligenceCoverageResponseDto | None:
    """
    Args:
        app_id (str):
        environment_id (str):
        from_ (str):
        to (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TraceIntelligenceCoverageResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            app_id=app_id,
            environment_id=environment_id,
            from_=from_,
            to=to,
        )
    ).parsed
