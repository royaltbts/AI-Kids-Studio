"""
Mock Video Renderer

Returns deterministic rendered video metadata.
"""

from pathlib import Path

from backend.app.core.settings import settings
from backend.app.renderers.base_renderer import BaseRenderer
from backend.app.schemas.rendered_video import RenderedVideo


class MockVideoRenderer(BaseRenderer):
    """
    Mock implementation of the video renderer.
    """

    def render(
        self,
        scene_number: int,
        title: str,
        image_path: Path,
        audio_path: Path,
        output_path: Path,
    ) -> RenderedVideo:
        """
        Simulate rendering a video clip.
        """

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        output_path.touch(
            exist_ok=True,
        )

        return RenderedVideo(
            scene_number=scene_number,
            title=title,
            video_path=str(output_path),
            duration_seconds=0,
            width=settings.DEFAULT_IMAGE_WIDTH,
            height=settings.DEFAULT_IMAGE_HEIGHT,
            fps=settings.DEFAULT_FPS,
            provider="mock",
            status="rendered",
        )
