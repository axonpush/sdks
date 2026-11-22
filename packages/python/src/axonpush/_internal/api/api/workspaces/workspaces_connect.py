from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_connect_result import ActivityConnectResult
from ...models.connect_input_body import ConnectInputBody
from ...models.error_model import ErrorModel
from ...types import UNSET, Response


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
    """Mint the application's publish key and return its env, OTLP, Sentry and SDK setup

     Get everything the application needs to send data to this workspace, so nobody copies keys from the
    dashboard.

    Choose the intended workspace, explicit environment and purpose first. An activity draft is not
    required for workflow verification. It mints a key that can only publish (events:publish), bound to
    this workspace's application and one environment, with the API URL, OTLP settings, a Sentry DSN when
    available, an env map and SDK snippets.

    When an agent calls it, the key and DSN are never returned: the result carries claim, a one-time
    link (valid 30 minutes) the signed-in user opens in the dashboard to reveal them, and the secret env
    values are placeholders. Ask the user to open the link and put the key into the app's git-ignored
    env file as AXONPUSH_API_KEY (and SENTRY_DSN if shown).

    For delegated calls, let the signed-in user open the claim link and save secrets in the app's git-
    ignored local environment file. Do not overwrite a working configuration with placeholder secret
    values, bypass the claim step, or expose credentials in chat or commits. Nonsecret settings can be
    merged using the project's existing convention.

    For workflow verification, follow workflows_describe, bind the evidence source to publisher
    key:<publishKey.id> from this connection, implement reliable post-commit fact publication and
    inspect an evaluated case. This connection is not proof of evidence coverage or verified completion.

    For optional business observability, add SDK observe/identify calls and reuse existing logging,
    OpenTelemetry or Sentry integrations so exceptions retain their original traceback and source
    locations. Reuse the existing provider/capture policy, correlate trace/span ids where available, and
    verify a controlled exception locally. Do not create synthetic production errors.

    Calling it again for the same environment and purpose does not mint another key: it returns the
    existing key's metadata without the secret. If the secret was lost, explain that rotate: true
    revokes the old key, and rotate only when the user intends that replacement.

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
    """Mint the application's publish key and return its env, OTLP, Sentry and SDK setup

     Get everything the application needs to send data to this workspace, so nobody copies keys from the
    dashboard.

    Choose the intended workspace, explicit environment and purpose first. An activity draft is not
    required for workflow verification. It mints a key that can only publish (events:publish), bound to
    this workspace's application and one environment, with the API URL, OTLP settings, a Sentry DSN when
    available, an env map and SDK snippets.

    When an agent calls it, the key and DSN are never returned: the result carries claim, a one-time
    link (valid 30 minutes) the signed-in user opens in the dashboard to reveal them, and the secret env
    values are placeholders. Ask the user to open the link and put the key into the app's git-ignored
    env file as AXONPUSH_API_KEY (and SENTRY_DSN if shown).

    For delegated calls, let the signed-in user open the claim link and save secrets in the app's git-
    ignored local environment file. Do not overwrite a working configuration with placeholder secret
    values, bypass the claim step, or expose credentials in chat or commits. Nonsecret settings can be
    merged using the project's existing convention.

    For workflow verification, follow workflows_describe, bind the evidence source to publisher
    key:<publishKey.id> from this connection, implement reliable post-commit fact publication and
    inspect an evaluated case. This connection is not proof of evidence coverage or verified completion.

    For optional business observability, add SDK observe/identify calls and reuse existing logging,
    OpenTelemetry or Sentry integrations so exceptions retain their original traceback and source
    locations. Reuse the existing provider/capture policy, correlate trace/span ids where available, and
    verify a controlled exception locally. Do not create synthetic production errors.

    Calling it again for the same environment and purpose does not mint another key: it returns the
    existing key's metadata without the secret. If the secret was lost, explain that rotate: true
    revokes the old key, and rotate only when the user intends that replacement.

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
    """Mint the application's publish key and return its env, OTLP, Sentry and SDK setup

     Get everything the application needs to send data to this workspace, so nobody copies keys from the
    dashboard.

    Choose the intended workspace, explicit environment and purpose first. An activity draft is not
    required for workflow verification. It mints a key that can only publish (events:publish), bound to
    this workspace's application and one environment, with the API URL, OTLP settings, a Sentry DSN when
    available, an env map and SDK snippets.

    When an agent calls it, the key and DSN are never returned: the result carries claim, a one-time
    link (valid 30 minutes) the signed-in user opens in the dashboard to reveal them, and the secret env
    values are placeholders. Ask the user to open the link and put the key into the app's git-ignored
    env file as AXONPUSH_API_KEY (and SENTRY_DSN if shown).

    For delegated calls, let the signed-in user open the claim link and save secrets in the app's git-
    ignored local environment file. Do not overwrite a working configuration with placeholder secret
    values, bypass the claim step, or expose credentials in chat or commits. Nonsecret settings can be
    merged using the project's existing convention.

    For workflow verification, follow workflows_describe, bind the evidence source to publisher
    key:<publishKey.id> from this connection, implement reliable post-commit fact publication and
    inspect an evaluated case. This connection is not proof of evidence coverage or verified completion.

    For optional business observability, add SDK observe/identify calls and reuse existing logging,
    OpenTelemetry or Sentry integrations so exceptions retain their original traceback and source
    locations. Reuse the existing provider/capture policy, correlate trace/span ids where available, and
    verify a controlled exception locally. Do not create synthetic production errors.

    Calling it again for the same environment and purpose does not mint another key: it returns the
    existing key's metadata without the secret. If the secret was lost, explain that rotate: true
    revokes the old key, and rotate only when the user intends that replacement.

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
    """Mint the application's publish key and return its env, OTLP, Sentry and SDK setup

     Get everything the application needs to send data to this workspace, so nobody copies keys from the
    dashboard.

    Choose the intended workspace, explicit environment and purpose first. An activity draft is not
    required for workflow verification. It mints a key that can only publish (events:publish), bound to
    this workspace's application and one environment, with the API URL, OTLP settings, a Sentry DSN when
    available, an env map and SDK snippets.

    When an agent calls it, the key and DSN are never returned: the result carries claim, a one-time
    link (valid 30 minutes) the signed-in user opens in the dashboard to reveal them, and the secret env
    values are placeholders. Ask the user to open the link and put the key into the app's git-ignored
    env file as AXONPUSH_API_KEY (and SENTRY_DSN if shown).

    For delegated calls, let the signed-in user open the claim link and save secrets in the app's git-
    ignored local environment file. Do not overwrite a working configuration with placeholder secret
    values, bypass the claim step, or expose credentials in chat or commits. Nonsecret settings can be
    merged using the project's existing convention.

    For workflow verification, follow workflows_describe, bind the evidence source to publisher
    key:<publishKey.id> from this connection, implement reliable post-commit fact publication and
    inspect an evaluated case. This connection is not proof of evidence coverage or verified completion.

    For optional business observability, add SDK observe/identify calls and reuse existing logging,
    OpenTelemetry or Sentry integrations so exceptions retain their original traceback and source
    locations. Reuse the existing provider/capture policy, correlate trace/span ids where available, and
    verify a controlled exception locally. Do not create synthetic production errors.

    Calling it again for the same environment and purpose does not mint another key: it returns the
    existing key's metadata without the secret. If the secret was lost, explain that rotate: true
    revokes the old key, and rotate only when the user intends that replacement.

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
