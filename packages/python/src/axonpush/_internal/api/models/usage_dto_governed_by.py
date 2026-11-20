from enum import Enum


class UsageDTOGovernedBy(str, Enum):
    LICENCE = "licence"
    PLAN = "plan"

    def __str__(self) -> str:
        return str(self.value)
