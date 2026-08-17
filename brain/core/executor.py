from brain.implementations.dummy_hardware import DummyHardware


class Executor:
    """Executes structured NOUS actions on simulated hardware."""

    def __init__(self, skills, hardware=None):
        self.skills = skills
        self.hardware = hardware or DummyHardware()

    def execute(self, action):
        if action is None:
            return "No action provided."

        if action.name == "navigate":
            return self.hardware.move_to(action.parameters["destination"])

        if action.name == "speak":
            return self.hardware.speak(action.parameters["text"])

        if action.name == "pick_up":
            return self.hardware.pick_up(action.parameters["object"])

        return f"Unknown action: {action.name}"
