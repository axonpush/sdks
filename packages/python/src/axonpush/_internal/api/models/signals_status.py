from enum import Enum


class SignalsStatus(str, Enum):
    COMPLETED = "completed"
    FAILED = "failed"
    PENDING = "pending"
    SKIPPED = "skipped"

    def __str__(self) -> str:
        return str(self.value)
