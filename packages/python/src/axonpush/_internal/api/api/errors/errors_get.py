from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.issue_detail_dto import IssueDetailDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    fingerprint: str,
    *,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["since"] = since

    params["until"] = until

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/errors/{fingerprint}".format(
            fingerprint=quote(str(fingerprint), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | IssueDetailDTO:
    if response.status_code == 200:
        response_200 = IssueDetailDTO.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | IssueDetailDTO]:
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
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
) -> Response[ErrorModel | IssueDetailDTO]:
    """Get an error Issue: sample event, stack, breadcrumbs, tags, affected traces

     Returns a self-contained debug bundle for one Issue: the recommended sample event fully hydrated,
    parsed stack frames (file:line:function + in-app), breadcrumbs (from Sentry, or synthesized from the
    trace), tag value distribution, affected trace ids, and occurrences over time.

    Args:
        fingerprint (str):
        since (str | Unset): Occurrence-bucket window start (RFC3339); defaults to firstSeen
        until (str | Unset): Occurrence-bucket window end (RFC3339); defaults to now

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | IssueDetailDTO]
    """

    kwargs = _get_kwargs(
        fingerprint=fingerprint,
        since=since,
        until=until,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fingerprint: str,
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
) -> ErrorModel | IssueDetailDTO | None:
    """Get an error Issue: sample event, stack, breadcrumbs, tags, affected traces

     Returns a self-contained debug bundle for one Issue: the recommended sample event fully hydrated,
    parsed stack frames (file:line:function + in-app), breadcrumbs (from Sentry, or synthesized from the
    trace), tag value distribution, affected trace ids, and occurrences over time.

    Args:
        fingerprint (str):
        since (str | Unset): Occurrence-bucket window start (RFC3339); defaults to firstSeen
        until (str | Unset): Occurrence-bucket window end (RFC3339); defaults to now

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | IssueDetailDTO
    """

    return sync_detailed(
        fingerprint=fingerprint,
        client=client,
        since=since,
        until=until,
    ).parsed


async def asyncio_detailed(
    fingerprint: str,
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
) -> Response[ErrorModel | IssueDetailDTO]:
    """Get an error Issue: sample event, stack, breadcrumbs, tags, affected traces

     Returns a self-contained debug bundle for one Issue: the recommended sample event fully hydrated,
    parsed stack frames (file:line:function + in-app), breadcrumbs (from Sentry, or synthesized from the
    trace), tag value distribution, affected trace ids, and occurrences over time.

    Args:
        fingerprint (str):
        since (str | Unset): Occurrence-bucket window start (RFC3339); defaults to firstSeen
        until (str | Unset): Occurrence-bucket window end (RFC3339); defaults to now

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | IssueDetailDTO]
    """

    kwargs = _get_kwargs(
        fingerprint=fingerprint,
        since=since,
        until=until,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fingerprint: str,
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
) -> ErrorModel | IssueDetailDTO | None:
    """Get an error Issue: sample event, stack, breadcrumbs, tags, affected traces

     Returns a self-contained debug bundle for one Issue: the recommended sample event fully hydrated,
    parsed stack frames (file:line:function + in-app), breadcrumbs (from Sentry, or synthesized from the
    trace), tag value distribution, affected trace ids, and occurrences over time.

    Args:
        fingerprint (str):
        since (str | Unset): Occurrence-bucket window start (RFC3339); defaults to firstSeen
        until (str | Unset): Occurrence-bucket window end (RFC3339); defaults to now

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | IssueDetailDTO
    """

    return (
        await asyncio_detailed(
            fingerprint=fingerprint,
            client=client,
            since=since,
            until=until,
        )
    ).parsed
