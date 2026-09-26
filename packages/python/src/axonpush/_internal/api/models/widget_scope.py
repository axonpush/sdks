from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WidgetScope")


@_attrs_define
class WidgetScope:
    """
    Attributes:
        app (str | Unset):
        channel (str | Unset): Scope to a channel id
        environment (str | Unset):
        filter_tag_key (str | Unset): Scope to a custom-dimension value; pair with filterTagValue
        filter_tag_value (str | Unset):
        model (str | Unset):
        provider (str | Unset):
        source (str | Unset):
    """

    app: str | Unset = UNSET
    channel: str | Unset = UNSET
    environment: str | Unset = UNSET
    filter_tag_key: str | Unset = UNSET
    filter_tag_value: str | Unset = UNSET
    model: str | Unset = UNSET
    provider: str | Unset = UNSET
    source: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        app = self.app

        channel = self.channel

        environment = self.environment

        filter_tag_key = self.filter_tag_key

        filter_tag_value = self.filter_tag_value

        model = self.model

        provider = self.provider

        source = self.source

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if app is not UNSET:
            field_dict["app"] = app
        if channel is not UNSET:
            field_dict["channel"] = channel
        if environment is not UNSET:
            field_dict["environment"] = environment
        if filter_tag_key is not UNSET:
            field_dict["filterTagKey"] = filter_tag_key
        if filter_tag_value is not UNSET:
            field_dict["filterTagValue"] = filter_tag_value
        if model is not UNSET:
            field_dict["model"] = model
        if provider is not UNSET:
            field_dict["provider"] = provider
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app = d.pop("app", UNSET)

        channel = d.pop("channel", UNSET)

        environment = d.pop("environment", UNSET)

        filter_tag_key = d.pop("filterTagKey", UNSET)

        filter_tag_value = d.pop("filterTagValue", UNSET)

        model = d.pop("model", UNSET)

        provider = d.pop("provider", UNSET)

        source = d.pop("source", UNSET)

        widget_scope = cls(
            app=app,
            channel=channel,
            environment=environment,
            filter_tag_key=filter_tag_key,
            filter_tag_value=filter_tag_value,
            model=model,
            provider=provider,
            source=source,
        )

        return widget_scope
