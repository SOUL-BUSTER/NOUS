from .base import Skill


class SpeakSkill(Skill):
    """Skill for robot speech."""

    @property
    def name(self) -> str:
        return "speak"

    def can_handle(self, goal: str) -> bool:
        return goal.lower().startswith("say")

    def extract_arguments(self, goal: str) -> dict:
        text = goal[3:].strip()

        if text.lower().startswith("to "):
            text = text[3:].strip()

        return {"text": text}

    def execute(self, **kwargs):
        text = kwargs.get("text")

        if not text:
            return "Speech failed: no text provided."

        return f"Speaking: {text}"
