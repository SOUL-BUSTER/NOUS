from abc import ABC, abstractmethod
from typing import Any


class Skill(ABC):
    """Base class for all NOUS skills."""

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def can_handle(self, goal: str) -> bool:
        pass

    @abstractmethod
    def extract_arguments(self, goal: str) -> dict[str, Any]:
        pass

    @abstractmethod
    def execute(self, **kwargs):
        pass
