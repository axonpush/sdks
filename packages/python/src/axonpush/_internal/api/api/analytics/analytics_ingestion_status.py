from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.ingestion_status_output_body import IngestionStatusOutputBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    environment: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["environment"] = environment

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/ingestion-status",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | IngestionStatusOutputBody:
    if response.status_code == 200:
        response_200 = IngestionStatusOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | IngestionStatusOutputBody]:
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
) -> Response[ErrorModel | IngestionStatusOutputBody]:
    """Whether this workspace has ever ingested an event (onboarding signal)

     A cheap connection signal for onboarding, distinct from recent activity: everIngested is true once
    any event has ever landed for the org (optionally scoped to one environment). A minted API key is
    NOT proof of instrumentation; observed ingestion is.

    Args:
        environment (str | Unset): Environment slug or id to scope the check to (omit for org-
            wide)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | IngestionStatusOutputBody]
    """

    kwargs = _get_kwargs(
        environment=environment,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
) -> ErrorModel | IngestionStatusOutputBody | None:
    """Whether this workspace has ever ingested an event (onboarding signal)

     A cheap connection signal for onboarding, distinct from recent activity: everIngested is true once
    any event has ever landed for the org (optionally scoped to one environment). A minted API key is
    NOT proof of instrumentation; observed ingestion is.

    Args:
        environment (str | Unset): Environment slug or id to scope the check to (omit for org-
            wide)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | IngestionStatusOutputBody
    """

    return sync_detailed(
        client=client,
        environment=environment,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
) -> Response[ErrorModel | IngestionStatusOutputBody]:
    """Whether this workspace has ever ingested an event (onboarding signal)

     A cheap connection signal for onboarding, distinct from recent activity: everIngested is true once
    any event has ever landed for the org (optionally scoped to one environment). A minted API key is
    NOT proof of instrumentation; observed ingestion is.

    Args:
        environment (str | Unset): Environment slug or id to scope the check to (omit for org-
            wide)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | IngestionStatusOutputBody]
    """

    kwargs = _get_kwargs(
        environment=environment,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    environment: str | Unset = UNSET,
) -> ErrorModel | IngestionStatusOutputBody | None:
    """Whether this workspace has ever ingested an event (onboarding signal)

     A cheap connection signal for onboarding, distinct from recent activity: everIngested is true once
    any event has ever landed for the org (optionally scoped to one environment). A minted API key is
    NOT proof of instrumentation; observed ingestion is.

    Args:
        environment (str | Unset): Environment slug or id to scope the check to (omit for org-
            wide)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | IngestionStatusOutputBody
    """

    return (
        await asyncio_detailed(
            client=client,
            environment=environment,
        )
    ).parsed
