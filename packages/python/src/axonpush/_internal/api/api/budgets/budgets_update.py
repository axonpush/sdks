from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cost_budget import CostBudget
from ...models.error_model import ErrorModel
from ...models.update_input_body import UpdateInputBody
from ...types import UNSET, Response


def _get_kwargs(
    budget_id: str,
    *,
    body: UpdateInputBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/budgets/{budget_id}".format(
            budget_id=quote(str(budget_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CostBudget | ErrorModel:
    if response.status_code == 200:
        response_200 = CostBudget.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CostBudget | ErrorModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    budget_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateInputBody,
) -> Response[CostBudget | ErrorModel]:
    """Update a cost budget

    Args:
        budget_id (str):
        body (UpdateInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CostBudget | ErrorModel]
    """

    kwargs = _get_kwargs(
        budget_id=budget_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    budget_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateInputBody,
) -> CostBudget | ErrorModel | None:
    """Update a cost budget

    Args:
        budget_id (str):
        body (UpdateInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CostBudget | ErrorModel
    """

    return sync_detailed(
        budget_id=budget_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    budget_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateInputBody,
) -> Response[CostBudget | ErrorModel]:
    """Update a cost budget

    Args:
        budget_id (str):
        body (UpdateInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CostBudget | ErrorModel]
    """

    kwargs = _get_kwargs(
        budget_id=budget_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    budget_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateInputBody,
) -> CostBudget | ErrorModel | None:
    """Update a cost budget

    Args:
        budget_id (str):
        body (UpdateInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CostBudget | ErrorModel
    """

    return (
        await asyncio_detailed(
            budget_id=budget_id,
            client=client,
            body=body,
        )
    ).parsed
