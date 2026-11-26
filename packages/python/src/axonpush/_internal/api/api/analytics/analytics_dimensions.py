from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dimensions_output_body import DimensionsOutputBody
from ...models.error_model import ErrorModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    environment: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["environment"] = environment

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/dimensions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DimensionsOutputBody | ErrorModel:
    if response.status_code == 200:
        response_200 = DimensionsOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DimensionsOutputBody | ErrorModel]:
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
    limit: int | Unset = UNSET,
) -> Response[DimensionsOutputBody | ErrorModel]:
    """Discover the custom dimensions (span-attribute keys) this org emits

     Start here for custom-dimension analytics: this lists the business attribute keys your app has
    stamped on its telemetry (e.g. participant_role, tenant, plan). Feed a key into
    /analytics/breakdown?dimension=tag&tagKey=<key> to rank it, then into filterTagKey+filterTagValue on
    /analytics/timeseries and /analytics/latency to trend and get percentiles for one value.

    Args:
        environment (str | Unset): Filter to one environment id or slug; empty = all
        limit (int | Unset): Max dimensions (default 50, max 500)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DimensionsOutputBody | ErrorModel]
    """

    kwargs = _get_kwargs(
        environment=environment,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> DimensionsOutputBody | ErrorModel | None:
    """Discover the custom dimensions (span-attribute keys) this org emits

     Start here for custom-dimension analytics: this lists the business attribute keys your app has
    stamped on its telemetry (e.g. participant_role, tenant, plan). Feed a key into
    /analytics/breakdown?dimension=tag&tagKey=<key> to rank it, then into filterTagKey+filterTagValue on
    /analytics/timeseries and /analytics/latency to trend and get percentiles for one value.

    Args:
        environment (str | Unset): Filter to one environment id or slug; empty = all
        limit (int | Unset): Max dimensions (default 50, max 500)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DimensionsOutputBody | ErrorModel
    """

    return sync_detailed(
        client=client,
        environment=environment,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[DimensionsOutputBody | ErrorModel]:
    """Discover the custom dimensions (span-attribute keys) this org emits

     Start here for custom-dimension analytics: this lists the business attribute keys your app has
    stamped on its telemetry (e.g. participant_role, tenant, plan). Feed a key into
    /analytics/breakdown?dimension=tag&tagKey=<key> to rank it, then into filterTagKey+filterTagValue on
    /analytics/timeseries and /analytics/latency to trend and get percentiles for one value.

    Args:
        environment (str | Unset): Filter to one environment id or slug; empty = all
        limit (int | Unset): Max dimensions (default 50, max 500)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DimensionsOutputBody | ErrorModel]
    """

    kwargs = _get_kwargs(
        environment=environment,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> DimensionsOutputBody | ErrorModel | None:
    """Discover the custom dimensions (span-attribute keys) this org emits

     Start here for custom-dimension analytics: this lists the business attribute keys your app has
    stamped on its telemetry (e.g. participant_role, tenant, plan). Feed a key into
    /analytics/breakdown?dimension=tag&tagKey=<key> to rank it, then into filterTagKey+filterTagValue on
    /analytics/timeseries and /analytics/latency to trend and get percentiles for one value.

    Args:
        environment (str | Unset): Filter to one environment id or slug; empty = all
        limit (int | Unset): Max dimensions (default 50, max 500)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DimensionsOutputBody | ErrorModel
    """

    return (
        await asyncio_detailed(
            client=client,
            environment=environment,
            limit=limit,
        )
    ).parsed
