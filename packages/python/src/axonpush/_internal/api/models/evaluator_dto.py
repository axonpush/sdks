from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.evaluator_kind import EvaluatorKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="EvaluatorDto")


@_attrs_define
class EvaluatorDto:
    """
    Attributes:
        created_at (datetime.datetime):
        evaluator_id (str):
        kind (EvaluatorKind):
        latest_version (float):
        name (str):
        org_id (str):
        updated_at (datetime.datetime):
    """

    created_at: datetime.datetime
    evaluator_id: str
    kind: EvaluatorKind
    latest_version: float
    name: str
    org_id: str
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        evaluator_id = self.evaluator_id

        kind = self.kind.value

        latest_version = self.latest_version

        name = self.name

        org_id = self.org_id

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "evaluatorId": evaluator_id,
                "kind": kind,
                "latestVersion": latest_version,
                "name": name,
                "orgId": org_id,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        evaluator_id = d.pop("evaluatorId")

        kind = EvaluatorKind(d.pop("kind"))

        latest_version = d.pop("latestVersion")

        name = d.pop("name")

        org_id = d.pop("orgId")

        updated_at = isoparse(d.pop("updatedAt"))

        evaluator_dto = cls(
            created_at=created_at,
            evaluator_id=evaluator_id,
            kind=kind,
            latest_version=latest_version,
            name=name,
            org_id=org_id,
            updated_at=updated_at,
        )

        evaluator_dto.additional_properties = d
        return evaluator_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
