from enum import Enum


class ActivityOutcomeCountClass(str, Enum):
    CANCELLED = "cancelled"
    EXPECTED = "expected"
    FAILED = "failed"
    PENDING = "pending"
    SUCCESS = "success"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
