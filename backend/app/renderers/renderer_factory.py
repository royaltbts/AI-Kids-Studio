"""
Renderer Factory

Creates renderer implementations.
"""

from backend.app.core.settings import settings
from backend.app.renderers.mock_image_renderer import MockImageRenderer
from backend.app.renderers.mock_music_renderer import MockMusicRenderer
from backend.app.renderers.mock_voice_renderer import MockVoiceRenderer


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

        #
        # Future
        #
        # if provider == "openai":
        #     return OpenAIImageRenderer()
        #

        raise ValueError(f"Unsupported image renderer: {provider}")

    @staticmethod
    def voice_renderer():
        """
        Return the configured voice renderer.
        """

        provider = settings.VOICE_PROVIDER.lower()

        if provider == "mock":
            return MockVoiceRenderer()

        #
        # Future
        #
        # if provider == "openai":
        #     return OpenAITTSRenderer()
        #

        raise ValueError(f"Unsupported voice renderer: {provider}")

    @staticmethod
    def music_renderer():
        """
        Return the configured music renderer.
        """

        provider = settings.MUSIC_PROVIDER.lower()

        if provider == "mock":
            return MockMusicRenderer()

        raise ValueError(f"Unsupported music renderer: {provider}")
