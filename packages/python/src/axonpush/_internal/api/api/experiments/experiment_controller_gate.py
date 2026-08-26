from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.experiment_gate_result_dto import ExperimentGateResultDto
from ...types import UNSET, Response


def _get_kwargs(
    experiment_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/experiments/{experiment_id}/gate".format(
            experiment_id=quote(str(experiment_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExperimentGateResultDto | None:
    if response.status_code == 200:
        response_200 = ExperimentGateResultDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ExperimentGateResultDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    experiment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ExperimentGateResultDto]:
    """
    Args:
        experiment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExperimentGateResultDto]
    """

    kwargs = _get_kwargs(
        experiment_id=experiment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    experiment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ExperimentGateResultDto | None:
    """
    Args:
        experiment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExperimentGateResultDto
    """

    return sync_detailed(
        experiment_id=experiment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    experiment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ExperimentGateResultDto]:
    """
    Args:
        experiment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExperimentGateResultDto]
    """

    kwargs = _get_kwargs(
        experiment_id=experiment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    experiment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ExperimentGateResultDto | None:
    """
    Args:
        experiment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExperimentGateResultDto
    """

    return (
        await asyncio_detailed(
            experiment_id=experiment_id,
            client=client,
        )
    ).parsed
