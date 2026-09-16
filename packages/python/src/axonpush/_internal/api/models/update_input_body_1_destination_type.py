from enum import Enum


class UpdateInputBody1DestinationType(str, Enum):
    EMAIL = "email"
    WEBHOOK = "webhook"

    def __str__(self) -> str:
        return str(self.value)
