from enum import Enum


class DatasetControllerExportRevisionFormat(str, Enum):
    CSV = "csv"
    JSONL = "jsonl"

    def __str__(self) -> str:
        return str(self.value)
