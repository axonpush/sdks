from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.get_output_body import GetOutputBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    trace_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["since"] = since

    params["until"] = until

    params["traceId"] = trace_id

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/audit-trail",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | GetOutputBody:
    if response.status_code == 200:
        response_200 = GetOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | GetOutputBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    trace_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ErrorModel | GetOutputBody]:
    """Query and export the decision audit trail

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now
        trace_id (str | Unset): Restrict to a single trace
        limit (int | Unset): Max rows (default 1000, max 10000)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | GetOutputBody]
    """

    kwargs = _get_kwargs(
        since=since,
        until=until,
        trace_id=trace_id,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    trace_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ErrorModel | GetOutputBody | None:
    """Query and export the decision audit trail

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now
        trace_id (str | Unset): Restrict to a single trace
        limit (int | Unset): Max rows (default 1000, max 10000)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | GetOutputBody
    """

    return sync_detailed(
        client=client,
        since=since,
        until=until,
        trace_id=trace_id,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    trace_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ErrorModel | GetOutputBody]:
    """Query and export the decision audit trail

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now
        trace_id (str | Unset): Restrict to a single trace
        limit (int | Unset): Max rows (default 1000, max 10000)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | GetOutputBody]
    """

    kwargs = _get_kwargs(
        since=since,
        until=until,
        trace_id=trace_id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    trace_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ErrorModel | GetOutputBody | None:
    """Query and export the decision audit trail

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now
        trace_id (str | Unset): Restrict to a single trace
        limit (int | Unset): Max rows (default 1000, max 10000)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | GetOutputBody
    """

    return (
        await asyncio_detailed(
            client=client,
            since=since,
            until=until,
            trace_id=trace_id,
            limit=limit,
        )
    ).parsed
