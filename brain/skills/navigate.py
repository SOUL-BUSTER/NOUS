from .base import Skill


class NavigateSkill(Skill):
    """Skill for robot navigation."""

    @property
    def name(self) -> str:
        return "navigate"

    def execute(self, **kwargs):
        destination = kwargs.get("destination")

        if not destination:
            return "No destination provided."

        return f"Navigating to {destination}"
