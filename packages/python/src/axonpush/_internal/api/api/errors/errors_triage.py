from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.issue_triage_dto import IssueTriageDTO
from ...models.patch_error_input_body import PatchErrorInputBody
from ...types import UNSET, Response


def _get_kwargs(
    fingerprint: str,
    *,
    body: PatchErrorInputBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/errors/{fingerprint}".format(
            fingerprint=quote(str(fingerprint), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | IssueTriageDTO:
    if response.status_code == 200:
        response_200 = IssueTriageDTO.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | IssueTriageDTO]:
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
    body: PatchErrorInputBody,
) -> Response[ErrorModel | IssueTriageDTO]:
    """Triage an error Issue (resolve, unresolve, ignore, mute, assign)

    Args:
        fingerprint (str):
        body (PatchErrorInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | IssueTriageDTO]
    """

    kwargs = _get_kwargs(
        fingerprint=fingerprint,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fingerprint: str,
    *,
    client: AuthenticatedClient | Client,
    body: PatchErrorInputBody,
) -> ErrorModel | IssueTriageDTO | None:
    """Triage an error Issue (resolve, unresolve, ignore, mute, assign)

    Args:
        fingerprint (str):
        body (PatchErrorInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | IssueTriageDTO
    """

    return sync_detailed(
        fingerprint=fingerprint,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    fingerprint: str,
    *,
    client: AuthenticatedClient | Client,
    body: PatchErrorInputBody,
) -> Response[ErrorModel | IssueTriageDTO]:
    """Triage an error Issue (resolve, unresolve, ignore, mute, assign)

    Args:
        fingerprint (str):
        body (PatchErrorInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | IssueTriageDTO]
    """

    kwargs = _get_kwargs(
        fingerprint=fingerprint,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fingerprint: str,
    *,
    client: AuthenticatedClient | Client,
    body: PatchErrorInputBody,
) -> ErrorModel | IssueTriageDTO | None:
    """Triage an error Issue (resolve, unresolve, ignore, mute, assign)

    Args:
        fingerprint (str):
        body (PatchErrorInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | IssueTriageDTO
    """

    return (
        await asyncio_detailed(
            fingerprint=fingerprint,
            client=client,
            body=body,
        )
    ).parsed
