from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.action_controller_list_review_state import ActionControllerListReviewState
from ...models.action_controller_list_state import ActionControllerListState
from ...models.action_list_dto import ActionListDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    app_id: str | Unset = UNSET,
    contract_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    review_state: ActionControllerListReviewState | Unset = UNSET,
    state: ActionControllerListState | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["appId"] = app_id

    params["contractId"] = contract_id

    params["cursor"] = cursor

    params["environmentId"] = environment_id

    json_review_state: str | Unset = UNSET
    if not isinstance(review_state, Unset):
        json_review_state = review_state.value

    params["reviewState"] = json_review_state

    json_state: str | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state.value

    params["state"] = json_state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/actions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActionListDto | None:
    if response.status_code == 200:
        response_200 = ActionListDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ActionListDto]:
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
    contract_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    review_state: ActionControllerListReviewState | Unset = UNSET,
    state: ActionControllerListState | Unset = UNSET,
) -> Response[ActionListDto]:
    """
    Args:
        app_id (str | Unset):
        contract_id (str | Unset):
        cursor (str | Unset):
        environment_id (str | Unset):
        review_state (ActionControllerListReviewState | Unset):
        state (ActionControllerListState | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionListDto]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        contract_id=contract_id,
        cursor=cursor,
        environment_id=environment_id,
        review_state=review_state,
        state=state,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    app_id: str | Unset = UNSET,
    contract_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    review_state: ActionControllerListReviewState | Unset = UNSET,
    state: ActionControllerListState | Unset = UNSET,
) -> ActionListDto | None:
    """
    Args:
        app_id (str | Unset):
        contract_id (str | Unset):
        cursor (str | Unset):
        environment_id (str | Unset):
        review_state (ActionControllerListReviewState | Unset):
        state (ActionControllerListState | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionListDto
    """

    return sync_detailed(
        client=client,
        app_id=app_id,
        contract_id=contract_id,
        cursor=cursor,
        environment_id=environment_id,
        review_state=review_state,
        state=state,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    app_id: str | Unset = UNSET,
    contract_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    review_state: ActionControllerListReviewState | Unset = UNSET,
    state: ActionControllerListState | Unset = UNSET,
) -> Response[ActionListDto]:
    """
    Args:
        app_id (str | Unset):
        contract_id (str | Unset):
        cursor (str | Unset):
        environment_id (str | Unset):
        review_state (ActionControllerListReviewState | Unset):
        state (ActionControllerListState | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionListDto]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        contract_id=contract_id,
        cursor=cursor,
        environment_id=environment_id,
        review_state=review_state,
        state=state,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    app_id: str | Unset = UNSET,
    contract_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    review_state: ActionControllerListReviewState | Unset = UNSET,
    state: ActionControllerListState | Unset = UNSET,
) -> ActionListDto | None:
    """
    Args:
        app_id (str | Unset):
        contract_id (str | Unset):
        cursor (str | Unset):
        environment_id (str | Unset):
        review_state (ActionControllerListReviewState | Unset):
        state (ActionControllerListState | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionListDto
    """

    return (
        await asyncio_detailed(
            client=client,
            app_id=app_id,
            contract_id=contract_id,
            cursor=cursor,
            environment_id=environment_id,
            review_state=review_state,
            state=state,
        )
    ).parsed
