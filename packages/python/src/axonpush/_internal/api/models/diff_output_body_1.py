from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.bundle import Bundle


T = TypeVar("T", bound="DiffOutputBody1")


@_attrs_define
class DiffOutputBody1:
    """
    Attributes:
        after (Bundle):
        before (Bundle):
        semantic_changed (bool):
        source_changed (bool):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    after: Bundle
    before: Bundle
    semantic_changed: bool
    source_changed: bool
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.bundle import Bundle

        after = self.after.to_dict()

        before = self.before.to_dict()

        semantic_changed = self.semantic_changed

        source_changed = self.source_changed

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "after": after,
                "before": before,
                "semantic_changed": semantic_changed,
                "source_changed": source_changed,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bundle import Bundle

        d = dict(src_dict)
        after = Bundle.from_dict(d.pop("after"))

        before = Bundle.from_dict(d.pop("before"))

        semantic_changed = d.pop("semantic_changed")

        source_changed = d.pop("source_changed")

        schema = d.pop("$schema", UNSET)

        diff_output_body_1 = cls(
            after=after,
            before=before,
            semantic_changed=semantic_changed,
            source_changed=source_changed,
            schema=schema,
        )

        return diff_output_body_1
