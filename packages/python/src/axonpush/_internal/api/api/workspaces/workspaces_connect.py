from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.activity_connect_result import ActivityConnectResult
from ...models.connect_input_body import ConnectInputBody
from ...models.error_model import ErrorModel
from typing import cast


def _get_kwargs(
    workspace_id: str,
    *,
    body: ConnectInputBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/workspaces/{workspace_id}/connect".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActivityConnectResult | ErrorModel:
    if response.status_code == 200:
        response_200 = ActivityConnectResult.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ActivityConnectResult | ErrorModel]:
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
    body: ConnectInputBody,
) -> Response[ActivityConnectResult | ErrorModel]:
    """Connect a workflow runtime or application: mint its key and return env, OTLP, Sentry and SDK setup

     Give an application the key and settings it needs for this workspace, so nobody copies keys from the
    dashboard.

    Choose the workspace, an explicit environment and a purpose first. The call mints one key bound to
    this workspace's application and that environment, and returns the API URL, an env map, OTLP
    settings, a Sentry DSN when available and SDK snippets.

    Workflow runtime (recommended for workflows): set purpose to workflow_runtime with workflow, every
    evidence source the runtime publishes and every action handler it runs. The key gets events:publish,
    plus workflows:execute when there are handlers, and the result includes workflowRuntime.id (also
    AXONPUSH_WORKFLOW_RUNTIME_ID in env). Next, run workflows_previewDeployment and, once the user
    approves, workflows_applyDeployment with that runtime ID; this binds the sources to this key. Follow
    workflows_describe for the full path. A connected runtime and a ready deployment are configuration
    only. Outcomes come from evaluated cases, which need facts published after the source write commits,
    explicit reconciliation coverage and, for actions, a record lookup after every execution. If sources
    or handlers change, reconnect with rotate: true.

    Secrets: when an agent calls this tool, the key and DSN are never returned. The result has claim, a
    one-time link (valid 30 minutes) the signed-in user opens in the dashboard, and secret env values
    are placeholders. Ask the user to open it and save the key in the app's git-ignored env file as
    AXONPUSH_API_KEY (and SENTRY_DSN if shown). Do not overwrite a working configuration with
    placeholders, skip the claim step, or put credentials in chat or commits. Non-secret settings can be
    merged using the project's existing convention.

    Other purposes (default, web, worker and so on) mint a publish-only key (events:publish) for
    diagnostics. They do not need a workflow. To add business observability, use SDK observe/identify
    calls and reuse existing logging, OpenTelemetry or Sentry setup so exceptions keep their original
    traceback and source locations. Keep the existing capture policy, correlate trace/span IDs where
    available, and test with a controlled local exception. Do not create synthetic production errors.

    Calling again with the same environment and purpose returns the existing key's metadata without the
    secret; it does not mint another key. If the secret was lost, explain that rotate: true revokes the
    old key, and rotate only when the user wants that.

    Args:
        workspace_id (str):
        body (ConnectInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivityConnectResult | ErrorModel]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ConnectInputBody,
) -> ActivityConnectResult | ErrorModel | None:
    """Connect a workflow runtime or application: mint its key and return env, OTLP, Sentry and SDK setup

     Give an application the key and settings it needs for this workspace, so nobody copies keys from the
    dashboard.

    Choose the workspace, an explicit environment and a purpose first. The call mints one key bound to
    this workspace's application and that environment, and returns the API URL, an env map, OTLP
    settings, a Sentry DSN when available and SDK snippets.

    Workflow runtime (recommended for workflows): set purpose to workflow_runtime with workflow, every
    evidence source the runtime publishes and every action handler it runs. The key gets events:publish,
    plus workflows:execute when there are handlers, and the result includes workflowRuntime.id (also
    AXONPUSH_WORKFLOW_RUNTIME_ID in env). Next, run workflows_previewDeployment and, once the user
    approves, workflows_applyDeployment with that runtime ID; this binds the sources to this key. Follow
    workflows_describe for the full path. A connected runtime and a ready deployment are configuration
    only. Outcomes come from evaluated cases, which need facts published after the source write commits,
    explicit reconciliation coverage and, for actions, a record lookup after every execution. If sources
    or handlers change, reconnect with rotate: true.

    Secrets: when an agent calls this tool, the key and DSN are never returned. The result has claim, a
    one-time link (valid 30 minutes) the signed-in user opens in the dashboard, and secret env values
    are placeholders. Ask the user to open it and save the key in the app's git-ignored env file as
    AXONPUSH_API_KEY (and SENTRY_DSN if shown). Do not overwrite a working configuration with
    placeholders, skip the claim step, or put credentials in chat or commits. Non-secret settings can be
    merged using the project's existing convention.

    Other purposes (default, web, worker and so on) mint a publish-only key (events:publish) for
    diagnostics. They do not need a workflow. To add business observability, use SDK observe/identify
    calls and reuse existing logging, OpenTelemetry or Sentry setup so exceptions keep their original
    traceback and source locations. Keep the existing capture policy, correlate trace/span IDs where
    available, and test with a controlled local exception. Do not create synthetic production errors.

    Calling again with the same environment and purpose returns the existing key's metadata without the
    secret; it does not mint another key. If the secret was lost, explain that rotate: true revokes the
    old key, and rotate only when the user wants that.

    Args:
        workspace_id (str):
        body (ConnectInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivityConnectResult | ErrorModel
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ConnectInputBody,
) -> Response[ActivityConnectResult | ErrorModel]:
    """Connect a workflow runtime or application: mint its key and return env, OTLP, Sentry and SDK setup

     Give an application the key and settings it needs for this workspace, so nobody copies keys from the
    dashboard.

    Choose the workspace, an explicit environment and a purpose first. The call mints one key bound to
    this workspace's application and that environment, and returns the API URL, an env map, OTLP
    settings, a Sentry DSN when available and SDK snippets.

    Workflow runtime (recommended for workflows): set purpose to workflow_runtime with workflow, every
    evidence source the runtime publishes and every action handler it runs. The key gets events:publish,
    plus workflows:execute when there are handlers, and the result includes workflowRuntime.id (also
    AXONPUSH_WORKFLOW_RUNTIME_ID in env). Next, run workflows_previewDeployment and, once the user
    approves, workflows_applyDeployment with that runtime ID; this binds the sources to this key. Follow
    workflows_describe for the full path. A connected runtime and a ready deployment are configuration
    only. Outcomes come from evaluated cases, which need facts published after the source write commits,
    explicit reconciliation coverage and, for actions, a record lookup after every execution. If sources
    or handlers change, reconnect with rotate: true.

    Secrets: when an agent calls this tool, the key and DSN are never returned. The result has claim, a
    one-time link (valid 30 minutes) the signed-in user opens in the dashboard, and secret env values
    are placeholders. Ask the user to open it and save the key in the app's git-ignored env file as
    AXONPUSH_API_KEY (and SENTRY_DSN if shown). Do not overwrite a working configuration with
    placeholders, skip the claim step, or put credentials in chat or commits. Non-secret settings can be
    merged using the project's existing convention.

    Other purposes (default, web, worker and so on) mint a publish-only key (events:publish) for
    diagnostics. They do not need a workflow. To add business observability, use SDK observe/identify
    calls and reuse existing logging, OpenTelemetry or Sentry setup so exceptions keep their original
    traceback and source locations. Keep the existing capture policy, correlate trace/span IDs where
    available, and test with a controlled local exception. Do not create synthetic production errors.

    Calling again with the same environment and purpose returns the existing key's metadata without the
    secret; it does not mint another key. If the secret was lost, explain that rotate: true revokes the
    old key, and rotate only when the user wants that.

    Args:
        workspace_id (str):
        body (ConnectInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivityConnectResult | ErrorModel]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ConnectInputBody,
) -> ActivityConnectResult | ErrorModel | None:
    """Connect a workflow runtime or application: mint its key and return env, OTLP, Sentry and SDK setup

     Give an application the key and settings it needs for this workspace, so nobody copies keys from the
    dashboard.

    Choose the workspace, an explicit environment and a purpose first. The call mints one key bound to
    this workspace's application and that environment, and returns the API URL, an env map, OTLP
    settings, a Sentry DSN when available and SDK snippets.

    Workflow runtime (recommended for workflows): set purpose to workflow_runtime with workflow, every
    evidence source the runtime publishes and every action handler it runs. The key gets events:publish,
    plus workflows:execute when there are handlers, and the result includes workflowRuntime.id (also
    AXONPUSH_WORKFLOW_RUNTIME_ID in env). Next, run workflows_previewDeployment and, once the user
    approves, workflows_applyDeployment with that runtime ID; this binds the sources to this key. Follow
    workflows_describe for the full path. A connected runtime and a ready deployment are configuration
    only. Outcomes come from evaluated cases, which need facts published after the source write commits,
    explicit reconciliation coverage and, for actions, a record lookup after every execution. If sources
    or handlers change, reconnect with rotate: true.

    Secrets: when an agent calls this tool, the key and DSN are never returned. The result has claim, a
    one-time link (valid 30 minutes) the signed-in user opens in the dashboard, and secret env values
    are placeholders. Ask the user to open it and save the key in the app's git-ignored env file as
    AXONPUSH_API_KEY (and SENTRY_DSN if shown). Do not overwrite a working configuration with
    placeholders, skip the claim step, or put credentials in chat or commits. Non-secret settings can be
    merged using the project's existing convention.

    Other purposes (default, web, worker and so on) mint a publish-only key (events:publish) for
    diagnostics. They do not need a workflow. To add business observability, use SDK observe/identify
    calls and reuse existing logging, OpenTelemetry or Sentry setup so exceptions keep their original
    traceback and source locations. Keep the existing capture policy, correlate trace/span IDs where
    available, and test with a controlled local exception. Do not create synthetic production errors.

    Calling again with the same environment and purpose returns the existing key's metadata without the
    secret; it does not mint another key. If the secret was lost, explain that rotate: true revokes the
    old key, and rotate only when the user wants that.

    Args:
        workspace_id (str):
        body (ConnectInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivityConnectResult | ErrorModel
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            body=body,
        )
    ).parsed
