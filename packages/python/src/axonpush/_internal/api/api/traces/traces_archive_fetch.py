from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.archive_fetch_output_body import ArchiveFetchOutputBody
from ...models.error_model import ErrorModel
from ...types import UNSET, Response


def _get_kwargs(
    trace_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/traces/{trace_id}/archive-fetch".format(
            trace_id=quote(str(trace_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ArchiveFetchOutputBody | ErrorModel:
    if response.status_code == 202:
        response_202 = ArchiveFetchOutputBody.from_dict(response.json())

        return response_202

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ArchiveFetchOutputBody | ErrorModel]:
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
) -> Response[ArchiveFetchOutputBody | ErrorModel]:
    """Load an archived trace into the short-lived read cache

     Use when GET /traces/{traceId} answers 404 with errors[].value ARCHIVED. Idempotent per caller while
    a fetch is live; poll archive.fetchStatus, then read traces.getArchived.

    Args:
        trace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArchiveFetchOutputBody | ErrorModel]
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
) -> ArchiveFetchOutputBody | ErrorModel | None:
    """Load an archived trace into the short-lived read cache

     Use when GET /traces/{traceId} answers 404 with errors[].value ARCHIVED. Idempotent per caller while
    a fetch is live; poll archive.fetchStatus, then read traces.getArchived.

    Args:
        trace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArchiveFetchOutputBody | ErrorModel
    """

    return sync_detailed(
        trace_id=trace_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    trace_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ArchiveFetchOutputBody | ErrorModel]:
    """Load an archived trace into the short-lived read cache

     Use when GET /traces/{traceId} answers 404 with errors[].value ARCHIVED. Idempotent per caller while
    a fetch is live; poll archive.fetchStatus, then read traces.getArchived.

    Args:
        trace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArchiveFetchOutputBody | ErrorModel]
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
) -> ArchiveFetchOutputBody | ErrorModel | None:
    """Load an archived trace into the short-lived read cache

     Use when GET /traces/{traceId} answers 404 with errors[].value ARCHIVED. Idempotent per caller while
    a fetch is live; poll archive.fetchStatus, then read traces.getArchived.

    Args:
        trace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArchiveFetchOutputBody | ErrorModel
    """

    return (
        await asyncio_detailed(
            trace_id=trace_id,
            client=client,
        )
    ).parsed
