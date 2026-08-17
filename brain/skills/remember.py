from .base import Skill


class RememberSkill(Skill):
    """Creates an action that stores a simple fact in memory."""

    @property
    def name(self) -> str:
        return "remember"

    def can_handle(self, goal: str) -> bool:
        return goal.lower().startswith("remember my ") and " is " in goal.lower()

    def extract_arguments(self, goal: str) -> dict:
        fact = goal[len("remember my "):].strip()
        key, value = fact.split(" is ", 1)
        return {"key": key.strip().lower(), "value": value.strip()}

    def execute(self, **kwargs):
        return "Memory actions are executed by the Executor."
