class SharedMemory:
    def __init__(self):
        self.storage = {}

    def write(self, key, value):
        self.storage[key] = value

    def read(self, key):
        return self.storage.get(key, None)

    def show_all(self):
        return self.storage
