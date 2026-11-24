from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.workflow_setup_guide import WorkflowSetupGuide
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: str,
    *,
    environment: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["environment"] = environment

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspaces/{workspace_id}/workflows/describe".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | WorkflowSetupGuide:
    if response.status_code == 200:
        response_200 = WorkflowSetupGuide.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | WorkflowSetupGuide]:
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
) -> Response[ErrorModel | WorkflowSetupGuide]:
    """Start here: workflow setup questions, the tool sequence from runtime connection to evaluated case,
    and a booking example; read-only

     Choose the workspace and an explicit environment first. Read this guide before generating hooks,
    connecting a runtime or deploying a workflow. Ask the user only what the repository cannot answer.
    Following it does not change existing observability.

    Args:
        workspace_id (str):
        environment (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | WorkflowSetupGuide]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
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
    environment: str | Unset = UNSET,
) -> ErrorModel | WorkflowSetupGuide | None:
    """Start here: workflow setup questions, the tool sequence from runtime connection to evaluated case,
    and a booking example; read-only

     Choose the workspace and an explicit environment first. Read this guide before generating hooks,
    connecting a runtime or deploying a workflow. Ask the user only what the repository cannot answer.
    Following it does not change existing observability.

    Args:
        workspace_id (str):
        environment (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | WorkflowSetupGuide
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        environment=environment,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
) -> Response[ErrorModel | WorkflowSetupGuide]:
    """Start here: workflow setup questions, the tool sequence from runtime connection to evaluated case,
    and a booking example; read-only

     Choose the workspace and an explicit environment first. Read this guide before generating hooks,
    connecting a runtime or deploying a workflow. Ask the user only what the repository cannot answer.
    Following it does not change existing observability.

    Args:
        workspace_id (str):
        environment (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | WorkflowSetupGuide]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        environment=environment,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
) -> ErrorModel | WorkflowSetupGuide | None:
    """Start here: workflow setup questions, the tool sequence from runtime connection to evaluated case,
    and a booking example; read-only

     Choose the workspace and an explicit environment first. Read this guide before generating hooks,
    connecting a runtime or deploying a workflow. Ask the user only what the repository cannot answer.
    Following it does not change existing observability.

    Args:
        workspace_id (str):
        environment (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | WorkflowSetupGuide
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            environment=environment,
        )
    ).parsed
