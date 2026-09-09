from enum import Enum


class ExperimentResultStatus(str, Enum):
    ERROR = "error"
    FAILED = "failed"
    NOT_EVALUATED = "not_evaluated"
    PASSED = "passed"
    PENDING = "pending"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
