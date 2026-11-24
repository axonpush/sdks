from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.ingest_outcomes_window import IngestOutcomesWindow
from ...models.list_outcomes_output_body import ListOutcomesOutputBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    window: IngestOutcomesWindow | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["appId"] = app_id

    params["environmentId"] = environment_id

    json_window: str | Unset = UNSET
    if not isinstance(window, Unset):
        json_window = window.value

    params["window"] = json_window

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ingest/outcomes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | ListOutcomesOutputBody:
    if response.status_code == 200:
        response_200 = ListOutcomesOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | ListOutcomesOutputBody]:
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
    window: IngestOutcomesWindow | Unset = UNSET,
) -> Response[ErrorModel | ListOutcomesOutputBody]:
    """Accepted and dropped ingest counts by category, source and reason

    Args:
        app_id (str | Unset):
        environment_id (str | Unset): Environment slug or id
        window (IngestOutcomesWindow | Unset): Look-back window, rounded to whole days (default
            24h)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ListOutcomesOutputBody]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        environment_id=environment_id,
        window=window,
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
    window: IngestOutcomesWindow | Unset = UNSET,
) -> ErrorModel | ListOutcomesOutputBody | None:
    """Accepted and dropped ingest counts by category, source and reason

    Args:
        app_id (str | Unset):
        environment_id (str | Unset): Environment slug or id
        window (IngestOutcomesWindow | Unset): Look-back window, rounded to whole days (default
            24h)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ListOutcomesOutputBody
    """

    return sync_detailed(
        client=client,
        app_id=app_id,
        environment_id=environment_id,
        window=window,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    window: IngestOutcomesWindow | Unset = UNSET,
) -> Response[ErrorModel | ListOutcomesOutputBody]:
    """Accepted and dropped ingest counts by category, source and reason

    Args:
        app_id (str | Unset):
        environment_id (str | Unset): Environment slug or id
        window (IngestOutcomesWindow | Unset): Look-back window, rounded to whole days (default
            24h)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ListOutcomesOutputBody]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        environment_id=environment_id,
        window=window,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    window: IngestOutcomesWindow | Unset = UNSET,
) -> ErrorModel | ListOutcomesOutputBody | None:
    """Accepted and dropped ingest counts by category, source and reason

    Args:
        app_id (str | Unset):
        environment_id (str | Unset): Environment slug or id
        window (IngestOutcomesWindow | Unset): Look-back window, rounded to whole days (default
            24h)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ListOutcomesOutputBody
    """

    return (
        await asyncio_detailed(
            client=client,
            app_id=app_id,
            environment_id=environment_id,
            window=window,
        )
    ).parsed
