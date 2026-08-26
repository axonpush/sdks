from enum import Enum


class DatasetRevisionSource(str, Enum):
    BULK_TRACE = "bulk_trace"
    IMPORT = "import"
    MANUAL = "manual"
    TRACE = "trace"

    def __str__(self) -> str:
        return str(self.value)
