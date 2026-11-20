from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.release_dto import ReleaseDTO


T = TypeVar("T", bound="ListReleasesOutputBody")


@_attrs_define
class ListReleasesOutputBody:
    """
    Attributes:
        releases (list[ReleaseDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    releases: list[ReleaseDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.release_dto import ReleaseDTO

        releases: list[dict[str, Any]] | None
        if isinstance(self.releases, list):
            releases = []
            for releases_type_0_item_data in self.releases:
                releases_type_0_item = releases_type_0_item_data.to_dict()
                releases.append(releases_type_0_item)

        else:
            releases = self.releases

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "releases": releases,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.release_dto import ReleaseDTO

        d = dict(src_dict)

        def _parse_releases(data: object) -> list[ReleaseDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                releases_type_0 = []
                _releases_type_0 = data
                for releases_type_0_item_data in _releases_type_0:
                    releases_type_0_item = ReleaseDTO.from_dict(releases_type_0_item_data)

                    releases_type_0.append(releases_type_0_item)

                return releases_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ReleaseDTO] | None, data)

        releases = _parse_releases(d.pop("releases"))

        schema = d.pop("$schema", UNSET)

        list_releases_output_body = cls(
            releases=releases,
            schema=schema,
        )

        return list_releases_output_body
