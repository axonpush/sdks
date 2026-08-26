from enum import Enum


class AlertOperator(str, Enum):
    GT = "gt"
    GTE = "gte"
    LT = "lt"
    LTE = "lte"

    def __str__(self) -> str:
        return str(self.value)
