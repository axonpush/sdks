from enum import Enum


class PolicyBodyWindowType(str, Enum):
    CUMULATIVE = "cumulative"
    DAILY = "daily"
    MONTHLY = "monthly"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
