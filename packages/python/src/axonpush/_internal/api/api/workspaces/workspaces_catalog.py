from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_catalog import ActivityCatalog
from ...models.error_model import ErrorModel
from ...models.workspaces_catalog_window import WorkspacesCatalogWindow
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: str,
    *,
    environment: str | Unset = UNSET,
    window: WorkspacesCatalogWindow | Unset = WorkspacesCatalogWindow.VALUE_1,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["environment"] = environment

    json_window: str | Unset = UNSET
    if not isinstance(window, Unset):
        json_window = window.value

    params["window"] = json_window

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspaces/{workspace_id}/catalog".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActivityCatalog | ErrorModel:
    if response.status_code == 200:
        response_200 = ActivityCatalog.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ActivityCatalog | ErrorModel]:
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
    window: WorkspacesCatalogWindow | Unset = WorkspacesCatalogWindow.VALUE_1,
) -> Response[ActivityCatalog | ErrorModel]:
    """Events actually received: counts, refs and attribute keys seen (declared and undeclared) and which
    entities consume each event

     Use it to find events no entity consumes yet and attributes your app sends that the dictionary does
    not declare.

    Args:
        workspace_id (str):
        environment (str | Unset): Defaults to every environment the caller may read
        window (WorkspacesCatalogWindow | Unset):  Default: WorkspacesCatalogWindow.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivityCatalog | ErrorModel]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        environment=environment,
        window=window,
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
    window: WorkspacesCatalogWindow | Unset = WorkspacesCatalogWindow.VALUE_1,
) -> ActivityCatalog | ErrorModel | None:
    """Events actually received: counts, refs and attribute keys seen (declared and undeclared) and which
    entities consume each event

     Use it to find events no entity consumes yet and attributes your app sends that the dictionary does
    not declare.

    Args:
        workspace_id (str):
        environment (str | Unset): Defaults to every environment the caller may read
        window (WorkspacesCatalogWindow | Unset):  Default: WorkspacesCatalogWindow.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivityCatalog | ErrorModel
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        environment=environment,
        window=window,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
    window: WorkspacesCatalogWindow | Unset = WorkspacesCatalogWindow.VALUE_1,
) -> Response[ActivityCatalog | ErrorModel]:
    """Events actually received: counts, refs and attribute keys seen (declared and undeclared) and which
    entities consume each event

     Use it to find events no entity consumes yet and attributes your app sends that the dictionary does
    not declare.

    Args:
        workspace_id (str):
        environment (str | Unset): Defaults to every environment the caller may read
        window (WorkspacesCatalogWindow | Unset):  Default: WorkspacesCatalogWindow.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivityCatalog | ErrorModel]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        environment=environment,
        window=window,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
    window: WorkspacesCatalogWindow | Unset = WorkspacesCatalogWindow.VALUE_1,
) -> ActivityCatalog | ErrorModel | None:
    """Events actually received: counts, refs and attribute keys seen (declared and undeclared) and which
    entities consume each event

     Use it to find events no entity consumes yet and attributes your app sends that the dictionary does
    not declare.

    Args:
        workspace_id (str):
        environment (str | Unset): Defaults to every environment the caller may read
        window (WorkspacesCatalogWindow | Unset):  Default: WorkspacesCatalogWindow.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivityCatalog | ErrorModel
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            environment=environment,
            window=window,
        )
    ).parsed
