"""
Tests for Mock Episode Renderer.
"""

from backend.app.schemas.rendered_episode import RenderedEpisode
from backend.app.video.mock_episode_renderer import MockEpisodeRenderer


def test_render_episode():

    renderer = MockEpisodeRenderer()

    episode = RenderedEpisode(
        total_duration=120,
    )

    video = renderer.render(
        episode,
    )

    assert video.title == "TinyVerse Episode"

    assert video.duration_seconds == 120

    assert video.video_path.endswith("episode.mp4")

    assert video.provider == "mock"

    assert video.status == "rendered"

    assert video.format == "mp4"

    assert video.fps == 30
