from abc import ABC, abstractmethod


class Skill(ABC):
    """Base class for all NOUS skills."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the skill name."""
        pass

    @abstractmethod
    def execute(self, **kwargs):
        """Execute the skill."""
        pass
