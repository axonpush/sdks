from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.prompt_comparison_dto import PromptComparisonDto
from ...types import UNSET, Response


def _get_kwargs(
    prompt_id: str,
    *,
    baseline: float,
    candidate: float,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["baseline"] = baseline

    params["candidate"] = candidate

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/prompts/{prompt_id}/compare".format(
            prompt_id=quote(str(prompt_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PromptComparisonDto | None:
    if response.status_code == 200:
        response_200 = PromptComparisonDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PromptComparisonDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    prompt_id: str,
    *,
    client: AuthenticatedClient | Client,
    baseline: float,
    candidate: float,
) -> Response[PromptComparisonDto]:
    """
    Args:
        prompt_id (str):
        baseline (float):
        candidate (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PromptComparisonDto]
    """

    kwargs = _get_kwargs(
        prompt_id=prompt_id,
        baseline=baseline,
        candidate=candidate,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    prompt_id: str,
    *,
    client: AuthenticatedClient | Client,
    baseline: float,
    candidate: float,
) -> PromptComparisonDto | None:
    """
    Args:
        prompt_id (str):
        baseline (float):
        candidate (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PromptComparisonDto
    """

    return sync_detailed(
        prompt_id=prompt_id,
        client=client,
        baseline=baseline,
        candidate=candidate,
    ).parsed


async def asyncio_detailed(
    prompt_id: str,
    *,
    client: AuthenticatedClient | Client,
    baseline: float,
    candidate: float,
) -> Response[PromptComparisonDto]:
    """
    Args:
        prompt_id (str):
        baseline (float):
        candidate (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PromptComparisonDto]
    """

    kwargs = _get_kwargs(
        prompt_id=prompt_id,
        baseline=baseline,
        candidate=candidate,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    prompt_id: str,
    *,
    client: AuthenticatedClient | Client,
    baseline: float,
    candidate: float,
) -> PromptComparisonDto | None:
    """
    Args:
        prompt_id (str):
        baseline (float):
        candidate (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PromptComparisonDto
    """

    return (
        await asyncio_detailed(
            prompt_id=prompt_id,
            client=client,
            baseline=baseline,
            candidate=candidate,
        )
    ).parsed
