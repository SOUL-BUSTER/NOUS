import os

from brain.core.brain import Brain
from brain.core.executor import Executor
from brain.implementations.dummy_hardware import DummyHardware
from brain.implementations.serial_hardware import SerialHardware


def create_hardware():
    mode = os.getenv("NOUS_HARDWARE", "dummy").lower()

    if mode == "dummy":
        return DummyHardware()

    if mode == "serial":
        port = os.getenv("NOUS_SERIAL_PORT")
        if not port:
            raise RuntimeError("Set NOUS_SERIAL_PORT before using serial hardware.")

        return SerialHardware(port)

    raise RuntimeError("NOUS_HARDWARE must be 'dummy' or 'serial'.")


def main():
    brain = Brain()
    executor = Executor(
        brain.skills,
        hardware=create_hardware(),
        status_provider=brain.status,
    )

    print("NOUS is ready.")
    print("Try: Go to kitchen | Please go to the kitchen | Go to kitchen and pick up the cup")
    print("Memory: Remember my name is Sotsai | What is my name? | Forget my name")
    print("System: Stop | Status | Help | History")
    print("Type 'exit' to stop.")

    while True:
        goal = input("\nYou: ").strip()

        if goal.lower() in {"exit", "quit"}:
            print("NOUS: Goodbye.")
            break

        if not goal:
            continue

        brain.think(goal)
        actions = brain.act_all()
        results = executor.execute_all(actions)

        for result in results:
            print(f"NOUS: {result}")


if __name__ == "__main__":
    main()
