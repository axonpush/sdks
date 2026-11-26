from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_output_body import DeleteOutputBody
from ...models.error_model import ErrorModel
from ...types import UNSET, Response


def _get_kwargs(
    alert_rule_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v2/alerts/{alert_rule_id}".format(
            alert_rule_id=quote(str(alert_rule_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteOutputBody | ErrorModel:
    if response.status_code == 200:
        response_200 = DeleteOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeleteOutputBody | ErrorModel]:
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
) -> Response[DeleteOutputBody | ErrorModel]:
    """Delete an alert rule

    Args:
        alert_rule_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteOutputBody | ErrorModel]
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
) -> DeleteOutputBody | ErrorModel | None:
    """Delete an alert rule

    Args:
        alert_rule_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteOutputBody | ErrorModel
    """

    return sync_detailed(
        alert_rule_id=alert_rule_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    alert_rule_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DeleteOutputBody | ErrorModel]:
    """Delete an alert rule

    Args:
        alert_rule_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteOutputBody | ErrorModel]
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
) -> DeleteOutputBody | ErrorModel | None:
    """Delete an alert rule

    Args:
        alert_rule_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteOutputBody | ErrorModel
    """

    return (
        await asyncio_detailed(
            alert_rule_id=alert_rule_id,
            client=client,
        )
    ).parsed
