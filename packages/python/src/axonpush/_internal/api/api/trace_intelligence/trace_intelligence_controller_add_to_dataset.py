from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_trace_cluster_to_dataset_dto import AddTraceClusterToDatasetDto
from ...models.trace_cluster_dataset_action_response_dto import TraceClusterDatasetActionResponseDto
from ...types import UNSET, Response


def _get_kwargs(
    cluster_id: str,
    *,
    body: AddTraceClusterToDatasetDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/trace-intelligence/clusters/{cluster_id}/actions/add-to-dataset".format(
            cluster_id=quote(str(cluster_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TraceClusterDatasetActionResponseDto | None:
    if response.status_code == 201:
        response_201 = TraceClusterDatasetActionResponseDto.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TraceClusterDatasetActionResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AddTraceClusterToDatasetDto,
) -> Response[TraceClusterDatasetActionResponseDto]:
    """
    Args:
        cluster_id (str):
        body (AddTraceClusterToDatasetDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TraceClusterDatasetActionResponseDto]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AddTraceClusterToDatasetDto,
) -> TraceClusterDatasetActionResponseDto | None:
    """
    Args:
        cluster_id (str):
        body (AddTraceClusterToDatasetDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TraceClusterDatasetActionResponseDto
    """

    return sync_detailed(
        cluster_id=cluster_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AddTraceClusterToDatasetDto,
) -> Response[TraceClusterDatasetActionResponseDto]:
    """
    Args:
        cluster_id (str):
        body (AddTraceClusterToDatasetDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TraceClusterDatasetActionResponseDto]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AddTraceClusterToDatasetDto,
) -> TraceClusterDatasetActionResponseDto | None:
    """
    Args:
        cluster_id (str):
        body (AddTraceClusterToDatasetDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TraceClusterDatasetActionResponseDto
    """

    return (
        await asyncio_detailed(
            cluster_id=cluster_id,
            client=client,
            body=body,
        )
    ).parsed
