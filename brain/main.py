from brain.core.brain import Brain
from brain.core.executor import Executor


def main():
    brain = Brain()
    executor = Executor(brain.skills)

    print("NOUS is ready.")
    print("Try: Go to kitchen | Say hello | Pick up the cup")
    print("Memory: Remember my name is Sotsai | What is my name?")
    print("Type 'exit' to stop.")

    while True:
        goal = input("\nYou: ").strip()

        if goal.lower() in {"exit", "quit"}:
            print("NOUS: Goodbye.")
            break

        if not goal:
            continue

        brain.think(goal)
        action = brain.act()
        result = executor.execute(action)

        print(f"NOUS: {result}")


if __name__ == "__main__":
    main()
