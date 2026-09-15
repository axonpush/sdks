from enum import Enum


class AnalyticsBreakdownDimension(str, Enum):
    MODEL = "model"
    PROVIDER = "provider"

    def __str__(self) -> str:
        return str(self.value)
