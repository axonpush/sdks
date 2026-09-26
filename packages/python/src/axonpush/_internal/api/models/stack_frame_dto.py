from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StackFrameDTO")


@_attrs_define
class StackFrameDTO:
    """
    Attributes:
        in_app (bool):
        context_line (str | Unset):
        file (str | Unset):
        function (str | Unset):
        line (int | Unset):
        post_context (list[str] | None | Unset):
        pre_context (list[str] | None | Unset):
    """

    in_app: bool
    context_line: str | Unset = UNSET
    file: str | Unset = UNSET
    function: str | Unset = UNSET
    line: int | Unset = UNSET
    post_context: list[str] | None | Unset = UNSET
    pre_context: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        in_app = self.in_app

        context_line = self.context_line

        file = self.file

        function = self.function

        line = self.line

        post_context: list[str] | None | Unset
        if isinstance(self.post_context, Unset):
            post_context = UNSET
        elif isinstance(self.post_context, list):
            post_context = self.post_context

        else:
            post_context = self.post_context

        pre_context: list[str] | None | Unset
        if isinstance(self.pre_context, Unset):
            pre_context = UNSET
        elif isinstance(self.pre_context, list):
            pre_context = self.pre_context

        else:
            pre_context = self.pre_context

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "inApp": in_app,
            }
        )
        if context_line is not UNSET:
            field_dict["contextLine"] = context_line
        if file is not UNSET:
            field_dict["file"] = file
        if function is not UNSET:
            field_dict["function"] = function
        if line is not UNSET:
            field_dict["line"] = line
        if post_context is not UNSET:
            field_dict["postContext"] = post_context
        if pre_context is not UNSET:
            field_dict["preContext"] = pre_context

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        in_app = d.pop("inApp")

        context_line = d.pop("contextLine", UNSET)

        file = d.pop("file", UNSET)

        function = d.pop("function", UNSET)

        line = d.pop("line", UNSET)

        def _parse_post_context(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                post_context_type_0 = cast(list[str], data)

                return post_context_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        post_context = _parse_post_context(d.pop("postContext", UNSET))

        def _parse_pre_context(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                pre_context_type_0 = cast(list[str], data)

                return pre_context_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        pre_context = _parse_pre_context(d.pop("preContext", UNSET))

        stack_frame_dto = cls(
            in_app=in_app,
            context_line=context_line,
            file=file,
            function=function,
            line=line,
            post_context=post_context,
            pre_context=pre_context,
        )

        return stack_frame_dto
