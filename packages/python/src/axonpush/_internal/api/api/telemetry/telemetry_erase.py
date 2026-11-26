from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.erase_evidence_output_body import EraseEvidenceOutputBody
from ...models.error_model import ErrorModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    subject_type: str,
    subject_id: str,
    *,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["appId"] = app_id

    params["environmentId"] = environment_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/telemetry/subjects/{subject_type}/{subject_id}".format(
            subject_type=quote(str(subject_type), safe=""),
            subject_id=quote(str(subject_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EraseEvidenceOutputBody | ErrorModel:
    if response.status_code == 200:
        response_200 = EraseEvidenceOutputBody.from_dict(response.json())

        return response_200

    response_default = ErrorModel.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EraseEvidenceOutputBody | ErrorModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    subject_type: str,
    subject_id: str,
    *,
    client: AuthenticatedClient | Client,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
) -> Response[EraseEvidenceOutputBody | ErrorModel]:
    """Erase subject evidence and prevent delayed ingestion restoring it

    Args:
        subject_type (str):
        subject_id (str):
        app_id (str | Unset):
        environment_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EraseEvidenceOutputBody | ErrorModel]
    """

    kwargs = _get_kwargs(
        subject_type=subject_type,
        subject_id=subject_id,
        app_id=app_id,
        environment_id=environment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subject_type: str,
    subject_id: str,
    *,
    client: AuthenticatedClient | Client,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
) -> EraseEvidenceOutputBody | ErrorModel | None:
    """Erase subject evidence and prevent delayed ingestion restoring it

    Args:
        subject_type (str):
        subject_id (str):
        app_id (str | Unset):
        environment_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EraseEvidenceOutputBody | ErrorModel
    """

    return sync_detailed(
        subject_type=subject_type,
        subject_id=subject_id,
        client=client,
        app_id=app_id,
        environment_id=environment_id,
    ).parsed


async def asyncio_detailed(
    subject_type: str,
    subject_id: str,
    *,
    client: AuthenticatedClient | Client,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
) -> Response[EraseEvidenceOutputBody | ErrorModel]:
    """Erase subject evidence and prevent delayed ingestion restoring it

    Args:
        subject_type (str):
        subject_id (str):
        app_id (str | Unset):
        environment_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EraseEvidenceOutputBody | ErrorModel]
    """

    kwargs = _get_kwargs(
        subject_type=subject_type,
        subject_id=subject_id,
        app_id=app_id,
        environment_id=environment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subject_type: str,
    subject_id: str,
    *,
    client: AuthenticatedClient | Client,
    app_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
) -> EraseEvidenceOutputBody | ErrorModel | None:
    """Erase subject evidence and prevent delayed ingestion restoring it

    Args:
        subject_type (str):
        subject_id (str):
        app_id (str | Unset):
        environment_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EraseEvidenceOutputBody | ErrorModel
    """

    return (
        await asyncio_detailed(
            subject_type=subject_type,
            subject_id=subject_id,
            client=client,
            app_id=app_id,
            environment_id=environment_id,
        )
    ).parsed
