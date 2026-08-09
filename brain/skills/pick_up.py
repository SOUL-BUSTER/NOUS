from .base import Skill
from brain.state import Action


class PickUpSkill(Skill):
    """Skill for picking up objects."""

    @property
    def name(self) -> str:
        return "pick_up"

    def can_handle(self, goal: str) -> bool:
        return goal.lower().startswith(("pick up ", "pick up the "))

    def extract_arguments(self, goal: str) -> dict:
        text = goal.strip()

        if text.lower().startswith("pick up the "):
            object_name = text[12:].strip()
        elif text.lower().startswith("pick up "):
            object_name = text[8:].strip()
        else:
            object_name = ""

        return {
            "object": object_name
        }

    def execute(self, **kwargs) -> Action:
        object_name = kwargs.get("object")

        return Action(
            name="pick_up",
            parameters={
                "object": object_name or ""
            }
        )
