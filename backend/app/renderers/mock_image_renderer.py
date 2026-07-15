"""
Mock Image Renderer

Generates deterministic rendered images for testing.
"""

from backend.app.renderers.image_renderer import ImageRenderer
from backend.app.schemas.image_prompt import ImagePrompt
from backend.app.schemas.rendered_image import RenderedImage


class MockImageRenderer(ImageRenderer):
    """
    Mock renderer used for development.
    """

    def render(
        self,
        image_prompt: ImagePrompt,
    ) -> RenderedImage:
        """
        Return deterministic image metadata.
        """

        return RenderedImage(
            scene_number=image_prompt.scene_number,
            image_path=f"renders/scene_{image_prompt.scene_number:03d}.png",
            width=1920,
            height=1080,
            status="rendered",
        )
