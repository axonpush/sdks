from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_model import ErrorModel
from ...models.register_source_input_body import RegisterSourceInputBody
from ...models.status_output_body import StatusOutputBody
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    workspace_id: str,
    *,
    body: RegisterSourceInputBody,
    environment: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["environment"] = environment

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/workspaces/{workspace_id}/workflows/sources".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | StatusOutputBody:
    if response.status_code == 200:
        response_200 = StatusOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | StatusOutputBody]:
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
    body: RegisterSourceInputBody,
    environment: str | Unset = UNSET,
) -> Response[ErrorModel | StatusOutputBody]:
    """Bind an evidence source to an explicit publisher identity

    Args:
        workspace_id (str):
        environment (str | Unset):
        body (RegisterSourceInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | StatusOutputBody]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        body=body,
        environment=environment,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RegisterSourceInputBody,
    environment: str | Unset = UNSET,
) -> ErrorModel | StatusOutputBody | None:
    """Bind an evidence source to an explicit publisher identity

    Args:
        workspace_id (str):
        environment (str | Unset):
        body (RegisterSourceInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | StatusOutputBody
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        body=body,
        environment=environment,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RegisterSourceInputBody,
    environment: str | Unset = UNSET,
) -> Response[ErrorModel | StatusOutputBody]:
    """Bind an evidence source to an explicit publisher identity

    Args:
        workspace_id (str):
        environment (str | Unset):
        body (RegisterSourceInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | StatusOutputBody]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        body=body,
        environment=environment,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RegisterSourceInputBody,
    environment: str | Unset = UNSET,
) -> ErrorModel | StatusOutputBody | None:
    """Bind an evidence source to an explicit publisher identity

    Args:
        workspace_id (str):
        environment (str | Unset):
        body (RegisterSourceInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | StatusOutputBody
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            body=body,
            environment=environment,
        )
    ).parsed
