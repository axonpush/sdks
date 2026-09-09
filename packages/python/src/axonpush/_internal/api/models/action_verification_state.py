from enum import Enum


class ActionVerificationState(str, Enum):
    CONFIRMED = "confirmed"
    CONTRADICTED = "contradicted"
    PENDING = "pending"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
