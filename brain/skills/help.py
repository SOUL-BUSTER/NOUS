from .base import Skill


class HelpSkill(Skill):
    """Creates an action that explains available NOUS commands."""

    @property
    def name(self) -> str:
        return "help"

    def can_handle(self, goal: str) -> bool:
        normalized_goal = goal.strip().lower().rstrip("?")
        return normalized_goal in {"help", "what can you do"}

    def extract_arguments(self, goal: str) -> dict:
        return {}

    def execute(self, **kwargs):
        return "Help actions are executed by the Executor."
