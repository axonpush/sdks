from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_dto import AppDTO


T = TypeVar("T", bound="ListAppsOutputBody")


@_attrs_define
class ListAppsOutputBody:
    """
    Attributes:
        apps (list[AppDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    apps: list[AppDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.app_dto import AppDTO

        apps: list[dict[str, Any]] | None
        if isinstance(self.apps, list):
            apps = []
            for apps_type_0_item_data in self.apps:
                apps_type_0_item = apps_type_0_item_data.to_dict()
                apps.append(apps_type_0_item)

        else:
            apps = self.apps

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "apps": apps,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_dto import AppDTO

        d = dict(src_dict)

        def _parse_apps(data: object) -> list[AppDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                apps_type_0 = []
                _apps_type_0 = data
                for apps_type_0_item_data in _apps_type_0:
                    apps_type_0_item = AppDTO.from_dict(apps_type_0_item_data)

                    apps_type_0.append(apps_type_0_item)

                return apps_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AppDTO] | None, data)

        apps = _parse_apps(d.pop("apps"))

        schema = d.pop("$schema", UNSET)

        list_apps_output_body = cls(
            apps=apps,
            schema=schema,
        )

        return list_apps_output_body
