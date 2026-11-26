from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.heatmap_band_dto import HeatmapBandDTO
    from ..models.heatmap_cell_dto import HeatmapCellDTO


T = TypeVar("T", bound="HeatmapOutputBody")


@_attrs_define
class HeatmapOutputBody:
    """
    Attributes:
        bucket (str):
        cells (list[HeatmapCellDTO] | None):
        duration_bands (list[HeatmapBandDTO] | None):
        max_duration_ms (float):
        min_duration_ms (float):
        sample_count (int):
        scale (str):
        time_buckets (list[str] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    bucket: str
    cells: list[HeatmapCellDTO] | None
    duration_bands: list[HeatmapBandDTO] | None
    max_duration_ms: float
    min_duration_ms: float
    sample_count: int
    scale: str
    time_buckets: list[str] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.heatmap_band_dto import HeatmapBandDTO
        from ..models.heatmap_cell_dto import HeatmapCellDTO

        bucket = self.bucket

        cells: list[dict[str, Any]] | None
        if isinstance(self.cells, list):
            cells = []
            for cells_type_0_item_data in self.cells:
                cells_type_0_item = cells_type_0_item_data.to_dict()
                cells.append(cells_type_0_item)

        else:
            cells = self.cells

        duration_bands: list[dict[str, Any]] | None
        if isinstance(self.duration_bands, list):
            duration_bands = []
            for duration_bands_type_0_item_data in self.duration_bands:
                duration_bands_type_0_item = duration_bands_type_0_item_data.to_dict()
                duration_bands.append(duration_bands_type_0_item)

        else:
            duration_bands = self.duration_bands

        max_duration_ms = self.max_duration_ms

        min_duration_ms = self.min_duration_ms

        sample_count = self.sample_count

        scale = self.scale

        time_buckets: list[str] | None
        if isinstance(self.time_buckets, list):
            time_buckets = self.time_buckets

        else:
            time_buckets = self.time_buckets

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "bucket": bucket,
                "cells": cells,
                "durationBands": duration_bands,
                "maxDurationMs": max_duration_ms,
                "minDurationMs": min_duration_ms,
                "sampleCount": sample_count,
                "scale": scale,
                "timeBuckets": time_buckets,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.heatmap_band_dto import HeatmapBandDTO
        from ..models.heatmap_cell_dto import HeatmapCellDTO

        d = dict(src_dict)
        bucket = d.pop("bucket")

        def _parse_cells(data: object) -> list[HeatmapCellDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cells_type_0 = []
                _cells_type_0 = data
                for cells_type_0_item_data in _cells_type_0:
                    cells_type_0_item = HeatmapCellDTO.from_dict(cells_type_0_item_data)

                    cells_type_0.append(cells_type_0_item)

                return cells_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HeatmapCellDTO] | None, data)

        cells = _parse_cells(d.pop("cells"))

        def _parse_duration_bands(data: object) -> list[HeatmapBandDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                duration_bands_type_0 = []
                _duration_bands_type_0 = data
                for duration_bands_type_0_item_data in _duration_bands_type_0:
                    duration_bands_type_0_item = HeatmapBandDTO.from_dict(
                        duration_bands_type_0_item_data
                    )

                    duration_bands_type_0.append(duration_bands_type_0_item)

                return duration_bands_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HeatmapBandDTO] | None, data)

        duration_bands = _parse_duration_bands(d.pop("durationBands"))

        max_duration_ms = d.pop("maxDurationMs")

        min_duration_ms = d.pop("minDurationMs")

        sample_count = d.pop("sampleCount")

        scale = d.pop("scale")

        def _parse_time_buckets(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                time_buckets_type_0 = cast(list[str], data)

                return time_buckets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        time_buckets = _parse_time_buckets(d.pop("timeBuckets"))

        schema = d.pop("$schema", UNSET)

        heatmap_output_body = cls(
            bucket=bucket,
            cells=cells,
            duration_bands=duration_bands,
            max_duration_ms=max_duration_ms,
            min_duration_ms=min_duration_ms,
            sample_count=sample_count,
            scale=scale,
            time_buckets=time_buckets,
            schema=schema,
        )

        return heatmap_output_body
