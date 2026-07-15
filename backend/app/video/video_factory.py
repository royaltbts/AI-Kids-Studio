"""
Video Factory

Creates video renderer implementations.
"""

from backend.app.video.mock_episode_renderer import MockEpisodeRenderer


class VideoFactory:
    """
    Factory for episode renderers.
    """

    @staticmethod
    def episode_renderer():
        return MockEpisodeRenderer()