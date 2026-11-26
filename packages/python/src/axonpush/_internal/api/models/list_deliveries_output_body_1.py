from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.export_delivery_dto import ExportDeliveryDTO


T = TypeVar("T", bound="ListDeliveriesOutputBody1")


@_attrs_define
class ListDeliveriesOutputBody1:
    """
    Attributes:
        deliveries (list[ExportDeliveryDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    deliveries: list[ExportDeliveryDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.export_delivery_dto import ExportDeliveryDTO

        deliveries: list[dict[str, Any]] | None
        if isinstance(self.deliveries, list):
            deliveries = []
            for deliveries_type_0_item_data in self.deliveries:
                deliveries_type_0_item = deliveries_type_0_item_data.to_dict()
                deliveries.append(deliveries_type_0_item)

        else:
            deliveries = self.deliveries

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "deliveries": deliveries,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.export_delivery_dto import ExportDeliveryDTO

        d = dict(src_dict)

        def _parse_deliveries(data: object) -> list[ExportDeliveryDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                deliveries_type_0 = []
                _deliveries_type_0 = data
                for deliveries_type_0_item_data in _deliveries_type_0:
                    deliveries_type_0_item = ExportDeliveryDTO.from_dict(
                        deliveries_type_0_item_data
                    )

                    deliveries_type_0.append(deliveries_type_0_item)

                return deliveries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ExportDeliveryDTO] | None, data)

        deliveries = _parse_deliveries(d.pop("deliveries"))

        schema = d.pop("$schema", UNSET)

        list_deliveries_output_body_1 = cls(
            deliveries=deliveries,
            schema=schema,
        )

        return list_deliveries_output_body_1
