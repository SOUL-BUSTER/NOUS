"""
NOUS Hardware Interface
"""

from abc import ABC, abstractmethod


class HardwareInterface(ABC):
    """Base interface for robot hardware."""

    @abstractmethod
    def execute(self, command: str):
        """
        Execute a hardware command.
        """
        pass

    @abstractmethod
    def stop(self):
        """
        Stop all hardware movement.
        """
        pass
