from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_input_body import CreateInputBody
from ...models.created_key import CreatedKey
from ...models.error_model import ErrorModel
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: CreateInputBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/organization/api-keys",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreatedKey | ErrorModel:
    if response.status_code == 200:
        response_200 = CreatedKey.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreatedKey | ErrorModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateInputBody,
) -> Response[CreatedKey | ErrorModel]:
    """Create a publish or read API key

     Create an API key for the active organisation (organisation admins only).

    Scopes are limited to events:publish, events:read and observe:read. When an agent calls this, the
    key is never returned: the result has a claim link that the signed-in user opens in the dashboard to
    reveal the key once (valid 30 minutes). Ask the user to open it and put the key in the app's git-
    ignored env file as AXONPUSH_API_KEY.

    Args:
        body (CreateInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatedKey | ErrorModel]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateInputBody,
) -> CreatedKey | ErrorModel | None:
    """Create a publish or read API key

     Create an API key for the active organisation (organisation admins only).

    Scopes are limited to events:publish, events:read and observe:read. When an agent calls this, the
    key is never returned: the result has a claim link that the signed-in user opens in the dashboard to
    reveal the key once (valid 30 minutes). Ask the user to open it and put the key in the app's git-
    ignored env file as AXONPUSH_API_KEY.

    Args:
        body (CreateInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatedKey | ErrorModel
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateInputBody,
) -> Response[CreatedKey | ErrorModel]:
    """Create a publish or read API key

     Create an API key for the active organisation (organisation admins only).

    Scopes are limited to events:publish, events:read and observe:read. When an agent calls this, the
    key is never returned: the result has a claim link that the signed-in user opens in the dashboard to
    reveal the key once (valid 30 minutes). Ask the user to open it and put the key in the app's git-
    ignored env file as AXONPUSH_API_KEY.

    Args:
        body (CreateInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatedKey | ErrorModel]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateInputBody,
) -> CreatedKey | ErrorModel | None:
    """Create a publish or read API key

     Create an API key for the active organisation (organisation admins only).

    Scopes are limited to events:publish, events:read and observe:read. When an agent calls this, the
    key is never returned: the result has a claim link that the signed-in user opens in the dashboard to
    reveal the key once (valid 30 minutes). Ask the user to open it and put the key in the app's git-
    ignored env file as AXONPUSH_API_KEY.

    Args:
        body (CreateInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatedKey | ErrorModel
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
