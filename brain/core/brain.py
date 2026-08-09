from brain.skills.registry import SkillRegistry
from brain.skills.navigate import NavigateSkill
from brain.skills.speak import SpeakSkill
from brain.skills.pick_up import PickUpSkill


class Brain:
    """Core intelligence system for NOUS."""

    def __init__(self):
        self.goal = None
        self.plan = []

        self.skills = SkillRegistry()

        self.skills.register(NavigateSkill())
        self.skills.register(SpeakSkill())
        self.skills.register(PickUpSkill())

    def think(self, goal: str):
        self.goal = goal

        print(f"[Brain] Thinking about: {goal}")

        self.plan = [
            f"Understand goal: {goal}",
            "Find appropriate skill",
            "Extract required information",
            "Execute skill",
        ]

        print("[Brain] Plan:")

        for step in self.plan:
            print(f"- {step}")

        return self.plan

    def act(self):
        if not self.goal:
            print("[Brain] No goal.")
            return None

        skill = self.skills.find_for_goal(self.goal)

        if skill is None:
            print(f"[Brain] No skill found for: {self.goal}")
            return None

        print(f"[Brain] Selected skill: {skill.name}")

        arguments = skill.extract_arguments(self.goal)

        print(f"[Brain] Arguments: {arguments}")

        result = skill.execute(**arguments)

        print(f"[Brain] Result: {result}")

        return result

    def status(self):
        return {
            "goal": self.goal,
            "plan": self.plan,
            "skills": self.skills.list(),
        }
