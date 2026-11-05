from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compliance_metrics import ComplianceMetrics
    from ..models.compliance_overview_attention_type_0_item import (
        ComplianceOverviewAttentionType0Item,
    )
    from ..models.compliance_overview_counts import ComplianceOverviewCounts
    from ..models.compliance_overview_integrity import ComplianceOverviewIntegrity


T = TypeVar("T", bound="ComplianceOverview")


@_attrs_define
class ComplianceOverview:
    """
    Attributes:
        attention (list[ComplianceOverviewAttentionType0Item] | None):
        counts (ComplianceOverviewCounts):
        evidence_disclaimer (str):
        integrity (ComplianceOverviewIntegrity):
        metrics (ComplianceMetrics):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    attention: list[ComplianceOverviewAttentionType0Item] | None
    counts: ComplianceOverviewCounts
    evidence_disclaimer: str
    integrity: ComplianceOverviewIntegrity
    metrics: ComplianceMetrics
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.compliance_metrics import ComplianceMetrics
        from ..models.compliance_overview_attention_type_0_item import (
            ComplianceOverviewAttentionType0Item,
        )
        from ..models.compliance_overview_counts import ComplianceOverviewCounts
        from ..models.compliance_overview_integrity import ComplianceOverviewIntegrity

        attention: list[dict[str, Any]] | None
        if isinstance(self.attention, list):
            attention = []
            for attention_type_0_item_data in self.attention:
                attention_type_0_item = attention_type_0_item_data.to_dict()
                attention.append(attention_type_0_item)

        else:
            attention = self.attention

        counts = self.counts.to_dict()

        evidence_disclaimer = self.evidence_disclaimer

        integrity = self.integrity.to_dict()

        metrics = self.metrics.to_dict()

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attention": attention,
                "counts": counts,
                "evidenceDisclaimer": evidence_disclaimer,
                "integrity": integrity,
                "metrics": metrics,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compliance_metrics import ComplianceMetrics
        from ..models.compliance_overview_attention_type_0_item import (
            ComplianceOverviewAttentionType0Item,
        )
        from ..models.compliance_overview_counts import ComplianceOverviewCounts
        from ..models.compliance_overview_integrity import ComplianceOverviewIntegrity

        d = dict(src_dict)

        def _parse_attention(data: object) -> list[ComplianceOverviewAttentionType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attention_type_0 = []
                _attention_type_0 = data
                for attention_type_0_item_data in _attention_type_0:
                    attention_type_0_item = ComplianceOverviewAttentionType0Item.from_dict(
                        attention_type_0_item_data
                    )

                    attention_type_0.append(attention_type_0_item)

                return attention_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ComplianceOverviewAttentionType0Item] | None, data)

        attention = _parse_attention(d.pop("attention"))

        counts = ComplianceOverviewCounts.from_dict(d.pop("counts"))

        evidence_disclaimer = d.pop("evidenceDisclaimer")

        integrity = ComplianceOverviewIntegrity.from_dict(d.pop("integrity"))

        metrics = ComplianceMetrics.from_dict(d.pop("metrics"))

        schema = d.pop("$schema", UNSET)

        compliance_overview = cls(
            attention=attention,
            counts=counts,
            evidence_disclaimer=evidence_disclaimer,
            integrity=integrity,
            metrics=metrics,
            schema=schema,
        )

        return compliance_overview
