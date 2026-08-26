from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataset_controller_export_revision_format import (
    DatasetControllerExportRevisionFormat,
)
from ...models.dataset_export_dto import DatasetExportDto
from ...types import UNSET, Response


def _get_kwargs(
    dataset_id: str,
    revision: float,
    format_: DatasetControllerExportRevisionFormat,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/datasets/{dataset_id}/revisions/{revision}/export/{format_}".format(
            dataset_id=quote(str(dataset_id), safe=""),
            revision=quote(str(revision), safe=""),
            format_=quote(str(format_), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatasetExportDto | None:
    if response.status_code == 200:
        response_200 = DatasetExportDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DatasetExportDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataset_id: str,
    revision: float,
    format_: DatasetControllerExportRevisionFormat,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DatasetExportDto]:
    """
    Args:
        dataset_id (str):
        revision (float):
        format_ (DatasetControllerExportRevisionFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetExportDto]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        revision=revision,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataset_id: str,
    revision: float,
    format_: DatasetControllerExportRevisionFormat,
    *,
    client: AuthenticatedClient | Client,
) -> DatasetExportDto | None:
    """
    Args:
        dataset_id (str):
        revision (float):
        format_ (DatasetControllerExportRevisionFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetExportDto
    """

    return sync_detailed(
        dataset_id=dataset_id,
        revision=revision,
        format_=format_,
        client=client,
    ).parsed


async def asyncio_detailed(
    dataset_id: str,
    revision: float,
    format_: DatasetControllerExportRevisionFormat,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DatasetExportDto]:
    """
    Args:
        dataset_id (str):
        revision (float):
        format_ (DatasetControllerExportRevisionFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetExportDto]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        revision=revision,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_id: str,
    revision: float,
    format_: DatasetControllerExportRevisionFormat,
    *,
    client: AuthenticatedClient | Client,
) -> DatasetExportDto | None:
    """
    Args:
        dataset_id (str):
        revision (float):
        format_ (DatasetControllerExportRevisionFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetExportDto
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            revision=revision,
            format_=format_,
            client=client,
        )
    ).parsed
