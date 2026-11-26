from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_edge_evidence import ActivityEdgeEvidence


T = TypeVar("T", bound="ActivityGraphEdge")


@_attrs_define
class ActivityGraphEdge:
    """
    Attributes:
        evidence (ActivityEdgeEvidence):
        from_ (str): type:id of the entity holding the reference
        to (str): type:id it references
    """

    evidence: ActivityEdgeEvidence
    from_: str
    to: str

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_edge_evidence import ActivityEdgeEvidence

        evidence = self.evidence.to_dict()

        from_ = self.from_

        to = self.to

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "evidence": evidence,
                "from": from_,
                "to": to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_edge_evidence import ActivityEdgeEvidence

        d = dict(src_dict)
        evidence = ActivityEdgeEvidence.from_dict(d.pop("evidence"))

        from_ = d.pop("from")

        to = d.pop("to")

        activity_graph_edge = cls(
            evidence=evidence,
            from_=from_,
            to=to,
        )

        return activity_graph_edge
