from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="SetupQuestion")


@_attrs_define
class SetupQuestion:
    """
    Attributes:
        hint (str):
        id (str):
        question (str):
        options (list[str] | None | Unset):
    """

    hint: str
    id: str
    question: str
    options: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        hint = self.hint

        id = self.id

        question = self.question

        options: list[str] | None | Unset
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, list):
            options = self.options

        else:
            options = self.options

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "hint": hint,
                "id": id,
                "question": question,
            }
        )
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hint = d.pop("hint")

        id = d.pop("id")

        question = d.pop("question")

        def _parse_options(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                options_type_0 = cast(list[str], data)

                return options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        options = _parse_options(d.pop("options", UNSET))

        setup_question = cls(
            hint=hint,
            id=id,
            question=question,
            options=options,
        )

        return setup_question
