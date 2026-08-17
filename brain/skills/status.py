from .base import Skill


class StatusSkill(Skill):
    """Creates an action that reports the current NOUS state."""

    @property
    def name(self) -> str:
        return "status"

    def can_handle(self, goal: str) -> bool:
        normalized_goal = goal.strip().lower().rstrip("?")
        return normalized_goal in {"status", "what is your status"}

    def extract_arguments(self, goal: str) -> dict:
        return {}

    def execute(self, **kwargs):
        return "Status actions are executed by the Executor."
