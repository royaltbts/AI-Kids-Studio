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
    def image_renderer():
        """
        Return configured image renderer.
        """

        provider = settings.IMAGE_PROVIDER.lower()

        if provider == "mock":
            return MockImageRenderer()

        if provider == "openai":
            return OpenAIImageRenderer()

        raise ValueError(f"Unsupported image provider: {provider}")

    @staticmethod
    def voice_renderer():
        """
        Return configured voice renderer.
        """

        provider = settings.VOICE_PROVIDER.lower()

        if provider == "mock":
            return MockVoiceRenderer()

        if provider == "openai":
            return OpenAIVoiceRenderer()

        raise ValueError(f"Unsupported voice provider: {provider}")

    @staticmethod
    def music_renderer():
        """
        Return configured music renderer.
        """

        provider = settings.MUSIC_PROVIDER.lower()

        #
        # Only Mock is available for now.
        #

        if provider == "mock":
            return MockMusicRenderer()

        raise ValueError(f"Unsupported music provider: {provider}")

    @staticmethod
    def video_renderer():
        """
        Return configured video renderer.
        """

        provider = settings.VIDEO_PROVIDER.lower()

        if provider == "mock":
            return MockVideoRenderer()

        if provider == "ffmpeg":
            return FFmpegVideoRenderer()

        raise ValueError(f"Unsupported video provider: {provider}")
