"""
Mock Image Renderer

Returns deterministic rendered images for testing.
"""

from pathlib import Path

from PIL import Image, ImageDraw

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
        Render a deterministic placeholder image.
        """

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        #
        # Create a simple placeholder image for tests.
        #

        image = Image.new(
            "RGB",
            (
                settings.DEFAULT_IMAGE_WIDTH,
                settings.DEFAULT_IMAGE_HEIGHT,
            ),
            color=(240, 240, 240),
        )

        draw = ImageDraw.Draw(image)

        draw.text(
            (40, 40),
            f"Scene {image_prompt.scene_number}",
            fill=(0, 0, 0),
        )

        image.save(output_path)

        return RenderedImage(
            scene_number=image_prompt.scene_number,
            image_path=str(output_path),
            width=settings.DEFAULT_IMAGE_WIDTH,
            height=settings.DEFAULT_IMAGE_HEIGHT,
            status="rendered",
        )
