from enum import Enum


class WorkflowDeploymentStatus(str, Enum):
    DEGRADED = "degraded"
    NOT_READY = "not_ready"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
