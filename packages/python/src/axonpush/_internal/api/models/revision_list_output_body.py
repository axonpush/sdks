from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_revision import ActivityRevision


T = TypeVar("T", bound="RevisionListOutputBody")


@_attrs_define
class RevisionListOutputBody:
    """
    Attributes:
        revisions (list[ActivityRevision] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    revisions: list[ActivityRevision] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_revision import ActivityRevision

        revisions: list[dict[str, Any]] | None
        if isinstance(self.revisions, list):
            revisions = []
            for revisions_type_0_item_data in self.revisions:
                revisions_type_0_item = revisions_type_0_item_data.to_dict()
                revisions.append(revisions_type_0_item)

        else:
            revisions = self.revisions

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "revisions": revisions,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_revision import ActivityRevision

        d = dict(src_dict)

        def _parse_revisions(data: object) -> list[ActivityRevision] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                revisions_type_0 = []
                _revisions_type_0 = data
                for revisions_type_0_item_data in _revisions_type_0:
                    revisions_type_0_item = ActivityRevision.from_dict(revisions_type_0_item_data)

                    revisions_type_0.append(revisions_type_0_item)

                return revisions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityRevision] | None, data)

        revisions = _parse_revisions(d.pop("revisions"))

        schema = d.pop("$schema", UNSET)

        revision_list_output_body = cls(
            revisions=revisions,
            schema=schema,
        )

        return revision_list_output_body
