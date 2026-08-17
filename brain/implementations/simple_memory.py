import json
from pathlib import Path

from interfaces.memory import MemoryInterface


class SimpleMemory(MemoryInterface):
    """Small JSON-backed memory store that persists between NOUS sessions."""

    def __init__(self, storage_path=None):
        project_root = Path(__file__).resolve().parents[2]
        self.storage_path = Path(storage_path) if storage_path else project_root / "data" / "nous_memory.json"
        self.data = self._load()

    def _load(self):
        if not self.storage_path.exists():
            return {}

        try:
            with self.storage_path.open(encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return {}

    def _save(self):
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)

        with self.storage_path.open("w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=2, ensure_ascii=False)

    def remember(self, key, value):
        self.data[key] = value
        self._save()

    def recall(self, key):
        return self.data.get(key)

    def forget(self, key):
        self.data.pop(key, None)
        self._save()
