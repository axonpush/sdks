from enum import Enum


class ActionEvidenceKind(str, Enum):
    CLAIM = "claim"
    OBSERVATION = "observation"
    REVIEW = "review"

    def __str__(self) -> str:
        return str(self.value)
