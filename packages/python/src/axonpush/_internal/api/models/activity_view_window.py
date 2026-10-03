from enum import Enum


class ActivityViewWindow(str, Enum):
    VALUE_0 = "15m"
    VALUE_1 = "1h"
    VALUE_2 = "24h"
    VALUE_3 = "7d"
    VALUE_4 = "30d"

    def __str__(self) -> str:
        return str(self.value)
