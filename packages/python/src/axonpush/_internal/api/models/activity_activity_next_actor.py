from enum import Enum


class ActivityActivityNextActor(str, Enum):
    CANDIDATE = "candidate"
    COMPANY = "company"
    HUMAN = "human"
    NONE = "none"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
