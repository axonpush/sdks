from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_model import ErrorModel
from ...models.list_attachments_output_body import ListAttachmentsOutputBody
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    event_id: str | Unset = UNSET,
    trace_id: str | Unset = UNSET,
    span_id: str | Unset = UNSET,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["eventId"] = event_id

    params["traceId"] = trace_id

    params["spanId"] = span_id

    params["appId"] = app_id

    params["environmentId"] = environment_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/attachments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | ListAttachmentsOutputBody:
    if response.status_code == 200:
        response_200 = ListAttachmentsOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | ListAttachmentsOutputBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    event_id: str | Unset = UNSET,
    trace_id: str | Unset = UNSET,
    span_id: str | Unset = UNSET,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
) -> Response[ErrorModel | ListAttachmentsOutputBody]:
    """List attachment metadata for a Sentry event, trace or span

    Args:
        event_id (str | Unset): Sentry event id
        trace_id (str | Unset):
        span_id (str | Unset):
        app_id (str | Unset):
        environment_id (str | Unset): Environment slug or id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ListAttachmentsOutputBody]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        trace_id=trace_id,
        span_id=span_id,
        app_id=app_id,
        environment_id=environment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    event_id: str | Unset = UNSET,
    trace_id: str | Unset = UNSET,
    span_id: str | Unset = UNSET,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
) -> ErrorModel | ListAttachmentsOutputBody | None:
    """List attachment metadata for a Sentry event, trace or span

    Args:
        event_id (str | Unset): Sentry event id
        trace_id (str | Unset):
        span_id (str | Unset):
        app_id (str | Unset):
        environment_id (str | Unset): Environment slug or id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ListAttachmentsOutputBody
    """

    return sync_detailed(
        client=client,
        event_id=event_id,
        trace_id=trace_id,
        span_id=span_id,
        app_id=app_id,
        environment_id=environment_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    event_id: str | Unset = UNSET,
    trace_id: str | Unset = UNSET,
    span_id: str | Unset = UNSET,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
) -> Response[ErrorModel | ListAttachmentsOutputBody]:
    """List attachment metadata for a Sentry event, trace or span

    Args:
        event_id (str | Unset): Sentry event id
        trace_id (str | Unset):
        span_id (str | Unset):
        app_id (str | Unset):
        environment_id (str | Unset): Environment slug or id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ListAttachmentsOutputBody]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        trace_id=trace_id,
        span_id=span_id,
        app_id=app_id,
        environment_id=environment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    event_id: str | Unset = UNSET,
    trace_id: str | Unset = UNSET,
    span_id: str | Unset = UNSET,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
) -> ErrorModel | ListAttachmentsOutputBody | None:
    """List attachment metadata for a Sentry event, trace or span

    Args:
        event_id (str | Unset): Sentry event id
        trace_id (str | Unset):
        span_id (str | Unset):
        app_id (str | Unset):
        environment_id (str | Unset): Environment slug or id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ListAttachmentsOutputBody
    """

    return (
        await asyncio_detailed(
            client=client,
            event_id=event_id,
            trace_id=trace_id,
            span_id=span_id,
            app_id=app_id,
            environment_id=environment_id,
        )
    ).parsed
