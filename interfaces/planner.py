"""
NOUS Planner Interface
"""

from abc import ABC, abstractmethod


class PlannerInterface(ABC):
    """Base interface for planning systems."""

    @abstractmethod
    def create_plan(self, goal: str):
        """
        Generate a plan from a goal.
        """
        pass

    @abstractmethod
    def next_action(self):
        """
        Return the next action in the current plan.
        """
        pass
