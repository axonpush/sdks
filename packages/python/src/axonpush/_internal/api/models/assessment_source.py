from enum import Enum


class AssessmentSource(str, Enum):
    END_USER = "end_user"
    EVALUATOR = "evaluator"
    IMPORT = "import"
    REVIEWER = "reviewer"

    def __str__(self) -> str:
        return str(self.value)
