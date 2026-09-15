from enum import Enum


class CreateInputBody2Category(str, Enum):
    BUG = "bug"
    IDEA = "idea"
    OTHER = "other"
    PRAISE = "praise"

    def __str__(self) -> str:
        return str(self.value)
