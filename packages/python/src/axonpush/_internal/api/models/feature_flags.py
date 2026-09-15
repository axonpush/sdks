from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FeatureFlags")


@_attrs_define
class FeatureFlags:
    """
    Attributes:
        async_ingest (bool):
        environments (bool):
        mcp_server (bool):
        sentry_ingest (bool):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    async_ingest: bool
    environments: bool
    mcp_server: bool
    sentry_ingest: bool
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        async_ingest = self.async_ingest

        environments = self.environments

        mcp_server = self.mcp_server

        sentry_ingest = self.sentry_ingest

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "asyncIngest": async_ingest,
                "environments": environments,
                "mcpServer": mcp_server,
                "sentryIngest": sentry_ingest,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        async_ingest = d.pop("asyncIngest")

        environments = d.pop("environments")

        mcp_server = d.pop("mcpServer")

        sentry_ingest = d.pop("sentryIngest")

        schema = d.pop("$schema", UNSET)

        feature_flags = cls(
            async_ingest=async_ingest,
            environments=environments,
            mcp_server=mcp_server,
            sentry_ingest=sentry_ingest,
            schema=schema,
        )

        return feature_flags
