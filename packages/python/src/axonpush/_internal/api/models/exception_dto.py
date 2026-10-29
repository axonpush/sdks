from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stack_frame_dto import StackFrameDTO


T = TypeVar("T", bound="ExceptionDTO")


@_attrs_define
class ExceptionDTO:
    """
    Attributes:
        stack (list[StackFrameDTO] | None):
        message (str | Unset):
        type_ (str | Unset):
    """

    stack: list[StackFrameDTO] | None
    message: str | Unset = UNSET
    type_: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.stack_frame_dto import StackFrameDTO

        stack: list[dict[str, Any]] | None
        if isinstance(self.stack, list):
            stack = []
            for stack_type_0_item_data in self.stack:
                stack_type_0_item = stack_type_0_item_data.to_dict()
                stack.append(stack_type_0_item)

        else:
            stack = self.stack

        message = self.message

        type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "stack": stack,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stack_frame_dto import StackFrameDTO

        d = dict(src_dict)

        def _parse_stack(data: object) -> list[StackFrameDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                stack_type_0 = []
                _stack_type_0 = data
                for stack_type_0_item_data in _stack_type_0:
                    stack_type_0_item = StackFrameDTO.from_dict(stack_type_0_item_data)

                    stack_type_0.append(stack_type_0_item)

                return stack_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[StackFrameDTO] | None, data)

        stack = _parse_stack(d.pop("stack"))

        message = d.pop("message", UNSET)

        type_ = d.pop("type", UNSET)

        exception_dto = cls(
            stack=stack,
            message=message,
            type_=type_,
        )

        return exception_dto
