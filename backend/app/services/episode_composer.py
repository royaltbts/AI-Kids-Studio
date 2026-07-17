"""
Episode Composer

Combines rendered scene videos into a single episode using FFmpeg.
"""

import shutil
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
        """

        if not scene_videos:
            raise ValueError("No scene videos were supplied.")

        video_dir = workspace / settings.VIDEO_DIR

        video_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        output_video = video_dir / "episode.mp4"

        #
        # Mock renderer produces empty placeholder videos.
        # Detect them and simply copy the first one.
        #

        if all(video.stat().st_size == 0 for video in scene_videos):
            shutil.copyfile(
                scene_videos[0],
                output_video,
            )
            return output_video

        #
        # Build concat list for FFmpeg.
        #

        concat_file = video_dir / "concat.txt"

        with concat_file.open(
            "w",
            encoding="utf-8",
        ) as file:

            for video in scene_videos:

                if not video.exists():
                    raise FileNotFoundError(f"Scene video not found: {video}")

                file.write(f"file '{video.resolve()}'\n")

        subprocess.run(
            [
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
            ],
            check=True,
        )

        return output_video
