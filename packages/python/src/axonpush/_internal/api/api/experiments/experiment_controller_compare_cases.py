from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.experiment_case_comparison_dto import ExperimentCaseComparisonDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    experiment_id: str,
    *,
    baseline_experiment_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["baselineExperimentId"] = baseline_experiment_id

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/experiments/{experiment_id}/compare/cases".format(
            experiment_id=quote(str(experiment_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExperimentCaseComparisonDto | None:
    if response.status_code == 200:
        response_200 = ExperimentCaseComparisonDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ExperimentCaseComparisonDto]:
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
    baseline_experiment_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[ExperimentCaseComparisonDto]:
    """
    Args:
        experiment_id (str):
        baseline_experiment_id (str | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExperimentCaseComparisonDto]
    """

    kwargs = _get_kwargs(
        experiment_id=experiment_id,
        baseline_experiment_id=baseline_experiment_id,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    experiment_id: str,
    *,
    client: AuthenticatedClient | Client,
    baseline_experiment_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> ExperimentCaseComparisonDto | None:
    """
    Args:
        experiment_id (str):
        baseline_experiment_id (str | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExperimentCaseComparisonDto
    """

    return sync_detailed(
        experiment_id=experiment_id,
        client=client,
        baseline_experiment_id=baseline_experiment_id,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    experiment_id: str,
    *,
    client: AuthenticatedClient | Client,
    baseline_experiment_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[ExperimentCaseComparisonDto]:
    """
    Args:
        experiment_id (str):
        baseline_experiment_id (str | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExperimentCaseComparisonDto]
    """

    kwargs = _get_kwargs(
        experiment_id=experiment_id,
        baseline_experiment_id=baseline_experiment_id,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    experiment_id: str,
    *,
    client: AuthenticatedClient | Client,
    baseline_experiment_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> ExperimentCaseComparisonDto | None:
    """
    Args:
        experiment_id (str):
        baseline_experiment_id (str | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExperimentCaseComparisonDto
    """

    return (
        await asyncio_detailed(
            experiment_id=experiment_id,
            client=client,
            baseline_experiment_id=baseline_experiment_id,
            cursor=cursor,
        )
    ).parsed
