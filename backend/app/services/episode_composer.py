"""
Episode Composer

Combines rendered scene videos into a single episode using FFmpeg.
"""

import subprocess
from pathlib import Path

from backend.app.core.settings import settings


class EpisodeComposer:
    """
    Combines rendered scene videos into one episode.
    """

    def compose(
        self,
        workspace: Path,
        scene_videos: list[Path],
    ) -> Path:
        """
        Combine multiple scene videos into one episode.

        Parameters
        ----------
        workspace : Path
            Episode workspace directory.

        scene_videos : list[Path]
            Ordered list of rendered scene videos.

        Returns
        -------
        Path
            Path to the final episode.mp4.
        """

        if not scene_videos:
            raise ValueError("No scene videos were supplied.")

        #
        # Create video directory if needed
        #

        video_dir = workspace / settings.VIDEO_DIR

        video_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        #
        # Create FFmpeg concat list
        #

        concat_file = video_dir / "concat.txt"

        with concat_file.open(
            mode="w",
            encoding="utf-8",
        ) as file:

            for video in scene_videos:

                if not video.exists():
                    raise FileNotFoundError(f"Scene video not found: {video}")

                file.write(f"file '{video.resolve()}'\n")

        #
        # Final output
        #

        output_video = video_dir / "episode.mp4"

        command = [
            "ffmpeg",
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat_file),
            "-c",
            "copy",
            str(output_video),
        ]

        subprocess.run(
            command,
            check=True,
        )

        return output_video
