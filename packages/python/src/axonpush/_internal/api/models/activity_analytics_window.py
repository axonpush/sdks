from enum import Enum


class ActivityAnalyticsWindow(str, Enum):
    VALUE_0 = "30d"
    VALUE_1 = "90d"

    def __str__(self) -> str:
        return str(self.value)
