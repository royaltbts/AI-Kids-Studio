"""
Renderer Factory

Creates renderer implementations.
"""

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
        Return configured image renderer.
        """
        return MockImageRenderer()

    @staticmethod
    def voice_renderer():
        """
        Return configured voice renderer.
        """
        return MockVoiceRenderer()

    @staticmethod
    def music_renderer():
        """
        Return configured music renderer.
        """
        return MockMusicRenderer()
