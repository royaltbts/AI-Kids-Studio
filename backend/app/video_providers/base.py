"""
Video Provider

Abstract interface for video generation providers.
"""

from abc import ABC, abstractmethod
from pathlib import Path


class VideoProvider(ABC):
    """
    Base interface for video providers.
    """

    @abstractmethod
    def provider_name(self) -> str:
        """
        Return the provider name.
        """
        raise NotImplementedError

    @abstractmethod
    def create_video(
        self,
        image_path: Path,
        audio_path: Path,
        output_path: Path,
    ) -> Path:
        """
        Create a video from one image and one narration track.

        Parameters
        ----------
        image_path : Path
            Source image.

        audio_path : Path
            Source narration.

        output_path : Path
            Destination MP4 file.

        Returns
        -------
        Path
            Path to the generated video.
        """
        raise NotImplementedError
