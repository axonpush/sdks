from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast


T = TypeVar("T", bound="Stage")


@_attrs_define
class Stage:
    """
    Attributes:
        id (str):
        label (str):
        requirements (list[str] | None):
    """

    id: str
    label: str
    requirements: list[str] | None

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label = self.label

        requirements: list[str] | None
        if isinstance(self.requirements, list):
            requirements = self.requirements

        else:
            requirements = self.requirements

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "label": label,
                "requirements": requirements,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        label = d.pop("label")

        def _parse_requirements(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                requirements_type_0 = cast(list[str], data)

                return requirements_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        requirements = _parse_requirements(d.pop("requirements"))

        stage = cls(
            id=id,
            label=label,
            requirements=requirements,
        )

        return stage
