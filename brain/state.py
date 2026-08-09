from dataclasses import dataclass
from typing import Any


@dataclass
class Action:
    """A structured action produced by NOUS."""

    name: str
    parameters: dict[str, Any]

    def __repr__(self):
        return (
            f"Action(name={self.name!r}, "
            f"parameters={self.parameters!r})"
        )
