from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.trace_signal_kind import TraceSignalKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trace_intelligence_cluster_response_dto_lineage import (
        TraceIntelligenceClusterResponseDtoLineage,
    )
    from ..models.trace_intelligence_related_cluster_response_dto import (
        TraceIntelligenceRelatedClusterResponseDto,
    )


T = TypeVar("T", bound="TraceIntelligenceClusterResponseDto")


@_attrs_define
class TraceIntelligenceClusterResponseDto:
    """
    Attributes:
        app_id (str):
        cluster_id (str):
        description (str):
        environment_id (str):
        label (str):
        percentage (float):
        representative_trace_ids (list[str]):
        signal_kind (TraceSignalKind):
        snapshot_id (str):
        trace_count (float):
        updated_at (datetime.datetime):
        algorithm_version (str | Unset):
        confidence (float | Unset):
        downstream (list[TraceIntelligenceRelatedClusterResponseDto] | Unset):
        extraction_version (str | Unset):
        lineage (TraceIntelligenceClusterResponseDtoLineage | Unset):
        provider_model (str | Unset):
        trend (float | Unset):
        upstream (list[TraceIntelligenceRelatedClusterResponseDto] | Unset):
    """

    app_id: str
    cluster_id: str
    description: str
    environment_id: str
    label: str
    percentage: float
    representative_trace_ids: list[str]
    signal_kind: TraceSignalKind
    snapshot_id: str
    trace_count: float
    updated_at: datetime.datetime
    algorithm_version: str | Unset = UNSET
    confidence: float | Unset = UNSET
    downstream: list[TraceIntelligenceRelatedClusterResponseDto] | Unset = UNSET
    extraction_version: str | Unset = UNSET
    lineage: TraceIntelligenceClusterResponseDtoLineage | Unset = UNSET
    provider_model: str | Unset = UNSET
    trend: float | Unset = UNSET
    upstream: list[TraceIntelligenceRelatedClusterResponseDto] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.trace_intelligence_cluster_response_dto_lineage import (
            TraceIntelligenceClusterResponseDtoLineage,
        )
        from ..models.trace_intelligence_related_cluster_response_dto import (
            TraceIntelligenceRelatedClusterResponseDto,
        )

        app_id = self.app_id

        cluster_id = self.cluster_id

        description = self.description

        environment_id = self.environment_id

        label = self.label

        percentage = self.percentage

        representative_trace_ids = self.representative_trace_ids

        signal_kind = self.signal_kind.value

        snapshot_id = self.snapshot_id

        trace_count = self.trace_count

        updated_at = self.updated_at.isoformat()

        algorithm_version = self.algorithm_version

        confidence = self.confidence

        downstream: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.downstream, Unset):
            downstream = []
            for downstream_item_data in self.downstream:
                downstream_item = downstream_item_data.to_dict()
                downstream.append(downstream_item)

        extraction_version = self.extraction_version

        lineage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lineage, Unset):
            lineage = self.lineage.to_dict()

        provider_model = self.provider_model

        trend = self.trend

        upstream: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.upstream, Unset):
            upstream = []
            for upstream_item_data in self.upstream:
                upstream_item = upstream_item_data.to_dict()
                upstream.append(upstream_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "appId": app_id,
                "clusterId": cluster_id,
                "description": description,
                "environmentId": environment_id,
                "label": label,
                "percentage": percentage,
                "representativeTraceIds": representative_trace_ids,
                "signalKind": signal_kind,
                "snapshotId": snapshot_id,
                "traceCount": trace_count,
                "updatedAt": updated_at,
            }
        )
        if algorithm_version is not UNSET:
            field_dict["algorithmVersion"] = algorithm_version
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if downstream is not UNSET:
            field_dict["downstream"] = downstream
        if extraction_version is not UNSET:
            field_dict["extractionVersion"] = extraction_version
        if lineage is not UNSET:
            field_dict["lineage"] = lineage
        if provider_model is not UNSET:
            field_dict["providerModel"] = provider_model
        if trend is not UNSET:
            field_dict["trend"] = trend
        if upstream is not UNSET:
            field_dict["upstream"] = upstream

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trace_intelligence_cluster_response_dto_lineage import (
            TraceIntelligenceClusterResponseDtoLineage,
        )
        from ..models.trace_intelligence_related_cluster_response_dto import (
            TraceIntelligenceRelatedClusterResponseDto,
        )

        d = dict(src_dict)
        app_id = d.pop("appId")

        cluster_id = d.pop("clusterId")

        description = d.pop("description")

        environment_id = d.pop("environmentId")

        label = d.pop("label")

        percentage = d.pop("percentage")

        representative_trace_ids = cast(list[str], d.pop("representativeTraceIds"))

        signal_kind = TraceSignalKind(d.pop("signalKind"))

        snapshot_id = d.pop("snapshotId")

        trace_count = d.pop("traceCount")

        updated_at = isoparse(d.pop("updatedAt"))

        algorithm_version = d.pop("algorithmVersion", UNSET)

        confidence = d.pop("confidence", UNSET)

        _downstream = d.pop("downstream", UNSET)
        downstream: list[TraceIntelligenceRelatedClusterResponseDto] | Unset = UNSET
        if _downstream is not UNSET:
            downstream = []
            for downstream_item_data in _downstream:
                downstream_item = TraceIntelligenceRelatedClusterResponseDto.from_dict(
                    downstream_item_data
                )

                downstream.append(downstream_item)

        extraction_version = d.pop("extractionVersion", UNSET)

        _lineage = d.pop("lineage", UNSET)
        lineage: TraceIntelligenceClusterResponseDtoLineage | Unset
        if isinstance(_lineage, Unset):
            lineage = UNSET
        else:
            lineage = TraceIntelligenceClusterResponseDtoLineage.from_dict(_lineage)

        provider_model = d.pop("providerModel", UNSET)

        trend = d.pop("trend", UNSET)

        _upstream = d.pop("upstream", UNSET)
        upstream: list[TraceIntelligenceRelatedClusterResponseDto] | Unset = UNSET
        if _upstream is not UNSET:
            upstream = []
            for upstream_item_data in _upstream:
                upstream_item = TraceIntelligenceRelatedClusterResponseDto.from_dict(
                    upstream_item_data
                )

                upstream.append(upstream_item)

        trace_intelligence_cluster_response_dto = cls(
            app_id=app_id,
            cluster_id=cluster_id,
            description=description,
            environment_id=environment_id,
            label=label,
            percentage=percentage,
            representative_trace_ids=representative_trace_ids,
            signal_kind=signal_kind,
            snapshot_id=snapshot_id,
            trace_count=trace_count,
            updated_at=updated_at,
            algorithm_version=algorithm_version,
            confidence=confidence,
            downstream=downstream,
            extraction_version=extraction_version,
            lineage=lineage,
            provider_model=provider_model,
            trend=trend,
            upstream=upstream,
        )

        trace_intelligence_cluster_response_dto.additional_properties = d
        return trace_intelligence_cluster_response_dto

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
