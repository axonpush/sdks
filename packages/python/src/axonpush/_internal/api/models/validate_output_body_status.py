from enum import Enum


class ValidateOutputBodyStatus(str, Enum):
    INVALID = "invalid"
    VALID = "valid"

    def __str__(self) -> str:
        return str(self.value)
