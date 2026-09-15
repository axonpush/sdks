from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access_request_dto import AccessRequestDTO


T = TypeVar("T", bound="ListAccessRequestsOutputBody")


@_attrs_define
class ListAccessRequestsOutputBody:
    """
    Attributes:
        requests (list[AccessRequestDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    requests: list[AccessRequestDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.access_request_dto import AccessRequestDTO

        requests: list[dict[str, Any]] | None
        if isinstance(self.requests, list):
            requests = []
            for requests_type_0_item_data in self.requests:
                requests_type_0_item = requests_type_0_item_data.to_dict()
                requests.append(requests_type_0_item)

        else:
            requests = self.requests

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "requests": requests,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.access_request_dto import AccessRequestDTO

        d = dict(src_dict)

        def _parse_requests(data: object) -> list[AccessRequestDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                requests_type_0 = []
                _requests_type_0 = data
                for requests_type_0_item_data in _requests_type_0:
                    requests_type_0_item = AccessRequestDTO.from_dict(requests_type_0_item_data)

                    requests_type_0.append(requests_type_0_item)

                return requests_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AccessRequestDTO] | None, data)

        requests = _parse_requests(d.pop("requests"))

        schema = d.pop("$schema", UNSET)

        list_access_requests_output_body = cls(
            requests=requests,
            schema=schema,
        )

        return list_access_requests_output_body
