from brain.skills.navigate import NavigateSkill
from brain.skills.speak import SpeakSkill
from brain.skills.pick_up import PickUpSkill


class Executor:
    """Execute structured NOUS actions."""

    def __init__(self):
        self.skills = {
            "navigate": NavigateSkill(),
            "speak": SpeakSkill(),
            "pick_up": PickUpSkill(),
        }

    def execute(self, action):
        skill = self.skills.get(action.name)

        if skill is None:
            return f"Unknown skill: {action.name}"

        result = skill.execute(**action.parameters)

        print(f"[Executor] Skill: {action.name}")
        print(f"[Executor] Result: {result}")

        return result
