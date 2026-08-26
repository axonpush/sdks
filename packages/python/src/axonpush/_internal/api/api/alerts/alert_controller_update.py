from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_rule_dto import AlertRuleDto
from ...types import UNSET, Response


def _get_kwargs(
    alert_rule_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v2/alerts/{alert_rule_id}".format(
            alert_rule_id=quote(str(alert_rule_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlertRuleDto | None:
    if response.status_code == 200:
        response_200 = AlertRuleDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AlertRuleDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    alert_rule_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AlertRuleDto]:
    """
    Args:
        alert_rule_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertRuleDto]
    """

    kwargs = _get_kwargs(
        alert_rule_id=alert_rule_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    alert_rule_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> AlertRuleDto | None:
    """
    Args:
        alert_rule_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertRuleDto
    """

    return sync_detailed(
        alert_rule_id=alert_rule_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    alert_rule_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AlertRuleDto]:
    """
    Args:
        alert_rule_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertRuleDto]
    """

    kwargs = _get_kwargs(
        alert_rule_id=alert_rule_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    alert_rule_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> AlertRuleDto | None:
    """
    Args:
        alert_rule_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertRuleDto
    """

    return (
        await asyncio_detailed(
            alert_rule_id=alert_rule_id,
            client=client,
        )
    ).parsed
