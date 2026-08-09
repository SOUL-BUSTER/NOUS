from dataclasses import dataclass
from typing import Any


@dataclass
class Action:
    """Structured action produced by the NOUS Brain."""

    name: str
    parameters: dict[str, Any]
