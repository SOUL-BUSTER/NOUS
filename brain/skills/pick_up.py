from .base import Skill


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

    def execute(self, **kwargs):
        object_name = kwargs.get("object")

        if not object_name:
            return "No object provided."

        return f"Picking up {object_name}"
