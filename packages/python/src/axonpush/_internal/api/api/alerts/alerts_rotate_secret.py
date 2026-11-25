from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_model import ErrorModel
from ...models.rotate_secret_output_body import RotateSecretOutputBody
from typing import cast


def _get_kwargs(
    alert_rule_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/alerts/{alert_rule_id}/rotate-secret".format(
            alert_rule_id=quote(str(alert_rule_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | RotateSecretOutputBody:
    if response.status_code == 200:
        response_200 = RotateSecretOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | RotateSecretOutputBody]:
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
) -> Response[ErrorModel | RotateSecretOutputBody]:
    """Replace an alert rule's webhook signing secret and return the new one once

    Args:
        alert_rule_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | RotateSecretOutputBody]
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
) -> ErrorModel | RotateSecretOutputBody | None:
    """Replace an alert rule's webhook signing secret and return the new one once

    Args:
        alert_rule_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | RotateSecretOutputBody
    """

    return sync_detailed(
        alert_rule_id=alert_rule_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    alert_rule_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorModel | RotateSecretOutputBody]:
    """Replace an alert rule's webhook signing secret and return the new one once

    Args:
        alert_rule_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | RotateSecretOutputBody]
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
) -> ErrorModel | RotateSecretOutputBody | None:
    """Replace an alert rule's webhook signing secret and return the new one once

    Args:
        alert_rule_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | RotateSecretOutputBody
    """

    return (
        await asyncio_detailed(
            alert_rule_id=alert_rule_id,
            client=client,
        )
    ).parsed
