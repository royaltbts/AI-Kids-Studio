"""
Output Manager.

Creates and manages episode workspaces.
"""

from datetime import datetime
from pathlib import Path


class OutputManager:
    """
    Creates output folders for generated episodes.
    """

    BASE_DIR = Path("output")

    @classmethod
    def create_episode_workspace(cls) -> Path:
        """
        Create a unique workspace for one episode.
        """

        episode_id = datetime.now().strftime("episode_%Y%m%d_%H%M%S")

        workspace = cls.BASE_DIR / episode_id

        for folder in (
            "images",
            "audio",
            "music",
            "video",
            "thumbnails",
            "logs",
        ):
            (workspace / folder).mkdir(
                parents=True,
                exist_ok=True,
            )

        return workspace
