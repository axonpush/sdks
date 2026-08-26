from enum import Enum


class EvaluationTargetType(str, Enum):
    HTTPS = "https"
    LOCAL = "local"
    PROMPT_MODEL = "prompt_model"

    def __str__(self) -> str:
        return str(self.value)
