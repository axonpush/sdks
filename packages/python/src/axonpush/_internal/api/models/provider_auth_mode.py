from enum import Enum


class ProviderAuthMode(str, Enum):
    API_KEY = "api-key"
    BEARER = "bearer"

    def __str__(self) -> str:
        return str(self.value)
