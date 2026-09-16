from enum import Enum


class CreateRuleInputBodyTarget(str, Enum):
    REQUEST = "request"
    RESPONSE = "response"
    TOOL_CALL = "tool_call"

    def __str__(self) -> str:
        return str(self.value)
