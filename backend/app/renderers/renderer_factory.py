"""
Renderer Factory

Creates configured renderer implementations.
"""

from backend.app.core.settings import settings
from backend.app.renderers.ffmpeg_video_renderer import FFmpegVideoRenderer
from backend.app.renderers.mock_image_renderer import MockImageRenderer
from backend.app.renderers.mock_music_renderer import MockMusicRenderer
from backend.app.renderers.mock_video_renderer import MockVideoRenderer
from backend.app.renderers.mock_voice_renderer import MockVoiceRenderer
from backend.app.renderers.openai_image_renderer import OpenAIImageRenderer
from backend.app.renderers.openai_voice_renderer import OpenAIVoiceRenderer


class RendererFactory:
    """
    Factory for renderer implementations.
    """

    @staticmethod
    def image_renderer(provider: str | None = None):
        """
        Return configured image renderer.
        """

        provider = (provider or settings.IMAGE_PROVIDER).lower()

        if provider == "mock":
            return MockImageRenderer()

        if provider == "openai":
            return OpenAIImageRenderer()

        raise ValueError(f"Unsupported image provider: {provider}")

    @staticmethod
    def voice_renderer(provider: str | None = None):
        """
        Return configured voice renderer.
        """

        provider = (provider or settings.VOICE_PROVIDER).lower()

        if provider == "mock":
            return MockVoiceRenderer()

        if provider == "openai":
            return OpenAIVoiceRenderer()

        raise ValueError(f"Unsupported voice provider: {provider}")

    @staticmethod
    def music_renderer(provider: str | None = None):
        provider = (provider or settings.MUSIC_PROVIDER).lower()

        if provider == "mock":
            return MockMusicRenderer()

        raise ValueError(f"Unsupported music provider: {provider}")

    @staticmethod
    def video_renderer(provider: str | None = None):
        provider = (provider or settings.VIDEO_PROVIDER).lower()

        if provider == "mock":
            return MockVideoRenderer()

        if provider == "ffmpeg":
            return FFmpegVideoRenderer()

        raise ValueError(f"Unsupported video provider: {provider}")
