from enum import Enum


class ProviderSecretSource(str, Enum):
    MANAGED = "managed"
    REFERENCE = "reference"

    def __str__(self) -> str:
        return str(self.value)
