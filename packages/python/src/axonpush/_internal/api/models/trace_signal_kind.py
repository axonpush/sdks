from enum import Enum


class TraceSignalKind(str, Enum):
    BEHAVIOR = "behavior"
    GOAL = "goal"
    OUTCOME = "outcome"
    SENTIMENT = "sentiment"

    def __str__(self) -> str:
        return str(self.value)
