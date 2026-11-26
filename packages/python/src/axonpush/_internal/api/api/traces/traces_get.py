from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.get_trace_output_body import GetTraceOutputBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    trace_id: str,
    *,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/traces/{trace_id}".format(
            trace_id=quote(str(trace_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | GetTraceOutputBody:
    if response.status_code == 200:
        response_200 = GetTraceOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | GetTraceOutputBody]:
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
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[ErrorModel | GetTraceOutputBody]:
    """Get a trace's spans, ordered by time

    Args:
        trace_id (str):
        limit (int | Unset): Span page size (default 500)
        cursor (str | Unset): Continuation cursor from the previous page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | GetTraceOutputBody]
    """

    kwargs = _get_kwargs(
        trace_id=trace_id,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    trace_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> ErrorModel | GetTraceOutputBody | None:
    """Get a trace's spans, ordered by time

    Args:
        trace_id (str):
        limit (int | Unset): Span page size (default 500)
        cursor (str | Unset): Continuation cursor from the previous page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | GetTraceOutputBody
    """

    return sync_detailed(
        trace_id=trace_id,
        client=client,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    trace_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[ErrorModel | GetTraceOutputBody]:
    """Get a trace's spans, ordered by time

    Args:
        trace_id (str):
        limit (int | Unset): Span page size (default 500)
        cursor (str | Unset): Continuation cursor from the previous page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | GetTraceOutputBody]
    """

    kwargs = _get_kwargs(
        trace_id=trace_id,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    trace_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> ErrorModel | GetTraceOutputBody | None:
    """Get a trace's spans, ordered by time

    Args:
        trace_id (str):
        limit (int | Unset): Span page size (default 500)
        cursor (str | Unset): Continuation cursor from the previous page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | GetTraceOutputBody
    """

    return (
        await asyncio_detailed(
            trace_id=trace_id,
            client=client,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
