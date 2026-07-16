"""
Mock Music Renderer

Returns deterministic background music.
"""

from backend.app.renderers.base_renderer import BaseRenderer
from backend.app.schemas.rendered_music import RenderedMusic


class MockMusicRenderer(BaseRenderer):
    """
    Mock implementation of a music renderer.
    """

    def render(
        self,
        title: str,
        duration_seconds: int,
    ) -> RenderedMusic:

        return RenderedMusic(
            title=title,
            music_path="output/music/background.mp3",
            duration_seconds=duration_seconds,
            genre="Kids",
            format="mp3",
            provider="mock",
            status="rendered",
        )
