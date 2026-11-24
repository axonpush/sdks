from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_check_in_dto import MonitorCheckInDTO


T = TypeVar("T", bound="ListMonitorCheckInsOutputBody")


@_attrs_define
class ListMonitorCheckInsOutputBody:
    """
    Attributes:
        check_ins (list[MonitorCheckInDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
        next_before (str | Unset): Pass as before to load the next (older) page
    """

    check_ins: list[MonitorCheckInDTO] | None
    schema: str | Unset = UNSET
    next_before: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.monitor_check_in_dto import MonitorCheckInDTO

        check_ins: list[dict[str, Any]] | None
        if isinstance(self.check_ins, list):
            check_ins = []
            for check_ins_type_0_item_data in self.check_ins:
                check_ins_type_0_item = check_ins_type_0_item_data.to_dict()
                check_ins.append(check_ins_type_0_item)

        else:
            check_ins = self.check_ins

        schema = self.schema

        next_before = self.next_before

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "checkIns": check_ins,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if next_before is not UNSET:
            field_dict["nextBefore"] = next_before

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_check_in_dto import MonitorCheckInDTO

        d = dict(src_dict)

        def _parse_check_ins(data: object) -> list[MonitorCheckInDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                check_ins_type_0 = []
                _check_ins_type_0 = data
                for check_ins_type_0_item_data in _check_ins_type_0:
                    check_ins_type_0_item = MonitorCheckInDTO.from_dict(
                        check_ins_type_0_item_data
                    )

                    check_ins_type_0.append(check_ins_type_0_item)

                return check_ins_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MonitorCheckInDTO] | None, data)

        check_ins = _parse_check_ins(d.pop("checkIns"))

        schema = d.pop("$schema", UNSET)

        next_before = d.pop("nextBefore", UNSET)

        list_monitor_check_ins_output_body = cls(
            check_ins=check_ins,
            schema=schema,
            next_before=next_before,
        )

        return list_monitor_check_ins_output_body
