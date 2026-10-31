from enum import Enum


class OperationCapabilityAvailability(str, Enum):
    ALLOWED = "allowed"
    CONDITIONAL = "conditional"
    DENIED = "denied"

    def __str__(self) -> str:
        return str(self.value)
