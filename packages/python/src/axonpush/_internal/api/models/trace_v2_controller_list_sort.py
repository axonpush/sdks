from enum import Enum


class TraceV2ControllerListSort(str, Enum):
    COST_DESC = "cost_desc"
    DURATION_DESC = "duration_desc"
    LAST_SEEN_ASC = "last_seen_asc"
    LAST_SEEN_DESC = "last_seen_desc"
    TOKENS_DESC = "tokens_desc"

    def __str__(self) -> str:
        return str(self.value)
