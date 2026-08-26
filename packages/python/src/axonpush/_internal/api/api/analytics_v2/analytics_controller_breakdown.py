from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_breakdown_response_dto import AnalyticsBreakdownResponseDto
from ...models.analytics_controller_breakdown_dimension import AnalyticsControllerBreakdownDimension
from ...models.analytics_controller_breakdown_measure import AnalyticsControllerBreakdownMeasure
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    dimension: AnalyticsControllerBreakdownDimension,
    environment: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    measure: AnalyticsControllerBreakdownMeasure | Unset = UNSET,
    to: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_dimension = dimension.value
    params["dimension"] = json_dimension

    params["environment"] = environment

    params["from"] = from_

    json_measure: str | Unset = UNSET
    if not isinstance(measure, Unset):
        json_measure = measure.value

    params["measure"] = json_measure

    params["to"] = to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/analytics/breakdown",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalyticsBreakdownResponseDto | None:
    if response.status_code == 200:
        response_200 = AnalyticsBreakdownResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AnalyticsBreakdownResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    dimension: AnalyticsControllerBreakdownDimension,
    environment: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    measure: AnalyticsControllerBreakdownMeasure | Unset = UNSET,
    to: str | Unset = UNSET,
) -> Response[AnalyticsBreakdownResponseDto]:
    """
    Args:
        dimension (AnalyticsControllerBreakdownDimension):
        environment (str | Unset):
        from_ (str | Unset):
        measure (AnalyticsControllerBreakdownMeasure | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsBreakdownResponseDto]
    """

    kwargs = _get_kwargs(
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
    dimension: AnalyticsControllerBreakdownDimension,
    environment: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    measure: AnalyticsControllerBreakdownMeasure | Unset = UNSET,
    to: str | Unset = UNSET,
) -> AnalyticsBreakdownResponseDto | None:
    """
    Args:
        dimension (AnalyticsControllerBreakdownDimension):
        environment (str | Unset):
        from_ (str | Unset):
        measure (AnalyticsControllerBreakdownMeasure | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsBreakdownResponseDto
    """

    return sync_detailed(
        client=client,
        dimension=dimension,
        environment=environment,
        from_=from_,
        measure=measure,
        to=to,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    dimension: AnalyticsControllerBreakdownDimension,
    environment: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    measure: AnalyticsControllerBreakdownMeasure | Unset = UNSET,
    to: str | Unset = UNSET,
) -> Response[AnalyticsBreakdownResponseDto]:
    """
    Args:
        dimension (AnalyticsControllerBreakdownDimension):
        environment (str | Unset):
        from_ (str | Unset):
        measure (AnalyticsControllerBreakdownMeasure | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsBreakdownResponseDto]
    """

    kwargs = _get_kwargs(
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
    dimension: AnalyticsControllerBreakdownDimension,
    environment: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    measure: AnalyticsControllerBreakdownMeasure | Unset = UNSET,
    to: str | Unset = UNSET,
) -> AnalyticsBreakdownResponseDto | None:
    """
    Args:
        dimension (AnalyticsControllerBreakdownDimension):
        environment (str | Unset):
        from_ (str | Unset):
        measure (AnalyticsControllerBreakdownMeasure | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsBreakdownResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            dimension=dimension,
            environment=environment,
            from_=from_,
            measure=measure,
            to=to,
        )
    ).parsed
