from enum import Enum


class AssessmentValueType(str, Enum):
    BOOLEAN = "boolean"
    CATEGORICAL = "categorical"
    NUMERIC = "numeric"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
