from enum import Enum


class ActivitySeriesWindow(str, Enum):
    VALUE_0 = "1h"
    VALUE_1 = "24h"
    VALUE_2 = "7d"

    def __str__(self) -> str:
        return str(self.value)
