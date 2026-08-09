from brain.skills.registry import SkillRegistry
from brain.skills.navigate import NavigateSkill
from brain.skills.speak import SpeakSkill
from brain.skills.pick_up import PickUpSkill


class Brain:
    """Core intelligence system for NOUS."""

    def __init__(self):
        self.goal = None
        self.plan = []
        self.last_action = None

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
            "Create structured action",
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

        action = skill.execute(**arguments)

        self.last_action = action

        print(f"[Brain] Action: {action}")

        return action

    def status(self):
        return {
            "goal": self.goal,
            "plan": self.plan,
            "skills": self.skills.list(),
            "last_action": self.last_action,
        }
