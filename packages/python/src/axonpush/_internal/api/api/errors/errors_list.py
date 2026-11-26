from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.errors_list_status import ErrorsListStatus
from ...models.list_errors_output_body import ListErrorsOutputBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    status: ErrorsListStatus | Unset = UNSET,
    service: str | Unset = UNSET,
    assignee: str | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["since"] = since

    params["until"] = until

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["service"] = service

    params["assignee"] = assignee

    params["q"] = q

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/errors",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | ListErrorsOutputBody:
    if response.status_code == 200:
        response_200 = ListErrorsOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | ListErrorsOutputBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    status: ErrorsListStatus | Unset = UNSET,
    service: str | Unset = UNSET,
    assignee: str | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ErrorModel | ListErrorsOutputBody]:
    """List error Issues (grouped by fingerprint) with triage state

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now
        status (ErrorsListStatus | Unset): Triage status filter (default unresolved)
        service (str | Unset): Filter by service (resource service.name)
        assignee (str | Unset): Filter by assignee user id
        q (str | Unset): Case-insensitive contains match on the error text
        limit (int | Unset): Max issues (default 50, max 500)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ListErrorsOutputBody]
    """

    kwargs = _get_kwargs(
        since=since,
        until=until,
        status=status,
        service=service,
        assignee=assignee,
        q=q,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    status: ErrorsListStatus | Unset = UNSET,
    service: str | Unset = UNSET,
    assignee: str | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ErrorModel | ListErrorsOutputBody | None:
    """List error Issues (grouped by fingerprint) with triage state

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now
        status (ErrorsListStatus | Unset): Triage status filter (default unresolved)
        service (str | Unset): Filter by service (resource service.name)
        assignee (str | Unset): Filter by assignee user id
        q (str | Unset): Case-insensitive contains match on the error text
        limit (int | Unset): Max issues (default 50, max 500)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ListErrorsOutputBody
    """

    return sync_detailed(
        client=client,
        since=since,
        until=until,
        status=status,
        service=service,
        assignee=assignee,
        q=q,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    status: ErrorsListStatus | Unset = UNSET,
    service: str | Unset = UNSET,
    assignee: str | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ErrorModel | ListErrorsOutputBody]:
    """List error Issues (grouped by fingerprint) with triage state

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now
        status (ErrorsListStatus | Unset): Triage status filter (default unresolved)
        service (str | Unset): Filter by service (resource service.name)
        assignee (str | Unset): Filter by assignee user id
        q (str | Unset): Case-insensitive contains match on the error text
        limit (int | Unset): Max issues (default 50, max 500)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ListErrorsOutputBody]
    """

    kwargs = _get_kwargs(
        since=since,
        until=until,
        status=status,
        service=service,
        assignee=assignee,
        q=q,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    status: ErrorsListStatus | Unset = UNSET,
    service: str | Unset = UNSET,
    assignee: str | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ErrorModel | ListErrorsOutputBody | None:
    """List error Issues (grouped by fingerprint) with triage state

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now
        status (ErrorsListStatus | Unset): Triage status filter (default unresolved)
        service (str | Unset): Filter by service (resource service.name)
        assignee (str | Unset): Filter by assignee user id
        q (str | Unset): Case-insensitive contains match on the error text
        limit (int | Unset): Max issues (default 50, max 500)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ListErrorsOutputBody
    """

    return (
        await asyncio_detailed(
            client=client,
            since=since,
            until=until,
            status=status,
            service=service,
            assignee=assignee,
            q=q,
            limit=limit,
        )
    ).parsed
