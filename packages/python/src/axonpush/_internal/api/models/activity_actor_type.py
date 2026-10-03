from enum import Enum


class ActivityActorType(str, Enum):
    AGENT = "agent"
    HUMAN = "human"
    INTEGRATION = "integration"
    UNKNOWN = "unknown"
    WORKER = "worker"

    def __str__(self) -> str:
        return str(self.value)
