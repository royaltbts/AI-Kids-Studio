"""
Progress Tracker

Provides simple progress reporting for TinyVerse workflows.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ProgressStage:
    """
    Represents one workflow stage.
    """

    name: str
    completed: bool = False


class ProgressTracker:
    """
    Tracks workflow progress.
    """

    def __init__(self) -> None:
        """
        Initialize an empty tracker.
        """

        self._stages: list[ProgressStage] = []

    def add_stage(
        self,
        name: str,
    ) -> None:
        """
        Register a workflow stage.
        """

        self._stages.append(
            ProgressStage(name=name),
        )

    def complete_stage(
        self,
        name: str,
    ) -> None:
        """
        Mark a stage as completed.
        """

        for stage in self._stages:

            if stage.name == name:
                stage.completed = True
                return

        raise ValueError(f"Unknown stage: {name}")

    def print_progress(self) -> None:
        """
        Print workflow progress.
        """

        total = len(self._stages)

        for index, stage in enumerate(
            self._stages,
            start=1,
        ):

            status = "✓" if stage.completed else "·"

            print(f"[{index}/{total}] " f"{stage.name:<22} {status}")

    @property
    def completed(self) -> int:
        """
        Number of completed stages.
        """

        return sum(stage.completed for stage in self._stages)

    @property
    def total(self) -> int:
        """
        Total registered stages.
        """

        return len(
            self._stages,
        )
