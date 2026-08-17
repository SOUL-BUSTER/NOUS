from brain.implementations.dummy_hardware import DummyHardware
from brain.implementations.simple_memory import SimpleMemory


class Executor:
    """Executes structured NOUS actions on simulated hardware."""

    def __init__(self, skills, hardware=None, memory=None):
        self.skills = skills
        self.hardware = hardware or DummyHardware()
        self.memory = memory or SimpleMemory()

    def execute(self, action):
        if action is None:
            return "No action provided."

        if action.name == "navigate":
            return self.hardware.move_to(action.parameters["destination"])

        if action.name == "speak":
            return self.hardware.speak(action.parameters["text"])

        if action.name == "pick_up":
            return self.hardware.pick_up(action.parameters["object"])

        if action.name == "remember":
            key = action.parameters["key"]
            value = action.parameters["value"]
            self.memory.remember(key, value)
            return f"I'll remember that your {key} is {value}."

        if action.name == "recall":
            key = action.parameters["key"]
            value = self.memory.recall(key)

            if value is None:
                return f"I don't know your {key} yet."

            return f"Your {key} is {value}."

        if action.name == "forget":
            key = action.parameters["key"]

            if self.memory.recall(key) is None:
                return f"I don't know your {key} yet."

            self.memory.forget(key)
            return f"I've forgotten your {key}."

        return f"Unknown action: {action.name}"
