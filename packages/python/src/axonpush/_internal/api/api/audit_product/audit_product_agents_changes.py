from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.changes_output_body import ChangesOutputBody
from ...models.error_model import ErrorModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    before: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["before"] = before

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/audit/agents/{id}/changes".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ChangesOutputBody | ErrorModel:
    if response.status_code == 200:
        response_200 = ChangesOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ChangesOutputBody | ErrorModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    before: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ChangesOutputBody | ErrorModel]:
    """Read agent revision history

    Args:
        id (str):
        before (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangesOutputBody | ErrorModel]
    """

    kwargs = _get_kwargs(
        id=id,
        before=before,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    before: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ChangesOutputBody | ErrorModel | None:
    """Read agent revision history

    Args:
        id (str):
        before (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangesOutputBody | ErrorModel
    """

    return sync_detailed(
        id=id,
        client=client,
        before=before,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    before: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ChangesOutputBody | ErrorModel]:
    """Read agent revision history

    Args:
        id (str):
        before (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangesOutputBody | ErrorModel]
    """

    kwargs = _get_kwargs(
        id=id,
        before=before,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    before: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ChangesOutputBody | ErrorModel | None:
    """Read agent revision history

    Args:
        id (str):
        before (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangesOutputBody | ErrorModel
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            before=before,
            limit=limit,
        )
    ).parsed
