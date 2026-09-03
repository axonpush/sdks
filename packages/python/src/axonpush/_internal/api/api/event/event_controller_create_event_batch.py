from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_event_batch_dto import CreateEventBatchDto
from ...models.event_batch_ingest_response_dto import EventBatchIngestResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateEventBatchDto,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/event/batch",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EventBatchIngestResponseDto | None:
    if response.status_code == 202:
        response_202 = EventBatchIngestResponseDto.from_dict(response.json())

        return response_202

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EventBatchIngestResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateEventBatchDto,
    idempotency_key: str | Unset = UNSET,
) -> Response[EventBatchIngestResponseDto]:
    """Ingest up to 100 events in one request

    Args:
        idempotency_key (str | Unset):
        body (CreateEventBatchDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EventBatchIngestResponseDto]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateEventBatchDto,
    idempotency_key: str | Unset = UNSET,
) -> EventBatchIngestResponseDto | None:
    """Ingest up to 100 events in one request

    Args:
        idempotency_key (str | Unset):
        body (CreateEventBatchDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EventBatchIngestResponseDto
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateEventBatchDto,
    idempotency_key: str | Unset = UNSET,
) -> Response[EventBatchIngestResponseDto]:
    """Ingest up to 100 events in one request

    Args:
        idempotency_key (str | Unset):
        body (CreateEventBatchDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EventBatchIngestResponseDto]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateEventBatchDto,
    idempotency_key: str | Unset = UNSET,
) -> EventBatchIngestResponseDto | None:
    """Ingest up to 100 events in one request

    Args:
        idempotency_key (str | Unset):
        body (CreateEventBatchDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EventBatchIngestResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
