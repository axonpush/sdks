from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ledger_storage_tier import LedgerStorageTier


T = TypeVar("T", bound="StorageOutputBody")


@_attrs_define
class StorageOutputBody:
    """
    Attributes:
        as_of (datetime.datetime):
        complete (bool):
        coverage (str):
        estimated (bool):
        gigabyte_bytes (int):
        governance_lift_available (bool):
        pricing_available (bool):
        region (str):
        scanned (int):
        source (str):
        tiers (list[LedgerStorageTier] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
        currency (str | Unset):
        next_cursor (str | Unset):
        price_source (str | Unset):
        prices_as_of (datetime.datetime | Unset):
    """

    as_of: datetime.datetime
    complete: bool
    coverage: str
    estimated: bool
    gigabyte_bytes: int
    governance_lift_available: bool
    pricing_available: bool
    region: str
    scanned: int
    source: str
    tiers: list[LedgerStorageTier] | None
    schema: str | Unset = UNSET
    currency: str | Unset = UNSET
    next_cursor: str | Unset = UNSET
    price_source: str | Unset = UNSET
    prices_as_of: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.ledger_storage_tier import LedgerStorageTier

        as_of = self.as_of.isoformat()

        complete = self.complete

        coverage = self.coverage

        estimated = self.estimated

        gigabyte_bytes = self.gigabyte_bytes

        governance_lift_available = self.governance_lift_available

        pricing_available = self.pricing_available

        region = self.region

        scanned = self.scanned

        source = self.source

        tiers: list[dict[str, Any]] | None
        if isinstance(self.tiers, list):
            tiers = []
            for tiers_type_0_item_data in self.tiers:
                tiers_type_0_item = tiers_type_0_item_data.to_dict()
                tiers.append(tiers_type_0_item)

        else:
            tiers = self.tiers

        schema = self.schema

        currency = self.currency

        next_cursor = self.next_cursor

        price_source = self.price_source

        prices_as_of: str | Unset = UNSET
        if not isinstance(self.prices_as_of, Unset):
            prices_as_of = self.prices_as_of.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "asOf": as_of,
                "complete": complete,
                "coverage": coverage,
                "estimated": estimated,
                "gigabyteBytes": gigabyte_bytes,
                "governanceLiftAvailable": governance_lift_available,
                "pricingAvailable": pricing_available,
                "region": region,
                "scanned": scanned,
                "source": source,
                "tiers": tiers,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if currency is not UNSET:
            field_dict["currency"] = currency
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor
        if price_source is not UNSET:
            field_dict["priceSource"] = price_source
        if prices_as_of is not UNSET:
            field_dict["pricesAsOf"] = prices_as_of

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ledger_storage_tier import LedgerStorageTier

        d = dict(src_dict)
        as_of = isoparse(d.pop("asOf"))

        complete = d.pop("complete")

        coverage = d.pop("coverage")

        estimated = d.pop("estimated")

        gigabyte_bytes = d.pop("gigabyteBytes")

        governance_lift_available = d.pop("governanceLiftAvailable")

        pricing_available = d.pop("pricingAvailable")

        region = d.pop("region")

        scanned = d.pop("scanned")

        source = d.pop("source")

        def _parse_tiers(data: object) -> list[LedgerStorageTier] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tiers_type_0 = []
                _tiers_type_0 = data
                for tiers_type_0_item_data in _tiers_type_0:
                    tiers_type_0_item = LedgerStorageTier.from_dict(tiers_type_0_item_data)

                    tiers_type_0.append(tiers_type_0_item)

                return tiers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LedgerStorageTier] | None, data)

        tiers = _parse_tiers(d.pop("tiers"))

        schema = d.pop("$schema", UNSET)

        currency = d.pop("currency", UNSET)

        next_cursor = d.pop("nextCursor", UNSET)

        price_source = d.pop("priceSource", UNSET)

        _prices_as_of = d.pop("pricesAsOf", UNSET)
        prices_as_of: datetime.datetime | Unset
        if isinstance(_prices_as_of, Unset):
            prices_as_of = UNSET
        else:
            prices_as_of = isoparse(_prices_as_of)

        storage_output_body = cls(
            as_of=as_of,
            complete=complete,
            coverage=coverage,
            estimated=estimated,
            gigabyte_bytes=gigabyte_bytes,
            governance_lift_available=governance_lift_available,
            pricing_available=pricing_available,
            region=region,
            scanned=scanned,
            source=source,
            tiers=tiers,
            schema=schema,
            currency=currency,
            next_cursor=next_cursor,
            price_source=price_source,
            prices_as_of=prices_as_of,
        )

        return storage_output_body
