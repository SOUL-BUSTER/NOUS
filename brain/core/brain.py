import re

from brain.skills.registry import SkillRegistry
from brain.skills.navigate import NavigateSkill
from brain.skills.speak import SpeakSkill
from brain.skills.pick_up import PickUpSkill
from brain.skills.forget import ForgetSkill
from brain.skills.recall import RecallSkill
from brain.skills.remember import RememberSkill
from brain.core.action import Action


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
        self.skills.register(ForgetSkill())
        self.skills.register(RememberSkill())
        self.skills.register(RecallSkill())

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

        return self._create_action(self.goal)

    def act_all(self):
        """Create ordered actions for a goal containing simple 'and' steps."""
        if not self.goal:
            print("[Brain] No goal.")
            return []

        goals = re.split(r"\s+\band\b\s+", self.goal, flags=re.IGNORECASE)
        actions = []

        for goal in goals:
            action = self._create_action(goal)
            if action is not None:
                actions.append(action)

        return actions

    def _create_action(self, goal: str):
        skill = self.skills.find_for_goal(goal)

        if skill is None:
            print(f"[Brain] No skill found for: {goal}")
            return None

        print(f"[Brain] Selected skill: {skill.name}")

        arguments = skill.extract_arguments(goal)

        print(f"[Brain] Arguments: {arguments}")

        action = Action(
            name=skill.name,
            parameters=arguments,
        )

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
