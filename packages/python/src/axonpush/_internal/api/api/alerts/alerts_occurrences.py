from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.occurrences_output_body import OccurrencesOutputBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    alert_rule_id: str,
    *,
    limit: int | Unset = 50,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/alerts/{alert_rule_id}/occurrences".format(
            alert_rule_id=quote(str(alert_rule_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | OccurrencesOutputBody:
    if response.status_code == 200:
        response_200 = OccurrencesOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | OccurrencesOutputBody]:
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
    limit: int | Unset = 50,
) -> Response[ErrorModel | OccurrencesOutputBody]:
    """List an alert rule's firing history

    Args:
        alert_rule_id (str):
        limit (int | Unset): Max occurrences to return, most recent first Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | OccurrencesOutputBody]
    """

    kwargs = _get_kwargs(
        alert_rule_id=alert_rule_id,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    alert_rule_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
) -> ErrorModel | OccurrencesOutputBody | None:
    """List an alert rule's firing history

    Args:
        alert_rule_id (str):
        limit (int | Unset): Max occurrences to return, most recent first Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | OccurrencesOutputBody
    """

    return sync_detailed(
        alert_rule_id=alert_rule_id,
        client=client,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    alert_rule_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
) -> Response[ErrorModel | OccurrencesOutputBody]:
    """List an alert rule's firing history

    Args:
        alert_rule_id (str):
        limit (int | Unset): Max occurrences to return, most recent first Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | OccurrencesOutputBody]
    """

    kwargs = _get_kwargs(
        alert_rule_id=alert_rule_id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    alert_rule_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
) -> ErrorModel | OccurrencesOutputBody | None:
    """List an alert rule's firing history

    Args:
        alert_rule_id (str):
        limit (int | Unset): Max occurrences to return, most recent first Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | OccurrencesOutputBody
    """

    return (
        await asyncio_detailed(
            alert_rule_id=alert_rule_id,
            client=client,
            limit=limit,
        )
    ).parsed
