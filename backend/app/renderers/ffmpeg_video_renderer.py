"""
FFmpeg Video Renderer

Creates rendered video clips using the configured provider.
Supports automatic asset caching.
"""

import logging
from pathlib import Path

from backend.app.core.settings import settings
from backend.app.renderers.base_renderer import BaseRenderer
from backend.app.schemas.rendered_video import RenderedVideo
from backend.app.video_providers.provider_factory import VideoProviderFactory

logger = logging.getLogger(__name__)


class FFmpegVideoRenderer(BaseRenderer):
    """
    FFmpeg implementation of the video renderer.
    """

    def __init__(self) -> None:
        """
        Initialize configured video provider.
        """

        self.provider = VideoProviderFactory.get_provider()

    def render(
        self,
        scene_number: int,
        title: str,
        image_path: Path,
        audio_path: Path,
        output_path: Path,
    ) -> RenderedVideo:
        """
        Render one scene video.

        If the video already exists it is reused.
        """

        #
        # Cached video
        #

        if output_path.exists():

            logger.info(
                "Using cached video for scene %s.",
                scene_number,
            )

            return RenderedVideo(
                scene_number=scene_number,
                title=title,
                video_path=str(output_path),
                duration_seconds=0,
                width=settings.DEFAULT_IMAGE_WIDTH,
                height=settings.DEFAULT_IMAGE_HEIGHT,
                fps=settings.DEFAULT_FPS,
                format="mp4",
                codec="h264",
                provider=self.provider.provider_name(),
                status="cached",
            )

        #
        # Generate video
        #

        logger.info(
            "Generating video for scene %s.",
            scene_number,
        )

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        video_path = self.provider.create_video(
            image_path=image_path,
            audio_path=audio_path,
            output_path=output_path,
        )

        logger.info(
            "Saved video to %s",
            video_path,
        )

        return RenderedVideo(
            scene_number=scene_number,
            title=title,
            video_path=str(video_path),
            duration_seconds=0,
            width=settings.DEFAULT_IMAGE_WIDTH,
            height=settings.DEFAULT_IMAGE_HEIGHT,
            fps=settings.DEFAULT_FPS,
            format="mp4",
            codec="h264",
            provider=self.provider.provider_name(),
            status="rendered",
        )
