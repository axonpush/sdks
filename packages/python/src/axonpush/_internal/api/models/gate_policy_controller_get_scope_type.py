from enum import Enum


class GatePolicyControllerGetScopeType(str, Enum):
    DATASET = "dataset"
    TARGET = "target"

    def __str__(self) -> str:
        return str(self.value)
