from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.provider_auth_mode import ProviderAuthMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="TraceIntelligenceProviderDto")


@_attrs_define
class TraceIntelligenceProviderDto:
    """
    Attributes:
        auth_mode (ProviderAuthMode):
        base_url (str):
        chat_model (str):
        embedding_model (str):
        api_key (str | Unset): Write-only provider credential
        chat_path (str | Unset):  Default: '/v1/chat/completions'.
        embedding_path (str | Unset):  Default: '/v1/embeddings'.
        secret_ref (str | Unset): Existing secret name or ARN under the configured prefix
    """

    auth_mode: ProviderAuthMode
    base_url: str
    chat_model: str
    embedding_model: str
    api_key: str | Unset = UNSET
    chat_path: str | Unset = "/v1/chat/completions"
    embedding_path: str | Unset = "/v1/embeddings"
    secret_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_mode = self.auth_mode.value

        base_url = self.base_url

        chat_model = self.chat_model

        embedding_model = self.embedding_model

        api_key = self.api_key

        chat_path = self.chat_path

        embedding_path = self.embedding_path

        secret_ref = self.secret_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authMode": auth_mode,
                "baseUrl": base_url,
                "chatModel": chat_model,
                "embeddingModel": embedding_model,
            }
        )
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key
        if chat_path is not UNSET:
            field_dict["chatPath"] = chat_path
        if embedding_path is not UNSET:
            field_dict["embeddingPath"] = embedding_path
        if secret_ref is not UNSET:
            field_dict["secretRef"] = secret_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auth_mode = ProviderAuthMode(d.pop("authMode"))

        base_url = d.pop("baseUrl")

        chat_model = d.pop("chatModel")

        embedding_model = d.pop("embeddingModel")

        api_key = d.pop("apiKey", UNSET)

        chat_path = d.pop("chatPath", UNSET)

        embedding_path = d.pop("embeddingPath", UNSET)

        secret_ref = d.pop("secretRef", UNSET)

        trace_intelligence_provider_dto = cls(
            auth_mode=auth_mode,
            base_url=base_url,
            chat_model=chat_model,
            embedding_model=embedding_model,
            api_key=api_key,
            chat_path=chat_path,
            embedding_path=embedding_path,
            secret_ref=secret_ref,
        )

        trace_intelligence_provider_dto.additional_properties = d
        return trace_intelligence_provider_dto

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
