from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_model import ErrorModel
from ...models.list_metric_names_output_body import ListMetricNamesOutputBody
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["appId"] = app_id

    params["environmentId"] = environment_id

    params["since"] = since

    params["until"] = until

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/metrics/names",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | ListMetricNamesOutputBody:
    if response.status_code == 200:
        response_200 = ListMetricNamesOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | ListMetricNamesOutputBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
) -> Response[ErrorModel | ListMetricNamesOutputBody]:
    """List trace metric names with type, unit, last seen and sample count

    Args:
        app_id (str | Unset):
        environment_id (str | Unset): Environment slug or id
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ListMetricNamesOutputBody]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        environment_id=environment_id,
        since=since,
        until=until,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
) -> ErrorModel | ListMetricNamesOutputBody | None:
    """List trace metric names with type, unit, last seen and sample count

    Args:
        app_id (str | Unset):
        environment_id (str | Unset): Environment slug or id
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ListMetricNamesOutputBody
    """

    return sync_detailed(
        client=client,
        app_id=app_id,
        environment_id=environment_id,
        since=since,
        until=until,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
) -> Response[ErrorModel | ListMetricNamesOutputBody]:
    """List trace metric names with type, unit, last seen and sample count

    Args:
        app_id (str | Unset):
        environment_id (str | Unset): Environment slug or id
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ListMetricNamesOutputBody]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        environment_id=environment_id,
        since=since,
        until=until,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
) -> ErrorModel | ListMetricNamesOutputBody | None:
    """List trace metric names with type, unit, last seen and sample count

    Args:
        app_id (str | Unset):
        environment_id (str | Unset): Environment slug or id
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        until (str | Unset): Window end (RFC3339); defaults to now

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ListMetricNamesOutputBody
    """

    return (
        await asyncio_detailed(
            client=client,
            app_id=app_id,
            environment_id=environment_id,
            since=since,
            until=until,
        )
    ).parsed
