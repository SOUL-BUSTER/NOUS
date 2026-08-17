import re

from .base import Skill


class NavigateSkill(Skill):
    """Skill for robot navigation."""

    @property
    def name(self) -> str:
        return "navigate"

    def can_handle(self, goal: str) -> bool:
        return re.search(r"\bgo to\s+(?:the\s+)?\S", goal, re.IGNORECASE) is not None

    def extract_arguments(self, goal: str) -> dict:
        match = re.search(r"\bgo to\s+(?:the\s+)?(.+?)[?.!]*\s*$", goal, re.IGNORECASE)
        destination = match.group(1).strip() if match else ""

        return {"destination": destination}

    def execute(self, **kwargs):
        destination = kwargs.get("destination")

        if not destination:
            return "Navigation failed: no destination provided."

        return f"Navigating to {destination}"
