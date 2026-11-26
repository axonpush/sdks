from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.reference_output_body import ReferenceOutputBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    kind: str,
    *,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    state: str | Unset = UNSET,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    agent_id: str | Unset = UNSET,
    segment_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["limit"] = limit

    params["cursor"] = cursor

    params["ids"] = ids

    params["state"] = state

    params["appId"] = app_id

    params["environmentId"] = environment_id

    params["agentId"] = agent_id

    params["segmentId"] = segment_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/audit/references/{kind}".format(
            kind=quote(str(kind), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | ReferenceOutputBody:
    if response.status_code == 200:
        response_200 = ReferenceOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | ReferenceOutputBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    kind: str,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    state: str | Unset = UNSET,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    agent_id: str | Unset = UNSET,
    segment_id: str | Unset = UNSET,
) -> Response[ErrorModel | ReferenceOutputBody]:
    """Search organization-scoped labeled relationship choices

    Args:
        kind (str):
        q (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        ids (str | Unset):
        state (str | Unset):
        app_id (str | Unset):
        environment_id (str | Unset):
        agent_id (str | Unset):
        segment_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ReferenceOutputBody]
    """

    kwargs = _get_kwargs(
        kind=kind,
        q=q,
        limit=limit,
        cursor=cursor,
        ids=ids,
        state=state,
        app_id=app_id,
        environment_id=environment_id,
        agent_id=agent_id,
        segment_id=segment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    kind: str,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    state: str | Unset = UNSET,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    agent_id: str | Unset = UNSET,
    segment_id: str | Unset = UNSET,
) -> ErrorModel | ReferenceOutputBody | None:
    """Search organization-scoped labeled relationship choices

    Args:
        kind (str):
        q (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        ids (str | Unset):
        state (str | Unset):
        app_id (str | Unset):
        environment_id (str | Unset):
        agent_id (str | Unset):
        segment_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ReferenceOutputBody
    """

    return sync_detailed(
        kind=kind,
        client=client,
        q=q,
        limit=limit,
        cursor=cursor,
        ids=ids,
        state=state,
        app_id=app_id,
        environment_id=environment_id,
        agent_id=agent_id,
        segment_id=segment_id,
    ).parsed


async def asyncio_detailed(
    kind: str,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    state: str | Unset = UNSET,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    agent_id: str | Unset = UNSET,
    segment_id: str | Unset = UNSET,
) -> Response[ErrorModel | ReferenceOutputBody]:
    """Search organization-scoped labeled relationship choices

    Args:
        kind (str):
        q (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        ids (str | Unset):
        state (str | Unset):
        app_id (str | Unset):
        environment_id (str | Unset):
        agent_id (str | Unset):
        segment_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ReferenceOutputBody]
    """

    kwargs = _get_kwargs(
        kind=kind,
        q=q,
        limit=limit,
        cursor=cursor,
        ids=ids,
        state=state,
        app_id=app_id,
        environment_id=environment_id,
        agent_id=agent_id,
        segment_id=segment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    kind: str,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    state: str | Unset = UNSET,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    agent_id: str | Unset = UNSET,
    segment_id: str | Unset = UNSET,
) -> ErrorModel | ReferenceOutputBody | None:
    """Search organization-scoped labeled relationship choices

    Args:
        kind (str):
        q (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        ids (str | Unset):
        state (str | Unset):
        app_id (str | Unset):
        environment_id (str | Unset):
        agent_id (str | Unset):
        segment_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ReferenceOutputBody
    """

    return (
        await asyncio_detailed(
            kind=kind,
            client=client,
            q=q,
            limit=limit,
            cursor=cursor,
            ids=ids,
            state=state,
            app_id=app_id,
            environment_id=environment_id,
            agent_id=agent_id,
            segment_id=segment_id,
        )
    ).parsed
