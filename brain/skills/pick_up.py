from .base import Skill


class PickUpSkill(Skill):
    """Skill for picking up objects."""

    @property
    def name(self) -> str:
        return "pick_up"

    def can_handle(self, goal: str) -> bool:
        return goal.lower().startswith("pick up")

    def extract_arguments(self, goal: str) -> dict:
        object_name = goal[7:].strip()

        if object_name.lower().startswith("the "):
            object_name = object_name[4:]

        return {"object": object_name}

    def execute(self, **kwargs):
        object_name = kwargs.get("object")

        if not object_name:
            return "Pick up failed: no object provided."

        return f"Picking up {object_name}"
