from enum import Enum


class TraceAttributeScope(str, Enum):
    RESOURCE = "resource"
    SPAN = "span"

    def __str__(self) -> str:
        return str(self.value)
