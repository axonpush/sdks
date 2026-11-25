from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.created_organization_dto import CreatedOrganizationDTO


T = TypeVar("T", bound="CreateOrganizationOutputBody")


@_attrs_define
class CreateOrganizationOutputBody:
    """
    Attributes:
        organization (CreatedOrganizationDTO):
        payment_required (bool): True when the organisation is beyond the free allowance and must be activated with a
            paid plan before it ingests
        schema (str | Unset): A URL to the JSON Schema for this object.
        hint (str | Unset):
    """

    organization: CreatedOrganizationDTO
    payment_required: bool
    schema: str | Unset = UNSET
    hint: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.created_organization_dto import CreatedOrganizationDTO

        organization = self.organization.to_dict()

        payment_required = self.payment_required

        schema = self.schema

        hint = self.hint

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "organization": organization,
                "paymentRequired": payment_required,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if hint is not UNSET:
            field_dict["hint"] = hint

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.created_organization_dto import CreatedOrganizationDTO

        d = dict(src_dict)
        organization = CreatedOrganizationDTO.from_dict(d.pop("organization"))

        payment_required = d.pop("paymentRequired")

        schema = d.pop("$schema", UNSET)

        hint = d.pop("hint", UNSET)

        create_organization_output_body = cls(
            organization=organization,
            payment_required=payment_required,
            schema=schema,
            hint=hint,
        )

        return create_organization_output_body
