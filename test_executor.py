from pathlib import Path
from tempfile import TemporaryDirectory

from brain.core.brain import Brain
from brain.core.executor import Executor
from brain.implementations.simple_memory import SimpleMemory


brain = Brain()
executor = Executor(brain.skills)


print("=== TEST NAVIGATION ===")
brain.think("Go to kitchen")
action = brain.act()
print("Action:", action)
print("Result:", executor.execute(action))

print()

print("=== TEST FLEXIBLE COMMANDS ===")
for goal in [
    "Please go to the kitchen",
    "Could you pick up a cup?",
    "Tell Sotsai hello",
]:
    brain.think(goal)
    action = brain.act()
    print("Action:", action)
    print("Result:", executor.execute(action))

print()

print("=== TEST MEMORY ===")
with TemporaryDirectory() as temp_dir:
    memory_path = Path(temp_dir) / "nous_memory.json"
    memory_executor = Executor(brain.skills, memory=SimpleMemory(memory_path))

    brain.think("Remember my name is Sotsai")
    action = brain.act()
    print("Action:", action)
    print("Result:", memory_executor.execute(action))

    brain.think("What is my name?")
    action = brain.act()
    print("Action:", action)
    print("Result:", memory_executor.execute(action))
    print("Result after restart:", Executor(brain.skills, memory=SimpleMemory(memory_path)).execute(action))

    brain.think("Forget my name")
    action = brain.act()
    print("Action:", action)
    print("Result:", memory_executor.execute(action))

    brain.think("What is my name?")
    action = brain.act()
    print("Action:", action)
    print("Result:", memory_executor.execute(action))

print()

print("=== TEST SPEECH ===")
brain.think("Say hello to Sotsai")
action = brain.act()
print("Action:", action)
print("Result:", executor.execute(action))

print()

print("=== TEST PICK UP ===")
brain.think("Pick up the cup")
action = brain.act()
print("Action:", action)
print("Result:", executor.execute(action))
