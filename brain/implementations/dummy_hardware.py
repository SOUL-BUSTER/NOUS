class DummyHardware:
    """Simulated robot hardware for NOUS."""

    def move_to(self, destination: str):
        return f"[Robot] Moving to {destination}"

    def speak(self, text: str):
        return f"[Robot] Speaking: {text}"

    def pick_up(self, object_name: str):
        return f"[Robot] Picking up {object_name}"

    def stop(self):
        return "[Robot] Stopped"
