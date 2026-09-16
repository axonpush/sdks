from enum import Enum


class PolicyBodyDestinationType(str, Enum):
    EMAIL = "email"
    VALUE_2 = ""
    WEBHOOK = "webhook"

    def __str__(self) -> str:
        return str(self.value)
