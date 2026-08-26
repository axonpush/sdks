from enum import Enum


class TraceV2ControllerAttributeKeysScope(str, Enum):
    RESOURCE = "resource"
    SPAN = "span"

    def __str__(self) -> str:
        return str(self.value)
