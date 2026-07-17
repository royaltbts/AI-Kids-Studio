"""
FFmpeg Video Provider

Creates MP4 videos using FFmpeg.
"""

import subprocess
from pathlib import Path

from backend.app.video_providers.base import VideoProvider


class FFmpegVideoProvider(VideoProvider):
    """
    FFmpeg implementation of the video provider.
    """

    def provider_name(self) -> str:
        """
        Return provider name.
        """

        return "ffmpeg"

    def create_video(
        self,
        image_path: Path,
        audio_path: Path,
        output_path: Path,
    ) -> Path:
        """
        Create an MP4 video using one image and one audio file.
        """

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        command = [
            "ffmpeg",
            "-y",
            "-loop",
            "1",
            "-i",
            str(image_path),
            "-i",
            str(audio_path),
            "-c:v",
            "libx264",
            "-tune",
            "stillimage",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-pix_fmt",
            "yuv420p",
            "-shortest",
            str(output_path),
        ]

        subprocess.run(
            command,
            check=True,
        )

        return output_path
