from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_workspace_spec import ActivityWorkspaceSpec
from ...models.error_model import ErrorModel
from ...models.validate_output_body import ValidateOutputBody
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: ActivityWorkspaceSpec,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/workspaces/validate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | ValidateOutputBody:
    if response.status_code == 200:
        response_200 = ValidateOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | ValidateOutputBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ActivityWorkspaceSpec,
) -> Response[ErrorModel | ValidateOutputBody]:
    """Validate a workspace spec without saving it; returns every issue

    Args:
        body (ActivityWorkspaceSpec):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ValidateOutputBody]
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
    body: ActivityWorkspaceSpec,
) -> ErrorModel | ValidateOutputBody | None:
    """Validate a workspace spec without saving it; returns every issue

    Args:
        body (ActivityWorkspaceSpec):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ValidateOutputBody
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ActivityWorkspaceSpec,
) -> Response[ErrorModel | ValidateOutputBody]:
    """Validate a workspace spec without saving it; returns every issue

    Args:
        body (ActivityWorkspaceSpec):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ValidateOutputBody]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ActivityWorkspaceSpec,
) -> ErrorModel | ValidateOutputBody | None:
    """Validate a workspace spec without saving it; returns every issue

    Args:
        body (ActivityWorkspaceSpec):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ValidateOutputBody
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
