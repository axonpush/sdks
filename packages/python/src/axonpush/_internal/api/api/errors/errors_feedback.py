from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_feedback_output_body import ErrorFeedbackOutputBody
from ...models.error_model import ErrorModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    fingerprint: str,
    *,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["appId"] = app_id

    params["environmentId"] = environment_id

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/errors/{fingerprint}/feedback".format(
            fingerprint=quote(str(fingerprint), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorFeedbackOutputBody | ErrorModel:
    if response.status_code == 200:
        response_200 = ErrorFeedbackOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorFeedbackOutputBody | ErrorModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    fingerprint: str,
    *,
    client: AuthenticatedClient | Client,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ErrorFeedbackOutputBody | ErrorModel]:
    """List user feedback linked to an error Issue by event id or shared trace

    Args:
        fingerprint (str):
        app_id (str | Unset):
        environment_id (str | Unset): Environment slug or id
        limit (int | Unset): Max feedback items (default 50, max 200)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorFeedbackOutputBody | ErrorModel]
    """

    kwargs = _get_kwargs(
        fingerprint=fingerprint,
        app_id=app_id,
        environment_id=environment_id,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fingerprint: str,
    *,
    client: AuthenticatedClient | Client,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ErrorFeedbackOutputBody | ErrorModel | None:
    """List user feedback linked to an error Issue by event id or shared trace

    Args:
        fingerprint (str):
        app_id (str | Unset):
        environment_id (str | Unset): Environment slug or id
        limit (int | Unset): Max feedback items (default 50, max 200)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorFeedbackOutputBody | ErrorModel
    """

    return sync_detailed(
        fingerprint=fingerprint,
        client=client,
        app_id=app_id,
        environment_id=environment_id,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    fingerprint: str,
    *,
    client: AuthenticatedClient | Client,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ErrorFeedbackOutputBody | ErrorModel]:
    """List user feedback linked to an error Issue by event id or shared trace

    Args:
        fingerprint (str):
        app_id (str | Unset):
        environment_id (str | Unset): Environment slug or id
        limit (int | Unset): Max feedback items (default 50, max 200)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorFeedbackOutputBody | ErrorModel]
    """

    kwargs = _get_kwargs(
        fingerprint=fingerprint,
        app_id=app_id,
        environment_id=environment_id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fingerprint: str,
    *,
    client: AuthenticatedClient | Client,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ErrorFeedbackOutputBody | ErrorModel | None:
    """List user feedback linked to an error Issue by event id or shared trace

    Args:
        fingerprint (str):
        app_id (str | Unset):
        environment_id (str | Unset): Environment slug or id
        limit (int | Unset): Max feedback items (default 50, max 200)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorFeedbackOutputBody | ErrorModel
    """

    return (
        await asyncio_detailed(
            fingerprint=fingerprint,
            client=client,
            app_id=app_id,
            environment_id=environment_id,
            limit=limit,
        )
    ).parsed
