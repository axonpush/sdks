from http import HTTPStatus
from io import BytesIO
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.webhook_output_body import WebhookOutputBody
from ...types import UNSET, File, FileTypes, Response, Unset


def _get_kwargs(
    *,
    body: File,
    webhook_id: str | Unset = UNSET,
    webhook_timestamp: str | Unset = UNSET,
    webhook_signature: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(webhook_id, Unset):
        headers["webhook-id"] = webhook_id

    if not isinstance(webhook_timestamp, Unset):
        headers["webhook-timestamp"] = webhook_timestamp

    if not isinstance(webhook_signature, Unset):
        headers["webhook-signature"] = webhook_signature

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/billing/webhook",
    }

    _kwargs["content"] = body.payload

    headers["Content-Type"] = "application/octet-stream"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | WebhookOutputBody:
    if response.status_code == 200:
        response_200 = WebhookOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | WebhookOutputBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: File,
    webhook_id: str | Unset = UNSET,
    webhook_timestamp: str | Unset = UNSET,
    webhook_signature: str | Unset = UNSET,
) -> Response[ErrorModel | WebhookOutputBody]:
    """Polar webhook

     Receives Polar subscription and order events, signed with Standard Webhooks.

    Args:
        webhook_id (str | Unset):
        webhook_timestamp (str | Unset):
        webhook_signature (str | Unset):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | WebhookOutputBody]
    """

    kwargs = _get_kwargs(
        body=body,
        webhook_id=webhook_id,
        webhook_timestamp=webhook_timestamp,
        webhook_signature=webhook_signature,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: File,
    webhook_id: str | Unset = UNSET,
    webhook_timestamp: str | Unset = UNSET,
    webhook_signature: str | Unset = UNSET,
) -> ErrorModel | WebhookOutputBody | None:
    """Polar webhook

     Receives Polar subscription and order events, signed with Standard Webhooks.

    Args:
        webhook_id (str | Unset):
        webhook_timestamp (str | Unset):
        webhook_signature (str | Unset):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | WebhookOutputBody
    """

    return sync_detailed(
        client=client,
        body=body,
        webhook_id=webhook_id,
        webhook_timestamp=webhook_timestamp,
        webhook_signature=webhook_signature,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: File,
    webhook_id: str | Unset = UNSET,
    webhook_timestamp: str | Unset = UNSET,
    webhook_signature: str | Unset = UNSET,
) -> Response[ErrorModel | WebhookOutputBody]:
    """Polar webhook

     Receives Polar subscription and order events, signed with Standard Webhooks.

    Args:
        webhook_id (str | Unset):
        webhook_timestamp (str | Unset):
        webhook_signature (str | Unset):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | WebhookOutputBody]
    """

    kwargs = _get_kwargs(
        body=body,
        webhook_id=webhook_id,
        webhook_timestamp=webhook_timestamp,
        webhook_signature=webhook_signature,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: File,
    webhook_id: str | Unset = UNSET,
    webhook_timestamp: str | Unset = UNSET,
    webhook_signature: str | Unset = UNSET,
) -> ErrorModel | WebhookOutputBody | None:
    """Polar webhook

     Receives Polar subscription and order events, signed with Standard Webhooks.

    Args:
        webhook_id (str | Unset):
        webhook_timestamp (str | Unset):
        webhook_signature (str | Unset):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | WebhookOutputBody
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            webhook_id=webhook_id,
            webhook_timestamp=webhook_timestamp,
            webhook_signature=webhook_signature,
        )
    ).parsed
