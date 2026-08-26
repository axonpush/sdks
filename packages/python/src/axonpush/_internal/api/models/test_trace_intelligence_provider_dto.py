from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.provider_auth_mode import ProviderAuthMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="TestTraceIntelligenceProviderDto")


@_attrs_define
class TestTraceIntelligenceProviderDto:
    """
    Attributes:
        api_key (str | Unset): Write-only credential used only for this test
        auth_mode (ProviderAuthMode | Unset):
        base_url (str | Unset):
        chat_model (str | Unset):
        chat_path (str | Unset):
        embedding_model (str | Unset):
        embedding_path (str | Unset):
        secret_ref (str | Unset):
    """

    api_key: str | Unset = UNSET
    auth_mode: ProviderAuthMode | Unset = UNSET
    base_url: str | Unset = UNSET
    chat_model: str | Unset = UNSET
    chat_path: str | Unset = UNSET
    embedding_model: str | Unset = UNSET
    embedding_path: str | Unset = UNSET
    secret_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        auth_mode: str | Unset = UNSET
        if not isinstance(self.auth_mode, Unset):
            auth_mode = self.auth_mode.value

        base_url = self.base_url

        chat_model = self.chat_model

        chat_path = self.chat_path

        embedding_model = self.embedding_model

        embedding_path = self.embedding_path

        secret_ref = self.secret_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key
        if auth_mode is not UNSET:
            field_dict["authMode"] = auth_mode
        if base_url is not UNSET:
            field_dict["baseUrl"] = base_url
        if chat_model is not UNSET:
            field_dict["chatModel"] = chat_model
        if chat_path is not UNSET:
            field_dict["chatPath"] = chat_path
        if embedding_model is not UNSET:
            field_dict["embeddingModel"] = embedding_model
        if embedding_path is not UNSET:
            field_dict["embeddingPath"] = embedding_path
        if secret_ref is not UNSET:
            field_dict["secretRef"] = secret_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey", UNSET)

        _auth_mode = d.pop("authMode", UNSET)
        auth_mode: ProviderAuthMode | Unset
        if isinstance(_auth_mode, Unset):
            auth_mode = UNSET
        else:
            auth_mode = ProviderAuthMode(_auth_mode)

        base_url = d.pop("baseUrl", UNSET)

        chat_model = d.pop("chatModel", UNSET)

        chat_path = d.pop("chatPath", UNSET)

        embedding_model = d.pop("embeddingModel", UNSET)

        embedding_path = d.pop("embeddingPath", UNSET)

        secret_ref = d.pop("secretRef", UNSET)

        test_trace_intelligence_provider_dto = cls(
            api_key=api_key,
            auth_mode=auth_mode,
            base_url=base_url,
            chat_model=chat_model,
            chat_path=chat_path,
            embedding_model=embedding_model,
            embedding_path=embedding_path,
            secret_ref=secret_ref,
        )

        test_trace_intelligence_provider_dto.additional_properties = d
        return test_trace_intelligence_provider_dto

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
