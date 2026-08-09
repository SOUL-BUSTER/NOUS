from interfaces.planner import PlannerInterface


class SimplePlanner(PlannerInterface):
    def __init__(self):
        self.plan = []

    def create_plan(self, goal: str):
        self.plan = [
            f"Understand goal: {goal}",
            "Generate actions",
            "Execute actions"
        ]

        return self.plan

    def next_action(self):
        if self.plan:
            return self.plan.pop(0)

        return None
