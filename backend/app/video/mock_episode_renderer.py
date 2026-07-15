"""
Mock Episode Renderer

Returns deterministic rendered videos.
"""

from backend.app.schemas.rendered_episode import RenderedEpisode
from backend.app.schemas.rendered_video import RenderedVideo
from backend.app.video.base_episode_renderer import EpisodeRenderer


class MockEpisodeRenderer(EpisodeRenderer):
    """
    Mock implementation of the episode renderer.
    """

    def render(
        self,
        episode: RenderedEpisode,
    ) -> RenderedVideo:

        return RenderedVideo(
            title="TinyVerse Episode",
            video_path="output/video/episode.mp4",
            duration_seconds=episode.total_duration,
            resolution="1920x1080",
            fps=30,
            format="mp4",
            provider="mock",
            status="rendered",
        )
