"""
NOUS Speech Interface

Defines the standard API for speech recognition and speech synthesis.
"""

from abc import ABC, abstractmethod


class SpeechInterface(ABC):
    """Base interface for speech systems."""

    @abstractmethod
    def listen(self) -> str:
        """
        Listen to the user's voice and return recognized text.
        """
        pass

    @abstractmethod
    def speak(self, text: str):
        """
        Convert text into speech.
        """
        pass
