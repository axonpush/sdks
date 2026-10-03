from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_graph_edge import ActivityGraphEdge
    from ..models.activity_graph_node import ActivityGraphNode


T = TypeVar("T", bound="ActivityGraphResult")


@_attrs_define
class ActivityGraphResult:
    """
    Attributes:
        edges (list[ActivityGraphEdge] | None):
        nodes (list[ActivityGraphNode] | None):
        truncated (bool): More entities matched than the view's limit
    """

    edges: list[ActivityGraphEdge] | None
    nodes: list[ActivityGraphNode] | None
    truncated: bool

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_graph_edge import ActivityGraphEdge
        from ..models.activity_graph_node import ActivityGraphNode

        edges: list[dict[str, Any]] | None
        if isinstance(self.edges, list):
            edges = []
            for edges_type_0_item_data in self.edges:
                edges_type_0_item = edges_type_0_item_data.to_dict()
                edges.append(edges_type_0_item)

        else:
            edges = self.edges

        nodes: list[dict[str, Any]] | None
        if isinstance(self.nodes, list):
            nodes = []
            for nodes_type_0_item_data in self.nodes:
                nodes_type_0_item = nodes_type_0_item_data.to_dict()
                nodes.append(nodes_type_0_item)

        else:
            nodes = self.nodes

        truncated = self.truncated

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "edges": edges,
                "nodes": nodes,
                "truncated": truncated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_graph_edge import ActivityGraphEdge
        from ..models.activity_graph_node import ActivityGraphNode

        d = dict(src_dict)

        def _parse_edges(data: object) -> list[ActivityGraphEdge] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                edges_type_0 = []
                _edges_type_0 = data
                for edges_type_0_item_data in _edges_type_0:
                    edges_type_0_item = ActivityGraphEdge.from_dict(edges_type_0_item_data)

                    edges_type_0.append(edges_type_0_item)

                return edges_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityGraphEdge] | None, data)

        edges = _parse_edges(d.pop("edges"))

        def _parse_nodes(data: object) -> list[ActivityGraphNode] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                nodes_type_0 = []
                _nodes_type_0 = data
                for nodes_type_0_item_data in _nodes_type_0:
                    nodes_type_0_item = ActivityGraphNode.from_dict(nodes_type_0_item_data)

                    nodes_type_0.append(nodes_type_0_item)

                return nodes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityGraphNode] | None, data)

        nodes = _parse_nodes(d.pop("nodes"))

        truncated = d.pop("truncated")

        activity_graph_result = cls(
            edges=edges,
            nodes=nodes,
            truncated=truncated,
        )

        return activity_graph_result
