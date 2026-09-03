from enum import Enum


class GatePolicyScope(str, Enum):
    DATASET = "dataset"
    TARGET = "target"

    def __str__(self) -> str:
        return str(self.value)
