from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_input_body_4 import CreateInputBody4
from ...models.create_output_body_1 import CreateOutputBody1
from ...models.error_model import ErrorModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateInputBody4,
    cf_connecting_ip: str | Unset = UNSET,
    x_forwarded_for: str | Unset = UNSET,
    x_real_ip: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    cf_ip_country: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(cf_connecting_ip, Unset):
        headers["CF-Connecting-IP"] = cf_connecting_ip

    if not isinstance(x_forwarded_for, Unset):
        headers["X-Forwarded-For"] = x_forwarded_for

    if not isinstance(x_real_ip, Unset):
        headers["X-Real-IP"] = x_real_ip

    if not isinstance(user_agent, Unset):
        headers["User-Agent"] = user_agent

    if not isinstance(cf_ip_country, Unset):
        headers["CF-IPCountry"] = cf_ip_country

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/access-requests",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateOutputBody1 | ErrorModel:
    if response.status_code == 201:
        response_201 = CreateOutputBody1.from_dict(response.json())

        return response_201

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateOutputBody1 | ErrorModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateInputBody4,
    cf_connecting_ip: str | Unset = UNSET,
    x_forwarded_for: str | Unset = UNSET,
    x_real_ip: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    cf_ip_country: str | Unset = UNSET,
) -> Response[CreateOutputBody1 | ErrorModel]:
    """Submit an access request

    Args:
        cf_connecting_ip (str | Unset):
        x_forwarded_for (str | Unset):
        x_real_ip (str | Unset):
        user_agent (str | Unset):
        cf_ip_country (str | Unset):
        body (CreateInputBody4):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateOutputBody1 | ErrorModel]
    """

    kwargs = _get_kwargs(
        body=body,
        cf_connecting_ip=cf_connecting_ip,
        x_forwarded_for=x_forwarded_for,
        x_real_ip=x_real_ip,
        user_agent=user_agent,
        cf_ip_country=cf_ip_country,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateInputBody4,
    cf_connecting_ip: str | Unset = UNSET,
    x_forwarded_for: str | Unset = UNSET,
    x_real_ip: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    cf_ip_country: str | Unset = UNSET,
) -> CreateOutputBody1 | ErrorModel | None:
    """Submit an access request

    Args:
        cf_connecting_ip (str | Unset):
        x_forwarded_for (str | Unset):
        x_real_ip (str | Unset):
        user_agent (str | Unset):
        cf_ip_country (str | Unset):
        body (CreateInputBody4):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateOutputBody1 | ErrorModel
    """

    return sync_detailed(
        client=client,
        body=body,
        cf_connecting_ip=cf_connecting_ip,
        x_forwarded_for=x_forwarded_for,
        x_real_ip=x_real_ip,
        user_agent=user_agent,
        cf_ip_country=cf_ip_country,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateInputBody4,
    cf_connecting_ip: str | Unset = UNSET,
    x_forwarded_for: str | Unset = UNSET,
    x_real_ip: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    cf_ip_country: str | Unset = UNSET,
) -> Response[CreateOutputBody1 | ErrorModel]:
    """Submit an access request

    Args:
        cf_connecting_ip (str | Unset):
        x_forwarded_for (str | Unset):
        x_real_ip (str | Unset):
        user_agent (str | Unset):
        cf_ip_country (str | Unset):
        body (CreateInputBody4):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateOutputBody1 | ErrorModel]
    """

    kwargs = _get_kwargs(
        body=body,
        cf_connecting_ip=cf_connecting_ip,
        x_forwarded_for=x_forwarded_for,
        x_real_ip=x_real_ip,
        user_agent=user_agent,
        cf_ip_country=cf_ip_country,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateInputBody4,
    cf_connecting_ip: str | Unset = UNSET,
    x_forwarded_for: str | Unset = UNSET,
    x_real_ip: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    cf_ip_country: str | Unset = UNSET,
) -> CreateOutputBody1 | ErrorModel | None:
    """Submit an access request

    Args:
        cf_connecting_ip (str | Unset):
        x_forwarded_for (str | Unset):
        x_real_ip (str | Unset):
        user_agent (str | Unset):
        cf_ip_country (str | Unset):
        body (CreateInputBody4):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateOutputBody1 | ErrorModel
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            cf_connecting_ip=cf_connecting_ip,
            x_forwarded_for=x_forwarded_for,
            x_real_ip=x_real_ip,
            user_agent=user_agent,
            cf_ip_country=cf_ip_country,
        )
    ).parsed
