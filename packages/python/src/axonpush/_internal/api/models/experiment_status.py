from enum import Enum


class ExperimentStatus(str, Enum):
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    DRAFT = "draft"
    FAILED = "failed"
    QUEUED = "queued"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
