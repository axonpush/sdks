from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_summary import ActivitySummary
from ...models.activity_summary_freshness import ActivitySummaryFreshness
from ...models.error_model import ErrorModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: str,
    *,
    environment: str | Unset = UNSET,
    entity: str | Unset = UNSET,
    entity_id: str | Unset = UNSET,
    ref: str | Unset = UNSET,
    with_: str | Unset = UNSET,
    side: str | Unset = UNSET,
    client_query: str | Unset = UNSET,
    outcome: str | Unset = UNSET,
    action: str | Unset = UNSET,
    state: str | Unset = UNSET,
    freshness: ActivitySummaryFreshness | Unset = UNSET,
    q: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 100,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["environment"] = environment

    params["entity"] = entity

    params["entityId"] = entity_id

    params["ref"] = ref

    params["with"] = with_

    params["side"] = side

    params["client"] = client_query

    params["outcome"] = outcome

    params["action"] = action

    params["state"] = state

    json_freshness: str | Unset = UNSET
    if not isinstance(freshness, Unset):
        json_freshness = freshness.value

    params["freshness"] = json_freshness

    params["q"] = q

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspaces/{workspace_id}/summary".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActivitySummary | ErrorModel:
    if response.status_code == 200:
        response_200 = ActivitySummary.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ActivitySummary | ErrorModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
    entity: str | Unset = UNSET,
    entity_id: str | Unset = UNSET,
    ref: str | Unset = UNSET,
    with_: str | Unset = UNSET,
    side: str | Unset = UNSET,
    client_query: str | Unset = UNSET,
    outcome: str | Unset = UNSET,
    action: str | Unset = UNSET,
    state: str | Unset = UNSET,
    freshness: ActivitySummaryFreshness | Unset = UNSET,
    q: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 100,
) -> Response[ActivitySummary | ErrorModel]:
    """Exact entity counts per state with a 15 minute activity window

    Args:
        workspace_id (str):
        environment (str | Unset):
        entity (str | Unset): Entity type
        entity_id (str | Unset):
        ref (str | Unset): type:id; entities that are, or link to, this entity. Timeline:
            observations that reference it
        with_ (str | Unset): Timeline only: type:id that a record must also reference, so ref plus
            with lists the records linking two entities (a graph edge's evidence)
        side (str | Unset): Filter by the actor_side role
        client_query (str | Unset): Filter by the client role
        outcome (str | Unset): Filter by the outcome role
        action (str | Unset): Filter by the last_action role
        state (str | Unset):
        freshness (ActivitySummaryFreshness | Unset): current: live evidence received in the last
            15 minutes; stale: quieter than that, or only known from a snapshot; unknown: an open
            state outlived its expected duration. fresh is an alias of current
        q (str | Unset): Matches the entity id and non-personal text fields and profile traits
        cursor (str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivitySummary | ErrorModel]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        environment=environment,
        entity=entity,
        entity_id=entity_id,
        ref=ref,
        with_=with_,
        side=side,
        client_query=client_query,
        outcome=outcome,
        action=action,
        state=state,
        freshness=freshness,
        q=q,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
    entity: str | Unset = UNSET,
    entity_id: str | Unset = UNSET,
    ref: str | Unset = UNSET,
    with_: str | Unset = UNSET,
    side: str | Unset = UNSET,
    client_query: str | Unset = UNSET,
    outcome: str | Unset = UNSET,
    action: str | Unset = UNSET,
    state: str | Unset = UNSET,
    freshness: ActivitySummaryFreshness | Unset = UNSET,
    q: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 100,
) -> ActivitySummary | ErrorModel | None:
    """Exact entity counts per state with a 15 minute activity window

    Args:
        workspace_id (str):
        environment (str | Unset):
        entity (str | Unset): Entity type
        entity_id (str | Unset):
        ref (str | Unset): type:id; entities that are, or link to, this entity. Timeline:
            observations that reference it
        with_ (str | Unset): Timeline only: type:id that a record must also reference, so ref plus
            with lists the records linking two entities (a graph edge's evidence)
        side (str | Unset): Filter by the actor_side role
        client_query (str | Unset): Filter by the client role
        outcome (str | Unset): Filter by the outcome role
        action (str | Unset): Filter by the last_action role
        state (str | Unset):
        freshness (ActivitySummaryFreshness | Unset): current: live evidence received in the last
            15 minutes; stale: quieter than that, or only known from a snapshot; unknown: an open
            state outlived its expected duration. fresh is an alias of current
        q (str | Unset): Matches the entity id and non-personal text fields and profile traits
        cursor (str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivitySummary | ErrorModel
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        environment=environment,
        entity=entity,
        entity_id=entity_id,
        ref=ref,
        with_=with_,
        side=side,
        client_query=client_query,
        outcome=outcome,
        action=action,
        state=state,
        freshness=freshness,
        q=q,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
    entity: str | Unset = UNSET,
    entity_id: str | Unset = UNSET,
    ref: str | Unset = UNSET,
    with_: str | Unset = UNSET,
    side: str | Unset = UNSET,
    client_query: str | Unset = UNSET,
    outcome: str | Unset = UNSET,
    action: str | Unset = UNSET,
    state: str | Unset = UNSET,
    freshness: ActivitySummaryFreshness | Unset = UNSET,
    q: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 100,
) -> Response[ActivitySummary | ErrorModel]:
    """Exact entity counts per state with a 15 minute activity window

    Args:
        workspace_id (str):
        environment (str | Unset):
        entity (str | Unset): Entity type
        entity_id (str | Unset):
        ref (str | Unset): type:id; entities that are, or link to, this entity. Timeline:
            observations that reference it
        with_ (str | Unset): Timeline only: type:id that a record must also reference, so ref plus
            with lists the records linking two entities (a graph edge's evidence)
        side (str | Unset): Filter by the actor_side role
        client_query (str | Unset): Filter by the client role
        outcome (str | Unset): Filter by the outcome role
        action (str | Unset): Filter by the last_action role
        state (str | Unset):
        freshness (ActivitySummaryFreshness | Unset): current: live evidence received in the last
            15 minutes; stale: quieter than that, or only known from a snapshot; unknown: an open
            state outlived its expected duration. fresh is an alias of current
        q (str | Unset): Matches the entity id and non-personal text fields and profile traits
        cursor (str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivitySummary | ErrorModel]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        environment=environment,
        entity=entity,
        entity_id=entity_id,
        ref=ref,
        with_=with_,
        side=side,
        client_query=client_query,
        outcome=outcome,
        action=action,
        state=state,
        freshness=freshness,
        q=q,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
    entity: str | Unset = UNSET,
    entity_id: str | Unset = UNSET,
    ref: str | Unset = UNSET,
    with_: str | Unset = UNSET,
    side: str | Unset = UNSET,
    client_query: str | Unset = UNSET,
    outcome: str | Unset = UNSET,
    action: str | Unset = UNSET,
    state: str | Unset = UNSET,
    freshness: ActivitySummaryFreshness | Unset = UNSET,
    q: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 100,
) -> ActivitySummary | ErrorModel | None:
    """Exact entity counts per state with a 15 minute activity window

    Args:
        workspace_id (str):
        environment (str | Unset):
        entity (str | Unset): Entity type
        entity_id (str | Unset):
        ref (str | Unset): type:id; entities that are, or link to, this entity. Timeline:
            observations that reference it
        with_ (str | Unset): Timeline only: type:id that a record must also reference, so ref plus
            with lists the records linking two entities (a graph edge's evidence)
        side (str | Unset): Filter by the actor_side role
        client_query (str | Unset): Filter by the client role
        outcome (str | Unset): Filter by the outcome role
        action (str | Unset): Filter by the last_action role
        state (str | Unset):
        freshness (ActivitySummaryFreshness | Unset): current: live evidence received in the last
            15 minutes; stale: quieter than that, or only known from a snapshot; unknown: an open
            state outlived its expected duration. fresh is an alias of current
        q (str | Unset): Matches the entity id and non-personal text fields and profile traits
        cursor (str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivitySummary | ErrorModel
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            environment=environment,
            entity=entity,
            entity_id=entity_id,
            ref=ref,
            with_=with_,
            side=side,
            client_query=client_query,
            outcome=outcome,
            action=action,
            state=state,
            freshness=freshness,
            q=q,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
