from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_compare_response_dto import AnalyticsCompareResponseDto
from ...models.analytics_controller_compare_attr import AnalyticsControllerCompareAttr
from ...models.analytics_controller_compare_attr_max import AnalyticsControllerCompareAttrMax
from ...models.analytics_controller_compare_attr_min import AnalyticsControllerCompareAttrMin
from ...models.analytics_controller_compare_dimension import AnalyticsControllerCompareDimension
from ...models.analytics_controller_compare_res import AnalyticsControllerCompareRes
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    agent: str | Unset = UNSET,
    app_id: str | Unset = UNSET,
    attr: AnalyticsControllerCompareAttr | Unset = UNSET,
    attr_max: AnalyticsControllerCompareAttrMax | Unset = UNSET,
    attr_min: AnalyticsControllerCompareAttrMin | Unset = UNSET,
    baseline: str,
    candidate: str,
    dimension: AnalyticsControllerCompareDimension,
    environment: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    max_cost_usd: str | Unset = UNSET,
    max_duration_ms: str | Unset = UNSET,
    max_tokens: str | Unset = UNSET,
    min_cost_usd: str | Unset = UNSET,
    min_duration_ms: str | Unset = UNSET,
    min_tokens: str | Unset = UNSET,
    model: str | Unset = UNSET,
    prompt_id: str | Unset = UNSET,
    prompt_version_id: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    query: str | Unset = UNSET,
    release: str | Unset = UNSET,
    res: AnalyticsControllerCompareRes | Unset = UNSET,
    semantic_kind: str | Unset = UNSET,
    service: str | Unset = UNSET,
    session_id: str | Unset = UNSET,
    span_kind: str | Unset = UNSET,
    span_min_duration_ms: str | Unset = UNSET,
    span_model: str | Unset = UNSET,
    span_status: str | Unset = UNSET,
    span_tool: str | Unset = UNSET,
    status: str | Unset = UNSET,
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

    params["baseline"] = baseline

    params["candidate"] = candidate

    json_dimension = dimension.value
    params["dimension"] = json_dimension

    params["environment"] = environment

    params["environmentId"] = environment_id

    params["maxCostUsd"] = max_cost_usd

    params["maxDurationMs"] = max_duration_ms

    params["maxTokens"] = max_tokens

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

    params["tool"] = tool

    params["userId"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/analytics/compare",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalyticsCompareResponseDto | None:
    if response.status_code == 200:
        response_200 = AnalyticsCompareResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AnalyticsCompareResponseDto]:
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
    attr: AnalyticsControllerCompareAttr | Unset = UNSET,
    attr_max: AnalyticsControllerCompareAttrMax | Unset = UNSET,
    attr_min: AnalyticsControllerCompareAttrMin | Unset = UNSET,
    baseline: str,
    candidate: str,
    dimension: AnalyticsControllerCompareDimension,
    environment: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    max_cost_usd: str | Unset = UNSET,
    max_duration_ms: str | Unset = UNSET,
    max_tokens: str | Unset = UNSET,
    min_cost_usd: str | Unset = UNSET,
    min_duration_ms: str | Unset = UNSET,
    min_tokens: str | Unset = UNSET,
    model: str | Unset = UNSET,
    prompt_id: str | Unset = UNSET,
    prompt_version_id: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    query: str | Unset = UNSET,
    release: str | Unset = UNSET,
    res: AnalyticsControllerCompareRes | Unset = UNSET,
    semantic_kind: str | Unset = UNSET,
    service: str | Unset = UNSET,
    session_id: str | Unset = UNSET,
    span_kind: str | Unset = UNSET,
    span_min_duration_ms: str | Unset = UNSET,
    span_model: str | Unset = UNSET,
    span_status: str | Unset = UNSET,
    span_tool: str | Unset = UNSET,
    status: str | Unset = UNSET,
    tool: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> Response[AnalyticsCompareResponseDto]:
    """
    Args:
        agent (str | Unset):
        app_id (str | Unset):
        attr (AnalyticsControllerCompareAttr | Unset):
        attr_max (AnalyticsControllerCompareAttrMax | Unset):
        attr_min (AnalyticsControllerCompareAttrMin | Unset):
        baseline (str):
        candidate (str):
        dimension (AnalyticsControllerCompareDimension):
        environment (str | Unset):
        environment_id (str | Unset):
        max_cost_usd (str | Unset):
        max_duration_ms (str | Unset):
        max_tokens (str | Unset):
        min_cost_usd (str | Unset):
        min_duration_ms (str | Unset):
        min_tokens (str | Unset):
        model (str | Unset):
        prompt_id (str | Unset):
        prompt_version_id (str | Unset):
        provider (str | Unset):
        query (str | Unset):
        release (str | Unset):
        res (AnalyticsControllerCompareRes | Unset):
        semantic_kind (str | Unset):
        service (str | Unset):
        session_id (str | Unset):
        span_kind (str | Unset):
        span_min_duration_ms (str | Unset):
        span_model (str | Unset):
        span_status (str | Unset):
        span_tool (str | Unset):
        status (str | Unset):
        tool (str | Unset):
        user_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsCompareResponseDto]
    """

    kwargs = _get_kwargs(
        agent=agent,
        app_id=app_id,
        attr=attr,
        attr_max=attr_max,
        attr_min=attr_min,
        baseline=baseline,
        candidate=candidate,
        dimension=dimension,
        environment=environment,
        environment_id=environment_id,
        max_cost_usd=max_cost_usd,
        max_duration_ms=max_duration_ms,
        max_tokens=max_tokens,
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
    attr: AnalyticsControllerCompareAttr | Unset = UNSET,
    attr_max: AnalyticsControllerCompareAttrMax | Unset = UNSET,
    attr_min: AnalyticsControllerCompareAttrMin | Unset = UNSET,
    baseline: str,
    candidate: str,
    dimension: AnalyticsControllerCompareDimension,
    environment: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    max_cost_usd: str | Unset = UNSET,
    max_duration_ms: str | Unset = UNSET,
    max_tokens: str | Unset = UNSET,
    min_cost_usd: str | Unset = UNSET,
    min_duration_ms: str | Unset = UNSET,
    min_tokens: str | Unset = UNSET,
    model: str | Unset = UNSET,
    prompt_id: str | Unset = UNSET,
    prompt_version_id: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    query: str | Unset = UNSET,
    release: str | Unset = UNSET,
    res: AnalyticsControllerCompareRes | Unset = UNSET,
    semantic_kind: str | Unset = UNSET,
    service: str | Unset = UNSET,
    session_id: str | Unset = UNSET,
    span_kind: str | Unset = UNSET,
    span_min_duration_ms: str | Unset = UNSET,
    span_model: str | Unset = UNSET,
    span_status: str | Unset = UNSET,
    span_tool: str | Unset = UNSET,
    status: str | Unset = UNSET,
    tool: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> AnalyticsCompareResponseDto | None:
    """
    Args:
        agent (str | Unset):
        app_id (str | Unset):
        attr (AnalyticsControllerCompareAttr | Unset):
        attr_max (AnalyticsControllerCompareAttrMax | Unset):
        attr_min (AnalyticsControllerCompareAttrMin | Unset):
        baseline (str):
        candidate (str):
        dimension (AnalyticsControllerCompareDimension):
        environment (str | Unset):
        environment_id (str | Unset):
        max_cost_usd (str | Unset):
        max_duration_ms (str | Unset):
        max_tokens (str | Unset):
        min_cost_usd (str | Unset):
        min_duration_ms (str | Unset):
        min_tokens (str | Unset):
        model (str | Unset):
        prompt_id (str | Unset):
        prompt_version_id (str | Unset):
        provider (str | Unset):
        query (str | Unset):
        release (str | Unset):
        res (AnalyticsControllerCompareRes | Unset):
        semantic_kind (str | Unset):
        service (str | Unset):
        session_id (str | Unset):
        span_kind (str | Unset):
        span_min_duration_ms (str | Unset):
        span_model (str | Unset):
        span_status (str | Unset):
        span_tool (str | Unset):
        status (str | Unset):
        tool (str | Unset):
        user_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsCompareResponseDto
    """

    return sync_detailed(
        client=client,
        agent=agent,
        app_id=app_id,
        attr=attr,
        attr_max=attr_max,
        attr_min=attr_min,
        baseline=baseline,
        candidate=candidate,
        dimension=dimension,
        environment=environment,
        environment_id=environment_id,
        max_cost_usd=max_cost_usd,
        max_duration_ms=max_duration_ms,
        max_tokens=max_tokens,
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
        tool=tool,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    agent: str | Unset = UNSET,
    app_id: str | Unset = UNSET,
    attr: AnalyticsControllerCompareAttr | Unset = UNSET,
    attr_max: AnalyticsControllerCompareAttrMax | Unset = UNSET,
    attr_min: AnalyticsControllerCompareAttrMin | Unset = UNSET,
    baseline: str,
    candidate: str,
    dimension: AnalyticsControllerCompareDimension,
    environment: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    max_cost_usd: str | Unset = UNSET,
    max_duration_ms: str | Unset = UNSET,
    max_tokens: str | Unset = UNSET,
    min_cost_usd: str | Unset = UNSET,
    min_duration_ms: str | Unset = UNSET,
    min_tokens: str | Unset = UNSET,
    model: str | Unset = UNSET,
    prompt_id: str | Unset = UNSET,
    prompt_version_id: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    query: str | Unset = UNSET,
    release: str | Unset = UNSET,
    res: AnalyticsControllerCompareRes | Unset = UNSET,
    semantic_kind: str | Unset = UNSET,
    service: str | Unset = UNSET,
    session_id: str | Unset = UNSET,
    span_kind: str | Unset = UNSET,
    span_min_duration_ms: str | Unset = UNSET,
    span_model: str | Unset = UNSET,
    span_status: str | Unset = UNSET,
    span_tool: str | Unset = UNSET,
    status: str | Unset = UNSET,
    tool: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> Response[AnalyticsCompareResponseDto]:
    """
    Args:
        agent (str | Unset):
        app_id (str | Unset):
        attr (AnalyticsControllerCompareAttr | Unset):
        attr_max (AnalyticsControllerCompareAttrMax | Unset):
        attr_min (AnalyticsControllerCompareAttrMin | Unset):
        baseline (str):
        candidate (str):
        dimension (AnalyticsControllerCompareDimension):
        environment (str | Unset):
        environment_id (str | Unset):
        max_cost_usd (str | Unset):
        max_duration_ms (str | Unset):
        max_tokens (str | Unset):
        min_cost_usd (str | Unset):
        min_duration_ms (str | Unset):
        min_tokens (str | Unset):
        model (str | Unset):
        prompt_id (str | Unset):
        prompt_version_id (str | Unset):
        provider (str | Unset):
        query (str | Unset):
        release (str | Unset):
        res (AnalyticsControllerCompareRes | Unset):
        semantic_kind (str | Unset):
        service (str | Unset):
        session_id (str | Unset):
        span_kind (str | Unset):
        span_min_duration_ms (str | Unset):
        span_model (str | Unset):
        span_status (str | Unset):
        span_tool (str | Unset):
        status (str | Unset):
        tool (str | Unset):
        user_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsCompareResponseDto]
    """

    kwargs = _get_kwargs(
        agent=agent,
        app_id=app_id,
        attr=attr,
        attr_max=attr_max,
        attr_min=attr_min,
        baseline=baseline,
        candidate=candidate,
        dimension=dimension,
        environment=environment,
        environment_id=environment_id,
        max_cost_usd=max_cost_usd,
        max_duration_ms=max_duration_ms,
        max_tokens=max_tokens,
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
    attr: AnalyticsControllerCompareAttr | Unset = UNSET,
    attr_max: AnalyticsControllerCompareAttrMax | Unset = UNSET,
    attr_min: AnalyticsControllerCompareAttrMin | Unset = UNSET,
    baseline: str,
    candidate: str,
    dimension: AnalyticsControllerCompareDimension,
    environment: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    max_cost_usd: str | Unset = UNSET,
    max_duration_ms: str | Unset = UNSET,
    max_tokens: str | Unset = UNSET,
    min_cost_usd: str | Unset = UNSET,
    min_duration_ms: str | Unset = UNSET,
    min_tokens: str | Unset = UNSET,
    model: str | Unset = UNSET,
    prompt_id: str | Unset = UNSET,
    prompt_version_id: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    query: str | Unset = UNSET,
    release: str | Unset = UNSET,
    res: AnalyticsControllerCompareRes | Unset = UNSET,
    semantic_kind: str | Unset = UNSET,
    service: str | Unset = UNSET,
    session_id: str | Unset = UNSET,
    span_kind: str | Unset = UNSET,
    span_min_duration_ms: str | Unset = UNSET,
    span_model: str | Unset = UNSET,
    span_status: str | Unset = UNSET,
    span_tool: str | Unset = UNSET,
    status: str | Unset = UNSET,
    tool: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> AnalyticsCompareResponseDto | None:
    """
    Args:
        agent (str | Unset):
        app_id (str | Unset):
        attr (AnalyticsControllerCompareAttr | Unset):
        attr_max (AnalyticsControllerCompareAttrMax | Unset):
        attr_min (AnalyticsControllerCompareAttrMin | Unset):
        baseline (str):
        candidate (str):
        dimension (AnalyticsControllerCompareDimension):
        environment (str | Unset):
        environment_id (str | Unset):
        max_cost_usd (str | Unset):
        max_duration_ms (str | Unset):
        max_tokens (str | Unset):
        min_cost_usd (str | Unset):
        min_duration_ms (str | Unset):
        min_tokens (str | Unset):
        model (str | Unset):
        prompt_id (str | Unset):
        prompt_version_id (str | Unset):
        provider (str | Unset):
        query (str | Unset):
        release (str | Unset):
        res (AnalyticsControllerCompareRes | Unset):
        semantic_kind (str | Unset):
        service (str | Unset):
        session_id (str | Unset):
        span_kind (str | Unset):
        span_min_duration_ms (str | Unset):
        span_model (str | Unset):
        span_status (str | Unset):
        span_tool (str | Unset):
        status (str | Unset):
        tool (str | Unset):
        user_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsCompareResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            agent=agent,
            app_id=app_id,
            attr=attr,
            attr_max=attr_max,
            attr_min=attr_min,
            baseline=baseline,
            candidate=candidate,
            dimension=dimension,
            environment=environment,
            environment_id=environment_id,
            max_cost_usd=max_cost_usd,
            max_duration_ms=max_duration_ms,
            max_tokens=max_tokens,
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
            tool=tool,
            user_id=user_id,
        )
    ).parsed
