from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.ok_output_body import OkOutputBody
from ...models.set_feedback_status_input_body import SetFeedbackStatusInputBody
from ...types import UNSET, Response


def _get_kwargs(
    feedback_id: str,
    *,
    body: SetFeedbackStatusInputBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/admin/feedback/{feedback_id}/status".format(
            feedback_id=quote(str(feedback_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | OkOutputBody:
    if response.status_code == 200:
        response_200 = OkOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | OkOutputBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    feedback_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetFeedbackStatusInputBody,
) -> Response[ErrorModel | OkOutputBody]:
    """Set feedback status

    Args:
        feedback_id (str):
        body (SetFeedbackStatusInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | OkOutputBody]
    """

    kwargs = _get_kwargs(
        feedback_id=feedback_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    feedback_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetFeedbackStatusInputBody,
) -> ErrorModel | OkOutputBody | None:
    """Set feedback status

    Args:
        feedback_id (str):
        body (SetFeedbackStatusInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | OkOutputBody
    """

    return sync_detailed(
        feedback_id=feedback_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    feedback_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetFeedbackStatusInputBody,
) -> Response[ErrorModel | OkOutputBody]:
    """Set feedback status

    Args:
        feedback_id (str):
        body (SetFeedbackStatusInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | OkOutputBody]
    """

    kwargs = _get_kwargs(
        feedback_id=feedback_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    feedback_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetFeedbackStatusInputBody,
) -> ErrorModel | OkOutputBody | None:
    """Set feedback status

    Args:
        feedback_id (str):
        body (SetFeedbackStatusInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | OkOutputBody
    """

    return (
        await asyncio_detailed(
            feedback_id=feedback_id,
            client=client,
            body=body,
        )
    ).parsed
