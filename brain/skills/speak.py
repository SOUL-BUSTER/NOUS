import re

from .base import Skill


class SpeakSkill(Skill):
    """Skill for robot speech."""

    @property
    def name(self) -> str:
        return "speak"

    def can_handle(self, goal: str) -> bool:
        can_say = re.search(r"\bsay\s+\S", goal, re.IGNORECASE) is not None
        can_tell = re.search(r"\btell\s+\S+\s+\S", goal, re.IGNORECASE) is not None
        return can_say or can_tell

    def extract_arguments(self, goal: str) -> dict:
        say_match = re.search(r"\bsay\s+(?:to\s+)?(.+?)[?.!]*\s*$", goal, re.IGNORECASE)
        tell_match = re.search(r"\btell\s+\S+\s+(.+?)[?.!]*\s*$", goal, re.IGNORECASE)

        if say_match:
            text = say_match.group(1).strip()
        elif tell_match:
            text = tell_match.group(1).strip()
        else:
            text = ""

        return {"text": text}

    def execute(self, **kwargs):
        text = kwargs.get("text")

        if not text:
            return "Speech failed: no text provided."

        return f"Speaking: {text}"
