from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.obligations_output_body import ObligationsOutputBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    agent_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["agentId"] = agent_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/audit/obligations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | ObligationsOutputBody:
    if response.status_code == 200:
        response_200 = ObligationsOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | ObligationsOutputBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    agent_id: str | Unset = UNSET,
) -> Response[ErrorModel | ObligationsOutputBody]:
    """Evaluate recorded evidence against the versioned catalogue

    Args:
        agent_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ObligationsOutputBody]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    agent_id: str | Unset = UNSET,
) -> ErrorModel | ObligationsOutputBody | None:
    """Evaluate recorded evidence against the versioned catalogue

    Args:
        agent_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ObligationsOutputBody
    """

    return sync_detailed(
        client=client,
        agent_id=agent_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    agent_id: str | Unset = UNSET,
) -> Response[ErrorModel | ObligationsOutputBody]:
    """Evaluate recorded evidence against the versioned catalogue

    Args:
        agent_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ObligationsOutputBody]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    agent_id: str | Unset = UNSET,
) -> ErrorModel | ObligationsOutputBody | None:
    """Evaluate recorded evidence against the versioned catalogue

    Args:
        agent_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ObligationsOutputBody
    """

    return (
        await asyncio_detailed(
            client=client,
            agent_id=agent_id,
        )
    ).parsed
