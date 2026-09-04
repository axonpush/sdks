from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.gate_policy_controller_get_scope_type import GatePolicyControllerGetScopeType
from ...models.gate_policy_dto import GatePolicyDto
from ...types import UNSET, Response


def _get_kwargs(
    scope_type: GatePolicyControllerGetScopeType,
    scope_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/gate-policies/{scope_type}/{scope_id}".format(
            scope_type=quote(str(scope_type), safe=""),
            scope_id=quote(str(scope_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GatePolicyDto | None:
    if response.status_code == 200:
        response_200 = GatePolicyDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GatePolicyDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    scope_type: GatePolicyControllerGetScopeType,
    scope_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GatePolicyDto]:
    """
    Args:
        scope_type (GatePolicyControllerGetScopeType):
        scope_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GatePolicyDto]
    """

    kwargs = _get_kwargs(
        scope_type=scope_type,
        scope_id=scope_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    scope_type: GatePolicyControllerGetScopeType,
    scope_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GatePolicyDto | None:
    """
    Args:
        scope_type (GatePolicyControllerGetScopeType):
        scope_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GatePolicyDto
    """

    return sync_detailed(
        scope_type=scope_type,
        scope_id=scope_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    scope_type: GatePolicyControllerGetScopeType,
    scope_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GatePolicyDto]:
    """
    Args:
        scope_type (GatePolicyControllerGetScopeType):
        scope_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GatePolicyDto]
    """

    kwargs = _get_kwargs(
        scope_type=scope_type,
        scope_id=scope_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    scope_type: GatePolicyControllerGetScopeType,
    scope_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GatePolicyDto | None:
    """
    Args:
        scope_type (GatePolicyControllerGetScopeType):
        scope_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GatePolicyDto
    """

    return (
        await asyncio_detailed(
            scope_type=scope_type,
            scope_id=scope_id,
            client=client,
        )
    ).parsed
