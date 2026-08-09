"""
NOUS Memory Interface

Defines the standard API for robot memory.
"""

from abc import ABC, abstractmethod
from typing import Any


class MemoryInterface(ABC):
    """Base interface for memory systems."""

    @abstractmethod
    def remember(self, key: str, value: Any):
        """
        Store information.
        """
        pass

    @abstractmethod
    def recall(self, key: str):
        """
        Retrieve stored information.
        """
        pass

    @abstractmethod
    def forget(self, key: str):
        """
        Remove stored information.
        """
        pass
