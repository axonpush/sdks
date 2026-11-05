from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.segment_list_output_body import SegmentListOutputBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["from"] = from_

    params["to"] = to

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/audit/segments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | SegmentListOutputBody:
    if response.status_code == 200:
        response_200 = SegmentListOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | SegmentListOutputBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> Response[ErrorModel | SegmentListOutputBody]:
    """List sealed archive parts

    Args:
        from_ (str | Unset):
        to (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | SegmentListOutputBody]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> ErrorModel | SegmentListOutputBody | None:
    """List sealed archive parts

    Args:
        from_ (str | Unset):
        to (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | SegmentListOutputBody
    """

    return sync_detailed(
        client=client,
        from_=from_,
        to=to,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> Response[ErrorModel | SegmentListOutputBody]:
    """List sealed archive parts

    Args:
        from_ (str | Unset):
        to (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | SegmentListOutputBody]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
) -> ErrorModel | SegmentListOutputBody | None:
    """List sealed archive parts

    Args:
        from_ (str | Unset):
        to (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | SegmentListOutputBody
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            to=to,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
