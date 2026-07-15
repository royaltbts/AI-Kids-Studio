"""
Tests for Mock Music Renderer.
"""

from backend.app.renderers.mock_music_renderer import MockMusicRenderer


def test_render_music():

    renderer = MockMusicRenderer()

    music = renderer.render(
        title="ABC Adventure",
        duration_seconds=120,
    )

    assert music.title == "ABC Adventure"

    assert music.duration_seconds == 120

    assert music.genre == "Kids"

    assert music.format == "mp3"

    assert music.provider == "mock"

    assert music.status == "rendered"

    assert music.music_path.endswith(
        "background.mp3"
    )