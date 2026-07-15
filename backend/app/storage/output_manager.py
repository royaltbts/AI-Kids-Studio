"""
Output Manager.

Creates and manages episode workspaces.
"""

from datetime import datetime
from pathlib import Path

from backend.app.core.settings import settings


class OutputManager:
    """
    Creates and manages episode workspaces.
    """

    BASE_DIR = settings.OUTPUT_DIR

    @classmethod
    def create_episode_workspace(cls) -> Path:
        """
        Create a unique workspace for a generated episode.
        """

        episode_id = datetime.now().strftime("episode_%Y%m%d_%H%M%S")

        workspace = cls.BASE_DIR / episode_id

        for folder in (
            settings.IMAGE_DIR,
            settings.AUDIO_DIR,
            settings.MUSIC_DIR,
            settings.VIDEO_DIR,
            settings.THUMBNAIL_DIR,
            settings.LOG_DIR,
        ):
            (workspace / folder).mkdir(
                parents=True,
                exist_ok=True,
            )

        return workspace

    @classmethod
    def get_workspace(
        cls,
        episode_id: str,
    ) -> Path:
        """
        Return the workspace path for an existing episode.
        """

        return cls.BASE_DIR / episode_id

    @classmethod
    def image_dir(
        cls,
        workspace: Path,
    ) -> Path:
        """
        Return the images directory.
        """

        return workspace / settings.IMAGE_DIR

    @classmethod
    def audio_dir(
        cls,
        workspace: Path,
    ) -> Path:
        """
        Return the audio directory.
        """

        return workspace / settings.AUDIO_DIR

    @classmethod
    def music_dir(
        cls,
        workspace: Path,
    ) -> Path:
        """
        Return the music directory.
        """

        return workspace / settings.MUSIC_DIR

    @classmethod
    def video_dir(
        cls,
        workspace: Path,
    ) -> Path:
        """
        Return the video directory.
        """

        return workspace / settings.VIDEO_DIR

    @classmethod
    def thumbnail_dir(
        cls,
        workspace: Path,
    ) -> Path:
        """
        Return the thumbnails directory.
        """

        return workspace / settings.THUMBNAIL_DIR

    @classmethod
    def log_dir(
        cls,
        workspace: Path,
    ) -> Path:
        """
        Return the logs directory.
        """

        return workspace / settings.LOG_DIR
