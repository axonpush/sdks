from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetBillingInputBody")


@_attrs_define
class SetBillingInputBody:
    """
    Attributes:
        billing_monthly_amount_usd (float): Negotiated monthly amount in USD
        schema (str | Unset): A URL to the JSON Schema for this object.
        billing_notes (str | Unset): Free-form commercial notes
    """

    billing_monthly_amount_usd: float
    schema: str | Unset = UNSET
    billing_notes: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        billing_monthly_amount_usd = self.billing_monthly_amount_usd

        schema = self.schema

        billing_notes = self.billing_notes

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "billingMonthlyAmountUsd": billing_monthly_amount_usd,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if billing_notes is not UNSET:
            field_dict["billingNotes"] = billing_notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        billing_monthly_amount_usd = d.pop("billingMonthlyAmountUsd")

        schema = d.pop("$schema", UNSET)

        billing_notes = d.pop("billingNotes", UNSET)

        set_billing_input_body = cls(
            billing_monthly_amount_usd=billing_monthly_amount_usd,
            schema=schema,
            billing_notes=billing_notes,
        )

        return set_billing_input_body
