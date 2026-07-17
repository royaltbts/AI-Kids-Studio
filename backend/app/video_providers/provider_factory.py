"""
Video Provider Factory

Creates configured video providers.
"""

from backend.app.core.settings import settings
from backend.app.video_providers.base import VideoProvider
from backend.app.video_providers.ffmpeg_video_provider import FFmpegVideoProvider
from backend.app.video_providers.mock_video_provider import MockVideoProvider


class VideoProviderFactory:
    """
    Factory responsible for creating video providers.
    """

    @staticmethod
    def get_provider(
        provider_name: str | None = None,
    ) -> VideoProvider:
        """
        Return the configured video provider.
        """

        provider = (
            provider_name.lower() if provider_name else settings.VIDEO_PROVIDER.lower()
        )

        if provider == "mock":
            return MockVideoProvider()

        if provider == "ffmpeg":
            return FFmpegVideoProvider()

        raise ValueError(f"Unsupported video provider: {provider}")
