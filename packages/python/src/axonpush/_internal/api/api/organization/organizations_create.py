from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_organization_input_body import CreateOrganizationInputBody
from ...models.create_organization_output_body import CreateOrganizationOutputBody
from ...models.error_model import ErrorModel
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: CreateOrganizationInputBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/organizations",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateOrganizationOutputBody | ErrorModel:
    if response.status_code == 200:
        response_200 = CreateOrganizationOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateOrganizationOutputBody | ErrorModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateOrganizationInputBody,
) -> Response[CreateOrganizationOutputBody | ErrorModel]:
    """Create an organisation owned by the current user

     Create a new organisation owned by the signed-in user and switch to it.

    Everybody gets one free organisation. Check user_me_orgAllowance first: when the free allowance is
    used up, the organisation is either created unpaid (paymentRequired: true, it ingests nothing until
    someone activates a paid plan in the dashboard) or refused with ORG_LIMIT_REACHED.

    Args:
        body (CreateOrganizationInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateOrganizationOutputBody | ErrorModel]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateOrganizationInputBody,
) -> CreateOrganizationOutputBody | ErrorModel | None:
    """Create an organisation owned by the current user

     Create a new organisation owned by the signed-in user and switch to it.

    Everybody gets one free organisation. Check user_me_orgAllowance first: when the free allowance is
    used up, the organisation is either created unpaid (paymentRequired: true, it ingests nothing until
    someone activates a paid plan in the dashboard) or refused with ORG_LIMIT_REACHED.

    Args:
        body (CreateOrganizationInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateOrganizationOutputBody | ErrorModel
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateOrganizationInputBody,
) -> Response[CreateOrganizationOutputBody | ErrorModel]:
    """Create an organisation owned by the current user

     Create a new organisation owned by the signed-in user and switch to it.

    Everybody gets one free organisation. Check user_me_orgAllowance first: when the free allowance is
    used up, the organisation is either created unpaid (paymentRequired: true, it ingests nothing until
    someone activates a paid plan in the dashboard) or refused with ORG_LIMIT_REACHED.

    Args:
        body (CreateOrganizationInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateOrganizationOutputBody | ErrorModel]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateOrganizationInputBody,
) -> CreateOrganizationOutputBody | ErrorModel | None:
    """Create an organisation owned by the current user

     Create a new organisation owned by the signed-in user and switch to it.

    Everybody gets one free organisation. Check user_me_orgAllowance first: when the free allowance is
    used up, the organisation is either created unpaid (paymentRequired: true, it ingests nothing until
    someone activates a paid plan in the dashboard) or refused with ORG_LIMIT_REACHED.

    Args:
        body (CreateOrganizationInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateOrganizationOutputBody | ErrorModel
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
