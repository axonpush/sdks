from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.setup_question import SetupQuestion
    from ..models.setup_step import SetupStep
    from ..models.workflow_setup_guide_example_struct import WorkflowSetupGuideExampleStruct


T = TypeVar("T", bound="WorkflowSetupGuide")


@_attrs_define
class WorkflowSetupGuide:
    """
    Attributes:
        boundaries (list[str] | None):
        compiler_version (str):
        example (WorkflowSetupGuideExampleStruct):
        purpose (str):
        questions (list[SetupQuestion] | None):
        steps (list[SetupStep] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    boundaries: list[str] | None
    compiler_version: str
    example: WorkflowSetupGuideExampleStruct
    purpose: str
    questions: list[SetupQuestion] | None
    steps: list[SetupStep] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.setup_question import SetupQuestion
        from ..models.setup_step import SetupStep
        from ..models.workflow_setup_guide_example_struct import WorkflowSetupGuideExampleStruct

        boundaries: list[str] | None
        if isinstance(self.boundaries, list):
            boundaries = self.boundaries

        else:
            boundaries = self.boundaries

        compiler_version = self.compiler_version

        example = self.example.to_dict()

        purpose = self.purpose

        questions: list[dict[str, Any]] | None
        if isinstance(self.questions, list):
            questions = []
            for questions_type_0_item_data in self.questions:
                questions_type_0_item = questions_type_0_item_data.to_dict()
                questions.append(questions_type_0_item)

        else:
            questions = self.questions

        steps: list[dict[str, Any]] | None
        if isinstance(self.steps, list):
            steps = []
            for steps_type_0_item_data in self.steps:
                steps_type_0_item = steps_type_0_item_data.to_dict()
                steps.append(steps_type_0_item)

        else:
            steps = self.steps

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "boundaries": boundaries,
                "compiler_version": compiler_version,
                "example": example,
                "purpose": purpose,
                "questions": questions,
                "steps": steps,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.setup_question import SetupQuestion
        from ..models.setup_step import SetupStep
        from ..models.workflow_setup_guide_example_struct import WorkflowSetupGuideExampleStruct

        d = dict(src_dict)

        def _parse_boundaries(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                boundaries_type_0 = cast(list[str], data)

                return boundaries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        boundaries = _parse_boundaries(d.pop("boundaries"))

        compiler_version = d.pop("compiler_version")

        example = WorkflowSetupGuideExampleStruct.from_dict(d.pop("example"))

        purpose = d.pop("purpose")

        def _parse_questions(data: object) -> list[SetupQuestion] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                questions_type_0 = []
                _questions_type_0 = data
                for questions_type_0_item_data in _questions_type_0:
                    questions_type_0_item = SetupQuestion.from_dict(questions_type_0_item_data)

                    questions_type_0.append(questions_type_0_item)

                return questions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SetupQuestion] | None, data)

        questions = _parse_questions(d.pop("questions"))

        def _parse_steps(data: object) -> list[SetupStep] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                steps_type_0 = []
                _steps_type_0 = data
                for steps_type_0_item_data in _steps_type_0:
                    steps_type_0_item = SetupStep.from_dict(steps_type_0_item_data)

                    steps_type_0.append(steps_type_0_item)

                return steps_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SetupStep] | None, data)

        steps = _parse_steps(d.pop("steps"))

        schema = d.pop("$schema", UNSET)

        workflow_setup_guide = cls(
            boundaries=boundaries,
            compiler_version=compiler_version,
            example=example,
            purpose=purpose,
            questions=questions,
            steps=steps,
            schema=schema,
        )

        return workflow_setup_guide
