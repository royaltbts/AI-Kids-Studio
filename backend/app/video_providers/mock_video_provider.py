"""
Mock Video Provider

Returns deterministic video paths for testing.
"""

from pathlib import Path

from backend.app.video_providers.base import VideoProvider


class MockVideoProvider(VideoProvider):
    """
    Mock implementation of the video provider.
    """

    def provider_name(self) -> str:
        """
        Return provider name.
        """

        return "mock"

    def create_video(
        self,
        image_path: Path,
        audio_path: Path,
        output_path: Path,
    ) -> Path:
        """
        Simulate video creation.

        Parameters
        ----------
        image_path : Path
            Source image.

        audio_path : Path
            Source narration.

        output_path : Path
            Destination video.

        Returns
        -------
        Path
            Expected output path.
        """

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        output_path.touch(
            exist_ok=True,
        )

        return output_path
