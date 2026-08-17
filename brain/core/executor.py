class Executor:
    """Executes structured NOUS actions."""

    def __init__(self, skills):
        self.skills = skills

    def execute(self, action):
        if action is None:
            return "No action provided."

        skill = self.skills.get(action.name)

        if skill is None:
            return f"Unknown skill: {action.name}"

        print(f"[Executor] Skill: {action.name}")

        result = skill.execute(**action.parameters)

        print(f"[Executor] Result: {result}")

        return result
