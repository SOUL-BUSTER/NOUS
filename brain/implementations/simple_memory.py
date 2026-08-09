from interfaces.memory import MemoryInterface

class SimpleMemory(MemoryInterface):
    def __init__(self):
        self.data = {}

    def remember(self, key, value):
        self.data[key] = value

    def recall(self, key):
        return self.data.get(key)

    def forget(self, key):
        self.data.pop(key, None)
