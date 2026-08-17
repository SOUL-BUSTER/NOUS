from .base import Skill


class StopSkill(Skill):
    """Creates an action that immediately stops the robot."""

    @property
    def name(self) -> str:
        return "stop"

    def can_handle(self, goal: str) -> bool:
        normalized_goal = goal.strip().lower().rstrip("?!.")
        return normalized_goal in {"stop", "stop now", "emergency stop"}

    def extract_arguments(self, goal: str) -> dict:
        return {}

    def execute(self, **kwargs):
        return "Stop actions are executed by the Executor."
