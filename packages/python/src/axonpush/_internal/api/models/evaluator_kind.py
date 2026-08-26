from enum import Enum


class EvaluatorKind(str, Enum):
    CONTAINS = "contains"
    EXACT_MATCH = "exact_match"
    JSON_SCHEMA = "json_schema"
    MANAGED_LLM = "managed_llm"
    REGEX = "regex"
    REMOTE = "remote"

    def __str__(self) -> str:
        return str(self.value)
