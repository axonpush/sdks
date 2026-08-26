from enum import Enum


class TraceIntelligenceScope(str, Enum):
    APP_ENVIRONMENT = "app_environment"

    def __str__(self) -> str:
        return str(self.value)
