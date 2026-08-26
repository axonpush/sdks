from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_controller_timeseries_attr import AnalyticsControllerTimeseriesAttr
from ...models.analytics_controller_timeseries_attr_max import AnalyticsControllerTimeseriesAttrMax
from ...models.analytics_controller_timeseries_attr_min import AnalyticsControllerTimeseriesAttrMin
from ...models.analytics_controller_timeseries_interval import AnalyticsControllerTimeseriesInterval
from ...models.analytics_controller_timeseries_measure import AnalyticsControllerTimeseriesMeasure
from ...models.analytics_controller_timeseries_res import AnalyticsControllerTimeseriesRes
from ...models.analytics_timeseries_response_dto import AnalyticsTimeseriesResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    agent: str | Unset = UNSET,
    app_id: str | Unset = UNSET,
    attr: AnalyticsControllerTimeseriesAttr | Unset = UNSET,
    attr_max: AnalyticsControllerTimeseriesAttrMax | Unset = UNSET,
    attr_min: AnalyticsControllerTimeseriesAttrMin | Unset = UNSET,
    environment: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    interval: AnalyticsControllerTimeseriesInterval | Unset = UNSET,
    max_cost_usd: str | Unset = UNSET,
    max_duration_ms: str | Unset = UNSET,
    max_tokens: str | Unset = UNSET,
    measure: AnalyticsControllerTimeseriesMeasure | Unset = UNSET,
    min_cost_usd: str | Unset = UNSET,
    min_duration_ms: str | Unset = UNSET,
    min_tokens: str | Unset = UNSET,
    model: str | Unset = UNSET,
    prompt_id: str | Unset = UNSET,
    prompt_version_id: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    query: str | Unset = UNSET,
    release: str | Unset = UNSET,
    res: AnalyticsControllerTimeseriesRes | Unset = UNSET,
    semantic_kind: str | Unset = UNSET,
    service: str | Unset = UNSET,
    session_id: str | Unset = UNSET,
    span_kind: str | Unset = UNSET,
    span_min_duration_ms: str | Unset = UNSET,
    span_model: str | Unset = UNSET,
    span_status: str | Unset = UNSET,
    span_tool: str | Unset = UNSET,
    status: str | Unset = UNSET,
    to: str | Unset = UNSET,
    tool: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["agent"] = agent

    params["appId"] = app_id

    json_attr: dict[str, Any] | Unset = UNSET
    if not isinstance(attr, Unset):
        json_attr = attr.to_dict()
    if not isinstance(json_attr, Unset):
        params.update(json_attr)

    json_attr_max: dict[str, Any] | Unset = UNSET
    if not isinstance(attr_max, Unset):
        json_attr_max = attr_max.to_dict()
    if not isinstance(json_attr_max, Unset):
        params.update(json_attr_max)

    json_attr_min: dict[str, Any] | Unset = UNSET
    if not isinstance(attr_min, Unset):
        json_attr_min = attr_min.to_dict()
    if not isinstance(json_attr_min, Unset):
        params.update(json_attr_min)

    params["environment"] = environment

    params["environmentId"] = environment_id

    params["from"] = from_

    json_interval: str | Unset = UNSET
    if not isinstance(interval, Unset):
        json_interval = interval.value

    params["interval"] = json_interval

    params["maxCostUsd"] = max_cost_usd

    params["maxDurationMs"] = max_duration_ms

    params["maxTokens"] = max_tokens

    json_measure: str | Unset = UNSET
    if not isinstance(measure, Unset):
        json_measure = measure.value

    params["measure"] = json_measure

    params["minCostUsd"] = min_cost_usd

    params["minDurationMs"] = min_duration_ms

    params["minTokens"] = min_tokens

    params["model"] = model

    params["promptId"] = prompt_id

    params["promptVersionId"] = prompt_version_id

    params["provider"] = provider

    params["query"] = query

    params["release"] = release

    json_res: dict[str, Any] | Unset = UNSET
    if not isinstance(res, Unset):
        json_res = res.to_dict()
    if not isinstance(json_res, Unset):
        params.update(json_res)

    params["semanticKind"] = semantic_kind

    params["service"] = service

    params["sessionId"] = session_id

    params["spanKind"] = span_kind

    params["spanMinDurationMs"] = span_min_duration_ms

    params["spanModel"] = span_model

    params["spanStatus"] = span_status

    params["spanTool"] = span_tool

    params["status"] = status

    params["to"] = to

    params["tool"] = tool

    params["userId"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/analytics/timeseries",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalyticsTimeseriesResponseDto | None:
    if response.status_code == 200:
        response_200 = AnalyticsTimeseriesResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AnalyticsTimeseriesResponseDto]:
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
    app_id: str | Unset = UNSET,
    attr: AnalyticsControllerTimeseriesAttr | Unset = UNSET,
    attr_max: AnalyticsControllerTimeseriesAttrMax | Unset = UNSET,
    attr_min: AnalyticsControllerTimeseriesAttrMin | Unset = UNSET,
    environment: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    interval: AnalyticsControllerTimeseriesInterval | Unset = UNSET,
    max_cost_usd: str | Unset = UNSET,
    max_duration_ms: str | Unset = UNSET,
    max_tokens: str | Unset = UNSET,
    measure: AnalyticsControllerTimeseriesMeasure | Unset = UNSET,
    min_cost_usd: str | Unset = UNSET,
    min_duration_ms: str | Unset = UNSET,
    min_tokens: str | Unset = UNSET,
    model: str | Unset = UNSET,
    prompt_id: str | Unset = UNSET,
    prompt_version_id: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    query: str | Unset = UNSET,
    release: str | Unset = UNSET,
    res: AnalyticsControllerTimeseriesRes | Unset = UNSET,
    semantic_kind: str | Unset = UNSET,
    service: str | Unset = UNSET,
    session_id: str | Unset = UNSET,
    span_kind: str | Unset = UNSET,
    span_min_duration_ms: str | Unset = UNSET,
    span_model: str | Unset = UNSET,
    span_status: str | Unset = UNSET,
    span_tool: str | Unset = UNSET,
    status: str | Unset = UNSET,
    to: str | Unset = UNSET,
    tool: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> Response[AnalyticsTimeseriesResponseDto]:
    """
    Args:
        agent (str | Unset):
        app_id (str | Unset):
        attr (AnalyticsControllerTimeseriesAttr | Unset):
        attr_max (AnalyticsControllerTimeseriesAttrMax | Unset):
        attr_min (AnalyticsControllerTimeseriesAttrMin | Unset):
        environment (str | Unset):
        environment_id (str | Unset):
        from_ (str | Unset):
        interval (AnalyticsControllerTimeseriesInterval | Unset):
        max_cost_usd (str | Unset):
        max_duration_ms (str | Unset):
        max_tokens (str | Unset):
        measure (AnalyticsControllerTimeseriesMeasure | Unset):
        min_cost_usd (str | Unset):
        min_duration_ms (str | Unset):
        min_tokens (str | Unset):
        model (str | Unset):
        prompt_id (str | Unset):
        prompt_version_id (str | Unset):
        provider (str | Unset):
        query (str | Unset):
        release (str | Unset):
        res (AnalyticsControllerTimeseriesRes | Unset):
        semantic_kind (str | Unset):
        service (str | Unset):
        session_id (str | Unset):
        span_kind (str | Unset):
        span_min_duration_ms (str | Unset):
        span_model (str | Unset):
        span_status (str | Unset):
        span_tool (str | Unset):
        status (str | Unset):
        to (str | Unset):
        tool (str | Unset):
        user_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsTimeseriesResponseDto]
    """

    kwargs = _get_kwargs(
        agent=agent,
        app_id=app_id,
        attr=attr,
        attr_max=attr_max,
        attr_min=attr_min,
        environment=environment,
        environment_id=environment_id,
        from_=from_,
        interval=interval,
        max_cost_usd=max_cost_usd,
        max_duration_ms=max_duration_ms,
        max_tokens=max_tokens,
        measure=measure,
        min_cost_usd=min_cost_usd,
        min_duration_ms=min_duration_ms,
        min_tokens=min_tokens,
        model=model,
        prompt_id=prompt_id,
        prompt_version_id=prompt_version_id,
        provider=provider,
        query=query,
        release=release,
        res=res,
        semantic_kind=semantic_kind,
        service=service,
        session_id=session_id,
        span_kind=span_kind,
        span_min_duration_ms=span_min_duration_ms,
        span_model=span_model,
        span_status=span_status,
        span_tool=span_tool,
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
    app_id: str | Unset = UNSET,
    attr: AnalyticsControllerTimeseriesAttr | Unset = UNSET,
    attr_max: AnalyticsControllerTimeseriesAttrMax | Unset = UNSET,
    attr_min: AnalyticsControllerTimeseriesAttrMin | Unset = UNSET,
    environment: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    interval: AnalyticsControllerTimeseriesInterval | Unset = UNSET,
    max_cost_usd: str | Unset = UNSET,
    max_duration_ms: str | Unset = UNSET,
    max_tokens: str | Unset = UNSET,
    measure: AnalyticsControllerTimeseriesMeasure | Unset = UNSET,
    min_cost_usd: str | Unset = UNSET,
    min_duration_ms: str | Unset = UNSET,
    min_tokens: str | Unset = UNSET,
    model: str | Unset = UNSET,
    prompt_id: str | Unset = UNSET,
    prompt_version_id: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    query: str | Unset = UNSET,
    release: str | Unset = UNSET,
    res: AnalyticsControllerTimeseriesRes | Unset = UNSET,
    semantic_kind: str | Unset = UNSET,
    service: str | Unset = UNSET,
    session_id: str | Unset = UNSET,
    span_kind: str | Unset = UNSET,
    span_min_duration_ms: str | Unset = UNSET,
    span_model: str | Unset = UNSET,
    span_status: str | Unset = UNSET,
    span_tool: str | Unset = UNSET,
    status: str | Unset = UNSET,
    to: str | Unset = UNSET,
    tool: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> AnalyticsTimeseriesResponseDto | None:
    """
    Args:
        agent (str | Unset):
        app_id (str | Unset):
        attr (AnalyticsControllerTimeseriesAttr | Unset):
        attr_max (AnalyticsControllerTimeseriesAttrMax | Unset):
        attr_min (AnalyticsControllerTimeseriesAttrMin | Unset):
        environment (str | Unset):
        environment_id (str | Unset):
        from_ (str | Unset):
        interval (AnalyticsControllerTimeseriesInterval | Unset):
        max_cost_usd (str | Unset):
        max_duration_ms (str | Unset):
        max_tokens (str | Unset):
        measure (AnalyticsControllerTimeseriesMeasure | Unset):
        min_cost_usd (str | Unset):
        min_duration_ms (str | Unset):
        min_tokens (str | Unset):
        model (str | Unset):
        prompt_id (str | Unset):
        prompt_version_id (str | Unset):
        provider (str | Unset):
        query (str | Unset):
        release (str | Unset):
        res (AnalyticsControllerTimeseriesRes | Unset):
        semantic_kind (str | Unset):
        service (str | Unset):
        session_id (str | Unset):
        span_kind (str | Unset):
        span_min_duration_ms (str | Unset):
        span_model (str | Unset):
        span_status (str | Unset):
        span_tool (str | Unset):
        status (str | Unset):
        to (str | Unset):
        tool (str | Unset):
        user_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsTimeseriesResponseDto
    """

    return sync_detailed(
        client=client,
        agent=agent,
        app_id=app_id,
        attr=attr,
        attr_max=attr_max,
        attr_min=attr_min,
        environment=environment,
        environment_id=environment_id,
        from_=from_,
        interval=interval,
        max_cost_usd=max_cost_usd,
        max_duration_ms=max_duration_ms,
        max_tokens=max_tokens,
        measure=measure,
        min_cost_usd=min_cost_usd,
        min_duration_ms=min_duration_ms,
        min_tokens=min_tokens,
        model=model,
        prompt_id=prompt_id,
        prompt_version_id=prompt_version_id,
        provider=provider,
        query=query,
        release=release,
        res=res,
        semantic_kind=semantic_kind,
        service=service,
        session_id=session_id,
        span_kind=span_kind,
        span_min_duration_ms=span_min_duration_ms,
        span_model=span_model,
        span_status=span_status,
        span_tool=span_tool,
        status=status,
        to=to,
        tool=tool,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    agent: str | Unset = UNSET,
    app_id: str | Unset = UNSET,
    attr: AnalyticsControllerTimeseriesAttr | Unset = UNSET,
    attr_max: AnalyticsControllerTimeseriesAttrMax | Unset = UNSET,
    attr_min: AnalyticsControllerTimeseriesAttrMin | Unset = UNSET,
    environment: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    interval: AnalyticsControllerTimeseriesInterval | Unset = UNSET,
    max_cost_usd: str | Unset = UNSET,
    max_duration_ms: str | Unset = UNSET,
    max_tokens: str | Unset = UNSET,
    measure: AnalyticsControllerTimeseriesMeasure | Unset = UNSET,
    min_cost_usd: str | Unset = UNSET,
    min_duration_ms: str | Unset = UNSET,
    min_tokens: str | Unset = UNSET,
    model: str | Unset = UNSET,
    prompt_id: str | Unset = UNSET,
    prompt_version_id: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    query: str | Unset = UNSET,
    release: str | Unset = UNSET,
    res: AnalyticsControllerTimeseriesRes | Unset = UNSET,
    semantic_kind: str | Unset = UNSET,
    service: str | Unset = UNSET,
    session_id: str | Unset = UNSET,
    span_kind: str | Unset = UNSET,
    span_min_duration_ms: str | Unset = UNSET,
    span_model: str | Unset = UNSET,
    span_status: str | Unset = UNSET,
    span_tool: str | Unset = UNSET,
    status: str | Unset = UNSET,
    to: str | Unset = UNSET,
    tool: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> Response[AnalyticsTimeseriesResponseDto]:
    """
    Args:
        agent (str | Unset):
        app_id (str | Unset):
        attr (AnalyticsControllerTimeseriesAttr | Unset):
        attr_max (AnalyticsControllerTimeseriesAttrMax | Unset):
        attr_min (AnalyticsControllerTimeseriesAttrMin | Unset):
        environment (str | Unset):
        environment_id (str | Unset):
        from_ (str | Unset):
        interval (AnalyticsControllerTimeseriesInterval | Unset):
        max_cost_usd (str | Unset):
        max_duration_ms (str | Unset):
        max_tokens (str | Unset):
        measure (AnalyticsControllerTimeseriesMeasure | Unset):
        min_cost_usd (str | Unset):
        min_duration_ms (str | Unset):
        min_tokens (str | Unset):
        model (str | Unset):
        prompt_id (str | Unset):
        prompt_version_id (str | Unset):
        provider (str | Unset):
        query (str | Unset):
        release (str | Unset):
        res (AnalyticsControllerTimeseriesRes | Unset):
        semantic_kind (str | Unset):
        service (str | Unset):
        session_id (str | Unset):
        span_kind (str | Unset):
        span_min_duration_ms (str | Unset):
        span_model (str | Unset):
        span_status (str | Unset):
        span_tool (str | Unset):
        status (str | Unset):
        to (str | Unset):
        tool (str | Unset):
        user_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsTimeseriesResponseDto]
    """

    kwargs = _get_kwargs(
        agent=agent,
        app_id=app_id,
        attr=attr,
        attr_max=attr_max,
        attr_min=attr_min,
        environment=environment,
        environment_id=environment_id,
        from_=from_,
        interval=interval,
        max_cost_usd=max_cost_usd,
        max_duration_ms=max_duration_ms,
        max_tokens=max_tokens,
        measure=measure,
        min_cost_usd=min_cost_usd,
        min_duration_ms=min_duration_ms,
        min_tokens=min_tokens,
        model=model,
        prompt_id=prompt_id,
        prompt_version_id=prompt_version_id,
        provider=provider,
        query=query,
        release=release,
        res=res,
        semantic_kind=semantic_kind,
        service=service,
        session_id=session_id,
        span_kind=span_kind,
        span_min_duration_ms=span_min_duration_ms,
        span_model=span_model,
        span_status=span_status,
        span_tool=span_tool,
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
    app_id: str | Unset = UNSET,
    attr: AnalyticsControllerTimeseriesAttr | Unset = UNSET,
    attr_max: AnalyticsControllerTimeseriesAttrMax | Unset = UNSET,
    attr_min: AnalyticsControllerTimeseriesAttrMin | Unset = UNSET,
    environment: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    interval: AnalyticsControllerTimeseriesInterval | Unset = UNSET,
    max_cost_usd: str | Unset = UNSET,
    max_duration_ms: str | Unset = UNSET,
    max_tokens: str | Unset = UNSET,
    measure: AnalyticsControllerTimeseriesMeasure | Unset = UNSET,
    min_cost_usd: str | Unset = UNSET,
    min_duration_ms: str | Unset = UNSET,
    min_tokens: str | Unset = UNSET,
    model: str | Unset = UNSET,
    prompt_id: str | Unset = UNSET,
    prompt_version_id: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    query: str | Unset = UNSET,
    release: str | Unset = UNSET,
    res: AnalyticsControllerTimeseriesRes | Unset = UNSET,
    semantic_kind: str | Unset = UNSET,
    service: str | Unset = UNSET,
    session_id: str | Unset = UNSET,
    span_kind: str | Unset = UNSET,
    span_min_duration_ms: str | Unset = UNSET,
    span_model: str | Unset = UNSET,
    span_status: str | Unset = UNSET,
    span_tool: str | Unset = UNSET,
    status: str | Unset = UNSET,
    to: str | Unset = UNSET,
    tool: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> AnalyticsTimeseriesResponseDto | None:
    """
    Args:
        agent (str | Unset):
        app_id (str | Unset):
        attr (AnalyticsControllerTimeseriesAttr | Unset):
        attr_max (AnalyticsControllerTimeseriesAttrMax | Unset):
        attr_min (AnalyticsControllerTimeseriesAttrMin | Unset):
        environment (str | Unset):
        environment_id (str | Unset):
        from_ (str | Unset):
        interval (AnalyticsControllerTimeseriesInterval | Unset):
        max_cost_usd (str | Unset):
        max_duration_ms (str | Unset):
        max_tokens (str | Unset):
        measure (AnalyticsControllerTimeseriesMeasure | Unset):
        min_cost_usd (str | Unset):
        min_duration_ms (str | Unset):
        min_tokens (str | Unset):
        model (str | Unset):
        prompt_id (str | Unset):
        prompt_version_id (str | Unset):
        provider (str | Unset):
        query (str | Unset):
        release (str | Unset):
        res (AnalyticsControllerTimeseriesRes | Unset):
        semantic_kind (str | Unset):
        service (str | Unset):
        session_id (str | Unset):
        span_kind (str | Unset):
        span_min_duration_ms (str | Unset):
        span_model (str | Unset):
        span_status (str | Unset):
        span_tool (str | Unset):
        status (str | Unset):
        to (str | Unset):
        tool (str | Unset):
        user_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsTimeseriesResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            agent=agent,
            app_id=app_id,
            attr=attr,
            attr_max=attr_max,
            attr_min=attr_min,
            environment=environment,
            environment_id=environment_id,
            from_=from_,
            interval=interval,
            max_cost_usd=max_cost_usd,
            max_duration_ms=max_duration_ms,
            max_tokens=max_tokens,
            measure=measure,
            min_cost_usd=min_cost_usd,
            min_duration_ms=min_duration_ms,
            min_tokens=min_tokens,
            model=model,
            prompt_id=prompt_id,
            prompt_version_id=prompt_version_id,
            provider=provider,
            query=query,
            release=release,
            res=res,
            semantic_kind=semantic_kind,
            service=service,
            session_id=session_id,
            span_kind=span_kind,
            span_min_duration_ms=span_min_duration_ms,
            span_model=span_model,
            span_status=span_status,
            span_tool=span_tool,
            status=status,
            to=to,
            tool=tool,
            user_id=user_id,
        )
    ).parsed
