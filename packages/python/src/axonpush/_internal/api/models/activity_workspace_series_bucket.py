from enum import Enum


class ActivityWorkspaceSeriesBucket(str, Enum):
    VALUE_0 = "5m"
    VALUE_1 = "1h"
    VALUE_2 = "1d"

    def __str__(self) -> str:
        return str(self.value)
