from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audit_jobs_state import AuditJobsState
from ...models.error_model import ErrorModel
from ...models.list_jobs_output_body import ListJobsOutputBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    state: AuditJobsState | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    json_state: str | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state.value

    params["state"] = json_state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/audit/jobs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | ListJobsOutputBody:
    if response.status_code == 200:
        response_200 = ListJobsOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | ListJobsOutputBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    state: AuditJobsState | Unset = UNSET,
) -> Response[ErrorModel | ListJobsOutputBody]:
    """List recent archive operations

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        state (AuditJobsState | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ListJobsOutputBody]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        state=state,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    state: AuditJobsState | Unset = UNSET,
) -> ErrorModel | ListJobsOutputBody | None:
    """List recent archive operations

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        state (AuditJobsState | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ListJobsOutputBody
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        state=state,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    state: AuditJobsState | Unset = UNSET,
) -> Response[ErrorModel | ListJobsOutputBody]:
    """List recent archive operations

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        state (AuditJobsState | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ListJobsOutputBody]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        state=state,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    state: AuditJobsState | Unset = UNSET,
) -> ErrorModel | ListJobsOutputBody | None:
    """List recent archive operations

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        state (AuditJobsState | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ListJobsOutputBody
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            state=state,
        )
    ).parsed
