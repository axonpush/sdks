from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.ledger_hold import LedgerHold
from ...models.release_hold_input_body import ReleaseHoldInputBody
from ...types import UNSET, Response


def _get_kwargs(
    hold_id: str,
    *,
    body: ReleaseHoldInputBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/audit/holds/{hold_id}".format(
            hold_id=quote(str(hold_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | LedgerHold:
    if response.status_code == 200:
        response_200 = LedgerHold.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | LedgerHold]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    hold_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ReleaseHoldInputBody,
) -> Response[ErrorModel | LedgerHold]:
    """Release a recorded legal hold

    Args:
        hold_id (str):
        body (ReleaseHoldInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | LedgerHold]
    """

    kwargs = _get_kwargs(
        hold_id=hold_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    hold_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ReleaseHoldInputBody,
) -> ErrorModel | LedgerHold | None:
    """Release a recorded legal hold

    Args:
        hold_id (str):
        body (ReleaseHoldInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | LedgerHold
    """

    return sync_detailed(
        hold_id=hold_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    hold_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ReleaseHoldInputBody,
) -> Response[ErrorModel | LedgerHold]:
    """Release a recorded legal hold

    Args:
        hold_id (str):
        body (ReleaseHoldInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | LedgerHold]
    """

    kwargs = _get_kwargs(
        hold_id=hold_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    hold_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ReleaseHoldInputBody,
) -> ErrorModel | LedgerHold | None:
    """Release a recorded legal hold

    Args:
        hold_id (str):
        body (ReleaseHoldInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | LedgerHold
    """

    return (
        await asyncio_detailed(
            hold_id=hold_id,
            client=client,
            body=body,
        )
    ).parsed
