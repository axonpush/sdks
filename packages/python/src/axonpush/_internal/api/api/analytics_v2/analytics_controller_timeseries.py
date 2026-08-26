from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_controller_timeseries_interval import AnalyticsControllerTimeseriesInterval
from ...models.analytics_controller_timeseries_measure import AnalyticsControllerTimeseriesMeasure
from ...models.analytics_timeseries_response_dto import AnalyticsTimeseriesResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    environment: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    interval: AnalyticsControllerTimeseriesInterval | Unset = UNSET,
    measure: AnalyticsControllerTimeseriesMeasure | Unset = UNSET,
    to: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["environment"] = environment

    params["from"] = from_

    json_interval: str | Unset = UNSET
    if not isinstance(interval, Unset):
        json_interval = interval.value

    params["interval"] = json_interval

    json_measure: str | Unset = UNSET
    if not isinstance(measure, Unset):
        json_measure = measure.value

    params["measure"] = json_measure

    params["to"] = to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/analytics/timeseries",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalyticsTimeseriesResponseDto | None:
    if response.status_code == 200:
        response_200 = AnalyticsTimeseriesResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AnalyticsTimeseriesResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    interval: AnalyticsControllerTimeseriesInterval | Unset = UNSET,
    measure: AnalyticsControllerTimeseriesMeasure | Unset = UNSET,
    to: str | Unset = UNSET,
) -> Response[AnalyticsTimeseriesResponseDto]:
    """
    Args:
        environment (str | Unset):
        from_ (str | Unset):
        interval (AnalyticsControllerTimeseriesInterval | Unset):
        measure (AnalyticsControllerTimeseriesMeasure | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsTimeseriesResponseDto]
    """

    kwargs = _get_kwargs(
        environment=environment,
        from_=from_,
        interval=interval,
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
    environment: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    interval: AnalyticsControllerTimeseriesInterval | Unset = UNSET,
    measure: AnalyticsControllerTimeseriesMeasure | Unset = UNSET,
    to: str | Unset = UNSET,
) -> AnalyticsTimeseriesResponseDto | None:
    """
    Args:
        environment (str | Unset):
        from_ (str | Unset):
        interval (AnalyticsControllerTimeseriesInterval | Unset):
        measure (AnalyticsControllerTimeseriesMeasure | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsTimeseriesResponseDto
    """

    return sync_detailed(
        client=client,
        environment=environment,
        from_=from_,
        interval=interval,
        measure=measure,
        to=to,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    interval: AnalyticsControllerTimeseriesInterval | Unset = UNSET,
    measure: AnalyticsControllerTimeseriesMeasure | Unset = UNSET,
    to: str | Unset = UNSET,
) -> Response[AnalyticsTimeseriesResponseDto]:
    """
    Args:
        environment (str | Unset):
        from_ (str | Unset):
        interval (AnalyticsControllerTimeseriesInterval | Unset):
        measure (AnalyticsControllerTimeseriesMeasure | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsTimeseriesResponseDto]
    """

    kwargs = _get_kwargs(
        environment=environment,
        from_=from_,
        interval=interval,
        measure=measure,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    interval: AnalyticsControllerTimeseriesInterval | Unset = UNSET,
    measure: AnalyticsControllerTimeseriesMeasure | Unset = UNSET,
    to: str | Unset = UNSET,
) -> AnalyticsTimeseriesResponseDto | None:
    """
    Args:
        environment (str | Unset):
        from_ (str | Unset):
        interval (AnalyticsControllerTimeseriesInterval | Unset):
        measure (AnalyticsControllerTimeseriesMeasure | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsTimeseriesResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            environment=environment,
            from_=from_,
            interval=interval,
            measure=measure,
            to=to,
        )
    ).parsed
