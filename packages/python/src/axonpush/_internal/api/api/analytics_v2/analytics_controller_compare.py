from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_compare_response_dto import AnalyticsCompareResponseDto
from ...models.analytics_controller_compare_dimension import AnalyticsControllerCompareDimension
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    baseline: str,
    candidate: str,
    dimension: AnalyticsControllerCompareDimension,
    environment: str | Unset = UNSET,
    from_: str,
    measure: str,
    to: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["baseline"] = baseline

    params["candidate"] = candidate

    json_dimension = dimension.value
    params["dimension"] = json_dimension

    params["environment"] = environment

    params["from"] = from_

    params["measure"] = measure

    params["to"] = to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/analytics/compare",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalyticsCompareResponseDto | None:
    if response.status_code == 200:
        response_200 = AnalyticsCompareResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AnalyticsCompareResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    baseline: str,
    candidate: str,
    dimension: AnalyticsControllerCompareDimension,
    environment: str | Unset = UNSET,
    from_: str,
    measure: str,
    to: str,
) -> Response[AnalyticsCompareResponseDto]:
    """
    Args:
        baseline (str):
        candidate (str):
        dimension (AnalyticsControllerCompareDimension):
        environment (str | Unset):
        from_ (str):
        measure (str):
        to (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsCompareResponseDto]
    """

    kwargs = _get_kwargs(
        baseline=baseline,
        candidate=candidate,
        dimension=dimension,
        environment=environment,
        from_=from_,
        measure=measure,
        to=to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    baseline: str,
    candidate: str,
    dimension: AnalyticsControllerCompareDimension,
    environment: str | Unset = UNSET,
    from_: str,
    measure: str,
    to: str,
) -> AnalyticsCompareResponseDto | None:
    """
    Args:
        baseline (str):
        candidate (str):
        dimension (AnalyticsControllerCompareDimension):
        environment (str | Unset):
        from_ (str):
        measure (str):
        to (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsCompareResponseDto
    """

    return sync_detailed(
        client=client,
        baseline=baseline,
        candidate=candidate,
        dimension=dimension,
        environment=environment,
        from_=from_,
        measure=measure,
        to=to,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    baseline: str,
    candidate: str,
    dimension: AnalyticsControllerCompareDimension,
    environment: str | Unset = UNSET,
    from_: str,
    measure: str,
    to: str,
) -> Response[AnalyticsCompareResponseDto]:
    """
    Args:
        baseline (str):
        candidate (str):
        dimension (AnalyticsControllerCompareDimension):
        environment (str | Unset):
        from_ (str):
        measure (str):
        to (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsCompareResponseDto]
    """

    kwargs = _get_kwargs(
        baseline=baseline,
        candidate=candidate,
        dimension=dimension,
        environment=environment,
        from_=from_,
        measure=measure,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    baseline: str,
    candidate: str,
    dimension: AnalyticsControllerCompareDimension,
    environment: str | Unset = UNSET,
    from_: str,
    measure: str,
    to: str,
) -> AnalyticsCompareResponseDto | None:
    """
    Args:
        baseline (str):
        candidate (str):
        dimension (AnalyticsControllerCompareDimension):
        environment (str | Unset):
        from_ (str):
        measure (str):
        to (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsCompareResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            baseline=baseline,
            candidate=candidate,
            dimension=dimension,
            environment=environment,
            from_=from_,
            measure=measure,
            to=to,
        )
    ).parsed
