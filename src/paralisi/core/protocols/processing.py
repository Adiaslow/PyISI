# src/paralisi/core/protocols/processing.py
"""Data processing protocols."""

from typing import Protocol
from ..data.data import RawData, ProcessedData

class DataProcessor(Protocol):
    """Interface for data processing strategies."""

    def process(self, data: RawData) -> ProcessedData:
        """Process raw data into processed form."""
        ...
