class BaseAgent:
    def __init__(self, name, memory):
        self.name = name
        self.memory = memory

    def log(self, message):
        print(f"[{self.name}] {message}")
