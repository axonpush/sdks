from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_ingest_token_dto import PublicIngestTokenDTO


T = TypeVar("T", bound="ListTokensOutputBody")


@_attrs_define
class ListTokensOutputBody:
    """
    Attributes:
        tokens (list[PublicIngestTokenDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    tokens: list[PublicIngestTokenDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.public_ingest_token_dto import PublicIngestTokenDTO

        tokens: list[dict[str, Any]] | None
        if isinstance(self.tokens, list):
            tokens = []
            for tokens_type_0_item_data in self.tokens:
                tokens_type_0_item = tokens_type_0_item_data.to_dict()
                tokens.append(tokens_type_0_item)

        else:
            tokens = self.tokens

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "tokens": tokens,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_ingest_token_dto import PublicIngestTokenDTO

        d = dict(src_dict)

        def _parse_tokens(data: object) -> list[PublicIngestTokenDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tokens_type_0 = []
                _tokens_type_0 = data
                for tokens_type_0_item_data in _tokens_type_0:
                    tokens_type_0_item = PublicIngestTokenDTO.from_dict(tokens_type_0_item_data)

                    tokens_type_0.append(tokens_type_0_item)

                return tokens_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PublicIngestTokenDTO] | None, data)

        tokens = _parse_tokens(d.pop("tokens"))

        schema = d.pop("$schema", UNSET)

        list_tokens_output_body = cls(
            tokens=tokens,
            schema=schema,
        )

        return list_tokens_output_body
