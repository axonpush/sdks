from enum import Enum


class CreateRuleInputBodyAction(str, Enum):
    ALLOW = "allow"
    BLOCK = "block"
    FLAG = "flag"
    REDACT = "redact"

    def __str__(self) -> str:
        return str(self.value)
