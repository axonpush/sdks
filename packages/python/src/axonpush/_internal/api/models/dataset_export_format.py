from enum import Enum


class DatasetExportFormat(str, Enum):
    CSV = "csv"
    JSONL = "jsonl"

    def __str__(self) -> str:
        return str(self.value)
