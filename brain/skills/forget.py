from .base import Skill


class ForgetSkill(Skill):
    """Creates an action that removes a fact from memory."""

    @property
    def name(self) -> str:
        return "forget"

    def can_handle(self, goal: str) -> bool:
        return goal.lower().startswith("forget my ")

    def extract_arguments(self, goal: str) -> dict:
        key = goal[len("forget my "):].strip().rstrip("?").lower()
        return {"key": key}

    def execute(self, **kwargs):
        return "Memory actions are executed by the Executor."
