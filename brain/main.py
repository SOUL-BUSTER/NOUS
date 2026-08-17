from brain.core.brain import Brain
from brain.core.executor import Executor


def main():
    brain = Brain()
    executor = Executor(brain.skills, status_provider=brain.status)

    print("NOUS is ready.")
    print("Try: Go to kitchen | Please go to the kitchen | Go to kitchen and pick up the cup")
    print("Memory: Remember my name is Sotsai | What is my name? | Forget my name")
    print("System: Status")
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
