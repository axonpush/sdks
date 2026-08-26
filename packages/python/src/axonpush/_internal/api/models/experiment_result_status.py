from enum import Enum


class ExperimentResultStatus(str, Enum):
    ERROR = "error"
    FAILED = "failed"
    PASSED = "passed"
    PENDING = "pending"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
