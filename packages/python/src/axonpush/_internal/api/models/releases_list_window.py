from enum import Enum


class ReleasesListWindow(str, Enum):
    VALUE_0 = "1h"
    VALUE_1 = "6h"
    VALUE_2 = "24h"
    VALUE_3 = "7d"
    VALUE_4 = "14d"
    VALUE_5 = "30d"

    def __str__(self) -> str:
        return str(self.value)
