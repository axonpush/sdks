from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.provider_auth_mode import ProviderAuthMode
from ..models.provider_secret_source import ProviderSecretSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="TraceIntelligenceProviderResponseDto")


@_attrs_define
class TraceIntelligenceProviderResponseDto:
    """
    Attributes:
        auth_mode (ProviderAuthMode):
        base_url (str):
        chat_model (str):
        chat_path (str):
        embedding_model (str):
        embedding_path (str):
        secret_configured (bool):
        secret_source (ProviderSecretSource | Unset):
    """

    auth_mode: ProviderAuthMode
    base_url: str
    chat_model: str
    chat_path: str
    embedding_model: str
    embedding_path: str
    secret_configured: bool
    secret_source: ProviderSecretSource | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_mode = self.auth_mode.value

        base_url = self.base_url

        chat_model = self.chat_model

        chat_path = self.chat_path

        embedding_model = self.embedding_model

        embedding_path = self.embedding_path

        secret_configured = self.secret_configured

        secret_source: str | Unset = UNSET
        if not isinstance(self.secret_source, Unset):
            secret_source = self.secret_source.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authMode": auth_mode,
                "baseUrl": base_url,
                "chatModel": chat_model,
                "chatPath": chat_path,
                "embeddingModel": embedding_model,
                "embeddingPath": embedding_path,
                "secretConfigured": secret_configured,
            }
        )
        if secret_source is not UNSET:
            field_dict["secretSource"] = secret_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auth_mode = ProviderAuthMode(d.pop("authMode"))

        base_url = d.pop("baseUrl")

        chat_model = d.pop("chatModel")

        chat_path = d.pop("chatPath")

        embedding_model = d.pop("embeddingModel")

        embedding_path = d.pop("embeddingPath")

        secret_configured = d.pop("secretConfigured")

        _secret_source = d.pop("secretSource", UNSET)
        secret_source: ProviderSecretSource | Unset
        if isinstance(_secret_source, Unset):
            secret_source = UNSET
        else:
            secret_source = ProviderSecretSource(_secret_source)

        trace_intelligence_provider_response_dto = cls(
            auth_mode=auth_mode,
            base_url=base_url,
            chat_model=chat_model,
            chat_path=chat_path,
            embedding_model=embedding_model,
            embedding_path=embedding_path,
            secret_configured=secret_configured,
            secret_source=secret_source,
        )

        trace_intelligence_provider_response_dto.additional_properties = d
        return trace_intelligence_provider_response_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
