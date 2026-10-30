from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.session_evidence_body import SessionEvidenceBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    session_id: str,
    *,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    replay_only: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["appId"] = app_id

    params["environmentId"] = environment_id

    params["limit"] = limit

    params["offset"] = offset

    params["cursor"] = cursor

    params["replayOnly"] = replay_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/telemetry/sessions/{session_id}".format(
            session_id=quote(str(session_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | SessionEvidenceBody:
    if response.status_code == 200:
        response_200 = SessionEvidenceBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | SessionEvidenceBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    replay_only: bool | Unset = UNSET,
) -> Response[ErrorModel | SessionEvidenceBody]:
    """Read a session's chronological interaction metadata

    Args:
        session_id (str):
        app_id (str | Unset):
        environment_id (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset): Legacy offset pagination; omit when using cursor
        cursor (str | Unset): Continue after the preceding page; preferred over offset
        replay_only (bool | Unset): Return only browser replay chunk metadata

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | SessionEvidenceBody]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        app_id=app_id,
        environment_id=environment_id,
        limit=limit,
        offset=offset,
        cursor=cursor,
        replay_only=replay_only,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    replay_only: bool | Unset = UNSET,
) -> ErrorModel | SessionEvidenceBody | None:
    """Read a session's chronological interaction metadata

    Args:
        session_id (str):
        app_id (str | Unset):
        environment_id (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset): Legacy offset pagination; omit when using cursor
        cursor (str | Unset): Continue after the preceding page; preferred over offset
        replay_only (bool | Unset): Return only browser replay chunk metadata

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | SessionEvidenceBody
    """

    return sync_detailed(
        session_id=session_id,
        client=client,
        app_id=app_id,
        environment_id=environment_id,
        limit=limit,
        offset=offset,
        cursor=cursor,
        replay_only=replay_only,
    ).parsed


async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    replay_only: bool | Unset = UNSET,
) -> Response[ErrorModel | SessionEvidenceBody]:
    """Read a session's chronological interaction metadata

    Args:
        session_id (str):
        app_id (str | Unset):
        environment_id (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset): Legacy offset pagination; omit when using cursor
        cursor (str | Unset): Continue after the preceding page; preferred over offset
        replay_only (bool | Unset): Return only browser replay chunk metadata

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | SessionEvidenceBody]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        app_id=app_id,
        environment_id=environment_id,
        limit=limit,
        offset=offset,
        cursor=cursor,
        replay_only=replay_only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    replay_only: bool | Unset = UNSET,
) -> ErrorModel | SessionEvidenceBody | None:
    """Read a session's chronological interaction metadata

    Args:
        session_id (str):
        app_id (str | Unset):
        environment_id (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset): Legacy offset pagination; omit when using cursor
        cursor (str | Unset): Continue after the preceding page; preferred over offset
        replay_only (bool | Unset): Return only browser replay chunk metadata

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | SessionEvidenceBody
    """

    return (
        await asyncio_detailed(
            session_id=session_id,
            client=client,
            app_id=app_id,
            environment_id=environment_id,
            limit=limit,
            offset=offset,
            cursor=cursor,
            replay_only=replay_only,
        )
    ).parsed
