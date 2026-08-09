"""
NOUS Vision Interface

Defines the standard API that every vision module must implement.
"""

from abc import ABC, abstractmethod
from typing import Any


class VisionInterface(ABC):
    """Base interface for all vision systems."""

    @abstractmethod
    def capture_frame(self) -> Any:
        """
        Capture a frame from the camera.
        """
        pass

    @abstractmethod
    def detect_objects(self, frame: Any):
        """
        Detect objects in a frame.
        """
        pass

    @abstractmethod
    def estimate_pose(self):
        """
        Estimate robot or camera pose.
        """
        pass
