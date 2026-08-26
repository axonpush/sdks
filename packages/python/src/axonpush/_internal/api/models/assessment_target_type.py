from enum import Enum


class AssessmentTargetType(str, Enum):
    SESSION = "session"
    SPAN = "span"
    TRACE = "trace"

    def __str__(self) -> str:
        return str(self.value)
