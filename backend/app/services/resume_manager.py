"""
Resume Manager

Supports resuming interrupted TinyVerse episode generation.
"""

from pathlib import Path


class ResumeManager:
    """
    Manages episode resume information.
    """

    @staticmethod
    def workspace_exists(
        workspace: Path,
    ) -> bool:
        """
        Return True if the workspace exists.
        """

        return workspace.exists()

    @staticmethod
    def metadata_exists(
        workspace: Path,
    ) -> bool:
        """
        Return True if metadata.json exists.
        """

        return (workspace / "metadata.json").exists()

    @staticmethod
    def scene_video_paths(
        workspace: Path,
        scene_count: int,
        video_dir: str,
    ) -> list[Path]:
        """
        Return expected scene video paths.
        """

        return [
            workspace / video_dir / f"scene_{scene:03d}.mp4"
            for scene in range(
                1,
                scene_count + 1,
            )
        ]

    @staticmethod
    def completed_scene_count(
        paths: list[Path],
    ) -> int:
        """
        Count completed scene videos.
        """

        return sum(path.exists() for path in paths)

    @staticmethod
    def first_missing_scene(
        paths: list[Path],
    ) -> int | None:
        """
        Return first missing scene index.
        """

        for index, path in enumerate(
            paths,
            start=1,
        ):
            if not path.exists():
                return index

        return None

    @staticmethod
    def episode_complete(
        paths: list[Path],
    ) -> bool:
        """
        Return True if every scene exists.
        """

        return all(path.exists() for path in paths)

    @staticmethod
    def cleanup_empty_workspace(
        workspace: Path,
    ) -> None:
        """
        Remove an empty workspace.
        """

        if workspace.exists() and not any(workspace.iterdir()):
            workspace.rmdir()
