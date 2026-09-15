from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.list_output_body_2 import ListOutputBody2
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    action: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    before: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["action"] = action

    params["resourceType"] = resource_type

    params["before"] = before

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/audit-logs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | ListOutputBody2:
    if response.status_code == 200:
        response_200 = ListOutputBody2.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | ListOutputBody2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    action: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    before: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> Response[ErrorModel | ListOutputBody2]:
    """List audit log entries

    Args:
        action (str | Unset):
        resource_type (str | Unset):
        before (str | Unset): RFC3339 upper bound (exclusive); defaults to now
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ListOutputBody2]
    """

    kwargs = _get_kwargs(
        action=action,
        resource_type=resource_type,
        before=before,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    action: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    before: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> ErrorModel | ListOutputBody2 | None:
    """List audit log entries

    Args:
        action (str | Unset):
        resource_type (str | Unset):
        before (str | Unset): RFC3339 upper bound (exclusive); defaults to now
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ListOutputBody2
    """

    return sync_detailed(
        client=client,
        action=action,
        resource_type=resource_type,
        before=before,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    action: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    before: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> Response[ErrorModel | ListOutputBody2]:
    """List audit log entries

    Args:
        action (str | Unset):
        resource_type (str | Unset):
        before (str | Unset): RFC3339 upper bound (exclusive); defaults to now
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ListOutputBody2]
    """

    kwargs = _get_kwargs(
        action=action,
        resource_type=resource_type,
        before=before,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    action: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    before: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> ErrorModel | ListOutputBody2 | None:
    """List audit log entries

    Args:
        action (str | Unset):
        resource_type (str | Unset):
        before (str | Unset): RFC3339 upper bound (exclusive); defaults to now
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ListOutputBody2
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            resource_type=resource_type,
            before=before,
            limit=limit,
        )
    ).parsed
