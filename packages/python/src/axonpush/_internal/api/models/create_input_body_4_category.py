from enum import Enum


class CreateInputBody4Category(str, Enum):
    BUG = "bug"
    IDEA = "idea"
    OTHER = "other"
    PRAISE = "praise"

    def __str__(self) -> str:
        return str(self.value)
