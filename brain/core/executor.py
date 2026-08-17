from brain.implementations.dummy_hardware import DummyHardware
from brain.implementations.simple_memory import SimpleMemory


class Executor:
    """Executes structured NOUS actions on simulated hardware."""

    def __init__(self, skills, hardware=None, memory=None, status_provider=None):
        self.skills = skills
        self.hardware = hardware or DummyHardware()
        self.memory = memory or SimpleMemory()
        self.status_provider = status_provider

    def execute(self, action):
        if action is None:
            return "No action provided."

        validation_error = self._validate_action(action)
        if validation_error:
            return validation_error

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

        if action.name == "status":
            return self._format_status()

        return f"Unknown action: {action.name}"

    def execute_all(self, actions):
        """Execute actions in the order provided by the Brain."""
        results = []

        for action in actions:
            result = self.execute(action)
            results.append(result)

            if result == "No action provided." or result.startswith(("Invalid action:", "Unknown action:")):
                break

        return results

    def _validate_action(self, action):
        required_parameters = {
            "navigate": "destination",
            "speak": "text",
            "pick_up": "object",
            "remember": "key",
            "recall": "key",
            "forget": "key",
            "status": None,
        }

        if action.name not in required_parameters:
            return f"Unknown action: {action.name}"

        parameter_name = required_parameters[action.name]
        if parameter_name is None:
            return None

        value = action.parameters.get(parameter_name)
        if not isinstance(value, str) or not value.strip():
            return f"Invalid action: {action.name} requires a {parameter_name}."

        if action.name == "remember":
            value = action.parameters.get("value")
            if not isinstance(value, str) or not value.strip():
                return "Invalid action: remember requires a value."

        return None

    def _format_status(self):
        if self.status_provider is None:
            return "Status is unavailable."

        status = self.status_provider()
        skills = ", ".join(status["skills"])
        last_action = status["last_action"]
        last_action_name = last_action.name if last_action else "None"

        return (
            f"Goal: {status['goal']} | Skills: {skills} | "
            f"Last action: {last_action_name}"
        )
