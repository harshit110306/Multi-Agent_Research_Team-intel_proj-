import os
import json
from datetime import datetime

class SessionManager:
    def __init__(self, folder="sessions"):
        self.folder = folder
        os.makedirs(folder, exist_ok=True)

    def save_session(self, memory, topic):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = os.path.join(self.folder, f"session_{timestamp}.json")

        data = {
            "topic": topic,
            "timestamp": timestamp,
            "memory": memory.show_all()
        }

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        return filename

    def list_sessions(self):
        return os.listdir(self.folder)

    def load_session(self, filename):
        path = os.path.join(self.folder, filename)
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
