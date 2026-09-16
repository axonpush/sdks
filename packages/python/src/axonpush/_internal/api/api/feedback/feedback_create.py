from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_input_body_3 import CreateInputBody3
from ...models.create_output_body import CreateOutputBody
from ...models.error_model import ErrorModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateInputBody3,
    cf_connecting_ip: str | Unset = UNSET,
    x_forwarded_for: str | Unset = UNSET,
    x_real_ip: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(cf_connecting_ip, Unset):
        headers["CF-Connecting-IP"] = cf_connecting_ip

    if not isinstance(x_forwarded_for, Unset):
        headers["X-Forwarded-For"] = x_forwarded_for

    if not isinstance(x_real_ip, Unset):
        headers["X-Real-IP"] = x_real_ip

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/feedback",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateOutputBody | ErrorModel:
    if response.status_code == 201:
        response_201 = CreateOutputBody.from_dict(response.json())

        return response_201

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateOutputBody | ErrorModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateInputBody3,
    cf_connecting_ip: str | Unset = UNSET,
    x_forwarded_for: str | Unset = UNSET,
    x_real_ip: str | Unset = UNSET,
) -> Response[CreateOutputBody | ErrorModel]:
    """Submit feedback

    Args:
        cf_connecting_ip (str | Unset):
        x_forwarded_for (str | Unset):
        x_real_ip (str | Unset):
        body (CreateInputBody3):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateOutputBody | ErrorModel]
    """

    kwargs = _get_kwargs(
        body=body,
        cf_connecting_ip=cf_connecting_ip,
        x_forwarded_for=x_forwarded_for,
        x_real_ip=x_real_ip,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateInputBody3,
    cf_connecting_ip: str | Unset = UNSET,
    x_forwarded_for: str | Unset = UNSET,
    x_real_ip: str | Unset = UNSET,
) -> CreateOutputBody | ErrorModel | None:
    """Submit feedback

    Args:
        cf_connecting_ip (str | Unset):
        x_forwarded_for (str | Unset):
        x_real_ip (str | Unset):
        body (CreateInputBody3):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateOutputBody | ErrorModel
    """

    return sync_detailed(
        client=client,
        body=body,
        cf_connecting_ip=cf_connecting_ip,
        x_forwarded_for=x_forwarded_for,
        x_real_ip=x_real_ip,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateInputBody3,
    cf_connecting_ip: str | Unset = UNSET,
    x_forwarded_for: str | Unset = UNSET,
    x_real_ip: str | Unset = UNSET,
) -> Response[CreateOutputBody | ErrorModel]:
    """Submit feedback

    Args:
        cf_connecting_ip (str | Unset):
        x_forwarded_for (str | Unset):
        x_real_ip (str | Unset):
        body (CreateInputBody3):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateOutputBody | ErrorModel]
    """

    kwargs = _get_kwargs(
        body=body,
        cf_connecting_ip=cf_connecting_ip,
        x_forwarded_for=x_forwarded_for,
        x_real_ip=x_real_ip,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateInputBody3,
    cf_connecting_ip: str | Unset = UNSET,
    x_forwarded_for: str | Unset = UNSET,
    x_real_ip: str | Unset = UNSET,
) -> CreateOutputBody | ErrorModel | None:
    """Submit feedback

    Args:
        cf_connecting_ip (str | Unset):
        x_forwarded_for (str | Unset):
        x_real_ip (str | Unset):
        body (CreateInputBody3):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateOutputBody | ErrorModel
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            cf_connecting_ip=cf_connecting_ip,
            x_forwarded_for=x_forwarded_for,
            x_real_ip=x_real_ip,
        )
    ).parsed
