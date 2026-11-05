from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LedgerStorageTier")


@_attrs_define
class LedgerStorageTier:
    """
    Attributes:
        bytes_stored (int):
        objects (int):
        storage_class (str):
        estimated_monthly_cost (float | Unset):
        price_per_gb_month (float | Unset):
    """

    bytes_stored: int
    objects: int
    storage_class: str
    estimated_monthly_cost: float | Unset = UNSET
    price_per_gb_month: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        bytes_stored = self.bytes_stored

        objects = self.objects

        storage_class = self.storage_class

        estimated_monthly_cost = self.estimated_monthly_cost

        price_per_gb_month = self.price_per_gb_month

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "bytesStored": bytes_stored,
                "objects": objects,
                "storageClass": storage_class,
            }
        )
        if estimated_monthly_cost is not UNSET:
            field_dict["estimatedMonthlyCost"] = estimated_monthly_cost
        if price_per_gb_month is not UNSET:
            field_dict["pricePerGBMonth"] = price_per_gb_month

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bytes_stored = d.pop("bytesStored")

        objects = d.pop("objects")

        storage_class = d.pop("storageClass")

        estimated_monthly_cost = d.pop("estimatedMonthlyCost", UNSET)

        price_per_gb_month = d.pop("pricePerGBMonth", UNSET)

        ledger_storage_tier = cls(
            bytes_stored=bytes_stored,
            objects=objects,
            storage_class=storage_class,
            estimated_monthly_cost=estimated_monthly_cost,
            price_per_gb_month=price_per_gb_month,
        )

        return ledger_storage_tier
