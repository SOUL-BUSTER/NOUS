from typing import Dict, Optional

from .base import Skill


class SkillRegistry:
    """Registry for managing NOUS skills."""

    def __init__(self):
        self._skills: Dict[str, Skill] = {}

    def register(self, skill: Skill):
        """Register a skill."""
        self._skills[skill.name] = skill

    def get(self, name: str) -> Optional[Skill]:
        """Get a skill by name."""
        return self._skills.get(name)

    def find_for_goal(self, goal: str) -> Optional[Skill]:
        """Find the first skill capable of handling the goal."""
        for skill in self._skills.values():
            if skill.can_handle(goal):
                return skill

        return None

    def list(self):
        """List all registered skill names."""
        return list(self._skills.keys())
