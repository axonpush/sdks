from enum import Enum


class ActivityWorkspaceSeriesSource(str, Enum):
    PROJECTION = "projection"
    ROLLUP = "rollup"

    def __str__(self) -> str:
        return str(self.value)
