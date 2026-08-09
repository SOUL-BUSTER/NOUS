from .base import Skill


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

    def execute(self, **kwargs):
        text = kwargs.get("text")

        if not text:
            return "No text provided."

        return f"Speaking: {text}"
