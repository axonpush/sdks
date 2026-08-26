from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.evaluator_delete_dto import EvaluatorDeleteDto
from ...types import UNSET, Response


def _get_kwargs(
    evaluator_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v2/evaluators/{evaluator_id}".format(
            evaluator_id=quote(str(evaluator_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EvaluatorDeleteDto | None:
    if response.status_code == 200:
        response_200 = EvaluatorDeleteDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EvaluatorDeleteDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    evaluator_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[EvaluatorDeleteDto]:
    """
    Args:
        evaluator_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EvaluatorDeleteDto]
    """

    kwargs = _get_kwargs(
        evaluator_id=evaluator_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    evaluator_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> EvaluatorDeleteDto | None:
    """
    Args:
        evaluator_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EvaluatorDeleteDto
    """

    return sync_detailed(
        evaluator_id=evaluator_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    evaluator_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[EvaluatorDeleteDto]:
    """
    Args:
        evaluator_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EvaluatorDeleteDto]
    """

    kwargs = _get_kwargs(
        evaluator_id=evaluator_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    evaluator_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> EvaluatorDeleteDto | None:
    """
    Args:
        evaluator_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EvaluatorDeleteDto
    """

    return (
        await asyncio_detailed(
            evaluator_id=evaluator_id,
            client=client,
        )
    ).parsed
