from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.event_body import EventBody
from ...models.event_output_body import EventOutputBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: EventBody,
    x_axonpush_api_key: str | Unset = UNSET,
    x_api_key: str | Unset = UNSET,
    x_public_token: str | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_axonpush_api_key, Unset):
        headers["x-axonpush-api-key"] = x_axonpush_api_key

    if not isinstance(x_api_key, Unset):
        headers["x-api-key"] = x_api_key

    if not isinstance(x_public_token, Unset):
        headers["x-public-token"] = x_public_token

    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/event",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | EventOutputBody:
    if response.status_code == 200:
        response_200 = EventOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | EventOutputBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: EventBody,
    x_axonpush_api_key: str | Unset = UNSET,
    x_api_key: str | Unset = UNSET,
    x_public_token: str | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> Response[ErrorModel | EventOutputBody]:
    """Ingest a single event

    Args:
        x_axonpush_api_key (str | Unset):
        x_api_key (str | Unset):
        x_public_token (str | Unset):
        authorization (str | Unset):
        body (EventBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | EventOutputBody]
    """

    kwargs = _get_kwargs(
        body=body,
        x_axonpush_api_key=x_axonpush_api_key,
        x_api_key=x_api_key,
        x_public_token=x_public_token,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: EventBody,
    x_axonpush_api_key: str | Unset = UNSET,
    x_api_key: str | Unset = UNSET,
    x_public_token: str | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> ErrorModel | EventOutputBody | None:
    """Ingest a single event

    Args:
        x_axonpush_api_key (str | Unset):
        x_api_key (str | Unset):
        x_public_token (str | Unset):
        authorization (str | Unset):
        body (EventBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | EventOutputBody
    """

    return sync_detailed(
        client=client,
        body=body,
        x_axonpush_api_key=x_axonpush_api_key,
        x_api_key=x_api_key,
        x_public_token=x_public_token,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: EventBody,
    x_axonpush_api_key: str | Unset = UNSET,
    x_api_key: str | Unset = UNSET,
    x_public_token: str | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> Response[ErrorModel | EventOutputBody]:
    """Ingest a single event

    Args:
        x_axonpush_api_key (str | Unset):
        x_api_key (str | Unset):
        x_public_token (str | Unset):
        authorization (str | Unset):
        body (EventBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | EventOutputBody]
    """

    kwargs = _get_kwargs(
        body=body,
        x_axonpush_api_key=x_axonpush_api_key,
        x_api_key=x_api_key,
        x_public_token=x_public_token,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: EventBody,
    x_axonpush_api_key: str | Unset = UNSET,
    x_api_key: str | Unset = UNSET,
    x_public_token: str | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> ErrorModel | EventOutputBody | None:
    """Ingest a single event

    Args:
        x_axonpush_api_key (str | Unset):
        x_api_key (str | Unset):
        x_public_token (str | Unset):
        authorization (str | Unset):
        body (EventBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | EventOutputBody
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_axonpush_api_key=x_axonpush_api_key,
            x_api_key=x_api_key,
            x_public_token=x_public_token,
            authorization=authorization,
        )
    ).parsed
