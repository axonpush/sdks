from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.list_traces_output_body import ListTracesOutputBody
from ...models.traces_list_sort import TracesListSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    q: str | Unset = UNSET,
    service: list[str] | None | Unset = UNSET,
    operation: list[str] | None | Unset = UNSET,
    model: list[str] | None | Unset = UNSET,
    provider: list[str] | None | Unset = UNSET,
    agent: list[str] | None | Unset = UNSET,
    tool: list[str] | None | Unset = UNSET,
    source: list[str] | None | Unset = UNSET,
    app: list[str] | None | Unset = UNSET,
    environment: list[str] | None | Unset = UNSET,
    api_key: list[str] | None | Unset = UNSET,
    release: list[str] | None | Unset = UNSET,
    status: list[str] | None | Unset = UNSET,
    session: list[str] | None | Unset = UNSET,
    user: list[str] | None | Unset = UNSET,
    semantic_kind: list[str] | None | Unset = UNSET,
    errors_only: bool | Unset = UNSET,
    min_duration_ms: float | Unset = UNSET,
    sort: TracesListSort | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["since"] = since

    params["until"] = until

    params["limit"] = limit

    params["offset"] = offset

    params["q"] = q

    json_service: list[str] | None | Unset
    if isinstance(service, Unset):
        json_service = UNSET
    elif isinstance(service, list):
        json_service = service

    else:
        json_service = service
    params["service"] = json_service

    json_operation: list[str] | None | Unset
    if isinstance(operation, Unset):
        json_operation = UNSET
    elif isinstance(operation, list):
        json_operation = operation

    else:
        json_operation = operation
    params["operation"] = json_operation

    json_model: list[str] | None | Unset
    if isinstance(model, Unset):
        json_model = UNSET
    elif isinstance(model, list):
        json_model = model

    else:
        json_model = model
    params["model"] = json_model

    json_provider: list[str] | None | Unset
    if isinstance(provider, Unset):
        json_provider = UNSET
    elif isinstance(provider, list):
        json_provider = provider

    else:
        json_provider = provider
    params["provider"] = json_provider

    json_agent: list[str] | None | Unset
    if isinstance(agent, Unset):
        json_agent = UNSET
    elif isinstance(agent, list):
        json_agent = agent

    else:
        json_agent = agent
    params["agent"] = json_agent

    json_tool: list[str] | None | Unset
    if isinstance(tool, Unset):
        json_tool = UNSET
    elif isinstance(tool, list):
        json_tool = tool

    else:
        json_tool = tool
    params["tool"] = json_tool

    json_source: list[str] | None | Unset
    if isinstance(source, Unset):
        json_source = UNSET
    elif isinstance(source, list):
        json_source = source

    else:
        json_source = source
    params["source"] = json_source

    json_app: list[str] | None | Unset
    if isinstance(app, Unset):
        json_app = UNSET
    elif isinstance(app, list):
        json_app = app

    else:
        json_app = app
    params["app"] = json_app

    json_environment: list[str] | None | Unset
    if isinstance(environment, Unset):
        json_environment = UNSET
    elif isinstance(environment, list):
        json_environment = environment

    else:
        json_environment = environment
    params["environment"] = json_environment

    json_api_key: list[str] | None | Unset
    if isinstance(api_key, Unset):
        json_api_key = UNSET
    elif isinstance(api_key, list):
        json_api_key = api_key

    else:
        json_api_key = api_key
    params["apiKey"] = json_api_key

    json_release: list[str] | None | Unset
    if isinstance(release, Unset):
        json_release = UNSET
    elif isinstance(release, list):
        json_release = release

    else:
        json_release = release
    params["release"] = json_release

    json_status: list[str] | None | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, list):
        json_status = status

    else:
        json_status = status
    params["status"] = json_status

    json_session: list[str] | None | Unset
    if isinstance(session, Unset):
        json_session = UNSET
    elif isinstance(session, list):
        json_session = session

    else:
        json_session = session
    params["session"] = json_session

    json_user: list[str] | None | Unset
    if isinstance(user, Unset):
        json_user = UNSET
    elif isinstance(user, list):
        json_user = user

    else:
        json_user = user
    params["user"] = json_user

    json_semantic_kind: list[str] | None | Unset
    if isinstance(semantic_kind, Unset):
        json_semantic_kind = UNSET
    elif isinstance(semantic_kind, list):
        json_semantic_kind = semantic_kind

    else:
        json_semantic_kind = semantic_kind
    params["semanticKind"] = json_semantic_kind

    params["errorsOnly"] = errors_only

    params["minDurationMs"] = min_duration_ms

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/traces",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | ListTracesOutputBody:
    if response.status_code == 200:
        response_200 = ListTracesOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | ListTracesOutputBody]:
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
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    q: str | Unset = UNSET,
    service: list[str] | None | Unset = UNSET,
    operation: list[str] | None | Unset = UNSET,
    model: list[str] | None | Unset = UNSET,
    provider: list[str] | None | Unset = UNSET,
    agent: list[str] | None | Unset = UNSET,
    tool: list[str] | None | Unset = UNSET,
    source: list[str] | None | Unset = UNSET,
    app: list[str] | None | Unset = UNSET,
    environment: list[str] | None | Unset = UNSET,
    api_key: list[str] | None | Unset = UNSET,
    release: list[str] | None | Unset = UNSET,
    status: list[str] | None | Unset = UNSET,
    session: list[str] | None | Unset = UNSET,
    user: list[str] | None | Unset = UNSET,
    semantic_kind: list[str] | None | Unset = UNSET,
    errors_only: bool | Unset = UNSET,
    min_duration_ms: float | Unset = UNSET,
    sort: TracesListSort | Unset = UNSET,
) -> Response[ErrorModel | ListTracesOutputBody]:
    """List traces over a time window

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now
        limit (int | Unset): Max traces to return (default 50, max 500)
        offset (int | Unset): Rows to skip for paging
        q (str | Unset): Free-text search over span content/metadata
        service (list[str] | None | Unset): Keep traces with a span from any of these services
        operation (list[str] | None | Unset): Keep traces with a span with any of these operations
            / span names
        model (list[str] | None | Unset): Keep traces with a span using any of these models
            (request or response)
        provider (list[str] | None | Unset): Keep traces with a span from any of these model
            providers
        agent (list[str] | None | Unset): Keep traces with a span from any of these agents
        tool (list[str] | None | Unset): Keep traces with a span invoking any of these tools
        source (list[str] | None | Unset): Keep traces with a span from any of these ingest
            sources
        app (list[str] | None | Unset): Keep traces with a span from any of these application ids
        environment (list[str] | None | Unset): Keep traces with a span from any of these
            environments (slug or id)
        api_key (list[str] | None | Unset): Keep traces with a span from any of these API key ids
        release (list[str] | None | Unset): Keep traces with a span from any of these
            release/build tags
        status (list[str] | None | Unset): Keep traces with a span of any of these statuses (e.g.
            ok/error)
        session (list[str] | None | Unset): Keep traces with a span from any of these session ids
        user (list[str] | None | Unset): Keep traces with a span from any of these end-user ids
        semantic_kind (list[str] | None | Unset): Keep traces with a span of any of these semantic
            kinds (e.g. llm)
        errors_only (bool | Unset): Keep only traces containing an error span
        min_duration_ms (float | Unset): Keep only traces at least this many ms long
        sort (TracesListSort | Unset): Row ordering: last_seen_desc (default), last_seen_asc,
            duration_desc, cost_desc, tokens_desc

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ListTracesOutputBody]
    """

    kwargs = _get_kwargs(
        since=since,
        until=until,
        limit=limit,
        offset=offset,
        q=q,
        service=service,
        operation=operation,
        model=model,
        provider=provider,
        agent=agent,
        tool=tool,
        source=source,
        app=app,
        environment=environment,
        api_key=api_key,
        release=release,
        status=status,
        session=session,
        user=user,
        semantic_kind=semantic_kind,
        errors_only=errors_only,
        min_duration_ms=min_duration_ms,
        sort=sort,
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
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    q: str | Unset = UNSET,
    service: list[str] | None | Unset = UNSET,
    operation: list[str] | None | Unset = UNSET,
    model: list[str] | None | Unset = UNSET,
    provider: list[str] | None | Unset = UNSET,
    agent: list[str] | None | Unset = UNSET,
    tool: list[str] | None | Unset = UNSET,
    source: list[str] | None | Unset = UNSET,
    app: list[str] | None | Unset = UNSET,
    environment: list[str] | None | Unset = UNSET,
    api_key: list[str] | None | Unset = UNSET,
    release: list[str] | None | Unset = UNSET,
    status: list[str] | None | Unset = UNSET,
    session: list[str] | None | Unset = UNSET,
    user: list[str] | None | Unset = UNSET,
    semantic_kind: list[str] | None | Unset = UNSET,
    errors_only: bool | Unset = UNSET,
    min_duration_ms: float | Unset = UNSET,
    sort: TracesListSort | Unset = UNSET,
) -> ErrorModel | ListTracesOutputBody | None:
    """List traces over a time window

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now
        limit (int | Unset): Max traces to return (default 50, max 500)
        offset (int | Unset): Rows to skip for paging
        q (str | Unset): Free-text search over span content/metadata
        service (list[str] | None | Unset): Keep traces with a span from any of these services
        operation (list[str] | None | Unset): Keep traces with a span with any of these operations
            / span names
        model (list[str] | None | Unset): Keep traces with a span using any of these models
            (request or response)
        provider (list[str] | None | Unset): Keep traces with a span from any of these model
            providers
        agent (list[str] | None | Unset): Keep traces with a span from any of these agents
        tool (list[str] | None | Unset): Keep traces with a span invoking any of these tools
        source (list[str] | None | Unset): Keep traces with a span from any of these ingest
            sources
        app (list[str] | None | Unset): Keep traces with a span from any of these application ids
        environment (list[str] | None | Unset): Keep traces with a span from any of these
            environments (slug or id)
        api_key (list[str] | None | Unset): Keep traces with a span from any of these API key ids
        release (list[str] | None | Unset): Keep traces with a span from any of these
            release/build tags
        status (list[str] | None | Unset): Keep traces with a span of any of these statuses (e.g.
            ok/error)
        session (list[str] | None | Unset): Keep traces with a span from any of these session ids
        user (list[str] | None | Unset): Keep traces with a span from any of these end-user ids
        semantic_kind (list[str] | None | Unset): Keep traces with a span of any of these semantic
            kinds (e.g. llm)
        errors_only (bool | Unset): Keep only traces containing an error span
        min_duration_ms (float | Unset): Keep only traces at least this many ms long
        sort (TracesListSort | Unset): Row ordering: last_seen_desc (default), last_seen_asc,
            duration_desc, cost_desc, tokens_desc

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ListTracesOutputBody
    """

    return sync_detailed(
        client=client,
        since=since,
        until=until,
        limit=limit,
        offset=offset,
        q=q,
        service=service,
        operation=operation,
        model=model,
        provider=provider,
        agent=agent,
        tool=tool,
        source=source,
        app=app,
        environment=environment,
        api_key=api_key,
        release=release,
        status=status,
        session=session,
        user=user,
        semantic_kind=semantic_kind,
        errors_only=errors_only,
        min_duration_ms=min_duration_ms,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    q: str | Unset = UNSET,
    service: list[str] | None | Unset = UNSET,
    operation: list[str] | None | Unset = UNSET,
    model: list[str] | None | Unset = UNSET,
    provider: list[str] | None | Unset = UNSET,
    agent: list[str] | None | Unset = UNSET,
    tool: list[str] | None | Unset = UNSET,
    source: list[str] | None | Unset = UNSET,
    app: list[str] | None | Unset = UNSET,
    environment: list[str] | None | Unset = UNSET,
    api_key: list[str] | None | Unset = UNSET,
    release: list[str] | None | Unset = UNSET,
    status: list[str] | None | Unset = UNSET,
    session: list[str] | None | Unset = UNSET,
    user: list[str] | None | Unset = UNSET,
    semantic_kind: list[str] | None | Unset = UNSET,
    errors_only: bool | Unset = UNSET,
    min_duration_ms: float | Unset = UNSET,
    sort: TracesListSort | Unset = UNSET,
) -> Response[ErrorModel | ListTracesOutputBody]:
    """List traces over a time window

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now
        limit (int | Unset): Max traces to return (default 50, max 500)
        offset (int | Unset): Rows to skip for paging
        q (str | Unset): Free-text search over span content/metadata
        service (list[str] | None | Unset): Keep traces with a span from any of these services
        operation (list[str] | None | Unset): Keep traces with a span with any of these operations
            / span names
        model (list[str] | None | Unset): Keep traces with a span using any of these models
            (request or response)
        provider (list[str] | None | Unset): Keep traces with a span from any of these model
            providers
        agent (list[str] | None | Unset): Keep traces with a span from any of these agents
        tool (list[str] | None | Unset): Keep traces with a span invoking any of these tools
        source (list[str] | None | Unset): Keep traces with a span from any of these ingest
            sources
        app (list[str] | None | Unset): Keep traces with a span from any of these application ids
        environment (list[str] | None | Unset): Keep traces with a span from any of these
            environments (slug or id)
        api_key (list[str] | None | Unset): Keep traces with a span from any of these API key ids
        release (list[str] | None | Unset): Keep traces with a span from any of these
            release/build tags
        status (list[str] | None | Unset): Keep traces with a span of any of these statuses (e.g.
            ok/error)
        session (list[str] | None | Unset): Keep traces with a span from any of these session ids
        user (list[str] | None | Unset): Keep traces with a span from any of these end-user ids
        semantic_kind (list[str] | None | Unset): Keep traces with a span of any of these semantic
            kinds (e.g. llm)
        errors_only (bool | Unset): Keep only traces containing an error span
        min_duration_ms (float | Unset): Keep only traces at least this many ms long
        sort (TracesListSort | Unset): Row ordering: last_seen_desc (default), last_seen_asc,
            duration_desc, cost_desc, tokens_desc

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ListTracesOutputBody]
    """

    kwargs = _get_kwargs(
        since=since,
        until=until,
        limit=limit,
        offset=offset,
        q=q,
        service=service,
        operation=operation,
        model=model,
        provider=provider,
        agent=agent,
        tool=tool,
        source=source,
        app=app,
        environment=environment,
        api_key=api_key,
        release=release,
        status=status,
        session=session,
        user=user,
        semantic_kind=semantic_kind,
        errors_only=errors_only,
        min_duration_ms=min_duration_ms,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    q: str | Unset = UNSET,
    service: list[str] | None | Unset = UNSET,
    operation: list[str] | None | Unset = UNSET,
    model: list[str] | None | Unset = UNSET,
    provider: list[str] | None | Unset = UNSET,
    agent: list[str] | None | Unset = UNSET,
    tool: list[str] | None | Unset = UNSET,
    source: list[str] | None | Unset = UNSET,
    app: list[str] | None | Unset = UNSET,
    environment: list[str] | None | Unset = UNSET,
    api_key: list[str] | None | Unset = UNSET,
    release: list[str] | None | Unset = UNSET,
    status: list[str] | None | Unset = UNSET,
    session: list[str] | None | Unset = UNSET,
    user: list[str] | None | Unset = UNSET,
    semantic_kind: list[str] | None | Unset = UNSET,
    errors_only: bool | Unset = UNSET,
    min_duration_ms: float | Unset = UNSET,
    sort: TracesListSort | Unset = UNSET,
) -> ErrorModel | ListTracesOutputBody | None:
    """List traces over a time window

    Args:
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now
        limit (int | Unset): Max traces to return (default 50, max 500)
        offset (int | Unset): Rows to skip for paging
        q (str | Unset): Free-text search over span content/metadata
        service (list[str] | None | Unset): Keep traces with a span from any of these services
        operation (list[str] | None | Unset): Keep traces with a span with any of these operations
            / span names
        model (list[str] | None | Unset): Keep traces with a span using any of these models
            (request or response)
        provider (list[str] | None | Unset): Keep traces with a span from any of these model
            providers
        agent (list[str] | None | Unset): Keep traces with a span from any of these agents
        tool (list[str] | None | Unset): Keep traces with a span invoking any of these tools
        source (list[str] | None | Unset): Keep traces with a span from any of these ingest
            sources
        app (list[str] | None | Unset): Keep traces with a span from any of these application ids
        environment (list[str] | None | Unset): Keep traces with a span from any of these
            environments (slug or id)
        api_key (list[str] | None | Unset): Keep traces with a span from any of these API key ids
        release (list[str] | None | Unset): Keep traces with a span from any of these
            release/build tags
        status (list[str] | None | Unset): Keep traces with a span of any of these statuses (e.g.
            ok/error)
        session (list[str] | None | Unset): Keep traces with a span from any of these session ids
        user (list[str] | None | Unset): Keep traces with a span from any of these end-user ids
        semantic_kind (list[str] | None | Unset): Keep traces with a span of any of these semantic
            kinds (e.g. llm)
        errors_only (bool | Unset): Keep only traces containing an error span
        min_duration_ms (float | Unset): Keep only traces at least this many ms long
        sort (TracesListSort | Unset): Row ordering: last_seen_desc (default), last_seen_asc,
            duration_desc, cost_desc, tokens_desc

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ListTracesOutputBody
    """

    return (
        await asyncio_detailed(
            client=client,
            since=since,
            until=until,
            limit=limit,
            offset=offset,
            q=q,
            service=service,
            operation=operation,
            model=model,
            provider=provider,
            agent=agent,
            tool=tool,
            source=source,
            app=app,
            environment=environment,
            api_key=api_key,
            release=release,
            status=status,
            session=session,
            user=user,
            semantic_kind=semantic_kind,
            errors_only=errors_only,
            min_duration_ms=min_duration_ms,
            sort=sort,
        )
    ).parsed
