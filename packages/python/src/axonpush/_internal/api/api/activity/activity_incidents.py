from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_incidents_freshness import ActivityIncidentsFreshness
from ...models.error_model import ErrorModel
from ...models.workspace_incidents_output_body import WorkspaceIncidentsOutputBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: str,
    *,
    environment: str | Unset = UNSET,
    entity: str | Unset = UNSET,
    entity_id: str | Unset = UNSET,
    side: str | Unset = UNSET,
    client_query: str | Unset = UNSET,
    action: str | Unset = UNSET,
    outcome: str | Unset = UNSET,
    state: str | Unset = UNSET,
    freshness: ActivityIncidentsFreshness | Unset = UNSET,
    q: str | Unset = UNSET,
    agent_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 100,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["environment"] = environment

    params["entity"] = entity

    params["entityId"] = entity_id

    params["side"] = side

    params["client"] = client_query

    params["action"] = action

    params["outcome"] = outcome

    params["state"] = state

    json_freshness: str | Unset = UNSET
    if not isinstance(freshness, Unset):
        json_freshness = freshness.value

    params["freshness"] = json_freshness

    params["q"] = q

    params["agentId"] = agent_id

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspaces/{workspace_id}/incidents".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | WorkspaceIncidentsOutputBody:
    if response.status_code == 200:
        response_200 = WorkspaceIncidentsOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | WorkspaceIncidentsOutputBody]:
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
    side: str | Unset = UNSET,
    client_query: str | Unset = UNSET,
    action: str | Unset = UNSET,
    outcome: str | Unset = UNSET,
    state: str | Unset = UNSET,
    freshness: ActivityIncidentsFreshness | Unset = UNSET,
    q: str | Unset = UNSET,
    agent_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 100,
) -> Response[ErrorModel | WorkspaceIncidentsOutputBody]:
    """Read lifecycle incidents and recovery without duplicate notifications

    Args:
        workspace_id (str):
        environment (str | Unset):
        entity (str | Unset):
        entity_id (str | Unset):
        side (str | Unset):
        client_query (str | Unset):
        action (str | Unset):
        outcome (str | Unset):
        state (str | Unset):
        freshness (ActivityIncidentsFreshness | Unset):
        q (str | Unset):
        agent_id (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | WorkspaceIncidentsOutputBody]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        environment=environment,
        entity=entity,
        entity_id=entity_id,
        side=side,
        client_query=client_query,
        action=action,
        outcome=outcome,
        state=state,
        freshness=freshness,
        q=q,
        agent_id=agent_id,
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
    side: str | Unset = UNSET,
    client_query: str | Unset = UNSET,
    action: str | Unset = UNSET,
    outcome: str | Unset = UNSET,
    state: str | Unset = UNSET,
    freshness: ActivityIncidentsFreshness | Unset = UNSET,
    q: str | Unset = UNSET,
    agent_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 100,
) -> ErrorModel | WorkspaceIncidentsOutputBody | None:
    """Read lifecycle incidents and recovery without duplicate notifications

    Args:
        workspace_id (str):
        environment (str | Unset):
        entity (str | Unset):
        entity_id (str | Unset):
        side (str | Unset):
        client_query (str | Unset):
        action (str | Unset):
        outcome (str | Unset):
        state (str | Unset):
        freshness (ActivityIncidentsFreshness | Unset):
        q (str | Unset):
        agent_id (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | WorkspaceIncidentsOutputBody
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        environment=environment,
        entity=entity,
        entity_id=entity_id,
        side=side,
        client_query=client_query,
        action=action,
        outcome=outcome,
        state=state,
        freshness=freshness,
        q=q,
        agent_id=agent_id,
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
    side: str | Unset = UNSET,
    client_query: str | Unset = UNSET,
    action: str | Unset = UNSET,
    outcome: str | Unset = UNSET,
    state: str | Unset = UNSET,
    freshness: ActivityIncidentsFreshness | Unset = UNSET,
    q: str | Unset = UNSET,
    agent_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 100,
) -> Response[ErrorModel | WorkspaceIncidentsOutputBody]:
    """Read lifecycle incidents and recovery without duplicate notifications

    Args:
        workspace_id (str):
        environment (str | Unset):
        entity (str | Unset):
        entity_id (str | Unset):
        side (str | Unset):
        client_query (str | Unset):
        action (str | Unset):
        outcome (str | Unset):
        state (str | Unset):
        freshness (ActivityIncidentsFreshness | Unset):
        q (str | Unset):
        agent_id (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | WorkspaceIncidentsOutputBody]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        environment=environment,
        entity=entity,
        entity_id=entity_id,
        side=side,
        client_query=client_query,
        action=action,
        outcome=outcome,
        state=state,
        freshness=freshness,
        q=q,
        agent_id=agent_id,
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
    side: str | Unset = UNSET,
    client_query: str | Unset = UNSET,
    action: str | Unset = UNSET,
    outcome: str | Unset = UNSET,
    state: str | Unset = UNSET,
    freshness: ActivityIncidentsFreshness | Unset = UNSET,
    q: str | Unset = UNSET,
    agent_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 100,
) -> ErrorModel | WorkspaceIncidentsOutputBody | None:
    """Read lifecycle incidents and recovery without duplicate notifications

    Args:
        workspace_id (str):
        environment (str | Unset):
        entity (str | Unset):
        entity_id (str | Unset):
        side (str | Unset):
        client_query (str | Unset):
        action (str | Unset):
        outcome (str | Unset):
        state (str | Unset):
        freshness (ActivityIncidentsFreshness | Unset):
        q (str | Unset):
        agent_id (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | WorkspaceIncidentsOutputBody
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            environment=environment,
            entity=entity,
            entity_id=entity_id,
            side=side,
            client_query=client_query,
            action=action,
            outcome=outcome,
            state=state,
            freshness=freshness,
            q=q,
            agent_id=agent_id,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
