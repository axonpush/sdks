from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.issue_response_dto import IssueResponseDto
from ...models.merge_issue_dto import MergeIssueDto
from ...types import UNSET, Response


def _get_kwargs(
    issue_id: str,
    *,
    body: MergeIssueDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/issues/{issue_id}/merge".format(
            issue_id=quote(str(issue_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IssueResponseDto | None:
    if response.status_code == 201:
        response_201 = IssueResponseDto.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IssueResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    issue_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MergeIssueDto,
) -> Response[IssueResponseDto]:
    """
    Args:
        issue_id (str):
        body (MergeIssueDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IssueResponseDto]
    """

    kwargs = _get_kwargs(
        issue_id=issue_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    issue_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MergeIssueDto,
) -> IssueResponseDto | None:
    """
    Args:
        issue_id (str):
        body (MergeIssueDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IssueResponseDto
    """

    return sync_detailed(
        issue_id=issue_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    issue_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MergeIssueDto,
) -> Response[IssueResponseDto]:
    """
    Args:
        issue_id (str):
        body (MergeIssueDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IssueResponseDto]
    """

    kwargs = _get_kwargs(
        issue_id=issue_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    issue_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MergeIssueDto,
) -> IssueResponseDto | None:
    """
    Args:
        issue_id (str):
        body (MergeIssueDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IssueResponseDto
    """

    return (
        await asyncio_detailed(
            issue_id=issue_id,
            client=client,
            body=body,
        )
    ).parsed
