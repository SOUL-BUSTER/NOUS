from .base import Skill
from brain.state import Action


class SpeakSkill(Skill):
    """Skill for robot speech."""

    @property
    def name(self) -> str:
        return "speak"

    def can_handle(self, goal: str) -> bool:
        return goal.lower().startswith(("say ", "speak "))

    def extract_arguments(self, goal: str) -> dict:
        text = goal

        if text.lower().startswith("say "):
            text = text[4:]
        elif text.lower().startswith("speak "):
            text = text[6:]

        return {
            "text": text.strip()
        }

    def execute(self, **kwargs) -> Action:
        text = kwargs.get("text")

        return Action(
            name="speak",
            parameters={
                "text": text or ""
            }
        )
