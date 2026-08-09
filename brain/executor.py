from brain.state import Action


class ActionExecutor:
    """Execute structured NOUS actions."""

    def execute(self, action: Action):
        if action is None:
            print("[Executor] No action provided.")
            return None

        print(f"[Executor] Executing: {action.name}")
        print(f"[Executor] Parameters: {action.parameters}")

        if action.name == "navigate":
            return self._navigate(action)

        if action.name == "speak":
            return self._speak(action)

        if action.name == "pick_up":
            return self._pick_up(action)

        print(f"[Executor] Unknown action: {action.name}")
        return None

    def _navigate(self, action: Action):
        destination = action.parameters.get("destination")

        if not destination:
            return "Navigation failed: no destination."

        result = f"Navigating to {destination}"

        print(f"[Executor] {result}")

        return result

    def _speak(self, action: Action):
        text = action.parameters.get("text")

        if not text:
            return "Speech failed: no text."

        result = f"Speaking: {text}"

        print(f"[Executor] {result}")

        return result

    def _pick_up(self, action: Action):
        object_name = action.parameters.get("object")

        if not object_name:
            return "Pick up failed: no object."

        result = f"Picking up {object_name}"

        print(f"[Executor] {result}")

        return result
