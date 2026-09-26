from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.diff_input_body import DiffInputBody
from ...models.diff_output_body import DiffOutputBody
from ...models.error_model import ErrorModel
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: DiffInputBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/analytics/diff",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DiffOutputBody | ErrorModel:
    if response.status_code == 200:
        response_200 = DiffOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DiffOutputBody | ErrorModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DiffInputBody,
) -> Response[DiffOutputBody | ErrorModel]:
    """BubbleUp attribute-diff: rank attributes by how differently their values appear in a selection vs a
    baseline cohort

     Honeycomb-style BubbleUp. Give a selection cohort and a baseline cohort (each the same filter shape
    as the other analytics reads, plus errorsOnly / minDurationMs so the selection can be the slow-or-
    error slice). For each cataloged attribute key it computes the value distribution in both cohorts
    and ranks keys by how over-represented a value is in the selection. Restrict the diffed keys with
    'keys' (else the top cataloged keys are used, capped).

    Args:
        body (DiffInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DiffOutputBody | ErrorModel]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: DiffInputBody,
) -> DiffOutputBody | ErrorModel | None:
    """BubbleUp attribute-diff: rank attributes by how differently their values appear in a selection vs a
    baseline cohort

     Honeycomb-style BubbleUp. Give a selection cohort and a baseline cohort (each the same filter shape
    as the other analytics reads, plus errorsOnly / minDurationMs so the selection can be the slow-or-
    error slice). For each cataloged attribute key it computes the value distribution in both cohorts
    and ranks keys by how over-represented a value is in the selection. Restrict the diffed keys with
    'keys' (else the top cataloged keys are used, capped).

    Args:
        body (DiffInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DiffOutputBody | ErrorModel
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DiffInputBody,
) -> Response[DiffOutputBody | ErrorModel]:
    """BubbleUp attribute-diff: rank attributes by how differently their values appear in a selection vs a
    baseline cohort

     Honeycomb-style BubbleUp. Give a selection cohort and a baseline cohort (each the same filter shape
    as the other analytics reads, plus errorsOnly / minDurationMs so the selection can be the slow-or-
    error slice). For each cataloged attribute key it computes the value distribution in both cohorts
    and ranks keys by how over-represented a value is in the selection. Restrict the diffed keys with
    'keys' (else the top cataloged keys are used, capped).

    Args:
        body (DiffInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DiffOutputBody | ErrorModel]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DiffInputBody,
) -> DiffOutputBody | ErrorModel | None:
    """BubbleUp attribute-diff: rank attributes by how differently their values appear in a selection vs a
    baseline cohort

     Honeycomb-style BubbleUp. Give a selection cohort and a baseline cohort (each the same filter shape
    as the other analytics reads, plus errorsOnly / minDurationMs so the selection can be the slow-or-
    error slice). For each cataloged attribute key it computes the value distribution in both cohorts
    and ranks keys by how over-represented a value is in the selection. Restrict the diffed keys with
    'keys' (else the top cataloged keys are used, capped).

    Args:
        body (DiffInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DiffOutputBody | ErrorModel
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
