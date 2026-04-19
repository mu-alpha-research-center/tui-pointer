"""
Two-pointer tracker API.

Usage:
    tracker = TwoPointerTracker()
    tracker.record(arr, left=0, right=len(arr)-1, message="initial")
    ...
    tracker.animate()

Pointers are passed as keyword arguments: name=index.
Any number of named pointers are supported.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Step:
    arr: list[Any]
    pointers: dict[str, int]  # name -> index
    message: str = ""


class TwoPointerTracker:
    def __init__(self):
        self.steps: list[Step] = []

    def record(self, arr, message: str = "", **pointers: int) -> None:
        """Record the current state of the array and pointer positions.

        Args:
            arr:      The array at this step (will be shallow-copied).
            message:  Optional annotation shown during animation.
            **pointers: Named pointer positions, e.g. left=0, right=5.
        """
        self.steps.append(Step(list(arr), dict(pointers), message))

    def animate(self, delay: float = 0.5) -> None:
        """Play back the recorded steps as a terminal animation.

        Args:
            delay: Seconds to pause between steps.
        """
        from .animator import animate
        animate(self.steps, delay=delay)
