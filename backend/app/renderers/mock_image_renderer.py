"""
Mock Image Renderer

Returns deterministic rendered images for testing.
"""

from pathlib import Path

from backend.app.core.settings import settings
from backend.app.renderers.base_image_renderer import ImageRenderer
from backend.app.schemas.image_prompt import ImagePrompt
from backend.app.schemas.rendered_image import RenderedImage


class MockImageRenderer(ImageRenderer):
    """
    Mock implementation of the image renderer.
    """

    def render(
        self,
        image_prompt: ImagePrompt,
        output_path: Path,
    ) -> RenderedImage:
        """
        Render a deterministic image.

        The mock renderer does not generate a real image.
        It simply returns metadata pointing to the expected
        output location.
        """

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        return RenderedImage(
            scene_number=image_prompt.scene_number,
            image_path=str(output_path),
            width=settings.DEFAULT_IMAGE_WIDTH,
            height=settings.DEFAULT_IMAGE_HEIGHT,
            status="rendered",
        )
