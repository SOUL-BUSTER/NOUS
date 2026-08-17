from .base import Skill


class RecallSkill(Skill):
    """Creates an action that retrieves a simple fact from memory."""

    @property
    def name(self) -> str:
        return "recall"

    def can_handle(self, goal: str) -> bool:
        return goal.lower().startswith("what is my ")

    def extract_arguments(self, goal: str) -> dict:
        key = goal[len("what is my "):].strip().rstrip("?").lower()
        return {"key": key}

    def execute(self, **kwargs):
        return "Memory actions are executed by the Executor."
