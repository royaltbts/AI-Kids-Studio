"""
Renderer Factory

Creates configured renderer implementations.
"""

from backend.app.core.settings import settings
from backend.app.renderers.mock_image_renderer import MockImageRenderer
from backend.app.renderers.mock_music_renderer import MockMusicRenderer
from backend.app.renderers.mock_voice_renderer import MockVoiceRenderer
from backend.app.renderers.openai_image_renderer import OpenAIImageRenderer


class RendererFactory:
    """
    Factory for renderer implementations.
    """

    @staticmethod
    def image_renderer():
        """
        Return the configured image renderer.
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
        Return the configured voice renderer.
        """

        return MockVoiceRenderer()

    @staticmethod
    def music_renderer():
        """
        Return the configured music renderer.
        """

        return MockMusicRenderer()
