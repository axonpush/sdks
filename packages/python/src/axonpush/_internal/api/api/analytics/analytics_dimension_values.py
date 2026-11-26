from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dimension_values_output_body import DimensionValuesOutputBody
from ...models.error_model import ErrorModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    key: str,
    environment: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["key"] = key

    params["environment"] = environment

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/dimensions/values",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DimensionValuesOutputBody | ErrorModel:
    if response.status_code == 200:
        response_200 = DimensionValuesOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DimensionValuesOutputBody | ErrorModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    key: str,
    environment: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[DimensionValuesOutputBody | ErrorModel]:
    """List the observed values of one custom dimension

     The distinct values seen for a dimension key (from /analytics/dimensions). Use a value with
    filterTagKey+filterTagValue to scope any analytics read to it.

    Args:
        key (str): Dimension (attribute) key to list values for
        environment (str | Unset): Filter to one environment id or slug; empty = all
        limit (int | Unset): Max values (default 50, max 500)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DimensionValuesOutputBody | ErrorModel]
    """

    kwargs = _get_kwargs(
        key=key,
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
    key: str,
    environment: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> DimensionValuesOutputBody | ErrorModel | None:
    """List the observed values of one custom dimension

     The distinct values seen for a dimension key (from /analytics/dimensions). Use a value with
    filterTagKey+filterTagValue to scope any analytics read to it.

    Args:
        key (str): Dimension (attribute) key to list values for
        environment (str | Unset): Filter to one environment id or slug; empty = all
        limit (int | Unset): Max values (default 50, max 500)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DimensionValuesOutputBody | ErrorModel
    """

    return sync_detailed(
        client=client,
        key=key,
        environment=environment,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    key: str,
    environment: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[DimensionValuesOutputBody | ErrorModel]:
    """List the observed values of one custom dimension

     The distinct values seen for a dimension key (from /analytics/dimensions). Use a value with
    filterTagKey+filterTagValue to scope any analytics read to it.

    Args:
        key (str): Dimension (attribute) key to list values for
        environment (str | Unset): Filter to one environment id or slug; empty = all
        limit (int | Unset): Max values (default 50, max 500)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DimensionValuesOutputBody | ErrorModel]
    """

    kwargs = _get_kwargs(
        key=key,
        environment=environment,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    key: str,
    environment: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> DimensionValuesOutputBody | ErrorModel | None:
    """List the observed values of one custom dimension

     The distinct values seen for a dimension key (from /analytics/dimensions). Use a value with
    filterTagKey+filterTagValue to scope any analytics read to it.

    Args:
        key (str): Dimension (attribute) key to list values for
        environment (str | Unset): Filter to one environment id or slug; empty = all
        limit (int | Unset): Max values (default 50, max 500)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DimensionValuesOutputBody | ErrorModel
    """

    return (
        await asyncio_detailed(
            client=client,
            key=key,
            environment=environment,
            limit=limit,
        )
    ).parsed
