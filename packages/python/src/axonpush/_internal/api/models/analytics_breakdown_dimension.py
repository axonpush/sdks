from enum import Enum


class AnalyticsBreakdownDimension(str, Enum):
    AGENT = "agent"
    MODEL = "model"
    PROVIDER = "provider"
    TOOL = "tool"

    def __str__(self) -> str:
        return str(self.value)
