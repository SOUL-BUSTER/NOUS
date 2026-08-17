from brain.core.brain import Brain
from brain.core.executor import Executor


brain = Brain()
executor = Executor(brain.skills)


print("=== TEST NAVIGATION ===")
brain.think("Go to kitchen")
action = brain.act()
print("Action:", action)
print("Result:", executor.execute(action))

print()

print("=== TEST MEMORY ===")
brain.think("Remember my name is Sotsai")
action = brain.act()
print("Action:", action)
print("Result:", executor.execute(action))

brain.think("What is my name?")
action = brain.act()
print("Action:", action)
print("Result:", executor.execute(action))
print("Result after restart:", Executor(brain.skills).execute(action))

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
