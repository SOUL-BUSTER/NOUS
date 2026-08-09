from brain.implementations.simple_planner import SimplePlanner
from brain.skills.navigate import NavigateSkill


class Brain:
    """Core intelligence system for NOUS."""

    def __init__(self):
        self.planner = SimplePlanner()
        self.navigate = NavigateSkill()
        self.goal = None

    def think(self, goal: str):
        self.goal = goal

        print(f"[Brain] Thinking about: {goal}")

        plan = self.planner.create_plan(goal)

        print("[Brain] Plan:")
        for step in plan:
            print(f"- {step}")

        return plan

    def act(self):
        if not self.goal:
            print("[Brain] No goal.")
            return

        goal = self.goal.lower()

        if "go to" in goal:
            destination = goal.split("go to", 1)[1].strip()

            result = self.navigate.execute(
                destination=destination
            )

            print(f"[Brain] {result}")

            return result

        print("[Brain] I don't know how to perform this task yet.")

    def status(self):
        return {
            "goal": self.goal
        }
