from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.diff_input_body_1 import DiffInputBody1
from ...models.diff_output_body_1 import DiffOutputBody1
from ...models.error_model import ErrorModel
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    workspace_id: str,
    *,
    body: DiffInputBody1,
    environment: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["environment"] = environment

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/workspaces/{workspace_id}/workflows/diff".format(
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
) -> DiffOutputBody1 | ErrorModel:
    if response.status_code == 200:
        response_200 = DiffOutputBody1.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DiffOutputBody1 | ErrorModel]:
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
    body: DiffInputBody1,
    environment: str | Unset = UNSET,
) -> Response[DiffOutputBody1 | ErrorModel]:
    """Compare semantic and source identities without changing deployed definitions

    Args:
        workspace_id (str):
        environment (str | Unset):
        body (DiffInputBody1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DiffOutputBody1 | ErrorModel]
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
    body: DiffInputBody1,
    environment: str | Unset = UNSET,
) -> DiffOutputBody1 | ErrorModel | None:
    """Compare semantic and source identities without changing deployed definitions

    Args:
        workspace_id (str):
        environment (str | Unset):
        body (DiffInputBody1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DiffOutputBody1 | ErrorModel
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
    body: DiffInputBody1,
    environment: str | Unset = UNSET,
) -> Response[DiffOutputBody1 | ErrorModel]:
    """Compare semantic and source identities without changing deployed definitions

    Args:
        workspace_id (str):
        environment (str | Unset):
        body (DiffInputBody1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DiffOutputBody1 | ErrorModel]
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
    body: DiffInputBody1,
    environment: str | Unset = UNSET,
) -> DiffOutputBody1 | ErrorModel | None:
    """Compare semantic and source identities without changing deployed definitions

    Args:
        workspace_id (str):
        environment (str | Unset):
        body (DiffInputBody1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DiffOutputBody1 | ErrorModel
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            body=body,
            environment=environment,
        )
    ).parsed
