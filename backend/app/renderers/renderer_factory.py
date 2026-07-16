"""
Renderer Factory

Creates renderer implementations.
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
            if not settings.OPENAI_API_KEY:
                raise ValueError(
                    "OPENAI_API_KEY is required when IMAGE_PROVIDER=openai."
                )

            return OpenAIImageRenderer()

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
