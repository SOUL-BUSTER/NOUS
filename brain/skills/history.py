from .base import Skill


class HistorySkill(Skill):
    """Creates an action that reports recently executed NOUS commands."""

    @property
    def name(self) -> str:
        return "history"

    def can_handle(self, goal: str) -> bool:
        normalized_goal = goal.strip().lower().rstrip("?")
        return normalized_goal in {"history", "what did you do"}

    def extract_arguments(self, goal: str) -> dict:
        return {}

    def execute(self, **kwargs):
        return "History actions are executed by the Executor."
