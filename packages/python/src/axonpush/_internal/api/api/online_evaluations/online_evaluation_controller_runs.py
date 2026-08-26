from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.online_rule_run_response_dto import OnlineRuleRunResponseDto
from ...types import UNSET, Response


def _get_kwargs(
    rule_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/online-evaluation-rules/{rule_id}/runs".format(
            rule_id=quote(str(rule_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[OnlineRuleRunResponseDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = OnlineRuleRunResponseDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[OnlineRuleRunResponseDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    rule_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[list[OnlineRuleRunResponseDto]]:
    """
    Args:
        rule_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[OnlineRuleRunResponseDto]]
    """

    kwargs = _get_kwargs(
        rule_id=rule_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    rule_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> list[OnlineRuleRunResponseDto] | None:
    """
    Args:
        rule_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[OnlineRuleRunResponseDto]
    """

    return sync_detailed(
        rule_id=rule_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    rule_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[list[OnlineRuleRunResponseDto]]:
    """
    Args:
        rule_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[OnlineRuleRunResponseDto]]
    """

    kwargs = _get_kwargs(
        rule_id=rule_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    rule_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> list[OnlineRuleRunResponseDto] | None:
    """
    Args:
        rule_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[OnlineRuleRunResponseDto]
    """

    return (
        await asyncio_detailed(
            rule_id=rule_id,
            client=client,
        )
    ).parsed
