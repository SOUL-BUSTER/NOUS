from .base import Skill


class NavigateSkill(Skill):
    """Skill for robot navigation."""

    @property
    def name(self) -> str:
        return "navigate"

    def can_handle(self, goal: str) -> bool:
        return goal.lower().startswith("go to")

    def extract_arguments(self, goal: str) -> dict:
        destination = goal[5:].strip()

        if destination.lower().startswith("the "):
            destination = destination[4:]

        return {"destination": destination}

    def execute(self, **kwargs):
        destination = kwargs.get("destination")

        if not destination:
            return "Navigation failed: no destination provided."

        return f"Navigating to {destination}"
