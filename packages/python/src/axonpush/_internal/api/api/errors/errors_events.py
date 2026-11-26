from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.list_error_events_output_body import ListErrorEventsOutputBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    fingerprint: str,
    *,
    before: str | Unset = UNSET,
    after: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["before"] = before

    params["after"] = after

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/errors/{fingerprint}/events".format(
            fingerprint=quote(str(fingerprint), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | ListErrorEventsOutputBody:
    if response.status_code == 200:
        response_200 = ListErrorEventsOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | ListErrorEventsOutputBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    fingerprint: str,
    *,
    client: AuthenticatedClient | Client,
    before: str | Unset = UNSET,
    after: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ErrorModel | ListErrorEventsOutputBody]:
    """List occurrences of one error Issue (older/newer paging)

    Args:
        fingerprint (str):
        before (str | Unset): Keyset upper bound (RFC3339, exclusive) for older occurrences
        after (str | Unset): Keyset lower bound (RFC3339, exclusive) for newer occurrences
        limit (int | Unset): Max occurrences (default 50, max 500)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ListErrorEventsOutputBody]
    """

    kwargs = _get_kwargs(
        fingerprint=fingerprint,
        before=before,
        after=after,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fingerprint: str,
    *,
    client: AuthenticatedClient | Client,
    before: str | Unset = UNSET,
    after: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ErrorModel | ListErrorEventsOutputBody | None:
    """List occurrences of one error Issue (older/newer paging)

    Args:
        fingerprint (str):
        before (str | Unset): Keyset upper bound (RFC3339, exclusive) for older occurrences
        after (str | Unset): Keyset lower bound (RFC3339, exclusive) for newer occurrences
        limit (int | Unset): Max occurrences (default 50, max 500)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ListErrorEventsOutputBody
    """

    return sync_detailed(
        fingerprint=fingerprint,
        client=client,
        before=before,
        after=after,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    fingerprint: str,
    *,
    client: AuthenticatedClient | Client,
    before: str | Unset = UNSET,
    after: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ErrorModel | ListErrorEventsOutputBody]:
    """List occurrences of one error Issue (older/newer paging)

    Args:
        fingerprint (str):
        before (str | Unset): Keyset upper bound (RFC3339, exclusive) for older occurrences
        after (str | Unset): Keyset lower bound (RFC3339, exclusive) for newer occurrences
        limit (int | Unset): Max occurrences (default 50, max 500)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ListErrorEventsOutputBody]
    """

    kwargs = _get_kwargs(
        fingerprint=fingerprint,
        before=before,
        after=after,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fingerprint: str,
    *,
    client: AuthenticatedClient | Client,
    before: str | Unset = UNSET,
    after: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ErrorModel | ListErrorEventsOutputBody | None:
    """List occurrences of one error Issue (older/newer paging)

    Args:
        fingerprint (str):
        before (str | Unset): Keyset upper bound (RFC3339, exclusive) for older occurrences
        after (str | Unset): Keyset lower bound (RFC3339, exclusive) for newer occurrences
        limit (int | Unset): Max occurrences (default 50, max 500)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ListErrorEventsOutputBody
    """

    return (
        await asyncio_detailed(
            fingerprint=fingerprint,
            client=client,
            before=before,
            after=after,
            limit=limit,
        )
    ).parsed
