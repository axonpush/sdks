from enum import Enum


class GatePolicyControllerRemoveScopeType(str, Enum):
    DATASET = "dataset"
    TARGET = "target"

    def __str__(self) -> str:
        return str(self.value)
