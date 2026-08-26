from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.prompt_version_dto import PromptVersionDto
from ...types import UNSET, Response


def _get_kwargs(
    prompt_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/prompts/{prompt_id}/versions".format(
            prompt_id=quote(str(prompt_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PromptVersionDto | None:
    if response.status_code == 200:
        response_200 = PromptVersionDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PromptVersionDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    prompt_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[PromptVersionDto]:
    """
    Args:
        prompt_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PromptVersionDto]
    """

    kwargs = _get_kwargs(
        prompt_id=prompt_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    prompt_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> PromptVersionDto | None:
    """
    Args:
        prompt_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PromptVersionDto
    """

    return sync_detailed(
        prompt_id=prompt_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    prompt_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[PromptVersionDto]:
    """
    Args:
        prompt_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PromptVersionDto]
    """

    kwargs = _get_kwargs(
        prompt_id=prompt_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    prompt_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> PromptVersionDto | None:
    """
    Args:
        prompt_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PromptVersionDto
    """

    return (
        await asyncio_detailed(
            prompt_id=prompt_id,
            client=client,
        )
    ).parsed
