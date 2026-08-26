from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataset_revision_items_dto import DatasetRevisionItemsDto
from ...types import UNSET, Response


def _get_kwargs(
    dataset_id: str,
    revision: float,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/datasets/{dataset_id}/revisions/{revision}/items".format(
            dataset_id=quote(str(dataset_id), safe=""),
            revision=quote(str(revision), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatasetRevisionItemsDto | None:
    if response.status_code == 200:
        response_200 = DatasetRevisionItemsDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DatasetRevisionItemsDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataset_id: str,
    revision: float,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DatasetRevisionItemsDto]:
    """
    Args:
        dataset_id (str):
        revision (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetRevisionItemsDto]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        revision=revision,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataset_id: str,
    revision: float,
    *,
    client: AuthenticatedClient | Client,
) -> DatasetRevisionItemsDto | None:
    """
    Args:
        dataset_id (str):
        revision (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetRevisionItemsDto
    """

    return sync_detailed(
        dataset_id=dataset_id,
        revision=revision,
        client=client,
    ).parsed


async def asyncio_detailed(
    dataset_id: str,
    revision: float,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DatasetRevisionItemsDto]:
    """
    Args:
        dataset_id (str):
        revision (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetRevisionItemsDto]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        revision=revision,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_id: str,
    revision: float,
    *,
    client: AuthenticatedClient | Client,
) -> DatasetRevisionItemsDto | None:
    """
    Args:
        dataset_id (str):
        revision (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetRevisionItemsDto
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            revision=revision,
            client=client,
        )
    ).parsed
