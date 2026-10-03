from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_description import ActivityDescription
from ...models.error_model import ErrorModel
from ...types import UNSET, Response


def _get_kwargs(
    workspace_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspaces/{workspace_id}/describe".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActivityDescription | ErrorModel:
    if response.status_code == 200:
        response_200 = ActivityDescription.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ActivityDescription | ErrorModel]:
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
) -> Response[ActivityDescription | ErrorModel]:
    """Start here: explains this workspace in plain language plus the spec format, roles and draft ops an
    agent uses to change it

     Call this first when you are setting up or changing what axonpush stores for an application.

    axonpush adapts per installation. A workspace spec declares, as data, what this application stores:
    - attributes: the data dictionary. Every attribute key the app may send, with a type, an optional
    role and a personal flag. Undeclared keys are dropped at ingest and counted.
    - entities: the things being tracked (for example agent, ticket, order). Each lists the attribute
    keys it stores (fields), the keys identify() may set (profile), terminal states, and the events that
    update it.
    - funnels, views and alerts: what the dashboard shows and what pages people.

    To change the spec, never rewrite it blindly: read the shared draft (workspaces.draft), send typed
    edits with workspaces.applyDraftOps using the draft's version, check workspaces.draftChanges, and
    ask the user to review before workspaces.activateDraft. Use workspaces.catalog to see which events
    and attributes the app really sends.

    SETTING UP AN APPLICATION (the user does not copy anything from the dashboard):
    1. Call workspaces_describe (this tool) and read the codebase to find what is worth tracking.
    2. Draft the data dictionary, entities and events with workspaces_draft and
    workspaces_applyDraftOps; explain any personal attributes to the user first.
    3. Ask the user to review and activate the draft in the dashboard, or call workspaces_activateDraft
    if they approve in the chat.
    4. Call workspaces_connect and write the returned env into the app's git-ignored env file
    (.env.local or the project's secret convention). Never commit, print or paste the key.
    5. Add the SDK observe calls where the events happen and identify calls for profile attributes,
    reading the env written in the previous step.
    6. Send one test event from the app and confirm it appears in workspaces_catalog.

    The response contains a plain-language summary of this workspace, the setup steps, the full format
    reference, the role list and the op catalogue with examples.

    Args:
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivityDescription | ErrorModel]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ActivityDescription | ErrorModel | None:
    """Start here: explains this workspace in plain language plus the spec format, roles and draft ops an
    agent uses to change it

     Call this first when you are setting up or changing what axonpush stores for an application.

    axonpush adapts per installation. A workspace spec declares, as data, what this application stores:
    - attributes: the data dictionary. Every attribute key the app may send, with a type, an optional
    role and a personal flag. Undeclared keys are dropped at ingest and counted.
    - entities: the things being tracked (for example agent, ticket, order). Each lists the attribute
    keys it stores (fields), the keys identify() may set (profile), terminal states, and the events that
    update it.
    - funnels, views and alerts: what the dashboard shows and what pages people.

    To change the spec, never rewrite it blindly: read the shared draft (workspaces.draft), send typed
    edits with workspaces.applyDraftOps using the draft's version, check workspaces.draftChanges, and
    ask the user to review before workspaces.activateDraft. Use workspaces.catalog to see which events
    and attributes the app really sends.

    SETTING UP AN APPLICATION (the user does not copy anything from the dashboard):
    1. Call workspaces_describe (this tool) and read the codebase to find what is worth tracking.
    2. Draft the data dictionary, entities and events with workspaces_draft and
    workspaces_applyDraftOps; explain any personal attributes to the user first.
    3. Ask the user to review and activate the draft in the dashboard, or call workspaces_activateDraft
    if they approve in the chat.
    4. Call workspaces_connect and write the returned env into the app's git-ignored env file
    (.env.local or the project's secret convention). Never commit, print or paste the key.
    5. Add the SDK observe calls where the events happen and identify calls for profile attributes,
    reading the env written in the previous step.
    6. Send one test event from the app and confirm it appears in workspaces_catalog.

    The response contains a plain-language summary of this workspace, the setup steps, the full format
    reference, the role list and the op catalogue with examples.

    Args:
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivityDescription | ErrorModel
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ActivityDescription | ErrorModel]:
    """Start here: explains this workspace in plain language plus the spec format, roles and draft ops an
    agent uses to change it

     Call this first when you are setting up or changing what axonpush stores for an application.

    axonpush adapts per installation. A workspace spec declares, as data, what this application stores:
    - attributes: the data dictionary. Every attribute key the app may send, with a type, an optional
    role and a personal flag. Undeclared keys are dropped at ingest and counted.
    - entities: the things being tracked (for example agent, ticket, order). Each lists the attribute
    keys it stores (fields), the keys identify() may set (profile), terminal states, and the events that
    update it.
    - funnels, views and alerts: what the dashboard shows and what pages people.

    To change the spec, never rewrite it blindly: read the shared draft (workspaces.draft), send typed
    edits with workspaces.applyDraftOps using the draft's version, check workspaces.draftChanges, and
    ask the user to review before workspaces.activateDraft. Use workspaces.catalog to see which events
    and attributes the app really sends.

    SETTING UP AN APPLICATION (the user does not copy anything from the dashboard):
    1. Call workspaces_describe (this tool) and read the codebase to find what is worth tracking.
    2. Draft the data dictionary, entities and events with workspaces_draft and
    workspaces_applyDraftOps; explain any personal attributes to the user first.
    3. Ask the user to review and activate the draft in the dashboard, or call workspaces_activateDraft
    if they approve in the chat.
    4. Call workspaces_connect and write the returned env into the app's git-ignored env file
    (.env.local or the project's secret convention). Never commit, print or paste the key.
    5. Add the SDK observe calls where the events happen and identify calls for profile attributes,
    reading the env written in the previous step.
    6. Send one test event from the app and confirm it appears in workspaces_catalog.

    The response contains a plain-language summary of this workspace, the setup steps, the full format
    reference, the role list and the op catalogue with examples.

    Args:
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivityDescription | ErrorModel]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ActivityDescription | ErrorModel | None:
    """Start here: explains this workspace in plain language plus the spec format, roles and draft ops an
    agent uses to change it

     Call this first when you are setting up or changing what axonpush stores for an application.

    axonpush adapts per installation. A workspace spec declares, as data, what this application stores:
    - attributes: the data dictionary. Every attribute key the app may send, with a type, an optional
    role and a personal flag. Undeclared keys are dropped at ingest and counted.
    - entities: the things being tracked (for example agent, ticket, order). Each lists the attribute
    keys it stores (fields), the keys identify() may set (profile), terminal states, and the events that
    update it.
    - funnels, views and alerts: what the dashboard shows and what pages people.

    To change the spec, never rewrite it blindly: read the shared draft (workspaces.draft), send typed
    edits with workspaces.applyDraftOps using the draft's version, check workspaces.draftChanges, and
    ask the user to review before workspaces.activateDraft. Use workspaces.catalog to see which events
    and attributes the app really sends.

    SETTING UP AN APPLICATION (the user does not copy anything from the dashboard):
    1. Call workspaces_describe (this tool) and read the codebase to find what is worth tracking.
    2. Draft the data dictionary, entities and events with workspaces_draft and
    workspaces_applyDraftOps; explain any personal attributes to the user first.
    3. Ask the user to review and activate the draft in the dashboard, or call workspaces_activateDraft
    if they approve in the chat.
    4. Call workspaces_connect and write the returned env into the app's git-ignored env file
    (.env.local or the project's secret convention). Never commit, print or paste the key.
    5. Add the SDK observe calls where the events happen and identify calls for profile attributes,
    reading the env written in the previous step.
    6. Send one test event from the app and confirm it appears in workspaces_catalog.

    The response contains a plain-language summary of this workspace, the setup steps, the full format
    reference, the role list and the op catalogue with examples.

    Args:
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivityDescription | ErrorModel
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
        )
    ).parsed
