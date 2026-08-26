from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trace_flow_status import TraceFlowStatus
from ..models.trace_signal_kind import TraceSignalKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trace_intelligence_coverage_response_dto import (
        TraceIntelligenceCoverageResponseDto,
    )
    from ..models.trace_intelligence_flow_link_response_dto import (
        TraceIntelligenceFlowLinkResponseDto,
    )
    from ..models.trace_intelligence_flow_node_response_dto import (
        TraceIntelligenceFlowNodeResponseDto,
    )
    from ..models.trace_intelligence_flow_response_dto_algorithm import (
        TraceIntelligenceFlowResponseDtoAlgorithm,
    )
    from ..models.trace_intelligence_flow_response_dto_trends_item import (
        TraceIntelligenceFlowResponseDtoTrendsItem,
    )
    from ..models.trace_intelligence_snapshot_response_dto import (
        TraceIntelligenceSnapshotResponseDto,
    )
    from ..models.trace_intelligence_top_path_response_dto import (
        TraceIntelligenceTopPathResponseDto,
    )


T = TypeVar("T", bound="TraceIntelligenceFlowResponseDto")


@_attrs_define
class TraceIntelligenceFlowResponseDto:
    """
    Attributes:
        columns (list[TraceSignalKind]):
        coverage (TraceIntelligenceCoverageResponseDto):
        links (list[TraceIntelligenceFlowLinkResponseDto]):
        nodes (list[TraceIntelligenceFlowNodeResponseDto]):
        status (TraceFlowStatus):
        top_paths (list[TraceIntelligenceTopPathResponseDto]):
        trends (list[TraceIntelligenceFlowResponseDtoTrendsItem]):
        algorithm (TraceIntelligenceFlowResponseDtoAlgorithm | Unset):
        snapshot (TraceIntelligenceSnapshotResponseDto | Unset):
    """

    columns: list[TraceSignalKind]
    coverage: TraceIntelligenceCoverageResponseDto
    links: list[TraceIntelligenceFlowLinkResponseDto]
    nodes: list[TraceIntelligenceFlowNodeResponseDto]
    status: TraceFlowStatus
    top_paths: list[TraceIntelligenceTopPathResponseDto]
    trends: list[TraceIntelligenceFlowResponseDtoTrendsItem]
    algorithm: TraceIntelligenceFlowResponseDtoAlgorithm | Unset = UNSET
    snapshot: TraceIntelligenceSnapshotResponseDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.trace_intelligence_coverage_response_dto import (
            TraceIntelligenceCoverageResponseDto,
        )
        from ..models.trace_intelligence_flow_link_response_dto import (
            TraceIntelligenceFlowLinkResponseDto,
        )
        from ..models.trace_intelligence_flow_node_response_dto import (
            TraceIntelligenceFlowNodeResponseDto,
        )
        from ..models.trace_intelligence_flow_response_dto_algorithm import (
            TraceIntelligenceFlowResponseDtoAlgorithm,
        )
        from ..models.trace_intelligence_flow_response_dto_trends_item import (
            TraceIntelligenceFlowResponseDtoTrendsItem,
        )
        from ..models.trace_intelligence_snapshot_response_dto import (
            TraceIntelligenceSnapshotResponseDto,
        )
        from ..models.trace_intelligence_top_path_response_dto import (
            TraceIntelligenceTopPathResponseDto,
        )

        columns = []
        for columns_item_data in self.columns:
            columns_item = columns_item_data.value
            columns.append(columns_item)

        coverage = self.coverage.to_dict()

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        nodes = []
        for nodes_item_data in self.nodes:
            nodes_item = nodes_item_data.to_dict()
            nodes.append(nodes_item)

        status = self.status.value

        top_paths = []
        for top_paths_item_data in self.top_paths:
            top_paths_item = top_paths_item_data.to_dict()
            top_paths.append(top_paths_item)

        trends = []
        for trends_item_data in self.trends:
            trends_item = trends_item_data.to_dict()
            trends.append(trends_item)

        algorithm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.algorithm, Unset):
            algorithm = self.algorithm.to_dict()

        snapshot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snapshot, Unset):
            snapshot = self.snapshot.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "columns": columns,
                "coverage": coverage,
                "links": links,
                "nodes": nodes,
                "status": status,
                "topPaths": top_paths,
                "trends": trends,
            }
        )
        if algorithm is not UNSET:
            field_dict["algorithm"] = algorithm
        if snapshot is not UNSET:
            field_dict["snapshot"] = snapshot

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trace_intelligence_coverage_response_dto import (
            TraceIntelligenceCoverageResponseDto,
        )
        from ..models.trace_intelligence_flow_link_response_dto import (
            TraceIntelligenceFlowLinkResponseDto,
        )
        from ..models.trace_intelligence_flow_node_response_dto import (
            TraceIntelligenceFlowNodeResponseDto,
        )
        from ..models.trace_intelligence_flow_response_dto_algorithm import (
            TraceIntelligenceFlowResponseDtoAlgorithm,
        )
        from ..models.trace_intelligence_flow_response_dto_trends_item import (
            TraceIntelligenceFlowResponseDtoTrendsItem,
        )
        from ..models.trace_intelligence_snapshot_response_dto import (
            TraceIntelligenceSnapshotResponseDto,
        )
        from ..models.trace_intelligence_top_path_response_dto import (
            TraceIntelligenceTopPathResponseDto,
        )

        d = dict(src_dict)
        columns = []
        _columns = d.pop("columns")
        for columns_item_data in _columns:
            columns_item = TraceSignalKind(columns_item_data)

            columns.append(columns_item)

        coverage = TraceIntelligenceCoverageResponseDto.from_dict(d.pop("coverage"))

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = TraceIntelligenceFlowLinkResponseDto.from_dict(links_item_data)

            links.append(links_item)

        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in _nodes:
            nodes_item = TraceIntelligenceFlowNodeResponseDto.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        status = TraceFlowStatus(d.pop("status"))

        top_paths = []
        _top_paths = d.pop("topPaths")
        for top_paths_item_data in _top_paths:
            top_paths_item = TraceIntelligenceTopPathResponseDto.from_dict(top_paths_item_data)

            top_paths.append(top_paths_item)

        trends = []
        _trends = d.pop("trends")
        for trends_item_data in _trends:
            trends_item = TraceIntelligenceFlowResponseDtoTrendsItem.from_dict(trends_item_data)

            trends.append(trends_item)

        _algorithm = d.pop("algorithm", UNSET)
        algorithm: TraceIntelligenceFlowResponseDtoAlgorithm | Unset
        if isinstance(_algorithm, Unset):
            algorithm = UNSET
        else:
            algorithm = TraceIntelligenceFlowResponseDtoAlgorithm.from_dict(_algorithm)

        _snapshot = d.pop("snapshot", UNSET)
        snapshot: TraceIntelligenceSnapshotResponseDto | Unset
        if isinstance(_snapshot, Unset):
            snapshot = UNSET
        else:
            snapshot = TraceIntelligenceSnapshotResponseDto.from_dict(_snapshot)

        trace_intelligence_flow_response_dto = cls(
            columns=columns,
            coverage=coverage,
            links=links,
            nodes=nodes,
            status=status,
            top_paths=top_paths,
            trends=trends,
            algorithm=algorithm,
            snapshot=snapshot,
        )

        trace_intelligence_flow_response_dto.additional_properties = d
        return trace_intelligence_flow_response_dto

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
