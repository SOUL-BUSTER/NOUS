from .base import Skill
from brain.state import Action


class NavigateSkill(Skill):
    """Skill for robot navigation."""

    @property
    def name(self) -> str:
        return "navigate"

    def can_handle(self, goal: str) -> bool:
        return goal.lower().startswith("go to ")

    def extract_arguments(self, goal: str) -> dict:
        destination = goal[6:].strip()

        return {
            "destination": destination
        }

    def execute(self, **kwargs) -> Action:
        destination = kwargs.get("destination")

        if not destination:
            return Action(
                name="navigate",
                parameters={}
            )

        return Action(
            name="navigate",
            parameters={
                "destination": destination
            }
        )
