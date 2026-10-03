from enum import Enum


class ActivityDraftUpdatedSource(str, Enum):
    APIKEY = "apikey"
    DASHBOARD = "dashboard"
    MCP = "mcp"

    def __str__(self) -> str:
        return str(self.value)
