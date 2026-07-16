"""
Mock Image Renderer

Returns deterministic rendered images for testing.
"""

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
        prompt: ImagePrompt,
    ) -> RenderedImage:
        """
        Render a deterministic image.
        """

        image_path = str(
            settings.OUTPUT_DIR
            / settings.IMAGE_DIR
            / f"scene_{prompt.scene_number:03d}.png"
        )

        return RenderedImage(
            scene_number=prompt.scene_number,
            image_path=image_path,
            width=settings.DEFAULT_IMAGE_WIDTH,
            height=settings.DEFAULT_IMAGE_HEIGHT,
            status="rendered",
        )
