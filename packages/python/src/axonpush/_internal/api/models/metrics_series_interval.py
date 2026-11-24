from enum import Enum


class MetricsSeriesInterval(str, Enum):
    VALUE_0 = "1m"
    VALUE_1 = "5m"
    VALUE_2 = "1h"
    VALUE_3 = "1d"

    def __str__(self) -> str:
        return str(self.value)
