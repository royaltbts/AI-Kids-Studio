"""
Renderer Factory

Creates renderer implementations.
"""

from backend.app.renderers.mock_image_renderer import MockImageRenderer
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
        return MockImageRenderer()

    @staticmethod
    def voice_renderer():
        """
        Return the configured voice renderer.
        """
        return MockVoiceRenderer()