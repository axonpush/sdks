from enum import Enum


class AnalyticsControllerCompareDimension(str, Enum):
    ENVIRONMENT = "environment"
    MODEL = "model"
    PROMPT_VERSION = "prompt_version"
    PROVIDER = "provider"
    RELEASE = "release"
    SERVICE = "service"

    def __str__(self) -> str:
        return str(self.value)
