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

    Call it after the workspace spec is active (or at least drafted). It mints a key that can only
    publish (events:publish), bound to this workspace's application and one environment, and returns it
    once with the API URL, OTLP settings, a Sentry DSN when available, a ready-to-write env map and SDK
    snippets.

    Write the returned env into the app's local secret file (for example .env.local, or the project's
    existing secret convention), make sure that file is git-ignored, and never commit, print or paste
    the key. Then add the SDK observe and identify calls and send a test event.

    Calling it again for the same environment and purpose does not mint another key: it returns the
    existing key's metadata without the secret. If the secret was lost, call again with rotate: true,
    which revokes the old key and mints a new one.

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

    Call it after the workspace spec is active (or at least drafted). It mints a key that can only
    publish (events:publish), bound to this workspace's application and one environment, and returns it
    once with the API URL, OTLP settings, a Sentry DSN when available, a ready-to-write env map and SDK
    snippets.

    Write the returned env into the app's local secret file (for example .env.local, or the project's
    existing secret convention), make sure that file is git-ignored, and never commit, print or paste
    the key. Then add the SDK observe and identify calls and send a test event.

    Calling it again for the same environment and purpose does not mint another key: it returns the
    existing key's metadata without the secret. If the secret was lost, call again with rotate: true,
    which revokes the old key and mints a new one.

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

    Call it after the workspace spec is active (or at least drafted). It mints a key that can only
    publish (events:publish), bound to this workspace's application and one environment, and returns it
    once with the API URL, OTLP settings, a Sentry DSN when available, a ready-to-write env map and SDK
    snippets.

    Write the returned env into the app's local secret file (for example .env.local, or the project's
    existing secret convention), make sure that file is git-ignored, and never commit, print or paste
    the key. Then add the SDK observe and identify calls and send a test event.

    Calling it again for the same environment and purpose does not mint another key: it returns the
    existing key's metadata without the secret. If the secret was lost, call again with rotate: true,
    which revokes the old key and mints a new one.

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

    Call it after the workspace spec is active (or at least drafted). It mints a key that can only
    publish (events:publish), bound to this workspace's application and one environment, and returns it
    once with the API URL, OTLP settings, a Sentry DSN when available, a ready-to-write env map and SDK
    snippets.

    Write the returned env into the app's local secret file (for example .env.local, or the project's
    existing secret convention), make sure that file is git-ignored, and never commit, print or paste
    the key. Then add the SDK observe and identify calls and send a test event.

    Calling it again for the same environment and purpose does not mint another key: it returns the
    existing key's metadata without the secret. If the secret was lost, call again with rotate: true,
    which revokes the old key and mints a new one.

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
