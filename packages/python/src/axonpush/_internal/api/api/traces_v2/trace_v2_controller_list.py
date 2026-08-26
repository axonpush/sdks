from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.trace_list_v2_response_dto import TraceListV2ResponseDto
from ...models.trace_v2_controller_list_sort import TraceV2ControllerListSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    agent: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    limit: float | Unset = UNSET,
    model: str | Unset = UNSET,
    prompt_id: str | Unset = UNSET,
    prompt_version_id: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    query: str | Unset = UNSET,
    release: str | Unset = UNSET,
    semantic_kind: str | Unset = UNSET,
    service: str | Unset = UNSET,
    session_id: str | Unset = UNSET,
    sort: TraceV2ControllerListSort | Unset = UNSET,
    status: str | Unset = UNSET,
    to: str | Unset = UNSET,
    tool: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["agent"] = agent

    params["cursor"] = cursor

    params["from"] = from_

    params["limit"] = limit

    params["model"] = model

    params["promptId"] = prompt_id

    params["promptVersionId"] = prompt_version_id

    params["provider"] = provider

    params["query"] = query

    params["release"] = release

    params["semanticKind"] = semantic_kind

    params["service"] = service

    params["sessionId"] = session_id

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params["status"] = status

    params["to"] = to

    params["tool"] = tool

    params["userId"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/traces",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TraceListV2ResponseDto | None:
    if response.status_code == 200:
        response_200 = TraceListV2ResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TraceListV2ResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    agent: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    limit: float | Unset = UNSET,
    model: str | Unset = UNSET,
    prompt_id: str | Unset = UNSET,
    prompt_version_id: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    query: str | Unset = UNSET,
    release: str | Unset = UNSET,
    semantic_kind: str | Unset = UNSET,
    service: str | Unset = UNSET,
    session_id: str | Unset = UNSET,
    sort: TraceV2ControllerListSort | Unset = UNSET,
    status: str | Unset = UNSET,
    to: str | Unset = UNSET,
    tool: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> Response[TraceListV2ResponseDto]:
    """
    Args:
        agent (str | Unset):
        cursor (str | Unset):
        from_ (str | Unset):
        limit (float | Unset):
        model (str | Unset):
        prompt_id (str | Unset):
        prompt_version_id (str | Unset):
        provider (str | Unset):
        query (str | Unset):
        release (str | Unset):
        semantic_kind (str | Unset):
        service (str | Unset):
        session_id (str | Unset):
        sort (TraceV2ControllerListSort | Unset):
        status (str | Unset):
        to (str | Unset):
        tool (str | Unset):
        user_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TraceListV2ResponseDto]
    """

    kwargs = _get_kwargs(
        agent=agent,
        cursor=cursor,
        from_=from_,
        limit=limit,
        model=model,
        prompt_id=prompt_id,
        prompt_version_id=prompt_version_id,
        provider=provider,
        query=query,
        release=release,
        semantic_kind=semantic_kind,
        service=service,
        session_id=session_id,
        sort=sort,
        status=status,
        to=to,
        tool=tool,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    agent: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    limit: float | Unset = UNSET,
    model: str | Unset = UNSET,
    prompt_id: str | Unset = UNSET,
    prompt_version_id: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    query: str | Unset = UNSET,
    release: str | Unset = UNSET,
    semantic_kind: str | Unset = UNSET,
    service: str | Unset = UNSET,
    session_id: str | Unset = UNSET,
    sort: TraceV2ControllerListSort | Unset = UNSET,
    status: str | Unset = UNSET,
    to: str | Unset = UNSET,
    tool: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> TraceListV2ResponseDto | None:
    """
    Args:
        agent (str | Unset):
        cursor (str | Unset):
        from_ (str | Unset):
        limit (float | Unset):
        model (str | Unset):
        prompt_id (str | Unset):
        prompt_version_id (str | Unset):
        provider (str | Unset):
        query (str | Unset):
        release (str | Unset):
        semantic_kind (str | Unset):
        service (str | Unset):
        session_id (str | Unset):
        sort (TraceV2ControllerListSort | Unset):
        status (str | Unset):
        to (str | Unset):
        tool (str | Unset):
        user_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TraceListV2ResponseDto
    """

    return sync_detailed(
        client=client,
        agent=agent,
        cursor=cursor,
        from_=from_,
        limit=limit,
        model=model,
        prompt_id=prompt_id,
        prompt_version_id=prompt_version_id,
        provider=provider,
        query=query,
        release=release,
        semantic_kind=semantic_kind,
        service=service,
        session_id=session_id,
        sort=sort,
        status=status,
        to=to,
        tool=tool,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    agent: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    limit: float | Unset = UNSET,
    model: str | Unset = UNSET,
    prompt_id: str | Unset = UNSET,
    prompt_version_id: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    query: str | Unset = UNSET,
    release: str | Unset = UNSET,
    semantic_kind: str | Unset = UNSET,
    service: str | Unset = UNSET,
    session_id: str | Unset = UNSET,
    sort: TraceV2ControllerListSort | Unset = UNSET,
    status: str | Unset = UNSET,
    to: str | Unset = UNSET,
    tool: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> Response[TraceListV2ResponseDto]:
    """
    Args:
        agent (str | Unset):
        cursor (str | Unset):
        from_ (str | Unset):
        limit (float | Unset):
        model (str | Unset):
        prompt_id (str | Unset):
        prompt_version_id (str | Unset):
        provider (str | Unset):
        query (str | Unset):
        release (str | Unset):
        semantic_kind (str | Unset):
        service (str | Unset):
        session_id (str | Unset):
        sort (TraceV2ControllerListSort | Unset):
        status (str | Unset):
        to (str | Unset):
        tool (str | Unset):
        user_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TraceListV2ResponseDto]
    """

    kwargs = _get_kwargs(
        agent=agent,
        cursor=cursor,
        from_=from_,
        limit=limit,
        model=model,
        prompt_id=prompt_id,
        prompt_version_id=prompt_version_id,
        provider=provider,
        query=query,
        release=release,
        semantic_kind=semantic_kind,
        service=service,
        session_id=session_id,
        sort=sort,
        status=status,
        to=to,
        tool=tool,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    agent: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    limit: float | Unset = UNSET,
    model: str | Unset = UNSET,
    prompt_id: str | Unset = UNSET,
    prompt_version_id: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    query: str | Unset = UNSET,
    release: str | Unset = UNSET,
    semantic_kind: str | Unset = UNSET,
    service: str | Unset = UNSET,
    session_id: str | Unset = UNSET,
    sort: TraceV2ControllerListSort | Unset = UNSET,
    status: str | Unset = UNSET,
    to: str | Unset = UNSET,
    tool: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> TraceListV2ResponseDto | None:
    """
    Args:
        agent (str | Unset):
        cursor (str | Unset):
        from_ (str | Unset):
        limit (float | Unset):
        model (str | Unset):
        prompt_id (str | Unset):
        prompt_version_id (str | Unset):
        provider (str | Unset):
        query (str | Unset):
        release (str | Unset):
        semantic_kind (str | Unset):
        service (str | Unset):
        session_id (str | Unset):
        sort (TraceV2ControllerListSort | Unset):
        status (str | Unset):
        to (str | Unset):
        tool (str | Unset):
        user_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TraceListV2ResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            agent=agent,
            cursor=cursor,
            from_=from_,
            limit=limit,
            model=model,
            prompt_id=prompt_id,
            prompt_version_id=prompt_version_id,
            provider=provider,
            query=query,
            release=release,
            semantic_kind=semantic_kind,
            service=service,
            session_id=session_id,
            sort=sort,
            status=status,
            to=to,
            tool=tool,
            user_id=user_id,
        )
    ).parsed
