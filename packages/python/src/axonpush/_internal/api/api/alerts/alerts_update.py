from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_rule_dto import AlertRuleDTO
from ...models.error_model import ErrorModel
from ...models.update_input_body import UpdateInputBody
from ...types import UNSET, Response


def _get_kwargs(
    alert_rule_id: str,
    *,
    body: UpdateInputBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v2/alerts/{alert_rule_id}".format(
            alert_rule_id=quote(str(alert_rule_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlertRuleDTO | ErrorModel:
    if response.status_code == 200:
        response_200 = AlertRuleDTO.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AlertRuleDTO | ErrorModel]:
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
    body: UpdateInputBody,
) -> Response[AlertRuleDTO | ErrorModel]:
    """Update an alert rule

    Args:
        alert_rule_id (str):
        body (UpdateInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertRuleDTO | ErrorModel]
    """

    kwargs = _get_kwargs(
        alert_rule_id=alert_rule_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    alert_rule_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateInputBody,
) -> AlertRuleDTO | ErrorModel | None:
    """Update an alert rule

    Args:
        alert_rule_id (str):
        body (UpdateInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertRuleDTO | ErrorModel
    """

    return sync_detailed(
        alert_rule_id=alert_rule_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    alert_rule_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateInputBody,
) -> Response[AlertRuleDTO | ErrorModel]:
    """Update an alert rule

    Args:
        alert_rule_id (str):
        body (UpdateInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertRuleDTO | ErrorModel]
    """

    kwargs = _get_kwargs(
        alert_rule_id=alert_rule_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    alert_rule_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateInputBody,
) -> AlertRuleDTO | ErrorModel | None:
    """Update an alert rule

    Args:
        alert_rule_id (str):
        body (UpdateInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertRuleDTO | ErrorModel
    """

    return (
        await asyncio_detailed(
            alert_rule_id=alert_rule_id,
            client=client,
            body=body,
        )
    ).parsed
