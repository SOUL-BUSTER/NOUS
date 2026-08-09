from .base import Skill


class SpeakSkill(Skill):
    def execute(self, text):
        print(f"[Robot] {text}")
