from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.action_spec_expected import ActionSpecExpected
    from ..models.action_spec_inputs import ActionSpecInputs
    from ..models.action_spec_outputs import ActionSpecOutputs
    from ..models.review_unless import ReviewUnless


T = TypeVar("T", bound="ActionSpec")


@_attrs_define
class ActionSpec:
    """
    Attributes:
        actors (list[str] | None):
        expected (ActionSpecExpected):
        from_ (str):
        handler (str):
        inputs (ActionSpecInputs):
        outputs (ActionSpecOutputs):
        requirement (str):
        to (str):
        always_review (bool | Unset):
        review_unless (list[ReviewUnless] | None | Unset):
    """

    actors: list[str] | None
    expected: ActionSpecExpected
    from_: str
    handler: str
    inputs: ActionSpecInputs
    outputs: ActionSpecOutputs
    requirement: str
    to: str
    always_review: bool | Unset = UNSET
    review_unless: list[ReviewUnless] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.action_spec_expected import ActionSpecExpected
        from ..models.action_spec_inputs import ActionSpecInputs
        from ..models.action_spec_outputs import ActionSpecOutputs
        from ..models.review_unless import ReviewUnless

        actors: list[str] | None
        if isinstance(self.actors, list):
            actors = self.actors

        else:
            actors = self.actors

        expected = self.expected.to_dict()

        from_ = self.from_

        handler = self.handler

        inputs = self.inputs.to_dict()

        outputs = self.outputs.to_dict()

        requirement = self.requirement

        to = self.to

        always_review = self.always_review

        review_unless: list[dict[str, Any]] | None | Unset
        if isinstance(self.review_unless, Unset):
            review_unless = UNSET
        elif isinstance(self.review_unless, list):
            review_unless = []
            for review_unless_type_0_item_data in self.review_unless:
                review_unless_type_0_item = review_unless_type_0_item_data.to_dict()
                review_unless.append(review_unless_type_0_item)

        else:
            review_unless = self.review_unless

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "actors": actors,
                "expected": expected,
                "from": from_,
                "handler": handler,
                "inputs": inputs,
                "outputs": outputs,
                "requirement": requirement,
                "to": to,
            }
        )
        if always_review is not UNSET:
            field_dict["always_review"] = always_review
        if review_unless is not UNSET:
            field_dict["review_unless"] = review_unless

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_spec_expected import ActionSpecExpected
        from ..models.action_spec_inputs import ActionSpecInputs
        from ..models.action_spec_outputs import ActionSpecOutputs
        from ..models.review_unless import ReviewUnless

        d = dict(src_dict)

        def _parse_actors(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                actors_type_0 = cast(list[str], data)

                return actors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        actors = _parse_actors(d.pop("actors"))

        expected = ActionSpecExpected.from_dict(d.pop("expected"))

        from_ = d.pop("from")

        handler = d.pop("handler")

        inputs = ActionSpecInputs.from_dict(d.pop("inputs"))

        outputs = ActionSpecOutputs.from_dict(d.pop("outputs"))

        requirement = d.pop("requirement")

        to = d.pop("to")

        always_review = d.pop("always_review", UNSET)

        def _parse_review_unless(data: object) -> list[ReviewUnless] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                review_unless_type_0 = []
                _review_unless_type_0 = data
                for review_unless_type_0_item_data in _review_unless_type_0:
                    review_unless_type_0_item = ReviewUnless.from_dict(
                        review_unless_type_0_item_data
                    )

                    review_unless_type_0.append(review_unless_type_0_item)

                return review_unless_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ReviewUnless] | None | Unset, data)

        review_unless = _parse_review_unless(d.pop("review_unless", UNSET))

        action_spec = cls(
            actors=actors,
            expected=expected,
            from_=from_,
            handler=handler,
            inputs=inputs,
            outputs=outputs,
            requirement=requirement,
            to=to,
            always_review=always_review,
            review_unless=review_unless,
        )

        return action_spec
