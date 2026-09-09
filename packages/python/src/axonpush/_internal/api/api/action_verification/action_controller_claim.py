from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.action_dto import ActionDto
from ...models.claim_action_dto import ClaimActionDto
from ...types import UNSET, Response


def _get_kwargs(
    action_id: str,
    *,
    body: ClaimActionDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/actions/{action_id}/claims".format(
            action_id=quote(str(action_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActionDto | None:
    if response.status_code == 200:
        response_200 = ActionDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ActionDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    action_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ClaimActionDto,
) -> Response[ActionDto]:
    """
    Args:
        action_id (str):
        body (ClaimActionDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionDto]
    """

    kwargs = _get_kwargs(
        action_id=action_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    action_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ClaimActionDto,
) -> ActionDto | None:
    """
    Args:
        action_id (str):
        body (ClaimActionDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionDto
    """

    return sync_detailed(
        action_id=action_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    action_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ClaimActionDto,
) -> Response[ActionDto]:
    """
    Args:
        action_id (str):
        body (ClaimActionDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionDto]
    """

    kwargs = _get_kwargs(
        action_id=action_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    action_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ClaimActionDto,
) -> ActionDto | None:
    """
    Args:
        action_id (str):
        body (ClaimActionDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionDto
    """

    return (
        await asyncio_detailed(
            action_id=action_id,
            client=client,
            body=body,
        )
    ).parsed
