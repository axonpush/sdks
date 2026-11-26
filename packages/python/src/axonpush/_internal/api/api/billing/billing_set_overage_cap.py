from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.overage_cap_input_body import OverageCapInputBody
from ...models.overage_cap_output_body import OverageCapOutputBody
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: OverageCapInputBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/billing/overage-cap",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | OverageCapOutputBody:
    if response.status_code == 200:
        response_200 = OverageCapOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | OverageCapOutputBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: OverageCapInputBody,
) -> Response[ErrorModel | OverageCapOutputBody]:
    """Set the monthly overage limit

     Pro and Team bill events above the monthly quota at the plan's overage price. The limit caps that
    overage in USD per month: ingestion stops once it is reached. Null removes the limit; 0 stops
    ingestion at the quota.

    Args:
        body (OverageCapInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | OverageCapOutputBody]
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
    body: OverageCapInputBody,
) -> ErrorModel | OverageCapOutputBody | None:
    """Set the monthly overage limit

     Pro and Team bill events above the monthly quota at the plan's overage price. The limit caps that
    overage in USD per month: ingestion stops once it is reached. Null removes the limit; 0 stops
    ingestion at the quota.

    Args:
        body (OverageCapInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | OverageCapOutputBody
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: OverageCapInputBody,
) -> Response[ErrorModel | OverageCapOutputBody]:
    """Set the monthly overage limit

     Pro and Team bill events above the monthly quota at the plan's overage price. The limit caps that
    overage in USD per month: ingestion stops once it is reached. Null removes the limit; 0 stops
    ingestion at the quota.

    Args:
        body (OverageCapInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | OverageCapOutputBody]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: OverageCapInputBody,
) -> ErrorModel | OverageCapOutputBody | None:
    """Set the monthly overage limit

     Pro and Team bill events above the monthly quota at the plan's overage price. The limit caps that
    overage in USD per month: ingestion stops once it is reached. Null removes the limit; 0 stops
    ingestion at the quota.

    Args:
        body (OverageCapInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | OverageCapOutputBody
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
