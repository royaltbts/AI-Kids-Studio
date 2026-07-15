"""
Tests for Video Factory.
"""

from backend.app.video.mock_episode_renderer import MockEpisodeRenderer
from backend.app.video.video_factory import VideoFactory


def test_returns_episode_renderer():
    renderer = VideoFactory.episode_renderer()

    assert isinstance(
        renderer,
        MockEpisodeRenderer,
    )
