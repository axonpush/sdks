from enum import Enum


class AnalyticsLatencyActivityClass(str, Enum):
    ALL = "all"
    BUSINESS = "business"
    SYSTEM = "system"

    def __str__(self) -> str:
        return str(self.value)
