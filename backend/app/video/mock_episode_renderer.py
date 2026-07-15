"""
Mock Episode Renderer

Returns deterministic rendered videos.
"""

import logging

logger = logging.getLogger(__name__)

from backend.app.core.settings import settings
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
        """
        Render a complete episode.
        """

        video_path = str(settings.OUTPUT_DIR / settings.VIDEO_DIR / "episode.mp4")

        logger.info("Rendering final episode video.")
        logger.info("Episode rendered successfully.")

        return RenderedVideo(
            title="TinyVerse Episode",
            video_path=video_path,
            duration_seconds=episode.total_duration,
            resolution=f"{settings.DEFAULT_IMAGE_WIDTH}x{settings.DEFAULT_IMAGE_HEIGHT}",
            fps=settings.DEFAULT_FPS,
            format="mp4",
            provider="mock",
            status="rendered",
        )
