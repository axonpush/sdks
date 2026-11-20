from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_feedback_dto import ErrorFeedbackDTO


T = TypeVar("T", bound="ErrorFeedbackOutputBody")


@_attrs_define
class ErrorFeedbackOutputBody:
    """
    Attributes:
        feedback (list[ErrorFeedbackDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    feedback: list[ErrorFeedbackDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.error_feedback_dto import ErrorFeedbackDTO

        feedback: list[dict[str, Any]] | None
        if isinstance(self.feedback, list):
            feedback = []
            for feedback_type_0_item_data in self.feedback:
                feedback_type_0_item = feedback_type_0_item_data.to_dict()
                feedback.append(feedback_type_0_item)

        else:
            feedback = self.feedback

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "feedback": feedback,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_feedback_dto import ErrorFeedbackDTO

        d = dict(src_dict)

        def _parse_feedback(data: object) -> list[ErrorFeedbackDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                feedback_type_0 = []
                _feedback_type_0 = data
                for feedback_type_0_item_data in _feedback_type_0:
                    feedback_type_0_item = ErrorFeedbackDTO.from_dict(feedback_type_0_item_data)

                    feedback_type_0.append(feedback_type_0_item)

                return feedback_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ErrorFeedbackDTO] | None, data)

        feedback = _parse_feedback(d.pop("feedback"))

        schema = d.pop("$schema", UNSET)

        error_feedback_output_body = cls(
            feedback=feedback,
            schema=schema,
        )

        return error_feedback_output_body
