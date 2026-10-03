from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_activation import ActivityActivation


T = TypeVar("T", bound="ActivityFunnel")


@_attrs_define
class ActivityFunnel:
    """
    Attributes:
        entity (str):
        name (str):
        stages (list[str] | None): Ordered stages; a|b means either stage, for methods that reach the same point
            differently
        activation (ActivityActivation | Unset):
        error_key (str | Unset): Attribute key holding the failure category
        failure (str | Unset): State that marks a failed attempt; it supersedes stages reached before it, not later ones
        linked_to (str | Unset): Entity type: attempts linked to one count as linked, the rest as unlinked
        split_by (str | Unset): Attribute key to split the funnel by
    """

    entity: str
    name: str
    stages: list[str] | None
    activation: ActivityActivation | Unset = UNSET
    error_key: str | Unset = UNSET
    failure: str | Unset = UNSET
    linked_to: str | Unset = UNSET
    split_by: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_activation import ActivityActivation

        entity = self.entity

        name = self.name

        stages: list[str] | None
        if isinstance(self.stages, list):
            stages = self.stages

        else:
            stages = self.stages

        activation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.activation, Unset):
            activation = self.activation.to_dict()

        error_key = self.error_key

        failure = self.failure

        linked_to = self.linked_to

        split_by = self.split_by

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "entity": entity,
                "name": name,
                "stages": stages,
            }
        )
        if activation is not UNSET:
            field_dict["activation"] = activation
        if error_key is not UNSET:
            field_dict["errorKey"] = error_key
        if failure is not UNSET:
            field_dict["failure"] = failure
        if linked_to is not UNSET:
            field_dict["linkedTo"] = linked_to
        if split_by is not UNSET:
            field_dict["splitBy"] = split_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_activation import ActivityActivation

        d = dict(src_dict)
        entity = d.pop("entity")

        name = d.pop("name")

        def _parse_stages(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                stages_type_0 = cast(list[str], data)

                return stages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        stages = _parse_stages(d.pop("stages"))

        _activation = d.pop("activation", UNSET)
        activation: ActivityActivation | Unset
        if isinstance(_activation, Unset):
            activation = UNSET
        else:
            activation = ActivityActivation.from_dict(_activation)

        error_key = d.pop("errorKey", UNSET)

        failure = d.pop("failure", UNSET)

        linked_to = d.pop("linkedTo", UNSET)

        split_by = d.pop("splitBy", UNSET)

        activity_funnel = cls(
            entity=entity,
            name=name,
            stages=stages,
            activation=activation,
            error_key=error_key,
            failure=failure,
            linked_to=linked_to,
            split_by=split_by,
        )

        return activity_funnel
