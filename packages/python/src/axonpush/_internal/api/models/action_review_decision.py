from enum import Enum


class ActionReviewDecision(str, Enum):
    NOISE = "noise"
    USEFUL = "useful"

    def __str__(self) -> str:
        return str(self.value)
