from enum import Enum


class IntelligenceJobStatus(str, Enum):
    COMPLETED = "completed"
    FAILED = "failed"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
