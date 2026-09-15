from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel_dto import ChannelDTO


T = TypeVar("T", bound="ListChannelsOutputBody")


@_attrs_define
class ListChannelsOutputBody:
    """
    Attributes:
        channels (list[ChannelDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    channels: list[ChannelDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.channel_dto import ChannelDTO

        channels: list[dict[str, Any]] | None
        if isinstance(self.channels, list):
            channels = []
            for channels_type_0_item_data in self.channels:
                channels_type_0_item = channels_type_0_item_data.to_dict()
                channels.append(channels_type_0_item)

        else:
            channels = self.channels

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "channels": channels,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.channel_dto import ChannelDTO

        d = dict(src_dict)

        def _parse_channels(data: object) -> list[ChannelDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                channels_type_0 = []
                _channels_type_0 = data
                for channels_type_0_item_data in _channels_type_0:
                    channels_type_0_item = ChannelDTO.from_dict(channels_type_0_item_data)

                    channels_type_0.append(channels_type_0_item)

                return channels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ChannelDTO] | None, data)

        channels = _parse_channels(d.pop("channels"))

        schema = d.pop("$schema", UNSET)

        list_channels_output_body = cls(
            channels=channels,
            schema=schema,
        )

        return list_channels_output_body
