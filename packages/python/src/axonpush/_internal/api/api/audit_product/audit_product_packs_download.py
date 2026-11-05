from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audit_product_packs_download_format import AuditProductPacksDownloadFormat
from ...models.error_model import ErrorModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    format_: AuditProductPacksDownloadFormat | Unset = AuditProductPacksDownloadFormat.JSON,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_format_: str | Unset = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/audit/packs/{id}/download".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorModel | str:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorModel | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    format_: AuditProductPacksDownloadFormat | Unset = AuditProductPacksDownloadFormat.JSON,
) -> Response[ErrorModel | str]:
    """Download a signed evidence pack

    Args:
        id (str):
        format_ (AuditProductPacksDownloadFormat | Unset):  Default:
            AuditProductPacksDownloadFormat.JSON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | str]
    """

    kwargs = _get_kwargs(
        id=id,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    format_: AuditProductPacksDownloadFormat | Unset = AuditProductPacksDownloadFormat.JSON,
) -> ErrorModel | str | None:
    """Download a signed evidence pack

    Args:
        id (str):
        format_ (AuditProductPacksDownloadFormat | Unset):  Default:
            AuditProductPacksDownloadFormat.JSON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | str
    """

    return sync_detailed(
        id=id,
        client=client,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    format_: AuditProductPacksDownloadFormat | Unset = AuditProductPacksDownloadFormat.JSON,
) -> Response[ErrorModel | str]:
    """Download a signed evidence pack

    Args:
        id (str):
        format_ (AuditProductPacksDownloadFormat | Unset):  Default:
            AuditProductPacksDownloadFormat.JSON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorModel | str]
    """

    kwargs = _get_kwargs(
        id=id,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    format_: AuditProductPacksDownloadFormat | Unset = AuditProductPacksDownloadFormat.JSON,
) -> ErrorModel | str | None:
    """Download a signed evidence pack

    Args:
        id (str):
        format_ (AuditProductPacksDownloadFormat | Unset):  Default:
            AuditProductPacksDownloadFormat.JSON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorModel | str
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            format_=format_,
        )
    ).parsed
