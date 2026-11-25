from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_model import ErrorModel
from ...models.release_detail_dto import ReleaseDetailDTO
from ...models.releases_get_window import ReleasesGetWindow
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    release: str,
    *,
    environment_id: str | Unset = UNSET,
    window: ReleasesGetWindow | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["environmentId"] = environment_id

    json_window: str | Unset = UNSET
    if not isinstance(window, Unset):
        json_window = window.value

    params["window"] = json_window

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/releases/{release}".format(
            release=quote(str(release), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | ReleaseDetailDTO:
    if response.status_code == 200:
        response_200 = ReleaseDetailDTO.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | ReleaseDetailDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    release: str,
    *,
    client: AuthenticatedClient | Client,
    environment_id: str | Unset = UNSET,
    window: ReleasesGetWindow | Unset = UNSET,
) -> Response[ErrorModel | ReleaseDetailDTO]:
    """Get one release's hourly session health and summary

    Args:
        release (str):
        environment_id (str | Unset): Environment slug or id
        window (ReleasesGetWindow | Unset): Look-back window (default 7d)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ReleaseDetailDTO]
    """

    kwargs = _get_kwargs(
        release=release,
        environment_id=environment_id,
        window=window,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    release: str,
    *,
    client: AuthenticatedClient | Client,
    environment_id: str | Unset = UNSET,
    window: ReleasesGetWindow | Unset = UNSET,
) -> ErrorModel | ReleaseDetailDTO | None:
    """Get one release's hourly session health and summary

    Args:
        release (str):
        environment_id (str | Unset): Environment slug or id
        window (ReleasesGetWindow | Unset): Look-back window (default 7d)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ReleaseDetailDTO
    """

    return sync_detailed(
        release=release,
        client=client,
        environment_id=environment_id,
        window=window,
    ).parsed


async def asyncio_detailed(
    release: str,
    *,
    client: AuthenticatedClient | Client,
    environment_id: str | Unset = UNSET,
    window: ReleasesGetWindow | Unset = UNSET,
) -> Response[ErrorModel | ReleaseDetailDTO]:
    """Get one release's hourly session health and summary

    Args:
        release (str):
        environment_id (str | Unset): Environment slug or id
        window (ReleasesGetWindow | Unset): Look-back window (default 7d)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | ReleaseDetailDTO]
    """

    kwargs = _get_kwargs(
        release=release,
        environment_id=environment_id,
        window=window,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    release: str,
    *,
    client: AuthenticatedClient | Client,
    environment_id: str | Unset = UNSET,
    window: ReleasesGetWindow | Unset = UNSET,
) -> ErrorModel | ReleaseDetailDTO | None:
    """Get one release's hourly session health and summary

    Args:
        release (str):
        environment_id (str | Unset): Environment slug or id
        window (ReleasesGetWindow | Unset): Look-back window (default 7d)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | ReleaseDetailDTO
    """

    return (
        await asyncio_detailed(
            release=release,
            client=client,
            environment_id=environment_id,
            window=window,
        )
    ).parsed
