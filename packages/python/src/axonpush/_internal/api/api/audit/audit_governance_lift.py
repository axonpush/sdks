from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.governance_input_body import GovernanceInputBody
from ...models.ledger_job import LedgerJob
from ...types import UNSET, Response


def _get_kwargs(
    segment_id: str,
    *,
    body: GovernanceInputBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/audit/segments/{segment_id}/governance-lift".format(
            segment_id=quote(str(segment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | LedgerJob:
    if response.status_code == 200:
        response_200 = LedgerJob.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | LedgerJob]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    segment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GovernanceInputBody,
) -> Response[ErrorModel | LedgerJob]:
    """Request separately authorized governance retention shortening with an immutable reason

    Args:
        segment_id (str):
        body (GovernanceInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | LedgerJob]
    """

    kwargs = _get_kwargs(
        segment_id=segment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    segment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GovernanceInputBody,
) -> ErrorModel | LedgerJob | None:
    """Request separately authorized governance retention shortening with an immutable reason

    Args:
        segment_id (str):
        body (GovernanceInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | LedgerJob
    """

    return sync_detailed(
        segment_id=segment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    segment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GovernanceInputBody,
) -> Response[ErrorModel | LedgerJob]:
    """Request separately authorized governance retention shortening with an immutable reason

    Args:
        segment_id (str):
        body (GovernanceInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | LedgerJob]
    """

    kwargs = _get_kwargs(
        segment_id=segment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    segment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GovernanceInputBody,
) -> ErrorModel | LedgerJob | None:
    """Request separately authorized governance retention shortening with an immutable reason

    Args:
        segment_id (str):
        body (GovernanceInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | LedgerJob
    """

    return (
        await asyncio_detailed(
            segment_id=segment_id,
            client=client,
            body=body,
        )
    ).parsed
