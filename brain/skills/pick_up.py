import re

from .base import Skill


class PickUpSkill(Skill):
    """Skill for picking up objects."""

    @property
    def name(self) -> str:
        return "pick_up"

    def can_handle(self, goal: str) -> bool:
        return re.search(r"\bpick up\s+(?:(?:the|a|an)\s+)?\S", goal, re.IGNORECASE) is not None

    def extract_arguments(self, goal: str) -> dict:
        match = re.search(r"\bpick up\s+(?:(?:the|a|an)\s+)?(.+?)[?.!]*\s*$", goal, re.IGNORECASE)
        object_name = match.group(1).strip() if match else ""

        return {"object": object_name}

    def execute(self, **kwargs):
        object_name = kwargs.get("object")

        if not object_name:
            return "Pick up failed: no object provided."

        return f"Picking up {object_name}"
