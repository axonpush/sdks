from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.issue_response_dto import IssueResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    severity: str | Unset = UNSET,
    status: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["severity"] = severity

    params["status"] = status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/issues",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[IssueResponseDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = IssueResponseDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[IssueResponseDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    severity: str | Unset = UNSET,
    status: str | Unset = UNSET,
) -> Response[list[IssueResponseDto]]:
    """
    Args:
        severity (str | Unset):
        status (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[IssueResponseDto]]
    """

    kwargs = _get_kwargs(
        severity=severity,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    severity: str | Unset = UNSET,
    status: str | Unset = UNSET,
) -> list[IssueResponseDto] | None:
    """
    Args:
        severity (str | Unset):
        status (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[IssueResponseDto]
    """

    return sync_detailed(
        client=client,
        severity=severity,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    severity: str | Unset = UNSET,
    status: str | Unset = UNSET,
) -> Response[list[IssueResponseDto]]:
    """
    Args:
        severity (str | Unset):
        status (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[IssueResponseDto]]
    """

    kwargs = _get_kwargs(
        severity=severity,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    severity: str | Unset = UNSET,
    status: str | Unset = UNSET,
) -> list[IssueResponseDto] | None:
    """
    Args:
        severity (str | Unset):
        status (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[IssueResponseDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            severity=severity,
            status=status,
        )
    ).parsed
