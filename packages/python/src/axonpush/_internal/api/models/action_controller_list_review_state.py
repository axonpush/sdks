from enum import Enum


class ActionControllerListReviewState(str, Enum):
    NOISE = "noise"
    UNREVIEWED = "unreviewed"
    USEFUL = "useful"

    def __str__(self) -> str:
        return str(self.value)
